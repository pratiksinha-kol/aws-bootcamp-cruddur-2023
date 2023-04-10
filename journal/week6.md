# Week 6 — Deploying Containers

## Homework Task Performed for Week 6

- **Provisioned Cruddur cluster where Fargate services would run**
** **

```
aws ecs create-cluster \
--cluster-name cruddur \
--service-connect-defaults namespace=cruddur
```

![ECS Fargate](https://user-images.githubusercontent.com/125117631/230785109-930b23c4-15fb-4d54-a93a-4d740af84b62.png)

- **Created private ECR repository for frontend and backend**
** **

```
aws ecr create-repository \
  --repository-name backend-flask \
  --image-tag-mutability MUTABLE
```

```
aws ecr create-repository \
  --repository-name frontend-react-js \
  --image-tag-mutability MUTABLE
```

![ECR Repositories](https://user-images.githubusercontent.com/125117631/230785305-33953fff-7199-4f8c-94b2-8375c9f2b6f3.png)

- **Register task definitions for frontend and backend**
** **

```
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/backend-flask.json
```
```
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/frontend-react-js.json
```

![ECS Task definitions](https://user-images.githubusercontent.com/125117631/230785293-e1a8d331-642d-429d-b721-cb4476b1366b.png)

- **Build, Tagged and Pushed them on their corresponding repository**
** **

***Need to login to ECR first***

```
aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"
```

```
docker build -t 
```

```
docker tag backend-flask:latest $ECR_BACKEND_FLASK_URL:latest
```

```
docker push $ECR_BACKEND_FLASK_URL:latest
```

*Same task was performed for Frontend-react*

- **Created [bash scripts](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/bin) to ensure easy work for ECR and ECS**

- **Refactored [bin directory](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/bin) and secured Flask so that it doesn't run in debug mode**


- **Start ECS Fargate Service for frontend and backend (Also Created [bash script](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/bin/backend/run) for easy access)**
** **

```sh
aws ecs create-service --cli-input-json file://aws/json/service-backend-flask.json
```

```sh
aws ecs create-service --cli-input-json file://aws/json/service-frontend-react-js.json
```

- **Implemented Service Connect for frontend and backend (Created bash script for easy access)**
** **

```
aws ecs execute-command  \
aws ecs execute-command  \
--region $AWS_DEFAULT_REGION \
--cluster cruddur \
--task $TASK_ID \
--container $CONTAINER_NAME \
--command "/bin/bash" \
--interactive
```

- **Implemented health checks for frontend and backend**
** **

```
@app.route('/api/health-check')
def health_check():
  return {'success': True}, 200
```
***In the task definition for backend-flask***
```
"healthCheck": {
          "command": [
            "CMD-SHELL",
            "python /backend-flask/bin/flask/health-check"
          ],
```

***In the task definition for frontend-react***
```
 "healthCheck": {
          "command": [
            "CMD-SHELL",
            "curl -f http://localhost:3000 || exit 1"
          ],
```

![halth-chck](https://user-images.githubusercontent.com/125117631/230787321-5b1d5d85-1fa1-448f-aa27-184618ee8f52.png)


- **Enabled Container insight**
** **

![Container Insights](https://user-images.githubusercontent.com/125117631/230786068-b24a8639-ca5e-4ccd-b3c2-d9ed13a924bd.png)


- **Modified Docker compose to use only user specific network**
** **

```
networks: 
    cruddur-net:
      driver: bridge
      name: cruddur-net
```

- **Created [Dockerfile](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/backend-flask/Dockerfile.prod) specifically for PROD**

- **Removed [hardcoded](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/docker-compose.yml) environment variables from Docker compose**

- **Generated env from Ruby [scripts](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/erb) for Docker**

```sh
./bin/backend/generate-env
```

```sh
./bin/frontend/generate-env
```

- **Resolved refresh token issue**
** **

![Token issue resolved](https://user-images.githubusercontent.com/125117631/230786533-eebe12de-ba51-4160-983b-e3d012f55619.png)

- **Resolved Timezone issue on Cruddur app (including messaging)**
** **

![T1](https://user-images.githubusercontent.com/125117631/230787443-f0c9df47-37d6-4deb-bc2a-c375f7e6bd5c.png)

![m1](https://user-images.githubusercontent.com/125117631/230787608-b732abea-4e8b-41c5-87d4-7f17ea7c6989.png)
