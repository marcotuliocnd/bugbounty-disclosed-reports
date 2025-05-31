# Line feed injection in get request leads AWS S3 Bucket information disclosure 

## Report Details
- **Report ID**: 460928
- **URL**: https://hackerone.com/reports/460928
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-12T02:52:23.638Z
- **Disclosed**: 2019-01-14T08:47:33.843Z

## Reporter
- **Username**: aty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
**Summary:** 
By added line feed control character to the end of url https://ratelimited.me/migration/
it is possible to list elements of bucket name "████████" , also it is possible to view source code of any php file in the bucket such as the php file with key "██████████" which is the "URIDefinition.php" from the open source HTMLPurifier , so no sensitive source code disclosure here unless this bucket directory contain sensitive .php files other than the HTMLPurifier library . 

**Description:** 
There seems to be an ACL misconfiguration with a bucket name "█████" that can be listed by issuing a GET request to https://ratelimited.me/migration/%0A/  , the response will return  XML document that list the content of this bucket , i tried to see if i can acces some of the files listed in the bucket but it seems the request append .php to any name after the  "%0A/" soo the only files i can access are php files such as the one from this link  https://ratelimited.me/migration/%0a/00f776  , it is also possible to issue some limited S3 REST requests such as https://ratelimited.me/migration/%0A/?location  which will show the AWS region of the bucket [according to aws documentation this should be only allowed to bucket owner https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETlocation.html ], also "PUT" and "POST" are not allowed so attacker can  not change the content of the bucket 

Also note that the bucket list that return from the GET request is limited to 1000 but we can view all the files using the last elements as a marker to view the next 1000 elements https://ratelimited.me/migration/%0A/?marker=02ff70.png
## Steps To Reproduce:
open the provided links in any browser 

https://ratelimited.me/migration/%0A/ 
 https://ratelimited.me/migration/%0a/00f776
https://ratelimited.me/migration/%0A/?location 
https://ratelimited.me/migration/%0A/?marker=02ff70.png

## Impact

Attacker can list the content of AWS S3 bucket list "███" and read the content of any .php file inside

## Attachments
No attachments
