# Race Condition leads to undeletable group member

## Report Details
- **Report ID**: 604534
- **URL**: https://hackerone.com/reports/604534
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-09T10:26:15.621Z
- **Disclosed**: 2020-03-20T17:17:47.781Z

## Reporter
- **Username**: yashrs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi,

**Summary:**
There exists a Race Condition in which the user can add themselves twice to a group which will make them unremovable from group. They themselves cannot remove themselves from the group as well as the group leader cannot remove that user from the group. Ofcourse this is a low severity as that malicious user first needs to have a valid invitation link, but nevertheless this leads to permanent membeship of group so this needs to be fixed in my opinion.


### Steps To Reproduce

We need two accounts to reproduce this.

- First account will be leader account
- Second account will be a normal account.

- Create a group from the first account and create an invitation link.
- Join using the invitation link on the second account and intercept the request:

```
POST /group/post_join HTTP/1.1
Host: ctf.hacker101.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ctf.hacker101.com/group/join?invite=bb5c42ab578b12c63e5d868b3e03816c8c45597262aaf095ca2be19116b8fd0a
Content-Type: application/x-www-form-urlencoded
Content-Length: 109
Connection: close
Cookie: COOKIES
Upgrade-Insecure-Requests: 1

csrf=391aecf0c3125e90c437d04c18204ab6&invite=bb5c42ab578b12c63e5d868b3e03816c8c45597262aaf095ca2be19116b8fd0a
```

Repeat the above requests in parallel. I did it for 5 parallel requests and I was able to add myself 2 times to that group:
{F505223}

- Now try deleting the user from first account(group leader). No matter how much you try, you won't be able to delete it.

This would lead to a state where the group leader will have to delete the group and create a new group if he wants the malicious user to get removed. 

Thanks,
Yash

## Impact

Irremovable/permanent member of the group. Even the group leader cannot remove that user.

## Attachments
- Capture.PNG
