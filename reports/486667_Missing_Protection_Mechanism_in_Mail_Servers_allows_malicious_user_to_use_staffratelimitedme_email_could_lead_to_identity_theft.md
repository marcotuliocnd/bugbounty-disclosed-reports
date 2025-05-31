# Missing Protection Mechanism in Mail Servers allows malicious user to use staff.ratelimited.me email could lead to identity theft.

## Report Details
- **Report ID**: 486667
- **URL**: https://hackerone.com/reports/486667
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-26T15:26:20.642Z
- **Disclosed**: 2019-02-02T10:28:36.030Z

## Reporter
- **Username**: notexist
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
Hello ratelimited,

I'm not really sure how your mail servers being configured but i guess there is a mis-configuration or missing protection mechanism that fails to verify if the email that is going to be sent are only made by authorized ratelimited staff only. From this point of view a malicious user could sent an email to a victim by using valid and email owned by staffs of ratelimited and to be specific one of them are `gtsatsis@staff.ratelimited.me` and i can surely tell it is based on #369581 wherein a team member acknowledge the hacker that is will be given a reward for efforts.

### So what now ?
If a malicious user could use `gtsatsis@staff.ratelimited.me` to send emails through the abuse of misconfigured mail server with missing protection, they can spread fake message from this point and make the reputation of ratelimited staffs and management bad from others point of view.

### POC 
I've attack my own email and tries to exploit the issue.
Here my gmail account has been received email from `gtsatsis@staff.ratelimited.me` says that i've received reward from ratelimited. If a normal user would received this email, they will not hesitate to claim the reward thinking that came from and request being done and sent by legitimate staff from ratelimited but it is actually not.
{F412930} 

### How could we verify this ?
Here is the steps to reproduce the issue:
- I use 3rd party email faker `emkei.cz` to use spoof email of `gtsatsis@staff.ratelimited.me`.
- Just compose a normal email and not forget to put email of the victim.
- Send the email.

### Still, who cares or implement mail protections from their servers ?
Hackerone itself is already done this way back years ago. They configured their mail server so whenever a malicious user could use @hackerone.com and tries to send mail using it from distributing messages. Hackerone mail server will prevent this before sending it to desired victim. And so facebook does, In case you want to verify this. Try the steps to reproduce above against the said website and you see the attack will never succeed on `*@hackerone.com` nor `*.facebook.com`.

> Don't get me wrong but this attack only made possible by opening ratelimited itself a window for exploitation.

Regards,
Mart Gil

## Impact

Could distribute fake email content/files using `gtsatsis@staff.ratelimited.me` or any email used by ratelimited. As a result, ratelimited will have a bad reputation and this can also be use by any counterpart company of ratelimited.

## Attachments
No attachments
