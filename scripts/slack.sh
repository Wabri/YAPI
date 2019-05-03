# Slack can help your team work together and get things done - https://slack.com/
wget -O slack.deb https://downloads.slack-edge.com/linux_releases/slack-desktop-3.4.0-amd64.deb
sudo dpkg -i slack.deb
sudo apt --fix-broken install
rm -r slack.deb
