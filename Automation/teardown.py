# 50.043 Databases and Big Data Systems: Group Project
# Automation Script - teardown
# Destroys created ec2 instances, security groups, key-pairs as well as
# uninstalls dependencies
#
# Group 08

import os

os.chdir('./terraform-group08')
os.system('echo "yes" | terraform destroy')
os.chdir('..')
os.system('sudo rm -r terraform-group08')
os.system('sudo rm /usr/bin/terraform')
os.system('sudo rm -f ec2-group08-keypair.pem')
os.system('sudo rm -f terraform_0.13.5_linux_amd64.zip')
os.system('sudo rm -f awscliversion2.zip')
os.system('sudo rm -r aws')
