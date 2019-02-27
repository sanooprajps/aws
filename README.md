# aws
AWS programmatic access

AWS CLI installation in Ubuntu
----------------------------

1) Make sure pip package is installed. (pip or pip3 if python3 is used)
2) pip install awscli
3) Add alias to 'aws' binary in '.bashrc' file
    alias aws="$HOME/.local/bin/aws"
4) Test whether aws CLI is installed properly using following command.
    :~$ aws --version
    aws-cli/1.16.113 Python/3.6.7 Linux/4.13.0-36-generic botocore/1.12.103
5) Perform 'aws configure' and provide 'aws_access_key_id' and 'aws_secret_access_key'. Keep the fields empty if you don't want to connect using keys and insteadm use IAM Roles.
6) Check if '.aws' directory is created in the home directory
    :~$ ls -l ~/.aws
    -rw------- 1 sanoop sanoop  29 Feb 27 15:05 config
    -rw------- 1 sanoop sanoop 116 Feb 27 15:05 credentials
7) Get IAM account summary to confirm aws cli is working fine.
    aws iam get-account-summary 
