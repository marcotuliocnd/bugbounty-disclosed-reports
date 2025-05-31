# Writable RubyCi Amazon s3 bucket

## Report Details
- **Report ID**: 207053
- **URL**: https://hackerone.com/reports/207053
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-17T06:43:02.543Z
- **Disclosed**: 2017-02-27T02:05:26.852Z

## Reporter
- **Username**: dataalchemist
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hello, I have discovered that the bucket:
http://rubyci.s3.amazonaws.com/
is able to be written to by authenticated aws users. This is due to the current permissions configurations
I have added a file here:
http://rubyci.s3.amazonaws.com/test.html
for proof of concept. This can be potentially dangerous to your users and website, as any of the web content in this bucket may be replaced with malicious files. 
More info about these permissions can be found here: http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html


## Attachments
- Screen_Shot_2017-02-16_at_10.41.47_PM.png
- Screen_Shot_2017-02-16_at_10.42.38_PM.png
