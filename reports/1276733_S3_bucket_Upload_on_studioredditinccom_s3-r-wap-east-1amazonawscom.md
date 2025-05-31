# S3 bucket Upload on studio.redditinc.com (s3-r-w.ap-east-1.amazonaws.com)

## Report Details
- **Report ID**: 1276733
- **URL**: https://hackerone.com/reports/1276733
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-24T14:50:52.373Z
- **Disclosed**: 2021-10-21T20:00:28.449Z

## Reporter
- **Username**: dinesh07
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Greetings team,

Found a s3 bucket that belongs to studio.redditinc.com and properly not configured.

bucket name:- s3-r-w.ap-east-1.amazonaws.com
Bucket Source:-studio.redditinc.com

Steps To reproduce:-

In terminal , " dig studio.redditinc.com "
will get the CNAME as d326d3e45wj426.cloudfront.net

Then, "host -t ns d326d3e45wj426.s3.ap-east-1.amazonaws.com"
will get 
d326d3e45wj426.s3.ap-east-1.amazonaws.com is an alias for s3-r-w.ap-east-1.amazonaws.com.
s3-r-w.ap-east-1.amazonaws.com name server ns-1885.awsdns-43.co.uk.
s3-r-w.ap-east-1.amazonaws.com name server ns-192.awsdns-24.com.
s3-r-w.ap-east-1.amazonaws.com name server ns-908.awsdns-49.net.
s3-r-w.ap-east-1.amazonaws.com name server ns-1338.awsdns-39.org.

So, I came to know that d326d3e45wj426.s3.ap-east-1.amazonaws.com is an alias for "s3-r-w.ap-east-1.amazonaws.com" 

Got the bucket name. Now I tried to upload by using command in authenticated  AWS CLI Machine
" aws s3 cp <path/filename> s3://s3-r-w

Uploaded was successful! Two files( dinesh.jpg and dinesh.html )

" aws s3 ls s3://<The_bucket_name> "
By this command I can list out  all the files in the bucket

I don't know is it possible or not. Attacker can delete the bucket using this command:-
" aws s3 rb s3://<The_bucket_name> "
and claim the bucket again to takeover the bucket.

Thanks team

## Impact

I can see every files present in the bucket .
I can upload any files . 
I can delete any file .

## Attachments
- Screenshot_(552).png
