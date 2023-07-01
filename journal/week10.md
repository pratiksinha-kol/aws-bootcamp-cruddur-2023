# Week 10 — CloudFormation


## Homework Task Performed for Week 10


_AWS CloudFormation Linter (also called as cfn-lint) is a tool that helps validate your CloudFormation template. The rules used by cfn-lint are guided by the AWS CloudFormation resource specification._

_TOML is a minimalistic and human readable configuration file. This stores all your configuration data, which will be used by our template for setting up CloudFormation._

_CloudFormation Guard is another tool that we will use, and it is a Domain-specific language that expresses policy as a code evaluation tool._

_As mentioned above, we need to include cfn-lint along with cfn-toml and cfn-guard, to begin our work with CloudFormation tasks. Hence, we start in the GitPod.yml file. In the gitpod.yml file, ensure that cfn-lint along with cfn-toml, cfn-guard and bundler._

```yml
- name: cfn
    before:
      pip install cfn-lint
      gem install cfn-toml
      bundle update --bundler
      cargo install cfn-guard 
```

_While working with CloudFormation on Gitpod, you might encounter some errors regarding the intrinsic function that we will use in the template._ 

_To manage these errors, you need to make a few changes in the settings.json under .vscode. Add the following to make it work without any issues that you might encounter._

```json
{
    "githubPullRequests.ignoredPullRequestBranches": [
        "main"
    ],
    "yaml.customTags": [
        "!Sub",
        "!Ref",
        "!Select",
        "!GetAtt",
        "!Join",
        "!Select sequence",
        "!split sequence",
        "!Join sequence",
        "!Import",
        "!GetAtt",
        "!GetAZs",
        "!FindInMap",
        "!Equals",
        "!Equals sequence",
        "!If sequence",
        "!If"
    ],
    "yaml.schemas": {
        "/workspace/aws-bootcamp-cruddur-2023/aws/cfn/service/template.yaml": "template.yaml",
    }
}
```

Create a S3 bucket where templates will be saved. The name of my bucket is `cfn-artifacts-cruddur-pratiksinha`.

Set it as an env variable for your GitPod environment

```
export CFN_BUCKET=cfn-artifacts-cruddur-pratiksinha	
gp env CFN_BUCKET=cfn-artifacts-cruddur-pratiksinha
```

Under the AWS folder, create a new folder and name it as [`cfn`](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/aws/cfn). This is where we would save all of our template files and their environment variables as ```config.toml``` file. All the templates would be saved here under appropriate names such as db, cicd, rds, cluster (backend service), ddb (dynamodb), networking, and frontend.  

- For each config.toml file, you must mention your own Region, Bucket, Stack Name and Parameters.

- We will build our whole CloudFormation infrastructure by executing bash command. The [scripts](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/bin/cfn) are under ```aws-bootcamp-cruddur-2023/bin/cfn```


** ** 



### Networking


- Ensure that all the GitPod commands (under name cfn) mentioned earlier are completed beforehand.

- To build the networking infrastructure, we will execute ```./bin/cfn/networking```.

- Bucket name under the ```config.toml``` file should be named after the bucket that you created for this purpose.

- Go to AWS CloudFormation and perform ```Execute ChangeSet``` to complete the process. This step is applicable for all the CloudFormation deployment, and it ensures you are in control of what needs is being deployed.

- _Mine VPC CIDR, Subnets and Region are different from the video._


** ** 



### Fargate Cluster Deployment


- In this step, we will be building an ECS cluster that supports Fargate by executing ```./bin/cfn/cluster```

- We will create an Application Load Balancer (ALB) and assign a security group to it.

- HTTP Listener is configured here and determines which traffic goes to which endpoint.

- _**FYI: Do remember to configure your Route53 that points to the `A Record` to `api.<domain_name>` after the creation of ALB.**_

- Test to see if your configured Route53 is working or not `api.pratiksinha.link` or `api.<domain_name>`.


** **



### RDS Database


- Before beginning of the creation process of the RDS Database, you need to configure your RDS Database Password.   

- Set it as an env variable for your GitPod environment.

	```
	export DB_PASSWORD=yyyyyyxxxxxxx
	gp env DB_PASSWORD=yyyyyyxxxxxxx
	```

- In this step, we will be building an RDS Database using Postgres.

- We will execute this ```./bin/cfn/cluster``` to setup our database. Be patient, as it will take few minutes to complete the setup.

- When not using the database, you can stop it. However, remember that after 7 days, it automatically starts without any prompt.

- Under the Db identifier, verify that it shows ```cruddur-instance```.

- After successfull completion of Database creation, you need to copy the DNS Name of the Database and copy it in the AWS System Manager `Parameter Store` of `/cruddur/backend-flask/CONNECTION_URL`.


** ** 



### Backend ECS Service 


- In this step, we will be building an ECS backend service.

- To do that just execute this ```./bin/cfn/service```

- If you notice that task are getting deployed and failing due to health check, you need to do an extra step.

- When we created ```Fargate Cluster Deployment```, along with ALB, Target Group was also created with it.  

- **In the _CrdClusterBackendTG_ Target Group, modify the health check setting. Override the port to `4567` from `80`.**

- After a while, you will notice that backend service are no longer failing health checks.

- To further confirm it, visit the Backend URL. `api.pratiksinha.link` or `api.<domain_name>`


![CFN](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/4f3c634c-cfe3-4951-87e3-c1c3cdfa4a7d)



** **



### DynamoDb Table 


- To deploy DynamoDb table, we won't be using CloudFormation, but will use SAM (Serverless Application Model).

- SAM is an framework with which you can build serverless application like Lambda, DynamoDb, Api and others. SAM uses CloudFormation in the background and it generates template like we encountered during Networking, ECS Cluster and ECS Service Deployment.  

- In our SAM template, we deploy oy DynamoDB, Lambda function and its execution role. We have also created CloudWatch LogGroups, to check out DynamoDb stream logs. 

- To get an in-depth idea about the creation of SAM Template, visit the [GitHub repo](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/ddb/template.yaml).

- You need to install SAM before using it. For that execute these steps: 
	
```
wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
sudo ./sam-installation/install
sam --version
```

- SAM Process
 	
	- To initialize SAM application, run `sam init`

	- To build SAM application, run `sam build`. In our case, we will use `sam build --use-container`

	- To package the SAM Application and create a `.zip` folder and upload it to the bucket, run ```sam package```.

	- To deploy SAM application, run `sam deploy`.

- We have broken these steps and created an individual bash script. So, you just need to execute 

	```./ddb/build```

	```./ddb/package```

	```./ddb/deploy```



** **



### CICD


- For CICD, you need to create a seperate S3 Bucket. I have named it as `codepipeline-cruddur-artifacts-pratik`.

- After creating the S3 bucket and assigning it to the config file, run ```./bin/cfn/cicd```.

- This CloudFormation template, uses Nested Stack. So, you will see a new stack being created along with it. **DO NOT DELETE OR MODIFY**

- Ensure that the `config.toml` file is correctly set, otherwise your CodePipeline will fail. Here is an example of the configuration of CloudFormation and CICD


```
[deploy]
bucket = 'cfn-artifacts-cruddur-pratiksinha'
region = 'us-east-1'
stack_name = 'CrdCicd'

[parameters]
ServiceStack = 'CrdSrvBackendFlask'
ClusterStack = 'CrdCluster'
GitHubBranch = 'prod'
GithubRepo = 'pratiksinha-kol/aws-bootcamp-cruddur-2023'
ArtifactBucketName = "codepipeline-cruddur-artifacts-pratik"
BuildSpec = 'backend-flask/buildspec.yml'
``` 

- Wait for the completion of the CloudFormation, now you need to connect your CICD Pipeine to your GitHub account. 

-  For this, go to `Developer Tools`, then to `Connections`. You will need to click on the `Update Pending Connection`, and from there select `Select your GitHub repo username`. 


![CFN CLSTER](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/27f51ab3-ecfe-474e-b3e1-f816d7585a11)



** **



**AWS RDS Database and Application Load Balancer (created during Cluster service deployment) cost money. You can stop the RDS Database the save the money, but there is no way where you can disable ALB.**

**To save the cost of running, I deleted the CloudFormation cluster after finishing my work and stop the RDS instance when not needed.RDS Instance will automatically start after 7 days, so be alert.**

**Similarly, running ECS Task also cost money, but it is easily managed, by updating task to `0`. This will ensure that no more Fagate task are running in the background.** 



** **
