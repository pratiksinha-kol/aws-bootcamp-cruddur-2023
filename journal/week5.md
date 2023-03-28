# Week 5 — DynamoDB and Serverless Caching

## Homework Task Performed for Week 5

- **Added Python in [```requirements.txt```](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/backend-flask/requirements.txt)**
** **
```
boto3
```

- **Created utility [```scripts```](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/backend-flask/bin/db) for Relational Database**
** **

```
#! /usr/bin/bash
set -e # stop if it fails at any point

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-setup"
printf "${CYAN}==== ${LABEL}${NO_COLOR}\n"

bin_path="$(realpath .)/bin"

source "$bin_path/db/drop"
source "$bin_path/db/create"
source "$bin_path/db/schema-load"
source "$bin_path/db/seed"
python "$bin_path/db/update_cognito_user_ids"
```

- **Created utility [```scripts```](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/backend-flask/bin/ddb) for DynamoDB Database**
** **
[```schema-load```](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/backend-flask/bin/ddb/schema-load)
[```seed```](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/backend-flask/bin/ddb/seed)
[```list-tables```](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/backend-flask/bin/ddb/list-tables)
[```drop```](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/backend-flask/bin/ddb/drop)

- **Worked on Message section of Cruddur to send messages**
** **
***Posted message and verified***

![1](https://user-images.githubusercontent.com/125117631/228142967-a3d15f42-31b9-460d-8210-2ed8d3c75b0b.png)


- **Ensured Cruddur application functioning after implementing ***Messaging*** service**
** **
***Cruddur app***

![3](https://user-images.githubusercontent.com/125117631/228144044-d4bdff58-3eda-41c6-82d3-efc49b6ed45b.png)

- *****Ensured Global Secondary Index (GSI)*** is created & working on AWS Prod environment**
** **
![gsi prod](https://user-images.githubusercontent.com/125117631/228145939-e554fcca-537e-4c4c-8dd4-5b5a11ad8e87.png)

- **Enabled DynamoDB stream on the Prod table to capture only NEW ADDITIONS**
** **
![Dynam_tams](https://user-images.githubusercontent.com/125117631/228146229-ff045326-d9e3-4b2e-a687-0c0accc966a7.png)

![DynamDBStream_mssag](https://user-images.githubusercontent.com/125117631/228146362-15c6fe95-2871-4d4d-bee9-bc87a4d28bdc.png)

- **Created [Lambda](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/aws/lambdas/cruddur-messaging-stream.py) function and inculcated it on DynamoDB stream as trigger**
** **

- **Implemented message with ```UUID```**

![2](https://user-images.githubusercontent.com/125117631/228143272-1d8d2eb6-3098-41d6-b6db-e69d3e1d18ba.png)

- **Verified on CloudWatch logs to see it is working properly and not throwing any error**
** **
