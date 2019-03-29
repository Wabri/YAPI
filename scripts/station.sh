# Station is the first smart browser for busy people, a single place for all of your web applications - https://getstation.com/
curl --get https://api.github.com/repos/getstation/desktop-app-releases/releases/latest | grep "browser_download" | grep "x86_64.AppImage" | tr -d '"'  > cout
cut -c 29- cout > clink
rm cout
wget -O station.AppImage -i clink
rm clink
sudo chmod +x station.AppImage
sudo mv station.AppImage /usr/local/bin/station
sudo chmod +x /usr/local/bin/station
