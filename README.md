# 1-shot-IFC
Single window system to configure and deploy a data flow processors, excecution stacks such as Function as Service(FaaS) at Fog and Cloud enviornment. The main objective of the project is to develop a toolset that can configure the fog enviornment with cloud connection along with necessary softwares required for data driven excecution using various commands. 

The system has the following components:

Add- diagram 
Write all the main components 

##Command line tool should be main focus here-
##Than try to add step by step configuration steps 


## Configuring cloud:
<br>

#### I. Installing Docker:
Create a directory in the virtual machine in the path: 
```
sudo mkdir /etc/docker
```
Create a file in the docker directory: 
```
sudo nano /etc/docker/daemon.json
```
Copy the following script:
```
{
"default-address-pools": [{"base":"172.80.0.0/16","size":24}]
}
```
Update the apt repo:
```
sudo apt-get update
```
Install packages to allow apt to use a repository over HTTPS:
```
sudo apt-get install apt-transport-https
sudo apt-get install ca-certificates
sudo apt-get install curl
sudo apt-get install gnupg-agent
sudo apt-get install software-properties-common
```
Add Docker’s official GPG key
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
Use the following command to set up the stable repository:
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
Update the apt package index:
```
sudo apt-get update
```
Install the docker:
```
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
<br><br>
#### II. Installing NiFi Docker:
Create a docker container with apache nifi image from docker hub using the following command line command:
```
sudo docker run --name nifi \
-p 8080:8080 \
-p 8081:8081 \
-d \
-e NIFI_WEB_HTTP_PORT='8080' \
apache/nifi:latest
```
```
sudo docker run --name nifi -p 8080:8080 -p 8081:8081 -d -e NIFI_WEB_HTTP_PORT='8080' apache/nifi:latest
```
The NiFi will run inside the docker container and the NiFi 8080 web interface port will be made available through the instance.
To access NiFi web interface, you can direct your browser to the following address <IP of Nifi Instance>:8080/nifi, afetr replacing the IP with the OpenStack instance IP.

<br><br>

#### III. Installing python3
```
sudo apt-get update
sudo apt-get install python3.6
```

<br><br><br>

## Configuring Fog Raspberry Pi

<br>

#### I. Installing MiNiFi:

Install Java
```
sudo apt-get update
sudo apt install openjdk-8-jdk
```
Install unzip
```
sudo apt install unzip
```
Install MiNiFi service:
```
wget https://downloads.apache.org/nifi/minifi/0.5.0/minifi-0.5.0-bin.zip
unzip minifi-0.5.0-bin.zip
cd minifi-0.5.0/
sudo bin/minifi.sh install
```
Install MiNiFi toolbox:
```
cd ~
wget https://downloads.apache.org/nifi/minifi/0.5.0/minifi-toolkit-0.5.0-bin.zip
unzip minifi-toolkit-0.5.0-bin.zip
```
Run/stop minifi:
```
/bin/minifi.sh run	: to run on foreground
/bin/minifi.sh {start|stop|run|restart|status|flowStatus|dump|install} : to run on background
```
Add a work flow:
Add config.yml to minifi/conf and restart the minifi

<br><br>
#### II. Installing Docker:
Create a directory in the virtual machine in the path: 
```
sudo mkdir /etc/docker
```
Create a file in the docker directory: 
```
sudo nano /etc/docker/daemon.json
```
Copy the following script:
```
{
"default-address-pools": [{"base":"172.80.0.0/16","size":24}]
}
```
Update the apt repo
```
sudo apt-get update
```
Install docker:
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
<br><br>
#### III. Installing Swarm:
Update the apt repo
```
sudo apt-get update
```
Install swarm:
```
sudo docker swarm init
```
If there are multiple raspberry pies to run swarm, install docker and swarm as mentioned above.
At worker machine type below command to join swarm cluster:
```
docker swarm join --token <TOKEN> <IP ADDRESS>:2377
```
<br><br>
#### IV. Installing openfaas:
Install the faas-cli:
```
curl -sL https://cli.openfaas.com | sudo sh
```
Install the OpenFaas:
```
cd ~
mkdir openfaas
cd openfaas
git clone https://github.com/openfaas/faas
cd faas
sudo ./deploy_stack.sh
```
Then save the username and password

Access the UI at:
http://<ip_address>:8080


<br><br><br>

## Configuring IoT Raspberry Pi 
<br>

#### I. Installing MiNiFi:
Install Java
```
sudo apt-get update
sudo apt install openjdk-8-jdk
```
Install unzip
```
sudo apt install unzip
```
Install MiNiFi service:
```
wget https://downloads.apache.org/nifi/minifi/0.5.0/minifi-0.5.0-bin.zip
unzip minifi-0.5.0-bin.zip
cd minifi-0.5.0/
sudo bin/minifi.sh install
```
Install MiNiFi toolbox:
```
cd ~
wget https://downloads.apache.org/nifi/minifi/0.5.0/minifi-toolkit-0.5.0-bin.zip
unzip minifi-toolkit-0.5.0-bin.zip
```
Run/stop minifi:
```
/bin/minifi.sh run	: to run on foreground
/bin/minifi.sh {start|stop|run|restart|status|flowStatus|dump|install} : to run on background
```
Add a work flow:
Add config.yml to minifi/conf and restart the minifi
<br><br>

