# 1-shot-IFC
Single window to bring and integrate IoT, fog and cloud environment.


## Configuring cloud:


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

#### III. Installing python3
```
sudo apt-get update
sudo apt-get install python3.6
```




