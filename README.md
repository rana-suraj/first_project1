# AWS S3 → Lambda → CloudWatch ETL Project

## 📌 Project Overview

This project demonstrates a simple serverless ETL pipeline using:

- Amazon S3
- AWS Lambda
- Amazon CloudWatch
- IAM Roles

The pipeline automatically triggers a Lambda function when a file is uploaded to an S3 bucket and logs the processing results to CloudWatch.

---

## 🏗️ Architecture

S3 (Upload File) → Lambda (Process File) → CloudWatch (Logs)

---

## 🔧 Step 1: Create S3 Buckets

1. Go to AWS Console → S3
2. Click **Create Bucket**
3. Create:
   - source-bucket-demo
   - destination-bucket-demo

---

## 🔐 Step 2: Create IAM Role for Lambda

1. Go to IAM → Roles → Create Role
2. Select:
   - Trusted entity: AWS Service
   - Use case: Lambda
3. Attach policies:
   - AmazonS3FullAccess
   - CloudWatchLogsFullAccess
4. Name the role:
   - lambda-s3-etl-role

---

## ⚡ Step 3: Create Lambda Function

1. Go to Lambda → Create Function
2. Author from scratch
3. Runtime: Python 3.x
4. Execution role: Use existing role
5. Select: lambda-s3-etl-role

---

## 🧠 Lambda Code

```python
import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        print(f"File uploaded: {key} in bucket: {bucket}")

        response = {
            "message": "File processed successfully",
            "file": key
        }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
