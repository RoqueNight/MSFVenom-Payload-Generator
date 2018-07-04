# MSFVenom-Payload-Generator
Simple Script to Generate an MSFVenom Payload

# Types of Payloads it Generates

- Windows 
- Linux
- Andriod
- Python
- PHP

# Installing Dependencies Ubuntu
```
sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install -y python3-pip
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
python3 -V
```

# Installing Dependencies CentOS7
```
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
sudo yum update
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
sudo yum groupinstall -y "Development Tools"
python3.6 -V
```

# Installing The Script
```
cd /
mkdir PG
cd PG
git clone https://github.com/RoqueNight/MSFVenom-Payload-Generator.git
cd MSFVenom-Payload-Generator
chmod +x pg.py
python pg.py
```
