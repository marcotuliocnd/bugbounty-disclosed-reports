# Open AWS S3 bucket leaks all Images uploaded to Zomato chat

## Report Details
- **Report ID**: 507097
- **URL**: https://hackerone.com/reports/507097
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-09T09:18:14.362Z
- **Disclosed**: 2019-05-01T14:28:37.047Z

## Reporter
- **Username**: yashrs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hey,

**Summary:** 
The vulnerable bucket is `████images` and we can use 

`aws s3 ls s3://$bucketname/2019/1/` to retreive all images uploaded in 2019 and in January. Similarly we can use different years and months to retreive all images uploaded to Zomato Chat!

The images can be accessed at https://s3-ap-southeast-1.amazonaws.com/████████images/2019/1/{imageid}

## Supporting Material/References:
- {F438150}

Thanks,
Yash :)

## Impact

It could have contained User PII too, I haven't checked all the contents. Most of them are food photos :P, but it could easily have been PII if user uploaded some bill or something else that sort of.

An attacker can download all images in mass. Please secure the AWS bucket

## Attachments
No attachments
