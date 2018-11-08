# NVIDIA driver support of Geforce 4xx and higher GPUs - https://wiki.debian.org/NvidiaGraphicsDrivers
sudo add-apt-repository "deb http://httpredir.debian.org/debian/ stretch main contrib non-free"
sudo apt update
sudo apt install linux-headers-$(uname -r|sed 's/[^-]*-[^-]*-//') nvidia-driver
lspci -k | grep -EA3 'VGA|3D|Display'
sudo apt install bumblebee-nvidia
