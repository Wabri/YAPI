# Java jdk 11 with path setup - https://www.oracle.com/technetwork/java/javase/downloads/index.html
wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie" -O jdk-11.tar.gz download.oracle.com/otn-pub/java/jdk/11.0.1+13/90cf5d8f270a4347a95050320eef3fb7/jdk-11.0.1_linux-x64_bin.tar.gz
sudo mkdir -p /usr/local/java
tar xvzf jdk-11.tar.gz
sudo cp -r jdk-11.0.1/ /usr/local/java
sudo rm -r jdk-11.0.1 jdk-11.tar.gz
echo '' | sudo tee -a /etc/profile
echo '# JAVA JDK' | sudo tee -a /etc/profile
echo 'JAVA_HOME=/usr/local/java/jdk-11' | sudo tee -a /etc/profile
echo 'PATH=$PATH:$HOME/bin:$JAVA_HOME/bin' | sudo tee -a /etc/profile
echo 'export JAVA_HOME' | sudo tee -a /etc/profile
echo 'export PATH' | sudo tee -a /etc/profile
echo '' | sudo tee -a /etc/profile
sudo update-alternatives --install "/usr/bin/java" "java" "/usr/local/java/jdk-11.0.1/bin/java" 1
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/local/java/jdk-11.0.1/bin/javac" 1
sudo update-alternatives --set java /usr/local/java/jdk-11.0.1/bin/java
sudo update-alternatives --set javac /usr/local/java/jdk-11.0.1/bin/javac
