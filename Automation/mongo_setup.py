# 50.043 Databases and Big Data Systems: Group Project
# Sets up mongo-flask server
#
# Group 08

import os


key = "ec2-group08-keypair.pem"
#key = "random.pem"
#mongo_ip = "54.236.56.4"

with open('./terraform-group08/ip.txt', 'r') as f: ips = f.readlines()
mongo_ip = ips[2][28:].rstrip('\r\n')

print("MONGO SERVER IP IS: " + mongo_ip)
os.system('scp -i {} -o StrictHostKeyChecking=no mongo_setup.sh ec2-user@{}:/home/ec2-user/mongo_setup.sh'.format(key, mongo_ip))
os.system('scp -i {} -o StrictHostKeyChecking=no mongod.conf ec2-user@{}:/home/ec2-user/mongod.conf'.format(key, mongo_ip))
os.system('ssh -i {} -o StrictHostKeyChecking=no ec2-user@{} -t "sudo chmod +x mongo_setup.sh && sudo ./mongo_setup.sh"'.format(key, mongo_ip))
