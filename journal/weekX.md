# Week X — Cleanup

## Homework Task Performed for Week X

_For this last week of bootcamp, we have to make changes and refactor few things so that our application runs without running into any issues on production. All these while we have performing our task on Gitpod and now its time to modify our application that it works without Gitpod_

_Since, we have already implemented Cloudformation for our services such as VPC, RDS Database, Fargate, ECS Backend service, DynamoDB and CICD, we have to integrate it with our production environment._ 


** **



### Frontend Static Website Hosting

- We have to create a static webpage so that users can access our application using the Domain name. 

- We will not only upload our local components folder to S3 but also invalidate cache from the CloudFront distribution.

- To achieve this task, we will used a newly created [script](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/bin/frontend/static-build) i.e. `bin/frontend/static-build` 

- Now, you need to create a zip file (`zip -r build.zip build/`) to upload to your domain named S3 bucket. In my case, it is `pratiksinha.link`

- Under the `erb/sync.env.erb`, you need to ensure the details of your setup (S3 Bucket and CloudFront Distribution ID). 

- Before executing our sync command, we need to perform additional steps. For example, created [Gemfile](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/Gemfile), and [Rakefile](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/Rakefile) 

- Execute the following commands on your GitPod environment, `gem install aws_s3_website_sync` and `gem install dotenv`.

- Ensure that env are enerated, if not use the following command `bin/frontend/generate-env`

- After completion of the above steps, you now need to execute the `bin/frontend/sync`. 

- For the domain name S3 bucket `pratiksinha.link`, you need to create a Role for actions such as GetObject, ListObject, PutObject and DeleteObject.

- Benefit of performing all these steps is that if you make any changes, you can execute the following command `bin/frontend/static-build` and `bin/frontend/sync`. It will not only not only build the package, but also invalidate cache of the CloudFront distribution. 


** ** 



### Production Database

- Assuming you are already running Postgres RDS Database using CloudFormation. We now need to make some changes for the data to reflect on the frontend of the website.

- Check if the PROD_CONNECTION_URL is updated in your SSM Parameter Store.  

- Go to Security Group section on you AWS portal and jot down RDS Security Group ID and Rule ID. We are going to need it. 

- Edit Inbound Rules and Add a new rule to your RDS Security Group and on port 5432 that allows connection to your IP only. Name it as GitPod.

- The newly created Security Group Rule ID needs to be updated and set it as your Gitpod env variables. Run the following `export GITPOD_IP=$(curl ifconfig.me)`, `./bin/rds/update-sg-rule`, `./bin/db/schema-load prod`. 

- We are performing all the above steps so that we can access our production database from our local environment. 

- To add column `bio` in the database, run `CONNECTION_URL=$PROD_CONNECTION_URL ./bin/db/migrate`.

- Moreover, in the `cruddur-post-confirmation` Lambda function, chose the production RDS Endpoint as your `CONNECTION_URL`. Since, it is under VPC, you have make sure that the security group is allowed in the RDS Security Group.  


** **


### Date Time issue, Activity Page Changes and other additonal changes

_We also resolved the Date time [issue](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/commit/9d409ba85be48dfe9bb2932056b061e5d8a077b6) and [fixed](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/commit/a9fe51719e4aa9746bd7d8947c3f4c5d5801d75d) Activity Show page_  


** **



### Improved Error handling  


_When we were working on the Cruddur homepage, error handling was not done properly and we had to inspect the webpage each time to know the exact reason for the webpage not functioning properly. To handle such errors in a more elegnat maaner, we altered the [code](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/commit/42b52a4ea82212c050e4001e183fcc74e5f426d4)._ 


** ** 



### Fix migration and made some UI changes

_There was issue while running migration `bin/db/migrate`. Resolved this issue by [modifying](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/commit/b1f5b7f447b45f659bdfe5ad57290d2a39a2d773) the time of the file._

_We also made changes to the Cruddur webpage to compensate for the code [changes](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/commit/118aa0724ea47c33b43ae6e4c8febad6362d3bce) that were performed._

_Moreover, as suggested we created an alternate account to ensure that we can post messages on Crud and also post reply_  


** **


### Cleanup


_Since, we created a production DynamoDb, as a security practice, we need to create a new user with limited permissions. The new user would have full DynamoDb Access and nothing else. After creating the user, generate access keys and secret access key. Store them in Parameter Store._ 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:GetItem",
                "dynamodb:Scan",
                "dynamodb:Query",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem",
                "dynamodb:BatchWriteItem"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```

_Now, we pull the code to the prod Github. It will automatically trigger a CICD pipeline event. Wait for it to complete_


_Now, we need to sync it to the Prod frontend. Execute `./bin/frontned/static-build`. It will invalidate the CloudFront cache and it does take time. You can visit the AWS CloudFront page to see if the changes were performed successfully._



** **
