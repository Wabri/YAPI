# Rambox workspace browser - https://rambox.pro
sudo apt install gconf2
curl --get https://api.github.com/repos/ramboxapp/community-edition/releases/latest | grep "browser_download" | grep "amd64.deb" | tr -d '"'  > cout
cut -c 29- cout > clink
rm cout
wget -O rambox.deb -i clink
rm clink
sudo dpkg -i rambox.deb
rm -r rambox.deb
