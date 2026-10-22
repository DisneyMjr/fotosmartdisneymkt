#!/usr/bin/env python3
"""Smart Batch DisneyMkt: conversao e redimensionamento em lote, sem modificar originais.

Requer Pillow (pip install Pillow). Uso: python tools/smart_batch.py --help
"""
import argparse
import csv
import re
import os
import shutil
import tempfile
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont

PRESETS = {"post": (1080, 1440), "quadrado": (1080, 1080),
           "story": (1080, 1920), "carrossel": (1080, 1350),
           "youtube": (1280, 720), "horizontal": (1920, 1080)}
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp"}

def safe_name(s):
    s = re.sub(r"[^\w. -]", "_", s, flags=re.UNICODE).strip(" .")
    return s[:100] or "imagem"

def run(args):
    src, dst = Path(args.entrada).resolve(), Path(args.saida).resolve()
    if not src.is_dir():
        raise SystemExit(f"Pasta de entrada inexistente: {src}")
    if src == dst:
        raise SystemExit("Entrada e saida precisam ser pastas diferentes")
    size = PRESETS.get(args.formato)
    if size is None:
        try:
            w, h = (int(x) for x in args.formato.lower().split("x", 1))
            if not (1 <= w <= 10000 and 1 <= h <= 10000):
                raise ValueError
            size = (w, h)
        except ValueError:
            raise SystemExit("Use um preset ou larguraXaltura (ex.: 1080x1440)")
    dst.mkdir(parents=True, exist_ok=True)
    if dst == src or src in dst.parents:
        raise SystemExit("Saida nao pode ficar dentro da pasta de entrada")
    free_mb = shutil.disk_usage(dst).free / (1024 * 1024)
    if free_mb < args.espaco_min_mb:
        raise SystemExit(f"Espaco insuficiente no disco de destino: {free_mb:.0f} MB livres; minimo exigido {args.espaco_min_mb} MB")
    files = sorted(x for x in src.iterdir() if x.is_file() and x.suffix.lower() in EXTENSIONS)
    if not files:
        raise SystemExit("Nenhuma imagem suportada encontrada na pasta")
    logo = None
    if args.logo:
        with Image.open(args.logo) as im:
            logo = im.convert("RGBA")
    report = []
    for index, path in enumerate(files, 1):
        target = dst / f"{index:04d}-{safe_name(path.stem)}.{args.tipo}"
        if target.exists() and not args.substituir:
            report.append([path.name, target.name, "ignorado: arquivo ja existe"])
            continue
        try:
            with Image.open(path) as original:
                im = ImageOps.exif_transpose(original).convert("RGBA")
            if args.ajuste == "recortar":
                im = ImageOps.fit(im, size, method=Image.Resampling.LANCZOS, centering=(args.foco_x, args.foco_y))
            else:
                inside = ImageOps.contain(im, size, method=Image.Resampling.LANCZOS)
                bg = Image.new("RGBA", size, args.fundo)
                bg.alpha_composite(inside, ((size[0]-inside.width)//2, (size[1]-inside.height)//2))
                im = bg
            if logo:
                maxw = max(1, round(size[0] * args.logo_pct / 100))
                wm = ImageOps.contain(logo, (maxw, max(1, size[1]//3)), Image.Resampling.LANCZOS)
                gap = max(8, int(size[0] * 0.025))
                im.alpha_composite(wm, (size[0]-wm.width-gap, size[1]-wm.height-gap))
            if args.texto:
                draw = ImageDraw.Draw(im)
                x, y = max(8, size[0]//40), size[1]-max(26, size[1]//35)
                draw.text((x+1,y+1), args.texto, fill="#000000", font=ImageFont.load_default())
                draw.text((x,y), args.texto, fill="#FFFFFF", font=ImageFont.load_default())
            # Arquivo temporario na propria pasta de destino: troca atomica evita
            # deixar arquivos finais incompletos em caso de falha ou interrupcao.
            fd, tmp_name = tempfile.mkstemp(prefix=".fotosmart-", suffix="." + args.tipo, dir=dst)
            os.close(fd)
            temp_target = Path(tmp_name)
            try:
                _save_image(im, temp_target, args, size)
                os.replace(temp_target, target)
            finally:
                temp_target.unlink(missing_ok=True)
            report.append([path.name, target.name, "ok"])
        except (OSError, ValueError, MemoryError, Image.DecompressionBombError) as exc:
            report.append([path.name, "", f"erro: {exc}"])
    manifest = dst / "relatorio-smart-batch.csv"
    with manifest.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["origem", "destino", "status"])
        writer.writerows(report)
    print(f"Smart Batch DisneyMkt: {sum(r[2] == 'ok' for r in report)}/{len(report)} criadas. Relatorio: {manifest}")
    return 1 if any(r[2].startswith("erro") for r in report) else 0


def _save_image(im, target, args, size):
    if args.tipo == "jpg":
        bg = Image.new("RGB", size, args.fundo)
        bg.paste(im, mask=im.getchannel("A"))
        bg.save(target, "JPEG", quality=args.qualidade, optimize=True)
    elif args.tipo == "webp":
        im.save(target, "WEBP", quality=args.qualidade, method=4)
    else:
        im.save(target, "PNG", optimize=True)


def main():
    p = argparse.ArgumentParser(description="Smart Batch DisneyMkt - producao de imagens em lote")
    p.add_argument("--entrada", required=True, help="Pasta de imagens originais")
    p.add_argument("--saida", required=True, help="Pasta para imagens finais")
    p.add_argument("--formato", default="post", help="post, quadrado, story, carrossel, youtube, horizontal ou 1080x1440")
    p.add_argument("--tipo", choices=["png", "jpg", "webp"], default="jpg")
    p.add_argument("--ajuste", choices=["recortar", "encaixar"], default="encaixar")
    p.add_argument("--fundo", default="#FFFFFF", help="Cor do fundo para ajuste encaixar/JPG")
    p.add_argument("--logo", help="Arquivo PNG com marca d'agua opcional")
    p.add_argument("--logo-pct", type=int, default=20, help="Largura maxima da marca em percentual (1 a 60)")
    p.add_argument("--texto", default="", help="Texto curto da marca d'agua")
    p.add_argument("--qualidade", type=int, default=90, help="Qualidade JPEG/WebP (1 a 100)")
    p.add_argument("--foco-x", type=float, default=0.5, help="Ponto horizontal de recorte entre 0 e 1")
    p.add_argument("--foco-y", type=float, default=0.5, help="Ponto vertical de recorte entre 0 e 1")
    p.add_argument("--espaco-min-mb", type=int, default=256, help="Espaco livre minimo no destino em MB (padrao: 256)")
    p.add_argument("--substituir", action="store_true", help="Permitir substituir imagens geradas")
    a = p.parse_args()
    if not 1 <= a.logo_pct <= 60 or not 1 <= a.qualidade <= 100:
        p.error("logo-pct deve estar entre 1 e 60, e qualidade entre 1 e 100")
    if not 0 <= a.foco_x <= 1 or not 0 <= a.foco_y <= 1 or a.espaco_min_mb < 0:
        p.error("foco-x e foco-y devem estar entre 0 e 1; espaco-min-mb nao pode ser negativo")
    raise SystemExit(run(a))

if __name__ == "__main__":
    main()
