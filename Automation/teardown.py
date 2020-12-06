# 50.043 Databases and Big Data Systems: Group Project
# Automation Script - teardown
# Destroys created ec2 instances, security groups, key-pairs as well as
# uninstalls dependencies
#
# Group 08

import os
import boto3

ec2 = boto3.client('ec2')
ec2.delete_key_pair(KeyName='ec2-group08-keypair')
print("*** ec2-group08-keypair has been deleted ***\n")
os.chdir('./terraform-group08')
os.system('echo "yes" | terraform destroy')
os.chdir('..')
os.system('sudo rm -r terraform-group08')
print("\n*** AWS Instances have been destroyed ***\n")
os.system('sudo rm /usr/bin/terraform')
os.system('sudo rm -f ec2-group08-keypair.pem')
os.system('sudo rm -f terraform_0.13.5_linux_amd64.zip')
os.system('sudo rm -f awscliversion2.zip')
os.system('sudo rm -r aws')
os.system('sudo rm sql_setup.sh')
os.system('sudo rm mongo_setup.sh')
os.system('sudo rm react_setup.sh')
os.system('sudo rm config.py')
os.system('sudo rm master_script_1.sh')
os.system('sudo rm master_script_2.sh')
os.system('sudo rm master_script_3.sh')
os.system('sudo rm run_analytics.sh')
os.system('sudo rm hosts')

print("*** security_group08 has been destroyed ***\n\n")
print("=========================\n|   TEARDOWN COMPLETE   |\n=========================")
