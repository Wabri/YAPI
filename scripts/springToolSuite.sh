# Spring Tools 4 is the next generation of Spring tooling for your favorite coding environment - https://spring.io/tools
wget -O sts.tar.gz download.springsource.com/release/STS4/4.1.0.RELEASE/dist/e4.10/spring-tool-suite-4-4.1.0.RELEASE-e4.10.0-linux.gtk.x86_64.tar.gz
tar zxvf sts.tar.gz
sudo rm -r sts.tar.gz
mv sts-* sts
ln -s $($pwd)/sts/sts /usr/local/bin/spring-tool-suite
