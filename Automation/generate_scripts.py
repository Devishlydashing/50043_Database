import config

github_user = config.github_user
github_pass = config.github_pass
nodes = config.nodes

with open('./terraform-group08/ip.txt', 'r') as f: ips = f.readlines()
react_ip = (ips[3].split(","))[1].rstrip('\r\n')
sql_ip = (ips[3].split(","))[0][28:].rstrip('\r\n')
mongo_ip = ips[2][28:].rstrip('\r\n')

# generate sql setup script

with open('sql_setup.sh', 'w') as f:
	f.write("""#!/bin/bash

# update repositories
sudo apt update

# install sqlserver
sudo apt -y install mysql-server
sudo mysql -e 'update mysql.user set plugin = "mysql_native_password" where user="root"'
sudo mysql -e 'create user "root"@"%" identified by "password"'
sudo mysql -e 'grant all privileges on *.* to "root"@"%" with grant option'
sudo mysql -e 'flush privileges'
sudo mysql -e 'set PASSWORD FOR "root"@"localhost" = PASSWORD("password")'
sudo service mysql restart

# get dataset
wget -c https://istd50043.s3-ap-southeast-1.amazonaws.com/kindle-reviews.zip -O kindle-reviews.zip
sudo apt install unzip
unzip kindle-reviews.zip
rm -rf kindle_reviews.json
rm -rf kindle-reviews.zip

# load data into mysql db
sudo mysql -u root -p"password" -e "create database 50043_db"
chmod 777 load_reviews_ec2.sql
sudo mysql -u root -p"password" < load_reviews_ec2.sql
sudo mysql -u root -p"password" 50043_db -e "rename table review to reviews"
sudo mv mysql.conf /etc/mysql/mysql.conf.d/mysqld.cnf
sudo service mysql restart

# install apache
sudo apt update
sudo apt-get -y install apache2
sudo apt-get -y install libapache2-mod-wsgi-py3

# install python3-pip
sudo apt-get -y install python3-pip

# install flask and rest of dependencies
pip3 install flask flask-restful flask_sqlalchemy pymysql
pip3 install flask_cors


# clone github to get flask server files
git clone https://{}:{}@github.com/leeminhan/50.043---Database.git

# set up flask-sql server
mv 50.043---Database flaskapp
sudo ln -sT ~/flaskapp /var/www/html/flaskapp
sudo cp flaskapp/000-default.conf /etc/apache2/sites-enabled/
sudo service apache2 restart
	""".format(github_user, github_pass))

# generate mongodb setup script

with open('mongo_setup.sh', 'w') as f:
	f.write("""#!/bin/bash

# install dependencies
sudo yum -y install git
sudo yum -y install wget
sudo yum -y install unzip

# install pip and relevant dependencies
sudo yum -y install python-setuptools
sudo easy_install pip
sudo pip install flask pymongo bson bs4
sudo pip install -U flask-cors

# set up httpd
sudo yum -y install httpd
sudo yum -y install mod_wsgi
sudo chkconfig --levels 235 httpd on
sudo service httpd restart
sudo /usr/sbin/setsebool -P httpd_can_network_connect 1

# obtain dataset and load into mongodb
sudo wget -c https://istd50043.s3-ap-southeast-1.amazonaws.com/meta_kindle_store.zip -O meta_kindle_store.zip
sudo unzip meta_kindle_store.zip
echo -e "[mongodb-org-4.4]\nname=MongoDB Repository\nbaseurl=https://repo.mongodb.org/yum/redhat/7/mongodb-org/4.4/x86_64/\ngpgcheck=1\nenabled=1\ngpgkey=https://www.mongodb.org/static/pgp/server-4.4.asc" | sudo tee /etc/yum.repos.d/mongodb-org-4.4.repo
sudo yum -y install mongodb-org
sudo systemctl start mongod
sudo mongoimport --db meta --collection newmetadata --file /home/ec2-user/meta_Kindle_Store.json --legacy
# set up apache server
cd /var/www/html
sudo git clone https://{}:{}@github.com/leeminhan/50.043---Database.git
sudo mv 50.043---Database middleware_mongo
cd middleware_mongo
sudo python mongoindex.py
sudo nohup python author.py > /dev/null 2>&1 &
sudo mv middleware-mongo.wsgi middleware_mongo.wsgi
sudo cp httpd.conf /etc/httpd/conf/httpd.conf 
sudo apachectl restart

sudo cp /home/ec2-user/mongod.conf /etc/mongod.conf
sudo service mongod restart
	""".format(github_user, github_pass))
	
# generate react setup script	

with open('react_setup.sh', 'w') as f:
	f.write("""#!/bin/bash

# update respositories
sudo apt update

# download nodejs
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs

# download yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update
sudo apt install --no-install-recommends yarn

# git clone into machine
sudo mkdir /var/www
cd /var/www/
sudo git clone https://{}:{}@github.com/leeminhan/50.043---Database.git

# set permissions to all
cd 50.043---Database
sudo chmod -R 777 frontend

# build
cd frontend
echo 'REACT_APP_MONGO_IP = \"{}\"\nREACT_APP_MYSQL_IP = {}' | sudo tee .env 1>/dev/null
npm install
yarn add semantic-ui-react
npm run build

# install nginx
sudo apt-get -y install nginx

# set config file for nginx
echo -e "server {{\\n        listen 80 default_server;\\n        root /var/www/50.043---Database/frontend/build;\\n        server_name {};\\n        index index.html;\\n        location / {{\\n                try_files \$uri /index.html;\\n        }}\\n}}" | sudo tee /etc/nginx/sites-available/default 1>/dev/null

sudo service nginx restart	
	""".format(github_user, github_pass, mongo_ip, sql_ip, react_ip))
	
	
print("*** Scripts Generated! ***")


# prepare hadoop ips
with open('./terraform-group08/ip.txt', 'r') as f: ips = f.readlines()
hadoop_priv_lst = ips[0].split(",")
hadoop_priv_lst[0] = hadoop_priv_lst[0].split(" ")[2]
hadoop_priv_lst[-1] = hadoop_priv_lst[-1].rstrip('\r\n')

# write hosts
with open('hosts', 'w') as f:
	f.write("127.0.0.1 localhost\n\n")
	f.write("{} com.avg.master\n".format(hadoop_priv_lst[0]))
	for i in range(1, len(hadoop_priv_lst)):
		f.write("{} com.avg.worker{}\n".format(hadoop_priv_lst[i],i))
	f.write("""
# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback 
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
	""")

# write master_script_1
with open('master_script_1.sh','w') as f:
	f.write("""
#!/bin/bash

sudo -u hadoop mkdir /home/hadoop/download
cd /home/hadoop/download
sudo -u hadoop wget https://apachemirror.sg.wuchna.com/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
sudo -u hadoop tar zxvf hadoop-3.3.0.tar.gz
export JH="\/usr\/lib\/jvm\/java-8-openjdk-amd64"
sudo sed -i "s/# export JAVA_HOME=.*/export\ JAVA_HOME=${{JH}}/g" /home/hadoop/download/hadoop-3.3.0/etc/hadoop/hadoop-env.sh


# configure core-site.xml
echo "<?xml version=\\"1.0\\"?>
<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
 <property>
  <name>fs.defaultFS</name>
  <value>hdfs://com.avg.master:9000</value>
 </property>
</configuration>
" | sudo tee /home/hadoop/download/hadoop-3.3.0/etc/hadoop/core-site.xml 1>/dev/null

# configure hdfs-site.xml
# send over (edit value)
echo "<?xml version=\\"1.0\\"?>
<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
 <property>
  <name>dfs.replication</name>
  <value>{}</value>
 </property>
 <property>
  <name>dfs.namenode.name.dir</name>
  <value>file:/mnt/hadoop/namenode</value>
 </property>
 <property>
  <name>dfs.datanode.data.dir</name>
  <value>file:/mnt/hadoop/datanode</value>
 </property>
</configuration>
" | sudo tee /home/hadoop/download/hadoop-3.3.0/etc/hadoop/hdfs-site.xml 1>/dev/null

# configure yarn-site.xml
echo "<?xml version=\\"1.0\\"?>
<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
 <!-- Site specific YARN configuration properties -->
 <property>
  <name>yarn.nodemanager.aux-services</name>
  <value>mapreduce_shuffle</value>
  <description>Tell NodeManagers that there will be an auxiliary
  service called mapreduce.shuffle
  that they need to implement
  </description>
 </property>
 <property>
  <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
  <value>org.apache.hadoop.mapred.ShuffleHandler</value>
  <description>A class name as a means to implement the service
  </description>
 </property>
 <property>
  <name>yarn.resourcemanager.hostname</name>
  <value>com.avg.master</value>
 </property>
</configuration>
" | sudo tee /home/hadoop/download/hadoop-3.3.0/etc/hadoop/yarn-site.xml 1>/dev/null
# ---

# Configure mapred-site.xml
echo "<?xml version=\\"1.0\\"?>
<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
 <!-- Site specific YARN configuration properties -->
 <property>
 <name>mapreduce.framework.name</name>
 <value>yarn</value>
 <description>Use yarn to tell MapReduce that it will run as a YARN application
 </description>
 </property>
 <property>
  <name>yarn.app.mapreduce.am.env</name>
  <value>HADOOP_MAPRED_HOME=/opt/hadoop-3.3.0/</value>
 </property>
 <property>
  <name>mapreduce.map.env</name>
  <value>HADOOP_MAPRED_HOME=/opt/hadoop-3.3.0/</value>
 </property>
 <property>
  <name>mapreduce.reduce.env</name>
  <value>HADOOP_MAPRED_HOME=/opt/hadoop-3.3.0/</value>
 </property>
</configuration>
" | sudo tee /home/hadoop/download/hadoop-3.3.0/etc/hadoop/mapred-site.xml 1>/dev/null

sudo rm /home/hadoop/download/hadoop-3.3.0/etc/hadoop/workers
	""".format(str(int(nodes)-1)))
	for i in range(1, int(nodes)):
		f.write("\necho -e \"com.avg.worker{}\" | sudo tee -a /home/hadoop/download/hadoop-3.3.0/etc/hadoop/workers 1>/dev/null".format(i))
	
	f.write("""
cd /home/hadoop/download
sudo -u hadoop tar czvf hadoop-3.3.0.tgz hadoop-3.3.0

sleep 5 	
	""")
	
	for i in range(1, int(nodes)):
		f.write("\nsudo -u hadoop scp -o StrictHostKeyChecking=no /home/hadoop/download/hadoop-3.3.0.tgz com.avg.worker{}:".format(i))
	
	f.write("""
sudo -u hadoop cp hadoop-3.3.0.tgz /home/hadoop/
sudo tar zxvf /home/hadoop/hadoop-3.3.0.tgz
sudo  mv /home/hadoop/download/hadoop-3.3.0 /opt/
	""")



# write master_script_2
with open('master_script_2.sh','w') as f:
	f.write("""
#!/bin/bash

sudo mkdir -p /mnt/hadoop/namenode/hadoop-hadoop
sudo chown -R hadoop:hadoop /mnt/hadoop/namenode
yes | sudo -u hadoop /opt/hadoop-3.3.0/bin/hdfs namenode -format

#sudo -i -u hadoop sh -c 'export PATH=/opt/hadoop-3.3.0/bin:$PATH'
#sudo -i -u hadoop sh -c 'export PATH=/opt/hadoop-3.3.0/sbin:$PATH'
sudo -i -u hadoop sh -c '/opt/hadoop-3.3.0/sbin/start-dfs.sh && /opt/hadoop-3.3.0/sbin/start-yarn.sh'
sleep 5


# sqoop
cd /home/hadoop/download
sudo -u hadoop wget https://apachemirror.sg.wuchna.com/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
sudo -u hadoop tar zxvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
sudo -u hadoop cp sqoop-1.4.7.bin__hadoop-2.6.0/conf/sqoop-env-template.sh sqoop-1.4.7.bin__hadoop-2.6.0/conf/sqoop-env.sh
export HD="\/opt\/hadoop-3.3.0"
sudo sed -i "s/#export HADOOP_COMMON_HOME=.*/export HADOOP_COMMON_HOME=${HD}/g" /home/hadoop/download/sqoop-1.4.7.bin__hadoop-2.6.0/conf/sqoop-env.sh
sudo sed -i "s/#export HADOOP_MAPRED_HOME=.*/export HADOOP_MAPRED_HOME=${HD}/g" /home/hadoop/download/sqoop-1.4.7.bin__hadoop-2.6.0/conf/sqoop-env.sh
sudo -u hadoop wget https://repo1.maven.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.jar
sudo -u hadoop cp commons-lang-2.6.jar sqoop-1.4.7.bin__hadoop-2.6.0/lib/
sudo cp -rf sqoop-1.4.7.bin__hadoop-2.6.0 /opt/sqoop-1.4.7
sudo apt install libmysql-java
sudo ln -snvf /usr/share/java/mysql-connector-java.jar /opt/sqoop-1.4.7/lib/mysql-connector-java.jar

#spark
cd /home/hadoop/download
sudo -u hadoop wget https://apachemirror.sg.wuchna.com/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz
sudo -u hadoop tar zxvf spark-3.0.1-bin-hadoop3.2.tgz
sudo -u hadoop cp spark-3.0.1-bin-hadoop3.2/conf/spark-env.sh.template spark-3.0.1-bin-hadoop3.2/conf/spark-env.sh
echo -e "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=/opt/hadoop-3.3.0
export SPARK_HOME=/opt/spark-3.0.1-bin-hadoop3.2
export SPARK_CONF_DIR=/opt/spark-3.0.1-bin-hadoop3.2/conf
export HADOOP_CONF_DIR=/opt/hadoop-3.3.0/etc/hadoop
export YARN_CONF_DIR=/opt/hadoop-3.3.0/etc/hadoop
export SPARK_EXECUTOR_CORES=1
export SPARK_EXECUTOR_MEMORY=2G
export SPARK_DRIVER_MEMORY=1G
export PYSPARK_PYTHON=python3" | sudo tee -a spark-3.0.1-bin-hadoop3.2/conf/spark-env.sh

	""")
	for i in range(1, int(nodes)):
		f.write("\necho -e \"com.avg.worker{}\" | sudo tee -a /home/hadoop/download/spark-3.0.1-bin-hadoop3.2/conf/slaves 1>/dev/null".format(i))
		
	f.write("\nsudo -u hadoop tar czvf spark-3.0.1-bin-hadoop3.2.tgz spark-3.0.1-bin-hadoop3.2/\n")
	
	for i in range(1, int(nodes)):
		f.write("\nsudo -u hadoop scp -o StrictHostKeyChecking=no /home/hadoop/download/spark-3.0.1-bin-hadoop3.2.tgz com.avg.worker{}:".format(i))
	
	f.write("""
sudo -u hadoop mv spark-3.0.1-bin-hadoop3.2.tgz /home/hadoop/
cd /home/hadoop
sudo -u hadoop tar zxvf spark-3.0.1-bin-hadoop3.2.tgz
sudo mv spark-3.0.1-bin-hadoop3.2 /opt/
sudo chown -R hadoop:hadoop /opt/spark-3.0.1-bin-hadoop3.2

	""")

with open('master_script_3.sh','w') as f:
	f.write("""#!/bin/bash

cd /home/hadoop

sleep  10
# run sqoop
# DYNAMIC PUT MYSQL IP
yes | sudo -u hadoop /opt/sqoop-1.4.7/bin/sqoop import --table reviews --username root --password password --as-parquetfile -m 1 --connect jdbc:mysql://{}:3306/50043_db?useSSL=false&allowPublicKeyRetrieval=true
# need to click enter to exit command havent check if yes can


# run spark
myFile_new=$(/opt/hadoop-3.3.0/bin/hdfs dfs -find /user/hadoop/reviews/*.parquet)

# check length of parquet file name - might not be 44
myFile=${{myFile_new:21:44}}

sudo -u hadoop mkdir /home/hadoop/reviews
sudo -u hadoop /opt/hadoop-3.3.0/bin/hdfs dfs -get ${{myFile_new}} /home/hadoop/reviews/

sudo apt -y install python3-pip
sudo pip3 install pandas
sudo pip3 install pyarrow
echo -e "
import pandas as pd
df=pd.read_parquet(\\"/home/hadoop/reviews/${{myFile}}\\")
df.to_csv(\\"/home/hadoop/reviews/reviews.csv\\")" | sudo tee test.py
sudo python3 test.py

#sudo -u hadoop /opt/hadoop-3.3.0/bin/hdfs dfs -put /home/hadoop/reviews/reviews.csv
sudo -u hadoop /opt/hadoop-3.3.0/bin/hdfs dfs -put /home/hadoop/reviews/reviews.csv /user/hadoop/reviews
	""".format(sql_ip))


with open('run_analytics.sh','w') as f:
	f.write("""#!/bin/bash

# get spark_app.py
cd /home/hadoop
sudo git clone https://{}:{}@github.com/leeminhan/50.043---Database.git

sudo mv /home/hadoop/50.043---Database/analytics/spark_app.py /user/hadoop/

sudo -u hadoop /opt/hadoop-3.3.0/bin/hdfs dfs -mkdir /user/hadoop/output

sudo -u hadoop /opt/spark-3.0.1-bin-hadoop3.2/bin/spark-submit --master yarn /user/hadoop/spark_app.py

myFiles=$(/opt/hadoop-3.3.0/bin/hdfs dfs -find /user/hadoop/output/*.csv)

sudo -u hadoop /opt/hadoop-3.3.0/bin/hdfs dfs -getmerge ${{myFiles}} /home/hadoop/output/tfidf_results.csv

sudo -u hadoop /opt/hadoop-3.3.0/bin/hdfs dfs -mkdir /user/hadoop/results

sudo -u hadoop /opt/hadoop-3.3.0/bin/hdfs dfs -put /home/hadoop/output/tfidf_results.csv /user/hadoop/results/
	""".format(github_user, github_pass))
	









