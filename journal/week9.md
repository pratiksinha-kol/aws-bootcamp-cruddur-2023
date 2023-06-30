# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

## Homework Task Performed for Week 9


_A pipeline automates the process of software delivery by performing build and deploy process in an automated manner. In our case, we will utilize the benefits of AWS CodePipeline to make it work. This is not a free service, but if you are under Free Tier, you can use one pipeline without paying a penny. _  

_Source repository can be AWS's own CodeCommit, or Bitbucket, and even GitHub. AWS also offers source repository from the S3, and ECR. We will be using GitHub as it is where we have our source code. As we have a running ECS Fargate servcice, we will deploy our changes on it._  



_Before proceeding towards CodePipeline (little bit different from the video), we need to prepare few things for it to work, especifically for CodeBuild._
 

- **In this case, we need to create a [`buildspec.yml`](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/backend-flask/buildspec.yml) file**

```yml
# Buildspec runs in the build stage of your pipeline.
version: 0.2
phases:
  install:
    runtime-versions:
      docker: 20
    commands:
      - echo "cd into $CODEBUILD_SRC_DIR/backend"
      - cd $CODEBUILD_SRC_DIR/backend-flask
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $IMAGE_URL
  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...          
      - docker build -t backend-flask .
      - "docker tag $REPO_NAME $IMAGE_URL/$REPO_NAME"
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker image..
      - docker push $IMAGE_URL/$REPO_NAME
      - cd $CODEBUILD_SRC_DIR
      - echo "imagedefinitions.json > [{\"name\":\"$CONTAINER_NAME\",\"imageUri\":\"$IMAGE_URL/$REPO_NAME\"}]" > imagedefinitions.json
      - printf "[{\"name\":\"$CONTAINER_NAME\",\"imageUri\":\"$IMAGE_URL/$REPO_NAME\"}]" > imagedefinitions.json

env:
  variables:
    AWS_ACCOUNT_ID: 999884903760
    AWS_DEFAULT_REGION: us-east-1
    CONTAINER_NAME: backend-flask
    IMAGE_URL: 999884903760.dkr.ecr.us-east-1.amazonaws.com
    REPO_NAME: backend-flask:latest
artifacts:
  files:
    - imagedefinitions.json
```


- **A json formatted policy [`ecr-codebuild-backend-role.json`](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/aws/policies/ecr-codebuild-backend-role.json).**  



**If you have a backend Fargate service in stopped state, change the desired state to _1_ as we will used it to deploy our `prod` version and see the changes.**


**_From your GitHub account, create a new branch and name it as `prod`. Ensure that a new Pull request is performed to `prod` from `main` branch._**

** **

###CodeBuild


- **Create a  build project and name it as `cruddur-backend-flask-bake-image`**

- **Enable build badge (this is optional)**

- **Select your repository and Source version should be `prod`**

- **Under Environment section, ensure these steps ====>**
	
	- **Opt for Managed Image and select amazon Linux 2 as operting system**

	- **The Role name is automatically genertared after you enter a project name**	 

	- **make necessary changes to the _Additional Configuration_. In our case, we opted for Timeout of 20 minutes and Compute power of 3GB & 2 vCPUs**

- **Under _Primary source webhook events_, select _Rebuild every time a code change is pushed to this repository_. This will ensure that everytime new changes are made to the `prod`, a build action is performed**

- **In the above case, don't forget to select *PULL_REQUEST_MERGED* Event type**

- **Path of the buildspec.yaml file which you had earlier created is present under `backend-flask/buildspec.yml`**

- **No Artifacts should be selected (depending on your choice)**

- **Select CloudWatch logs and give it a name `/cruddur/build/backend` and also a stream name such as `backend-flask`** 


** **


###CodePipeline


- **Create Pipeline and give it a name. In my case, it was `cruddur-backend-fargate`**

- **You will notice that a Role name is created based on the name mentioned above.**

- **To store Artifacts, choose a bucket location that you have previously created.**

- **Now, you have to select the repository. As mentioned previously, we have source from different place, but in this case, we will opt for GitHub Version 2.**

- **Click on Connect to Github (give a connection name). You maybe need to asked to `Install App`. After performing these steps, select the appropriate repository.**

- **Then choose the branch name which is `prod` in our case and leave everything as default.**

_Everytime a new changes are made to the prod branch of your repo, CodePipeline will start to CodeBuild and then perform CodeDeploy_


** **

_CICD in Action_

![11](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/594b0f33-7e55-40d2-8c03-d245597d8543)


![22](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/3b57e37f-8b83-4c27-97fc-42882bb63c78)


![33](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/9c48030c-ebaa-45d2-a497-3dfba6a5b4d1)


_Deployment of changes on ECS Fargate service_

![CodePipeline ECS](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/9139c51a-ee74-42c2-bd87-869fb64be037)


![ECS](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/1ae4966b-6322-4e44-a67b-003096cd9f2b)
