#!/bin/bash

sudo -u hadoop tar zxvf /home/hadoop/hadoop-3.3.0.tgz -C /home/hadoop/
sudo mv /home/hadoop/hadoop-3.3.0 /opt/
sudo mkdir -p /mnt/hadoop/datanode/
sudo chown -R hadoop:hadoop /mnt/hadoop/datanode/

