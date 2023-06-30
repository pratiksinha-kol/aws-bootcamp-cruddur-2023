# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

## Homework Task Performed for Week 9


Source can be AWS's own CodeCommit, Bitbucket, and even GitHub. AWS also offers source repository from the S3, and ECR.


**before proceeding towards CICD (Codebuild, CodePipeline and CodeDeply), we need to prepare few things for it to work.** 

- **In this case, we need to create a [`buildspec.yml`](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/backend-flask/buildspec.yml) file**

- **A json formatted policy [`ecr-codebuild-backend-role.json`](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/aws/policies/ecr-codebuild-backend-role.json).**  



**If you have a backend Fargate service in stopped state, change the desired state to _1_ as we will used it to deploy our `prod` version and see the changes.**


**_From your GitHub account, create a new branch and name it as `prod`. Ensure that a new Pull request is performed to `prod` from `main` branch._**

**CodeBuild** 


- **Create a  build project and name it as `cruddur-backend-flask-bake-image`**

- ** **

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


**CodePipeline** 


- **Create Pipeline and give it a name. `cruddur-backend-fargate`**

- **You will notice that a Role name is created based on the name mentioned above.**

- **To store Artifacts, choose a bucket location that you have previously created.**

- **Now, you have to select the repository. As mentioned previously, we have source from different place, but in this case, we will opt for GitHub Version 2.**

- **Click on Connect to Github (give a connection name). You maybe need to asked to `Install App`. After performing these steps, select the appropriate repository.**

- **Then choose the branch name which is `prod` in our case and leave everything as default.**

- ****
