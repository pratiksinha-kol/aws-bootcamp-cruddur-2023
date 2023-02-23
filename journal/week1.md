# Week 1 — App Containerization
## Homework Task Performed for Week 1 ##

- **Installed Docker on Windows & ran sample Docker locally**
 
 ![Docker Deskstp](https://user-images.githubusercontent.com/125117631/220989926-048d6d39-42f5-44c1-acb9-caae67c82704.png)

- **Built Docker image via CLI and resolved issue of npm while running it on local Desktop environment**

![Cruddur local error](https://user-images.githubusercontent.com/125117631/220990591-e002229b-adc3-4209-a4ec-263acdf12398.png)
![Cruddur local error-rectification](https://user-images.githubusercontent.com/125117631/220990614-bd894688-a39d-45f8-8adf-bae56ab77d31.png)

- **Ran Cruddur Docker locally after cloning Git**

![Cruddur local 2](https://user-images.githubusercontent.com/125117631/220991127-8164cd28-2362-4513-b450-a9e036a49aca.png)
![Cruddur local 1](https://user-images.githubusercontent.com/125117631/220991164-f63eb466-ace0-42dd-9a63-e75ebb9f91e6.png)

- **Launched EC2 Instance with SSM Role Permission Unlimited burstable t2.micro *(No key pair was used)*** 

- **Installing Docker on launched Amazon Linux 2** [REF LINK](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html)

- **Created Dockerfile on the launched t2 instance** 

![Dockerfile creation on ec2](https://user-images.githubusercontent.com/125117631/220993778-62e31f5f-ecda-486e-add2-368cef025289.png)

- **Build the sample Hello-world Docker file**

 ![Sample Hello World on ec2](https://user-images.githubusercontent.com/125117631/220994838-7cfbb1ce-6189-4152-adb0-0d54679a7e54.png)

- **Ran the sample Hello-world Docker file and tested on browser using Public IP**

 ![Sample Hello World on ec2 saml](https://user-images.githubusercontent.com/125117631/220994695-0477541a-6258-40a4-8c40-6f7069799566.png)
 
- **Logged into Docker from EC2 CLI to pulled Docker and for future push of Docker images** ```docker login -u```

- **Pulled few Docker images on launched Amazon Linux 2** 

![Docker pull image from Docker hub 1](https://user-images.githubusercontent.com/125117631/220995453-8bf55d24-bc7a-4d88-87e3-1ecbc9e73f5a.png)

- **Ran container based on the pulled Docker images**

![Docker pull image from Docker hub run on ec2](https://user-images.githubusercontent.com/125117631/220995769-b9b9da1d-97c2-4745-8318-b8896e15ece5.png)
![Sample WebApp on ec2](https://user-images.githubusercontent.com/125117631/221003160-9cacbb72-2c40-4f9e-8662-fa0d1bcb7c58.png)

- **Exposed port 80 using the following run command. Used Public IPV4 address of the EC2 instance to verify the running status of the container** ```docker run -t -i -p 80:80 Repository-Tag```

- **Install Git In AWS EC2 Instance** [REF LINK](https://cloudaffaire.com/how-to-install-git-in-aws-ec2-instance/)

- **Cloned Cruddur app in /home directory of EC2. Learned that docker-compose is unavailable, even after installing Docker on the instance and thus needs to be installed separately. It was required to build Cruddur docker container** ```docker-compose up```

![Cruddur docker build on ec2](https://user-images.githubusercontent.com/125117631/221002543-44a49c23-f178-4b70-8ed3-2d90d8b34918.png)

- **Installed docker compose on EC2** ```sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/bin/docker-compose && sudo chmod +x /usr/bin/docker-compose && docker-compose --version```
[REF LINK](https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9)

- **Ran the Cruddur app**

![Cruddur app on ec2](https://user-images.githubusercontent.com/125117631/221002672-7ff159d7-9119-4358-b010-f9f64e604776.png)
![Cruddur app on ec2 11](https://user-images.githubusercontent.com/125117631/221002677-670bae28-79e9-48b0-be25-683441d122c2.png)
![Cruddur app on ec2 22](https://user-images.githubusercontent.com/125117631/221002657-e40d39dd-1a3f-4bf8-b81e-ce333732d951.png)

- **Pushing Docker image to Docker hub public repository after tagging each of them**

![Docker Hub push](https://user-images.githubusercontent.com/125117631/221003264-3c89388a-10b3-4d0f-8626-5f1955c83d11.png)
```docker image push```
```docker tag IMAGE_ID REPOSITORY/VERSION```

- **While running and eventually stopping Docker container locally, encountered that volumes were still *in-use* on Docker Destop app, even after confirming that the container was stopped. To rectify this issue, used following commands** [REF LINK](https://stackoverflow.com/questions/34658836/docker-is-in-volume-in-use-but-there-arent-any-docker-containers)
```docker container prune```
```docker volume prune```
