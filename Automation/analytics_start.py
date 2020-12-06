# 50.043 Databases and Big Data Systems: Group Project
# starts spark tasks
#
# Group 08

import os

key = "ec2-group08-keypair.pem"

# obtain hadoop ips
with open('./terraform-group08/ip.txt', 'r') as f: ips = f.readlines()
hadoop_priv_lst = []
hadoop_priv_lst = ips[0].split(",")
hadoop_priv_lst[0] = hadoop_priv_lst[0].split(" ")[2]
hadoop_priv_lst[-1] = hadoop_priv_lst[-1].rstrip('\r\n')

hadoop_pub_lst = []
hadoop_pub_lst = ips[1].split(",")
hadoop_pub_lst[0] = hadoop_pub_lst[0].split(" ")[2]
hadoop_pub_lst[-1] = hadoop_pub_lst[-1].rstrip('\r\n')


# send run_analytics.sh to master node and run
os.system('scp -i {} -o StrictHostKeyChecking=no run_analytics.sh ubuntu@{}:/home/ubuntu/run_analytics.sh'.format(key,hadoop_pub_lst[0]))
os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo chmod +x run_analytics.sh && sudo ./run_analytics.sh"'.format(key, hadoop_pub_lst[0]))

