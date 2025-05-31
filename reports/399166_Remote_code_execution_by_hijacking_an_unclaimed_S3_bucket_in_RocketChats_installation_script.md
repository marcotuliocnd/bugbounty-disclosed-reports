# Remote code execution by hijacking an unclaimed S3 bucket in Rocket.Chat's installation script.

## Report Details
- **Report ID**: 399166
- **URL**: https://hackerone.com/reports/399166
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-24T22:50:43.484Z
- **Disclosed**: 2018-08-28T12:32:29.636Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
Hi team,

When I downloaded the latest release of Rocket.Chat to test the fix for my previous report I spotted an `install.sh` script. Inside that installation script I noticed [the following line](https://github.com/RocketChat/Rocket.Chat/blob/develop/install.sh#L14):

```diff
#!/bin/bash
set -x
set -euvo pipefail
IFS=$'\n\t'

ROOTPATH=/var/www/rocket.chat
PM2FILE=pm2.json
if [ "$1" == "development" ]; then
  ROOTPATH=/var/www/rocket.chat.dev
  PM2FILE=pm2.dev.json
fi

cd $ROOTPATH
+ curl -fSL "https://s3.amazonaws.com/rocketchatbuild/rocket.chat-develop.tgz" -o rocket.chat.tgz
tar zxf rocket.chat.tgz  &&  rm rocket.chat.tgz
cd $ROOTPATH/bundle/programs/server
npm install
pm2 startOrRestart $ROOTPATH/current/$PM2FILE
```

So I decided to see if I could access the contents of that S3 bucket. To my surprise, I got the following error message:

```
$ aws s3 ls s3://rocketchatbuild

An error occurred (NoSuchBucket) when calling the ListObjects operation: The specified bucket does not exist
```

That is when I realised that you were requesting a file from an unclaimed S3 bucket. I created a bucket with that name and I am currently serving my own `rocket.chat-develop.tgz` file that your script now fetches. The script then executes my code on any user's machine. **Please note that I do not want to cause any harm to Rocket.Chat users so all I did was upload a text file with my username in it and will happily remove the file as soon as you have seen this report.**

```
~ λ curl -fSL "https://s3.amazonaws.com/rocketchatbuild/rocket.chat-develop.tgz" -o rocket.chat.tgz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--   100   179  100   179    0     0    250      0 --:--:-- --:--:-- --:--:--   250
~ λ tar -xvzf rocket.chat.tgz 
frogs-find-bugs/
frogs-find-bugs/hehehe
~ λ cat frogs-find-bugs/hehehe 
EdOverflow :D
```

Please let me know how you would like to proceed with this report and I will try my best to help you out wherever I can.

\- Ed

## Impact

An adversary or, at the very least, I can execute arbitrary code whenever someone runs `install.sh`.

## Attachments
No attachments
