# Path traversal in deeplink query parameter can expose any user's private info to a public directory (one click)

## Report Details
- **Report ID**: 2553411
- **URL**: https://hackerone.com/reports/2553411
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-06-16T08:02:30.035Z
- **Disclosed**: 2024-07-09T11:01:19.059Z

## Reporter
- **Username**: fr4via
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
```java
[------------------------------------Package Details---------------------------------------]:
|    Application Name  :Basecamp
|    Package Name      :com.basecamp.bc3
|    Version code      :380
|    Version Name      :4.8.6
|    Mimimum SDK       :28
|    Target  SDK       :34
|    Max SDK           :None
|    Sha256            :124861dde5cbb9a38d0994c3ca994fbbe5bae83b79621b7e476a0aa78bb711f2
[------------------------------------------------------------------------------------------]
````

## Summary

It was found that the basecamp.bc3 app can be forced to expose the user's private info (any), to the device's shared directory which is accessible by any 3p app with READ/MANAGE external storage permissions. 


## Technical details

The application declares to its android manifest that it handles deeplinks of the form: https://3.basecamp.com/* . The particular deeplink can "take" an additional parameter, called "filename" which is used by the app to save the file locally.  By using a textbook path traversal exploit, it is possible to force the app to save the file to any directory, including ones which are shared and thus accessible by 3rd party apps. 


## Steps to reproduce

The following link stores the user's progress report to the /sdcard/Download/disclosure.txt file:

<a href="https://3.basecamp.com/5195267/reports/progress?filename=/../../../../../../../../../../sdcard/Download/disclosure.txt">click me</a>


Since basecamp supports link within comments/projects e.t.c. , it is possible to add a malicious link, literally anywhere:

{F3360970}

## Impact

An attacker can send/add a malicious link which can expose user's private and files to 3rd party entities.

## Attachments
- Screen_Recording_2024-06-16_at_08.58.13.mov
