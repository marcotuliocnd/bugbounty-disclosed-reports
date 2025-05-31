# S3 ACL misconfiguration

## Report Details
- **Report ID**: 189023
- **URL**: https://hackerone.com/reports/189023
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-07T01:51:29.130Z
- **Disclosed**: 2017-08-29T03:19:52.604Z

## Reporter
- **Username**: baseballislife
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
**Summary**:

Legal Robot's s3 bucket [**legalrobot.com**] is misconfigured. The ACL allows me to _access_ and _copy_ **all files**. This means that I could go through and copy all the media files on the s3 bucket.  I did not attempt to _delete_ any files as I did not want to go too far and affect your operations.

**Steps to Reproduce**:

1) Generate a random AWS key from the AWS Console
2) Perform the following proof-of-concept:
```
$ aws s3 ls s3://legalrobot
                      PRE email/
                      PRE video/
2015-12-28 21:39:20    536901 Dan-sq-gray.jpg
2015-12-28 21:39:21     546125 Dan-sq.jpg
2015-10-06 21:35:54     363060 Gizmo-Foldable.pdf
2016-02-26 12:37:45      22945 Megan.jpg
2015-12-08 01:58:52     420926 logo_huge.png
2015-12-08 01:59:04      14714 logo_text_huge.png

copy: aws s3 cp s3://legalrobot/video/meeting-room/MP4/Meeting-Room.mp4
```
I've noticed that this particular video file is being played in the background of your homepage. 

**Remediation**:

Update your ACL to the proper configuration, preventing other users' from potentially modifying or accessing your s3 bucket. 


## Attachments
No attachments
