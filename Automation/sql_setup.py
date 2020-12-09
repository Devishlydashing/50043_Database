# 50.043 Databases and Big Data Systems: Group Project
# Sets up sql-flask server
#
# Group 08

import os

key = "ec2-group08-keypair.pem"
#key = "random.pem"

#sql_ip = "100.25.37.225"
with open('./terraform-group08/ip.txt', 'r') as f: ips = f.readlines()
sql_ip = (ips[3].split(","))[0][28:].rstrip('\r\n')
print("SQL SERVER IP IS: " + sql_ip)

os.system('scp -i {} -o StrictHostKeyChecking=no ../scripts/load_reviews_ec2.sql ubuntu@{}:/home/ubuntu/load_reviews_ec2.sql'.format(key, sql_ip))
os.system('scp -i {} -o StrictHostKeyChecking=no mysql.conf ubuntu@{}:/home/ubuntu/mysql.conf'.format(key, sql_ip))
os.system('scp -i {} -o StrictHostKeyChecking=no sql_setup.sh ubuntu@{}:/home/ubuntu/sql_setup.sh'.format(key, sql_ip))
os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo chmod +x sql_setup.sh"'.format(key, sql_ip))
os.system('scp -i {} -o StrictHostKeyChecking=no ./terraform_group08/ip.txt ubuntu@{}:/home/ubuntu/ip.txt'.format(key, sql_ip))
#os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -n -t "sudo nohup ./sql_setup.sh > /dev/null 2>&1 &"'.format(key, sql_ip))
os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo ./sql_setup.sh"'.format(key, sql_ip))



