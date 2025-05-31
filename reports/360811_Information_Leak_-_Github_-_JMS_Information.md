# Information Leak - Github - JMS Information

## Report Details
- **Report ID**: 360811
- **URL**: https://hackerone.com/reports/360811
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-06-01T14:42:40.959Z
- **Disclosed**: 2018-08-16T20:12:51.016Z

## Reporter
- **Username**: p3t3r_r4bb1t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,

After some research, I found a leak on GitHub that might lead to accessing sensitive data of employees or clients (not sure based on the code). There is also a SAP S-user to access a cloud based HANA service. I have not confirmed what kind of data is in there to avoid potential legal issues. I will let you guys figure that out ;)

I am not sure who is the owner of the repository, but I can tell you that the SAP credentials are for someone at Starbucks China.

https://github.com/karaskay/personalware

Some interesting files:
https://github.com/karaskay/personalware/blob/989723f896eec67a50a9b9f59ceefc48a046049b/python/PycharmProjects/JMS36/testhttprequestjson.py
(SAP Cloud HANA credentials)

https://github.com/karaskay/personalware/blob/989723f896eec67a50a9b9f59ceefc48a046049b/python/PycharmProjects/JMS36/JMSproducerforsurvey.py
(starbuckstest domain credentials)

Thanks!

## Impact

High potential of an unauthorized access to PII data

## Attachments
No attachments
