# Enumerate class codes via yahoo dork - Can access any course under teacher - Sensitive information leaked

## Report Details
- **Report ID**: 1514356
- **URL**: https://hackerone.com/reports/1514356
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-03-16T23:30:59.147Z
- **Disclosed**: 2022-05-01T18:05:32.828Z

## Reporter
- **Username**: bughunterpol
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Hello Team,
I am quality researcher and I found some links using yahoo dorking techniques
I used yahoo dork `site:pl.khanacademy.org/join` 
I used Firefox browser.

Steps to reproduce:
1.Go to yahoo search page and use above query to enumerate.
2.Create student account by filling all the required details
3.Now you are in the class without actually invited by teacher.
4.You can pick any course from item and start you course.

I can also able to see teacher Full name- This is sensitive information 

Attached POC:

## Impact

Any black hacker can enumerate all the classes and join in them and can make chaos.
Some chances of IDOR too.
If you can encrypt this class details which some hashing technique and this will not showed up with dorking queries.

## Attachments
- khanacademyyahoodork.mov
