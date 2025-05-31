# Download attribute allows downloading local files

## Report Details
- **Report ID**: 258710
- **URL**: https://hackerone.com/reports/258710
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-10T18:10:16.714Z
- **Disclosed**: 2018-03-29T03:04:59.964Z

## Reporter
- **Username**: skansing
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

The attribute `download` in a `a` tag allows for download the `href` target to file and saving it locally. 
In mozilla and chrome, it is forbidden to download local file via `file:// ..`, in Brave however this is not enforced and it is not clear to the user if they are downloading something remote or local. This could be abused to social engineering and phishing that is hard to spot without reviewing the js code.

## Products affected: 
```
Name	Version
Brave	0.18.16
rev	8003c66
Muon	4.3.6
libchromiumcontent	60.0.3112.78
V8	6.0.286.44
Node.js	7.9.0
Update Channel	dev
OS Platform	Linux
OS Release	4.4.0-64-generic
OS Architecture	x64
```
## Steps To Reproduce:
Create a `<a href="files:///etc///passwd" download>Download local file</a>`
On a linux machine, click the link, download the file, open it. It's the local file.

Expected result `file:// not allowd`
Result `file downloaded`

Please see the poc below and screenshots

## Supporting Material/References:
I added a POC with a phishing page that attempts to gets users passwd file. 
`http://159.203.190.123/braaaaaaaaaave/3t98j2398jegjsguieiu3tuihsgdiu___brave_0010-localfile.html` with the purpose to phish passwd files and added pictures of each frame of the attack.


## Attachments
- brave_3.png
- brave_4.png
- brave_2.png
- brave_1.png
