# Full Sub Domain Takeover at s3.websummit.net

## Report Details
- **Report ID**: 173412
- **URL**: https://hackerone.com/reports/173412
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-10-01T19:21:41.653Z
- **Disclosed**: 2017-02-02T11:10:45.859Z

## Reporter
- **Username**: dhaval
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: websummit

## Vulnerability Information
Hey

The sub domain at `s3.websummit.net` is pointing to `dws-content.s3-website-eu-west-1.amazonaws.com.`

> http://s3.websummit.net/

````
404 Not Found

    Code: NoSuchBucket
    Message: The specified bucket does not exist
    BucketName: s3.websummit.net
    RequestId: DB4C92F0D805D3F3
    HostId: NdSB/5EgNAiQz7B2pjzfBy5QwA6977cvAroA5vCyqfSsPR3nZLgdEyv4vQA4NCISzpILKP0WddM=
````

This means that the bucket has now expired and this  can now be claimed and content can be hosted on behalf of `http://s3.websummit.net/`

## Attachments
No attachments
