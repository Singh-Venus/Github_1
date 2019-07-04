# ec2Ops-flask
In this repository, I've created a flask application which prints the details of the running EC2 instance in a Browser, and many EC2 operations using Python Boto3 Library.
# Boto3 Python
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software which makes the use of services like Amazon S3 and Amazon EC2.In this repository, I've created a flask application which prints the details of the running EC2 instance in a Browser, and many EC2 operations using Python Boto3 Library.
 
 ## QUICK START
 First, install the library and set a default region:

  $ pip install boto3

  Next, set up credentials (in e.g. ~/.aws/credentials):

 [default]
 aws_access_key_id = YOUR_KEY
 aws_secret_access_key = YOUR_SECRET
                                                                                                                                      
 Then, set up a default region (in e.g. ~/.aws/config):

[default]
region=us-east-1

Next, install the flask, jinja2 and werkzeug packages

$ pip install flask

$ pip install jinja2

$ pip install werkzeug

After all the installations and the settings go for coding and development.

## Tools Used:
For coding and development, I've used Pycharm IDE.
You would require an AWS account.

## EC2-Flask-Operations:
There are two kinds of program files in this repository, one being the flask application and another being python Boto3 files.

### Instance-On-Flask:
The Instance-on-Flask is a python file which is capable of creating a flask web application.
The Instance-on-Flask file is capable of creating a website which can print some Documentation and ("/instanceinfo") will navigate you to print the details and descritions of the EC2 instance created in your AWS console.

### Instance Operational Files:
The instance operational files are capable of performing different-different operations of AWS EC2 instance. Creation, Deletion, Stopping, Starting, Rebooting, Monitoring an instance and similarly for other parameters like security-groups creation-deletion,Permission-granting, key-pair creation and deletion. Performing SES (Simple E-mail Services), sending attachments using SES etc.

