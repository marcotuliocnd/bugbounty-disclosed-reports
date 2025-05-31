# Subdomain takeover on healthyhackathon.khanacademy.org and hackweek.khanacademy.org

## Report Details
- **Report ID**: 474798
- **URL**: https://hackerone.com/reports/474798
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-04T17:57:56.717Z
- **Disclosed**: 2019-08-25T07:02:41.660Z

## Reporter
- **Username**: katsuragicsl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
#Summary :
healthyhackathon.khanacademy.org can be took over, since it points to a bucket in S3 but that bucket does not exists.

I know this domain is used to host information of healthyhackathon which is held by khanacademy, but you will not be able to do this anymore if someone is going to claim that bucket. 

#Reference :
[S3_takeover](https://github.com/EdOverflow/can-i-take-over-xyz/issues/36)

## Impact

Taking control of healthyhackathon.khanacademy.org and spoof khanacademy users that healthyhackathon is reopened/"archived for you to challenge" and collect their information.

## Attachments
- sub_take1.png
- sub_take2.png
