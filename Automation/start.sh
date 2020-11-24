#!/bin/bash

# 50.043 Databases and Big Data Systems: Group Project
# Automation Script  --> Do not move this file!
# 
# Group 08

echo
echo  =====================
echo '|     STARTING...   |'
echo  =====================

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

# install boto3
echo
echo Installing boto3 library, please wait...
echo ---
python3 -m pip install boto3

# install aws-cli
echo
echo Instaling aws-cli, please wait...
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
echo AWS CONFIGURATION: Please input the necessary information.
echo ---
aws configure

# initiate ec2 instances - run ec2_start.py
echo
echo
echo  =======================
echo '| EC2 INITIALIZING... |'
echo  =======================
python3 ec2_create.py
