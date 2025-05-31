# [information disclosure] Validate existence of a private project.

## Report Details
- **Report ID**: 605608
- **URL**: https://hackerone.com/reports/605608
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-10T20:29:57.735Z
- **Disclosed**: 2021-03-09T17:21:19.892Z

## Reporter
- **Username**: pandaonair
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
In Gitlab, we have a feature of creating groups and setting their permissions to public/internal/private. While testing I discovered that a user can check existence of a project in a group of which he is not a part judging by the difference in types of error messages generated.

This request is generated at the `/toggle_star.json` endpoint which is sent when the user clicks on (*) (star) button on the UI.

{F506173}

For instance, Let's assume that their are 2 users here User A, and User B.

User A: Creates a group with `internal` privacy and deploys a project.

In this case let's assume that the group created by User A is `chocolatecake` at url https://gitlab.com/chocolatecake . The privacy settings of this group should be either internal/private.
This user creates a project named `Choco Brownie Sundae` with url https://gitlab.com/chocolatecake/choco-brownie-sundae.

Hence, we notice that a project with slug `choco-brownie-sundae` is created. 


User B: Is a malicious user who wants to find out if the organization of ChocolateCake is working on some secret project so, he sends the following request and based on the difference in responses he can extrapolate some information.

```
POST /chocolatecake/choco-brownie-sundae/toggle_star.json HTTP/1.1
Host: gitlab.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-CSRF-Token: REDACTED
X-Requested-With: XMLHttpRequest
DNT: 1
Connection: close
Cookie: REDACTED
Content-Length: 0


```

Response: **For Valid Project** (meaning that the project exists)

```
HTTP/1.1 404 Not Found
Server: nginx
Date: Mon, 10 Jun 2019 20:09:20 GMT
Content-Type: application/json
Content-Length: 0
Connection: close
Cache-Control: max-age=0, private, must-revalidate
Pragma: no-cache
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Request-Id: iKCIJhxyam
X-Runtime: 0.059894
X-Ua-Compatible: IE=edge
X-Xss-Protection: 1; mode=block
Content-Security-Policy: object-src 'none'; worker-src https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://gitlab.com blob:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://www.gstatic.com/recaptcha/ https://apis.google.com; style-src 'self' 'unsafe-inline' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net; img-src * data: blob:; frame-src 'self' https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://content.googleapis.com https://content-compute.googleapis.com https://content-cloudbilling.googleapis.com https://content-cloudresourcemanager.googleapis.com https://*.codesandbox.io; frame-ancestors 'self'; connect-src 'self' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net wss://gitlab.com https://sentry.gitlab.net https://customers.gitlab.com https://snowplow.trx.gitlab.net


```

Response: **For Invalid Project** (meaning that the project does not exists)

```
HTTP/1.1 404 Not Found
Server: nginx
Date: Mon, 10 Jun 2019 20:13:00 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3108
Connection: close
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Expires: Fri, 01 Jan 1990 00:00:00 GMT
Pragma: no-cache
X-Request-Id: 6vFQwUWj4V
X-Runtime: 0.193010
Content-Security-Policy: object-src 'none'; worker-src https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://gitlab.com blob:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://www.gstatic.com/recaptcha/ https://apis.google.com; style-src 'self' 'unsafe-inline' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net; img-src * data: blob:; frame-src 'self' https://www.google.com/recaptcha/ https://www.recaptcha.net/ https://content.googleapis.com https://content-compute.googleapis.com https://content-cloudbilling.googleapis.com https://content-cloudresourcemanager.googleapis.com https://*.codesandbox.io; frame-ancestors 'self'; connect-src 'self' https://assets.gitlab-static.net https://gl-canary.freetls.fastly.net wss://gitlab.com https://sentry.gitlab.net https://customers.gitlab.com https://snowplow.trx.gitlab.net

<!DOCTYPE html>
<html>
<head>
  <meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
  <title>The page you're looking for could not be found (404)</title>
  <style>
    body {
      color: #666;
      text-align: center;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      margin: auto;
      font-size: 14px;
    }

    h1 {
      font-size: 56px;
      line-height: 100px;
      font-weight: 400;
      color: #456;
    }

    h2 {
      font-size: 24px;
      color: #666;
      line-height: 1.5em;
    }

    h3 {
      color: #456;
      font-size: 20px;
      font-weight: 400;
      line-height: 28px;
    }

    hr {
      max-width: 800px;
      margin: 18px auto;
      border: 0;
      border-top: 1px solid #EEE;
      border-bottom: 1px solid white;
    }

    img {
      max-width: 40vw;
      display: block;
      margin: 40px auto;
    }

    a {
      line-height: 100px;
      font-weight: 400;
      color: #4A8BEE;
      font-size: 18px;
      text-decoration: none;
    }

    .container {
      margin: auto 20px;
    }

    .go-back {
      display: none;
    }

  </style>
</head>

<body>
  <a href="/">
    <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjEwIiBoZWlnaHQ9IjIxMCIgdmlld0JveD0iMCAwIDIxMCAyMTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHBhdGggZD0iTTEwNS4wNjE0IDIwMy42NTVsMzguNjQtMTE4LjkyMWgtNzcuMjhsMzguNjQgMTE4LjkyMXoiIGZpbGw9IiNlMjQzMjkiLz4KICA8cGF0aCBkPSJNMTA1LjA2MTQgMjAzLjY1NDhsLTM4LjY0LTExOC45MjFoLTU0LjE1M2w5Mi43OTMgMTE4LjkyMXoiIGZpbGw9IiNmYzZkMjYiLz4KICA8cGF0aCBkPSJNMTIuMjY4NSA4NC43MzQxbC0xMS43NDIgMzYuMTM5Yy0xLjA3MSAzLjI5Ni4xMDIgNi45MDcgMi45MDYgOC45NDRsMTAxLjYyOSA3My44MzgtOTIuNzkzLTExOC45MjF6IiBmaWxsPSIjZmNhMzI2Ii8+CiAgPHBhdGggZD0iTTEyLjI2ODUgODQuNzM0Mmg1NC4xNTNsLTIzLjI3My03MS42MjVjLTEuMTk3LTMuNjg2LTYuNDExLTMuNjg1LTcuNjA4IDBsLTIzLjI3MiA3MS42MjV6IiBmaWxsPSIjZTI0MzI5Ii8+CiAgPHBhdGggZD0iTTEwNS4wNjE0IDIwMy42NTQ4bDM4LjY0LTExOC45MjFoNTQuMTUzbC05Mi43OTMgMTE4LjkyMXoiIGZpbGw9IiNmYzZkMjYiLz4KICA8cGF0aCBkPSJNMTk3Ljg1NDQgODQuNzM0MWwxMS43NDIgMzYuMTM5YzEuMDcxIDMuMjk2LS4xMDIgNi45MDctMi45MDYgOC45NDRsLTEwMS42MjkgNzMuODM4IDkyLjc5My0xMTguOTIxeiIgZmlsbD0iI2ZjYTMyNiIvPgogIDxwYXRoIGQ9Ik0xOTcuODU0NCA4NC43MzQyaC01NC4xNTNsMjMuMjczLTcxLjYyNWMxLjE5Ny0zLjY4NiA2LjQxMS0zLjY4NSA3LjYwOCAwbDIzLjI3MiA3MS42MjV6IiBmaWxsPSIjZTI0MzI5Ii8+Cjwvc3ZnPgo="
       alt="GitLab Logo" />
  </a>
  <h1>
    404
  </h1>
  <div class="container">
    <h3>The page could not be found or you don't have permission to view it.</h3>
    <hr />
    <p>The resource that you are attempting to access does not exist or you don't have the necessary permissions to view it.</p>
    <p>Make sure the address is correct and that the page hasn't moved.</p>
    <p>Please contact your GitLab administrator if you think this is a mistake.</p>
    <a href="javascript:history.back()" class="js-go-back go-back">Go back</a>
  </div>
  <script>
    (function () {
      var goBack = document.querySelector('.js-go-back');

      if (history.length > 1) {
        goBack.style.display = 'inline';
      }
    })();
  </script>
</body>
</html>

```


As it can be seen, there is a difference in both the responses that allow an attacker to exfiterate information about private/internal project. 

Since, this works for both internal/private project, the severity for private projects with internal groups is relatively higher as the group name is already know to the attacker.

### Steps to reproduce

1. Create a project from User A's account with private/internal privacy.
2. Go to user B' account and send the above mentioned request.
3. Based on the difference in responses, a user will be able to exfiltrate information about existance of a project.

### Impact

Information disclosure about existence of projects will lead to privacy breach.

### What is the current *bug* behavior?

Project does not exists response: 

████████

Project exists response:

██████████

### What is the expected *correct* behavior?

There should not be any difference in both the responses

### Output of checks

This bug happens on GitLab.com

## Impact

As mentioned above, 

Let me know, if you need more info,

Thanks,

-Milind

## Attachments
- 0.PNG
