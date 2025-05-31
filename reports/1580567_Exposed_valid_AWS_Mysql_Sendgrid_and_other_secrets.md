# Exposed valid AWS, Mysql, Sendgrid and other secrets

## Report Details
- **Report ID**: 1580567
- **URL**: https://hackerone.com/reports/1580567
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-05-24T23:38:35.714Z
- **Disclosed**: 2022-07-08T15:48:55.275Z

## Reporter
- **Username**: mehdisadir
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glovo

## Vulnerability Information
## Summary:
Hi team,

I just discovered some hardcoded credentials allowing access to AWS, Mysql database, ...

To make this report short, here is the POC: 
see ███ & █████
## Steps To Reproduce:

where there are the info : 

<p>
APP_NAME=Glovo
APP_ENV=local
APP_KEY=█████
APP_DEBUG=false
APP_URL=http://localhost
LOG_CHANNEL=stack
LOG_LEVEL=debug
DB_CONNECTION=mysql
DB_HOST=██████████
DB_PORT=3306
DB_DATABASE=████████
DB_USERNAME=█████
DB_PASSWORD=█████████
BROADCAST_DRIVER=log
CACHE_DRIVER=file
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120
MEMCACHED_HOST=127.0.0.1
REDIS_HOST=█████
REDIS_PASSWORD=██████████
REDIS_PORT=11773
MAIL_MAILER=smtp
MAIL_HOST=mailhog
MAIL_PORT=1025
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS=null
MAIL_FROM_NAME="${APP_NAME}"
AWS_ACCESS_KEY_ID=███
AWS_SECRET_ACCESS_KEY=███████
AWS_DEFAULT_REGION=eu-central-1
AWS_BUCKET=glovos3
PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1
MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"
SENDGRID_API_KEY=████
MAIL_FROM=glovo@appsmart.ro
MAIL_REPLY_TO=glovo@appsmart.ro
REDIS_URL=█████
LINK_RECEIPT=https://glovo.onlineservice.io/g/c/
SENDGRID_TEMPLATE=d-6ae3f2fe536c41fda21ad60a18c10cce
SENDGRID_PUBLIC_KEY=███████
</p>




  1. The leak was found using Leakix : https://leakix.net/host/16.170.179.191

#Mitigation :

Remove the exposed credentials and revoke them.

Regards,

NB: After checking some files which i deleted immediatly, I found the company name is GLOVOAPPRO SRL and im not sure if it is related to Glovo company, but I can confirm a little bit from the database where I could see delivery fees ... which is about Glovo's principal service (delivery).

## Impact

Anyone could access

## Attachments
No attachments
