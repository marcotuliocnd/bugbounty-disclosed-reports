# Enumerate all the class codes via google dorking 

## Report Details
- **Report ID**: 1210043
- **URL**: https://hackerone.com/reports/1210043
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-26T16:19:43.401Z
- **Disclosed**: 2021-07-22T01:44:36.165Z

## Reporter
- **Username**: renganathan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
I used this particular google dork `site:khanacademy.org/join/*` to enumerate all the links of joining classes. 

1. Go to google and use the above query to enumerate all of them. 
2. Create the student account by filling all the required details 
3. Now you're in the class without being actually invited by the teacher 

Attached POC:
████████

## Impact

An attacker can enumerate all the classes and join in them and make chaos there are chances of IDOR too... a class code can look like `a57d5d5548f302ef4a` instead of `A45JST`

## Attachments
No attachments
