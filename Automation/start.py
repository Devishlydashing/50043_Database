# 50.043 Databases and Big Data Systems: Group Project
# Automation Script
# Downloads required libraries and creates required ec2 instances
#
# Group 08

import boto3
import os
import config

print("=====================")
print("|     STARTING...   |")
print("=====================")

# install python3 and pip3
print("\nUpdating package information\n---")
os.system('sudo apt-get update')
print("\nInstalling python3, please wait...\n---")
os.system('sudo apt -y  install python3')
print("\nInstalling pip3, please wait...\n---")
os.system('sudo apt -y install python3-pip')

# install unzip
print("\nInstalling unzip, please wait...\n---")
os.system('sudo apt -y install unzip')

# install boto3
print("\nInstalling boto3 library, please wait...\n---")
os.system('python3 -m pip install boto3')

# install aws-cli
print("\nInstaling aws-cli, please wait...\n---")
os.system('sudo wget https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -O awscliversion2.zip')
os.system('unzip awscliversion2.zip')
os.system('sudo ./aws/install')

# install terraform
print("\nInstalling Terraform, please wait...\n---")
os.system('wget https://releases.hashicorp.com/terraform/0.13.5/terraform_0.13.5_linux_amd64.zip')
os.system('sudo unzip terraform_0.13.5_linux_amd64.zip')
os.system('sudo mv terraform /usr/bin/')

# configure aws
print("\nAWS CONFIGURATION: Please input the necessary information.\n---")
os.system('aws configure')

# set up ec2
print("\n\n\n=======================")
print("| EC2 INITIALIZING... |")
print("=======================")


# obtain configuration
access_key = config.access_key
secret_key = config.secret_access_key
session_token = config.session_token
region = config.region

if region == 'us-east-1':
	ami = 'ami-0f82752aa17ff8f5d'
else:
	ami = 'ami-04613ff1fdcd2eab1'


# for normal aws account (make sure credentials is set up with aws configure)
ec2 = boto3.resource('ec2')


# for aws educate account
#session = boto3.session.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, aws_session_token=session_token, region_name=region)

#ec2 = session.resource('ec2')

# create key file for instances (using boto3)
print("Creating key-pair as 'ec2-group08-keypair'.")
outfile = open('ec2-group08-keypair.pem','w')
key_pair = ec2.create_key_pair(KeyName='ec2-group08-keypair')
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)
outfile.close()

# change permissions
os.system('chmod 400 ec2-group08-keypair.pem')

# create ec2 instances (using terraform)
print("Creating ec2 instances...")

#instances = ec2.create_instances(
#	ImageId=ami,
#	MinCount=1,
#	MaxCount=4,
#	InstanceType='t2.micro',
#	KeyName='ec2-group08-keypair'
#)

os.system('mkdir terraform-group08')
os.chdir('./terraform-group08')
with open('aws.tf', 'w') as f:
	f.write("""provider "aws" {{
  access_key = "{}"
  secret_key = "{}"  
  region     = "{}"
}} 
	""".format(access_key, secret_key, region))
	
os.system('terraform init')

with open('create_ec2.tf', 'w') as f:
	f.write("""resource "aws_instance" "group08_instance" {{
  ami           = "{}"
  count=4
  key_name = "ec2-group08-keypair"
  instance_type = "t2.micro"
  security_groups= [ "group_08_sg"]
  tags= {{
    Name = "group08-instance"
  }}
}}

resource "aws_security_group" "security_group08" {{
  name        = "group_08_sg"
  description = "security group for group 08"

 # inbound rules
 ingress {{
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }}

 # outbound rules
  egress {{
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }}

  tags= {{
    Name = "security_group08"
  }}
}}	
	""".format(ami ))
	
with open('output.tf', 'w') as f:
	f.write("""output "instance_public_ip" {
	value = "${join(",",aws_instance.group08_instance.*.public_ip)}"
}
	""")

os.system('terraform plan')
os.system('echo "yes" | terraform apply')



print("\n\nec2 instances have been created!")

