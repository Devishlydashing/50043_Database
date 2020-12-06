# 50.043 Databases and Big Data Systems: Group Project
# Creates required instances for production and analytics
#
# Group 08

import boto3
import os
import config
import time

# obtain configuration
access_key = config.access_key
secret_key = config.secret_access_key
region = config.region
nodes = config.nodes
ami_ubuntu = 'ami-00ddb0e5626798373'
ami_redhat = 'ami-2051294a'

# for normal aws account (make sure credentials is set up with aws configure)
ec2 = boto3.resource('ec2')

# create key file for instances (using boto3)
#os.system("sudo -u nicholas touch ec2-group08-keypair.pem")
print("*** Creating key-pair as 'ec2-group08-keypair' ***")
outfile = open('ec2-group08-keypair.pem','w')
key_pair = ec2.create_key_pair(KeyName='ec2-group08-keypair')
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)
outfile.close()

# change key permissions
os.system('chmod 400 ec2-group08-keypair.pem')

# create ec2 instances (using terraform)
print("\n*** Creating ec2 instances... This might take awhile... ***")
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
	f.write("""resource "aws_instance" "group08_instance_ubuntu" {{
  ami           = "{}"
  count=2
  key_name = "ec2-group08-keypair"
  instance_type = "t2.xlarge"
  security_groups = ["${{aws_security_group.security_group08.name}}"]
  tags= {{
    Name = "group08-instance_ubuntu"
  }}
}}

resource "aws_instance" "group08_instance_redhat" {{
  ami           = "{}"
  count=1
  key_name = "ec2-group08-keypair"
  instance_type = "t2.xlarge"
  security_groups = ["${{aws_security_group.security_group08.name}}"]
  tags= {{
    Name = "group08-instance_redhat"
  }}
}}

resource "aws_instance" "group08_instance_hadoop" {{
  ami           = "{}"
  count={}
  key_name = "ec2-group08-keypair"
  instance_type = "t2.xlarge"
  security_groups = ["${{aws_security_group.security_group08.name}}"]
  tags= {{
    Name = "group08-instance_hadoop"
  }}
  
  root_block_device {{
    volume_type = "gp2"
    volume_size = "32"
    delete_on_termination = "true"
  
  }}
}}

resource "aws_security_group" "security_group08" {{
  name        = "group_08_sg"
  description = "security group for group 08"

 # inbound rules
 
  ingress {{
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }}

 # outbound rules
  egress {{
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }}


  tags= {{
    Name = "security_group08"
  }}
}}	
	""".format(ami_ubuntu,ami_redhat,ami_ubuntu,nodes))
	
with open('output.tf', 'w') as f:
	f.write("""output "instance_public_ip_ubuntu" {
	value = "${join(",",aws_instance.group08_instance_ubuntu.*.public_ip)}"
}

output "instance_public_ip_redhat" {
	value = "${join(",",aws_instance.group08_instance_redhat.*.public_ip)}"
}

output "instance_public_ip_hadoop" {
	value = "${join(",",aws_instance.group08_instance_hadoop.*.public_ip)}"
}

output "instance_private_ip_hadoop" {
	value = "${join(",",aws_instance.group08_instance_hadoop.*.private_ip)}"
}
	""")

os.system('terraform plan')
os.system('echo "yes" | terraform apply')

# store ec2 instance ip addresses in textfile
os.system('terraform output | sudo tee ip.txt')



print("\n\n*** ec2 instances have been created! ***")
print("Waiting for awhile for servers to fully initialize...")
time.sleep(30)

