# Week 8 — Serverless Image Processing

## Homework Task Performed for Week 8

_AWS Cloud Development Kit (AWS CDK) is an open-source softftware development framework that supports language such as Python, C#, Java, TypeScript, JavaScript and Go. Using CDK, you can build cloud infrastructure with the programming language you are confortable with. In simpler terms, CDK is a tool to define your cloud infratsurcture as a as code._

***Task Performed from Live Stream***
** **
- **Made a new folder and named it as thumbing-serverless-cdk**
```mkdir thumbing-serverless-cdk```

- **From the Gitpod environment, installed AWS cdk**
```npm install aws-cdk -g```

- **From the thumbing-serverless-cdk folder (created in above), installed TypeScript**
```cdk init app --language typescript```

- **To test it, we created a S3 bucket and imported required libraries for it using [TypeScript](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/blob/main/thumbing-serverless-cdk/lib/thumbing-serverless-cdk-stack.ts)**
 ```ts
createBucket(bucketName: string): s3.IBucket {
    const bucket = new s3.Bucket(this, 'UploadsBucket', {
      bucketName: bucketName,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });
    return bucket;
  }
```

_CDK Synth is used to transform defined resource to turn into a CloudFormation template . Moreover, CDK bootstrap is used to provision resource before the deployment process_

```cdk synth```

```cdk bootstrap aws://ACCOUNT-NUMBER/REGION"```

- **To Deploy, after performing bootstrap**
```cdk deploy```

- **If you are unhappy with the deployment,and want to destroy it use the following command**
```cdk destroy``` (**BE VERY CAREFUL** :fearful:)
** **

**Created a new [folder](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/aws/lambdas/process-images) in the `aws/lambdas` by the name of `process-images`**

- **Created a test.js for the lambda function**
```ts
const {getClient, getOriginalImage, processImage, uploadProcessedImage} = require('./s3-image-processing.js')

async function main(){
  client = getClient()
  const srcBucket = 'cruddur-thumbs'
  const srcKey = 'avatar/original/data.jpg'
  const dstBucket = 'cruddur-thumbs'
  const dstKey = 'avatar/processed/data.png'
  const width = 256
  const height = 256

  const originalImage = await getOriginalImage(client,srcBucket,srcKey)
  console.log(originalImage)
  const processedImage = await processImage(originalImage,width,height)
  await uploadProcessedImage(dstBucket,dstKey,processedImage)
}

main()
```

- **Inside the `process-images` folder created above, run the following sript**

```npm init -y```

```npm i sharp```

```npm i @aws-sdk/client-s3```

- **For the said Lambda fuunction, created a trigger accordingly**

![S3 thumbing](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/ce0c3c43-02a5-4978-a7a6-3af6b022cd57)

** **

- **Created API Gateway and named it as the backend of the my Route53 domain name**

![API GATEWAY](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/944c19c0-ec10-4dfa-a48e-0bee2ca3f0ad)

- **Configured  CORS for API Gateway**

![333](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/1e0b21b7-aed4-4cc4-9bfe-4a4af1b5bb1a)
_Click on CLEAR at the top right corner_
 
- **Configured Routes for API Gateway**

![444](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/6f4c9ac8-eccd-43a7-8cd1-e429c1c0a0d4)

- **Configured Lambda Authorizer for API Gateway**
 
![555](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/c929c8bf-4189-428c-8130-89cecb6cfebc)

- **Lambda Code used for Avatar Upload**
```rb
require 'aws-sdk-s3'
require 'json'
require 'jwt'

def handler(event:, context:)
  puts event
  # return cors headers for preflight check
  if event['routeKey'] == "OPTIONS /{proxy+}"
    puts({step: 'preflight', message: 'preflight CORS check'}.to_json)
    { 
      headers: {
        "Access-Control-Allow-Headers": "*, Authorization",
        "Access-Control-Allow-Origin": "https://3000-pratiksinha-awsbootcamp-f5zsfm7tjk7.ws-us96b.gitpod.io",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
      },
      statusCode: 200
    }
  else
    token = event['headers']['authorization'].split(' ')[1]
    

    body_hash = JSON.parse(event["body"])
    extension = body_hash["extension"]

    #decoded_token = JWT.decode token, nil, false
    #cognito_user_uuid = decoded_token[0]['sub']
    
    cognito_user_id = event["requestContext"]["authorizer"]["lambda"]["sub"]
    puts({step: 'presignedurl', access_token: token}.to_json)

    s3 = Aws::S3::Resource.new
    bucket_name = ENV["UPLOADS_BUCKET_NAME"]
    #object_key = "#{cognito_user_uuid}.#{extension}"
    object_key = "#{cognito_user_id}.#{extension}"

    puts({object_key: object_key}.to_json)

    obj = s3.bucket(bucket_name).object(object_key)
    url = obj.presigned_url(:put, expires_in: 60 * 5)
    url # this is the data that will be returned
    body = {url: url}.to_json
    { 
      headers: {
        "Access-Control-Allow-Headers": "*, Authorization",
        "Access-Control-Allow-Origin": "https://3000-pratiksinha-awsbootcamp-f5zsfm7tjk7.ws-us96b.gitpod.io",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
      },
      statusCode: 200, 
      body: body 
    }
  end # if 
end # def handler
```

- **Lambda Authorizer code used in API Gateway**
```js
"use strict";
const { CognitoJwtVerifier } = require("aws-jwt-verify");
//const { assertStringEquals } = require("aws-jwt-verify/assert");

const jwtVerifier = CognitoJwtVerifier.create({
  userPoolId: process.env.USER_POOL_ID,
  tokenUse: "access",
  clientId: process.env.CLIENT_ID//,
  //customJwtCheck: ({ payload }) => {
  //  assertStringEquals("e-mail", payload["email"], process.env.USER_EMAIL);
  //},
});

exports.handler = async (event) => {
  console.log("request:", JSON.stringify(event, undefined, 2));
  const jwt = event.headers.authorization;
  //const jwt = event.headers.authorization('Bearer','');
  var token = jwt.substring(7, jwt.length);
  console.log("event", event);
  console.log("HEADER", token);

  
  try {
    const payload = await jwtVerifier.verify(token);
    console.log("Access allowed. JWT payload:", payload);
    return {
        isAuthorized: true,
        "context": {
            "sub": payload.sub
        },
    };
  } catch (err) {
      console.error("Access forbidden:", err);
      return {
        isAuthorized: false,
      };
  }
  
};
```
** **

**Faced CORS error along with 500 error while uploading image. Eventualy made it work by tweaking the Lambda Authorizer code and by extracting the bearer token which was causing the issue.**
