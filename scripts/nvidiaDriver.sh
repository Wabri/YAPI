# NVIDIA driver support of Geforce 4xx and higher GPUs - https://wiki.debian.org/NvidiaGraphicsDrivers
# stretch-backports
sudo add-apt-repository "deb http://httpredir.debian.org/debian stretch-backports main contrib non-free"
sudo apt-get install linux-headers-$(uname -r|sed 's/[^-]*-[^-]*-//')
sudo apt update
sudo apt-get install -t stretch-backports nvidia-driver 
sudo apt install bumblebee-nvidia
lspci -k | grep -EA3 'VGA|3D|Display'
