#!/bin/bash

# 50.043 Databases and Big Data Systems: Group Project
# Automation Script
# DO NOT run as root! == ./start.sh
# 
# Group 08

echo
echo  =========================
echo '|     CONFIGURATION     |'
echo  =========================
echo Press ctrl-c and restart the script if information is entered incorrectly.
echo
echo Input AWS Access Key ID:
read access_key
echo Input Secret Access Key:
read secret_key
echo Input Default Region Name:
read region
echo Input Github Username:
read git_user
echo Input Github Password:
read git_pass
echo Input number of nodes for analytics:
read nodes
echo access_key = "'$access_key'" > config.py
echo secret_access_key = "'$secret_key'" >> config.py
echo region = "'$region'" >> config.py
echo github_user = "'$git_user'" >> config.py
echo github_pass = "'$git_pass'" >> config.py
echo nodes = "'$nodes'" >> config.py
echo
echo  ==================================================
echo '|    Configuration File saved as config.py!      |'
echo '|         Average setup time - 30 mins           |'
echo '|           Maybe go grab a coffee :)            |'
echo  ==================================================
sleep 5


echo
echo
echo  ===================================
echo '|     INSTALLING DEPENDENCIES     |'
echo  ===================================

# install python3 and pip3
echo
echo Updating package information
echo ---
sudo apt-get update
echo
echo Installing python3, please wait...
echo ---
sudo apt -y  install python3
echo
echo Installing pip3, please wait...
echo ---
sudo apt -y install python3-pip

# install unzip
echo
echo Installing unzip, please wait...
echo ---
sudo apt -y install unzip

# install boto3 and paramiko
echo
echo Installing boto3 library, please wait...
echo ---
python3 -m pip install boto3

# install paramiko
echo
echo Installing Paramiko, please wait...
echo ---
python3 -m pip install paramiko

# install aws-cli
echo
echo Installing aws-cli, please wait...
echo ---
sudo wget https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -O awscliversion2.zip
unzip awscliversion2.zip
sudo ./aws/install

# install terraform
echo
echo Installing Terraform, please wait...
echo ---
sudo wget https://releases.hashicorp.com/terraform/0.13.5/terraform_0.13.5_linux_amd64.zip
sudo unzip terraform_0.13.5_linux_amd64.zip
sudo mv terraform /usr/bin/


# configure aws
echo
echo ---
printf '%s\n' $access_key $secret_key $region json | aws configure 1>/dev/null


echo
echo
echo  ===============================
echo '|    INITIALIZING INSTANCES   |'
echo  ===============================
sleep 1
python3 ec2_create.py

echo
echo
echo  =================================
echo '|    GENERATING SETUP SCRIPTS   |'
echo  =================================
sleep 1
python3 generate_scripts.py

echo
echo
echo  =================================
echo '|    SETTING UP MYSQL SERVER    |'
echo  =================================
sleep 1
python3 sql_setup.py

echo
echo
echo  ===================================
echo '|    SETTING UP MONGODB SERVER    |'
echo  ===================================
sleep 1
python3 mongo_setup.py

echo
echo
echo  ===================================
echo '|    SETTING UP REACT SERVER      |'
echo  ===================================
sleep 1
python3 react_setup.py

echo
echo
echo  ===================================
echo '|      SETTING UP ANALYTICS       |'
echo  ===================================
sleep 1
python3 analytics_setup.py




while [ true ]; do
echo Type 'Y' to start analytics tasks:
read start
if [ $start = Y ]; then
python3 analytics_start.py
exit;
else
echo Please type 'Y' to continue with analytic tasks
fi
done

