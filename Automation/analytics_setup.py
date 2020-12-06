# 50.043 Databases and Big Data Systems: Group Project
# Sets up analytics server (hadoop cluster, sqoop, spark)
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


# send first script and hosts file to all
for i in range(len(hadoop_pub_lst)):
	os.system('scp -i {} -o StrictHostKeyChecking=no hosts ubuntu@{}:/home/ubuntu/hosts'.format(key,hadoop_pub_lst[i]))
	os.system('scp -i {} -o StrictHostKeyChecking=no all_script_1.sh ubuntu@{}:/home/ubuntu/all_script_1.sh'.format(key,hadoop_pub_lst[i]))

# run on all
for i in range(len(hadoop_pub_lst)):
	os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo chmod +x all_script_1.sh && sudo ./all_script_1.sh"'.format(key, hadoop_pub_lst[i]))


# walkaround 2
for i in range(len(hadoop_pub_lst)):
	os.system('ssh ubuntu@{} -i {} "sudo cat /home/hadoop/.ssh/id_rsa.pub" | ssh ubuntu@{} -i {} "sudo cat - | sudo tee -a /home/hadoop/.ssh/authorized_keys"'.format(hadoop_pub_lst[0],key,hadoop_pub_lst[i],key))


# send master_script_1.sh to master node
os.system('scp -i {} -o StrictHostKeyChecking=no master_script_1.sh ubuntu@{}:/home/ubuntu/master_script_1.sh'.format(key,hadoop_pub_lst[0]))
os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo chmod +x master_script_1.sh && sudo ./master_script_1.sh"'.format(key, hadoop_pub_lst[0]))


# send worker_script_2 to all worker nodes
for i in range(1, len(hadoop_pub_lst)):
	os.system('scp -i {} -o StrictHostKeyChecking=no worker_script_2.sh ubuntu@{}:/home/ubuntu/worker_script_2.sh'.format(key,hadoop_pub_lst[i]))
	os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo chmod +x worker_script_2.sh && sudo ./worker_script_2.sh"'.format(key, hadoop_pub_lst[i]))


# send master_script_2.sh to master node
os.system('scp -i {} -o StrictHostKeyChecking=no master_script_2.sh ubuntu@{}:/home/ubuntu/master_script_2.sh'.format(key,hadoop_pub_lst[0]))
os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo chmod +x master_script_2.sh && sudo ./master_script_2.sh"'.format(key, hadoop_pub_lst[0]))


# send worker_script_3 to all worker nodes
for i in range(1, len(hadoop_pub_lst)):
	os.system('scp -i {} -o StrictHostKeyChecking=no worker_script_3.sh ubuntu@{}:/home/ubuntu/worker_script_3.sh'.format(key,hadoop_pub_lst[i]))
	os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo chmod +x worker_script_3.sh && sudo ./worker_script_3.sh"'.format(key, hadoop_pub_lst[i]))
	

# send master_script_3 to master node
os.system('scp -i {} -o StrictHostKeyChecking=no master_script_3.sh ubuntu@{}:/home/ubuntu/master_script_3.sh'.format(key,hadoop_pub_lst[0]))
os.system('ssh -i {} -o StrictHostKeyChecking=no ubuntu@{} -t "sudo chmod +x master_script_3.sh && sudo ./master_script_3.sh"'.format(key, hadoop_pub_lst[0]))

# send ip.txt to master node (in /user/hadoop)
os.system('scp -i {} -o StrictHostKeyChecking=no ./terraform-group08/ip.txt ubuntu@{}:/user/hadoop/ip.txt'.format(key,hadoop_pub_lst[0]))









	
	

