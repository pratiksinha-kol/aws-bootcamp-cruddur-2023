# Week 1 — App Containerization
## Homework Task Performed for Week 1 ##

- **Installed Docker on Windows & ran sample Docker locally** ![Docker Deskstp](https://user-images.githubusercontent.com/125117631/220989926-048d6d39-42f5-44c1-acb9-caae67c82704.png)

- **Built Docker image via CLI and resolved issue of npm while running it on local Desktop environment**
![Cruddur local error](https://user-images.githubusercontent.com/125117631/220990591-e002229b-adc3-4209-a4ec-263acdf12398.png)
![Cruddur local error-rectification](https://user-images.githubusercontent.com/125117631/220990614-bd894688-a39d-45f8-8adf-bae56ab77d31.png)

- **Ran Cruddur Docker locally after cloning Git** ![Cruddur local 2](https://user-images.githubusercontent.com/125117631/220991127-8164cd28-2362-4513-b450-a9e036a49aca.png)
![Cruddur local 1](https://user-images.githubusercontent.com/125117631/220991164-f63eb466-ace0-42dd-9a63-e75ebb9f91e6.png)

- **Launched EC2 Instance with SSM Role Permission Unlimited burstable t2.micro *(No key pair was used)*** 

- **Installing Docker on launched Amazon Linux 2** [REF USED](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html)

- **Created Dockerfile on the launched t2 instance** 
![Dockerfile creation on ec2](https://user-images.githubusercontent.com/125117631/220993778-62e31f5f-ecda-486e-add2-368cef025289.png)

- **Ran the sample Hello-world Docker file** ![Sample Hello World on ec2](https://user-images.githubusercontent.com/125117631/220994838-7cfbb1ce-6189-4152-adb0-0d54679a7e54.png)

- **Ran the sample Hello-world Docker file** ![Sample Hello World on ec2 saml](https://user-images.githubusercontent.com/125117631/220994695-0477541a-6258-40a4-8c40-6f7069799566.png)

- **Pulled few Docker images on launched Amazon Linux 2** 
![Docker pull image from Docker hub 1](https://user-images.githubusercontent.com/125117631/220995453-8bf55d24-bc7a-4d88-87e3-1ecbc9e73f5a.png)

- **Ran container based on the pulled Docker images**![Docker pull image from Docker hub run on ec2](https://user-images.githubusercontent.com/125117631/220995769-b9b9da1d-97c2-4745-8318-b8896e15ece5.png)
![Sample Hello World on ec2 saml](https://user-images.githubusercontent.com/125117631/220995800-aa8232b5-29d6-4c91-ab00-a9560443f56d.png)

- **Exposed port 80 using the following run command. Used Public IPV4 address of the EC2 instance to verify the running status of the container** ```docker run -t -i -p 80:80 Repository-Tag```

- ****
