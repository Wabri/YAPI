# install NVIDIA GeForce 940MX driver
sudo add-apt-repository "deb http://httpredir.debian.org/debian/ stretch main contrib non-free"
sudo apt update
sudo apt install linux-headers-$(uname -r|sed 's/[^-]*-[^-]*-//') nvidia-driver
lspci -k | grep -EA3 'VGA|3D|Display'
sudo apt install bumblebee-nvidia
