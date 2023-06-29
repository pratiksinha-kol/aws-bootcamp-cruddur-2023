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
