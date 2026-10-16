# FotoSmart – Linux e Windows

Na aba **Actions** do GitHub, execute **Gerar Linux FotoSmart** na branch `main`.
Quando o workflow terminar com sucesso, abra **Artifacts** e baixe `FotoSmart-Linux-x64`.
Pacotes: AppImage, DEB, RPM, TAR.GZ e SHA256SUMS.txt.

Ubuntu/Debian/Mint: `sudo apt install ./arquivo.deb`
Fedora: `sudo dnf install ./arquivo.rpm`
AppImage: `chmod +x arquivo.AppImage && ./arquivo.AppImage`

A compilacao ainda precisa ser validada no GitHub Actions. Os nomes internos dos executaveis
continuam `photocraft` para compatibilidade com o codigo original.
Para atualizacoes automaticas com AppImageUpdate, os arquivos precisam ser publicados no
GitHub Releases (a acao manual apenas disponibiliza Artifacts).
