# Telegram Fast and secure desktop app, perfectly synced with your mobile phoneDesktop - https://desktop.telegram.org/
curl --get https://api.github.com/repos/telegramdesktop/tdesktop/releases/latest | grep "browser_download" | grep "tar.xz" | tr -d '"'  > tout
cut -c 29- tout > tlast
rm tout
wget -O telegram.tar.xz -i tlast
rm tlast
tar xf telegram.tar.xz
sudo mv Telegram/Telegram /usr/local/bin/telegram
rm -r ?elegram*
