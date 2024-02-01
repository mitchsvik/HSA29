# HSA29
Serverless calculations

# Serverless on AWS

This template demonstrates how to develop and deploy a simple Python function running on AWS Lambda using the Serverless Framework.

It configures a single function, `HandleS3Image`, which is responsible for handling all uploading of image to `/upload` path on specified S3 bucket. 

## Usage

### Prerequisites

In order to package your dependencies locally with `serverless-python-requirements`, you need to have `docker` installed locally. 

You can create and activate a dedicated virtual environment with the following command:

```bash
python3 -m venv ./venv
source ./venv/bin/activate
```
### Deployment

Install dependencies with:

```
npm install
```

and

```
pip install -r requirements.txt
```

You should have AWS CLI configured locally and then perform deployment with:

```
serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying HSA29 to stage dev (us-east-1)

✔ Service deployed to stack HSA29-dev (80s)

functions:
  S3PutMedia: HSA29-dev-S3PutMedia (17 MB)
```
