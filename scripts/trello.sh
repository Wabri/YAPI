# An unofficial Trello desktop app - https://github.com/danielchatfield/trello-desktop
mkdir trello
cd trello
wget -o trello.zip https://github.com/danielchatfield/trello-desktop/releases/download/v0.1.9/Trello-linux-0.1.9.zip
unzip trello.zip
sudo ln -s $(pwd)/Trello /usr/local/bin/trello
