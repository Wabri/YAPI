# Wavebox a focused workspace for all your web apps - https://wavebox.io
sudo wget -O wavebox.key https://wavebox.io/dl/client/repo/archive.key
sudo apt-key add wavebox.key
rm wavebox.key
echo "deb https://wavebox.io/dl/client/repo/ x86_64/" | sudo tee -a /etc/apt/sources.list.d/repo.list
sudo apt update
sudo apt install wavebox
echo "/opt/wavebox/Wavebox --mailto=%u \> /dev/null" > wavebox
sudo mv wavebox /usr/local/bin/.
sudo chmod +x /usr/local/bin/wavebox
