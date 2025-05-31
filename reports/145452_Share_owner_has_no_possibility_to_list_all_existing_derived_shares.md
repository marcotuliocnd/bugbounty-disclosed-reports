# Share owner has no possibility to list all existing derived shares

## Report Details
- **Report ID**: 145452
- **URL**: https://hackerone.com/reports/145452
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-17T15:52:32.076Z
- **Disclosed**: 2016-12-13T16:20:08.706Z

## Reporter
- **Username**: detroitsmash
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi,

I found a bug where a shared link of particular file can disclose all files of that folder. 

###Steps to reproduce

+ Make a group( ```http://*/nextcloud/index.php/settings/users```) and a standard user in it.
+ Now goto any folder and change it to gallery view
{F99993}

+ Invite that group which u made in step 1 with ``share`` privilege .
+ From standard user account, goto that shared folder and make a shared link of any file. E.g:

{F99992}

+ Untick the ``can share`` privilege from that group using folder owner account. Eg: 

{F99994}




Now the shared link which was created by standard user will work as folder shared link. And when folder untick the ``can share`` privilege public is automatically created without asking folder owner.

Thanks

## Attachments
- Screenshot_from_2016-06-17_21_08_32.png
- Screenshot_from_2016-06-17_20_56_19.png
- Screenshot_from_2016-06-17_21_14_13.png
