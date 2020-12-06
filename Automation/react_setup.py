# 50.043 Databases and Big Data Systems: Group Project
# Sets up react-frontend server
#
# Group 08

import os
import time


key = "ec2-group08-keypair.pem"
#key = "random.pem"

with open('./terraform-group08/ip.txt', 'r') as f: ips = f.readlines()
react_ip = (ips[3].split(","))[1].rstrip('\r\n')


print("REACT SERVER IP IS: " + react_ip)

os.system('scp -i {} -o StrictHostKeyChecking=no react_setup.sh ubuntu@{}:/home/ubuntu/react_setup.sh'.format(key, react_ip))
os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo chmod +x react_setup.sh && sudo ./react_setup.sh"'.format(key, react_ip))


print("""\n\n\n
===================================
Access our bookstore here!  
http://{}/home
===================================\n\n\n
""".format(react_ip))

time.sleep(15)
