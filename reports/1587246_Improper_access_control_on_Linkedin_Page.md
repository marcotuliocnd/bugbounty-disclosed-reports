# Improper access control on Linkedin Page

## Report Details
- **Report ID**: 1587246
- **URL**: https://hackerone.com/reports/1587246
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-05-31T11:00:11.713Z
- **Disclosed**: 2023-08-24T02:42:45.051Z

## Reporter
- **Username**: cipherai
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
Dear security team,
I found a critical bug on linkedin page.
If any user added someone as super admin by mistakenly , and then edited the role and changes to analyst, still they can publish post on the page as super admin.

Step to reproduce:
1.Add someone(ex name: jesna) as superadmin
2.Jesna saw it and opened the page in super admin view(You've open linkedin page as jesna in other private window or other device)
3.Then you change the role of jesna to analyst
4.But jesna didn't refreshed her page, she is still in the super admin view
5.jesna try to publish a post
6.post got published in the page

I'm attaching complete POC: █████

## Impact

1.The analyst can publish post
2.It is harmful for page or to the company
3.Improper access to the page will degrade the company,if the user post something bad in the page

## Attachments
No attachments
