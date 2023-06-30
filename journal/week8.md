# Week 8 — Serverless Image Processing

## Homework Task Performed for Week 8

_AWS Cloud Development Kit (AWS CDK) is an open-source softftware development framework that supports language such as Python, C#, Java, TypeScript, JavaScript and Go. Using CDK, you can build cloud infrastructure with the programming language you are comfortable with. In simpler terms, CDK is a tool to define your cloud infratsurcture as a code._

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
**CDK with create the bucket `cruddur-upload-avatars`**

_CDK Synth is used to transform defined resource to turn into a CloudFormation template . Moreover, CDK bootstrap is used to provision resource before the deployment process_

```cdk synth```

```cdk bootstrap aws://ACCOUNT-NUMBER/REGION"```

- **To Deploy, after performing bootstrap**
```cdk deploy```

- **If you are unhappy with the deployment and want to destroy it use the following command**
```cdk destroy``` (**BE VERY CAREFUL** :fearful:)

**I manually created a S3 bucket by the name of `assets.pratiksinha.link(asset.domainname)`, which will in future be used by Cloudfront. Also set Domain name in the Gitpod environment.**

**Set these environment variables in Gitpod**
```
export DOMAIN_NAME=pratiksinha.link	
gp env DOMAIN_NAME=pratiksinha.link
export UPLOADS_BUCKET_NAME=cruddur-upload-avatars	
gp env UPLOADS_BUCKET_NAME=cruddur-upload-avatars	
```

** **

**Distribution of Avatars using CloudFront**
_CloudFront is an content delivery service from AWS that cacches frequently accessed data that improves user experience. The latency is improved by using AWS Global caching infrastructure made possible with the help of edge locations_

- **Go to CloudFront (available under Network and Content Deliver)**
- **Create a new CloudFront distribution and select the origin name with the manual S3 bucket you had created earlier `assets.pratiksinha.link`**
- **Restrict access to the aforementioned bucket by selecting `Origin Access Control Setting`**
- **Create Control setting if already not created.**
- **Redirect traffic from HTTP to HTTPS.**
- **Under Cache key and origin requests, opt for CachingOptimized Caching Policy. Under the Origin request policy, select CORS-CustomOrigin policy and SimpleCORS under Response Headers Policy**
- **For Alternate domain name (CNAME), use the assets.domainname. In my case, its assets.pratiksinha..link**
- **Since, we are redirecting traffic to HTTPS, we need to select a TLS certificate for it. It can be choose from the already procured certificate or request one for it specifically**
- **Don't forget to update the bucket policy with the OAI of the CloudFront. You can find it under `Origins` under the created CloudFront distribution. Select the `Origins`, and click      on Edit at the top right corner. You can click on `Copy Policy` to paste it in the Bucket permissions policy.**

** **

**Created a new [folder](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/aws/lambdas/process-images) in the `aws/lambdas` by the name of `process-images`**

- **Created a test.js for the Lambda function**
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

- **To test if the function is working correctly or not, use the [bash script](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/tree/main/bin/avatar) file to upload, clear and build.**

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

- **Lambda Code used for Avatar Upload (CruddurAvatarUpload)**
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

- **Lambda Authorizer code used in API Gateway (CruddurApiGatewayLambdaAuthorizer)**
```Node.js
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

**Faced CORS error along with 500 error while uploading image. Eventually made it work by tweaking the Lambda Authorizer code and by extracting the bearer token which was causing the issue.**

![11](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/e93279d1-4629-4530-9f3f-d63f62e8a04e)

![111](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/123831fa-b6f0-42ef-bef5-7d1e1634afc2)

![222](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/57f6a845-465a-4e2f-af42-7f582441e88c)

![666](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/94668a83-e589-4c02-869d-75fc7f0f4e0f)

![777](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/2b355d45-b36b-45fd-88e6-9564121fe682)

**Rendered Image delivered from Cloudfront**

![Rendering Avatar from CloudFront](https://github.com/pratiksinha-kol/aws-bootcamp-cruddur-2023/assets/125117631/811be74f-ecf2-4c12-bf82-43d897757d8a)

**Performed these steps so that the above functionality doesn't fail**
* Set `Access-Control-Allow-Origin` as your own frontend URL `function.rb` in `CruddurAvatarUpload`. 
* Correctly extracting the authorization headertoken (I faced this issue) in `CruddurApiGatewayLambdaAuthorizer`.
* In CruddurApiGatewayLambdaAuthorizer Lambda, set the Environment variables with correct Cognito User ID and and Client ID. 
* In CruddurAvatarUpload Lambda, set the Environment variables with correct Upload Bucket name. 
* Set the `gateway_url` and `backend_url` correctly in `frontend-react-js/src/components/ProfileForm.js`.

** **
