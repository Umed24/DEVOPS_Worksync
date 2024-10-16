#!/bin/bash
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo docker pull umed24/worksync:01
sudo docker run -d -p 1000:1000 -p 3000:3000 --name worksync_app umed24/worksync:01
