# Tweets and retweets referring to the top 10 actors of the last 10 years

## Description
  
The script downloads the files from the IMDB database necessary to cross-reference the information and return the names of the 10 actors who performed the most in the last 10 years. In the next step, the script searches twitter using the twitter api for tweets and retweets related to this top 10 and stores in a Bucket s3.

`Python version 3.9 or later`

**Terraform**

The creation of EC2 and S3 instances are done using terraform. It is only necessary to write the variables in the terraform/terraform.tfvars file and execute the commands of terraform.

**.env**

The .env file in main path must contain the following keys:

API_KEY = '`Twitter API key`'

API_KEY_SECRET = '`Twitter API secret key`'

ACCESS_TOKEN = '`Twitter API access token`'

ACCESS_TOKEN_SECRET = '`Twitter API token secret`'

## Execution

1. If there are no created ec2 and s3 instances, you can create them using terraform. If there are already instances created, skip this step.

2. The IMDB database files needed to perform the data search are downloaded

3. The script merges IMDB data and searches for the top 10 actresses and actors who performed the most in the last 10 years

4. The script fetches the 10 tweets or retweets related to each actor and stores them locally in a .csv file

5. Csv file, script.log and script_erros.log are uploaded to the s3 bucket