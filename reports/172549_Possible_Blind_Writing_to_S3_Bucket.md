# Possible Blind Writing to S3 Bucket

## Report Details
- **Report ID**: 172549
- **URL**: https://hackerone.com/reports/172549
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-28T03:13:16.405Z
- **Disclosed**: 2018-04-27T01:27:18.855Z

## Reporter
- **Username**: yaworsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reverb

## Vulnerability Information
Hi All,
I noticed that you are using S3 and I believe I may have found one of your buckets and am able to write to it. However, I can not list the files in the bucket and such can not be 100% sure you own it. If you don't, I'd really appreciate being able to close this report myself or have you close it as informative to avoid the negative reputation/signal loss but respect your decision either way.

##Description
I noticed you are using the bucket reverb-files-staging. As such, I found reverb-ssh. Using the AWS CLI as an authenticated user, I am able to write to the bucket with the comment ```aws s3 cp teespring_buckets s3://reverb-ssh``` --- please excuse the file name, I uploaded the wrong test file.

After running the command I get ```upload: ./teespring_buckets to s3://reverb-ssh/teespring-buckets``` instead of an access denied message.

##Vulnerability
I'm reporting as I believe you likely own the bucket and if so, an attacker can write arbitrary files to the bucket which your team may trust seeing as the bucket appears to be for internal use. As a result, it could be possible to install malware on internal reverb machines to escalate an attack.

Please let me know if you have any questions.
Pete

## Attachments
No attachments
