# [bot.brew.sh] Full Path Disclosure

## Report Details
- **Report ID**: 222096
- **URL**: https://hackerone.com/reports/222096
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-04-19T09:48:08.614Z
- **Disclosed**: 2017-04-26T11:06:27.957Z

## Reporter
- **Username**: zephrfish
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: homebrew

## Vulnerability Information
Full Path Disclosure (FPD) vulnerabilities enable the attacker to see the path to the webroot/file. e.g.: /home/omg/htdocs/file/. Certain vulnerabilities, such as using the load_file() (within a SQL Injection) query to view the page source, require the attacker to have the full path to the file they wish to view.

The affected domain has a logging instance that discloses the full operating system path on certain pages. 

Affected URLs:
 - https://bot.brew.sh/job/Homebrew%20Bottles/lastFailedBuild/logText/progressiveText?start=0
 - https://bot.brew.sh/job/Homebrew%20Bottles/*


It was possible to discover the path where the brew distrobution server is installed as can be seen in the output below:

```
The request GET /job/Homebrew%20Bottles/lastSuccessfulBuild/logText/progressiveText?start=0 HTTP/1.1
Host: bot.brew.sh
Accept-Charset: iso-8859-1,utf-8;q=0.9,*;q=0.1
Accept-Language: en
Connection: Close
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)
Pragma: no-cache
Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, image/png, */*



produces the following path information :
[EnvInject] - Injecting as environment variables the properties content
HOMEBREW_UPDATE_TO_TAG=1
PATH=bin:/usr/bin:/bin:/usr/sbin:/sbin
HOMEBREW_DEVELOPER=1


The request GET /job/Homebrew%20Bottles/lastFailedBuild/logText/progressiveText?start=0 HTTP/1.1
Host: bot.brew.sh
Accept-Charset: iso-8859-1,utf-8;q=0.9,*;q=0.1
Accept-Language: en
Connection: Close
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)
Pragma: no-cache
Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, image/png, */*



produces the following path information :
[EnvInject] - Injecting as environment variables the properties content
HOMEBREW_UPDATE_TO_TAG=1
PATH=bin:/usr/bin:/bin:/usr/sbin:/sbin
HOMEBREW_DEVELOPER=1


The request GET /job/Homebrew%20Bottles/lastFailedBuild/logText/progressiveHtml?start=0 HTTP/1.1
Host: bot.brew.sh
Accept-Charset: iso-8859-1,utf-8;q=0.9,*;q=0.1
Accept-Language: en
Connection: Close
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)
Pragma: no-cache
Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, image/png, */*



produces the following path information :
[EnvInject] - Injecting as environment variables the properties content
HOMEBREW_UPDATE_TO_TAG=1
PATH=bin:/usr/bin:/bin:/usr/sbin:/sbin
HOMEBREW_DEVELOPER=1
```

# Recommendation
Implement basic authentication to protect the root folder, alternatively remove the offending files causing the stack trace errors.

## Attachments
No attachments
