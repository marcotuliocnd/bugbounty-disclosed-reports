# Bypass Tracking Blocker Protection Using Slashes Without Protocol On The Image Source.

## Report Details
- **Report ID**: 1050656
- **URL**: https://hackerone.com/reports/1050656
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-04T15:33:38.615Z
- **Disclosed**: 2020-12-17T17:02:57.685Z

## Reporter
- **Username**: demonia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
## Summary:
- Some Way Has Been Discovered To Bypass Image Rewriting On HeyMail Using Slashes Without Protocol `\/\www.evil.com` That Allows Bypassing Tracking Blocker And Collect Users Information Via Emails.

## Description:
- While Searching I Found That The Image Rewriting Function On Heymail Could Be Bypass Using Slashes Since It Seems To Be Depending On A Blacklist. In The Normal Users Are Able To Request External URLs From Images, JS Imports , CSS Imports, ..etc Using Two Slashes Before The Domain. In This Case Users Wasn't Able To Do That Since When The Image Rewriting Function Is Detecting  Two Slashes On The First Two Chars Of The URL Source It Creates An External URL For It On gopher.hey.com. But Due To Some Lack On This Validation Users Are Able To Bypass The Images Rewriting By Inserting Another Slash Between The Two Slashes That Won't Change The URL. In This Case I Used `\/\`.

- I Created A Simple Image Tag With This Payload: `<img src="\/\www.evil.com">` And I Sended It Into My Testing HeyMail Email And I Got That The Web Browser Sent A GET Request Into `www.evil.com` Directly. 
{F1104089}

## Proof Of Concept:
- There Isn't Much Stuff Here. But, Here's A Simple Exploit HTML Code You Can Use To Trigger This Issue.

```html
<h1>Hello World</h1>
<img src="\/\www.evil.com"  >
<h3>Open The Network Tab</h3>
```

Best Regards.

## Impact

Bypassing Image Rewriting Function Witch Allows Trackers To Collect Users IPs Using Images.

## Attachments
- Mail-Network.png
