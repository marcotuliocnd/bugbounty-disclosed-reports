# Transferring incorrect data to the http://gip.rocks/v1 endpoint with correct Content-Type leads to local paths disclosure through the error message

## Report Details
- **Report ID**: 219601
- **URL**: https://hackerone.com/reports/219601
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-08T18:48:38.907Z
- **Disclosed**: 2017-04-08T19:30:14.931Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Description
Hi. I found the way to raise 500 Internal Server Error with some sensitive information disclosure (some local paths of the python installation). The issue is not critical, however, you can prevent this information leak.

Request:
```
POST /v1 HTTP/1.1
Host: gip.rocks
Cache-Control: max-age=0
Content-Type: image/jpeg
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch
Accept-Language: ru,en-US;q=0.8,en;q=0.6,uk;q=0.4
Content-Length: 3

111
```
Response:
```
<html>
    <head>
        <title>500 Internal Server Error</title>
        <style>
            
            BODY {
                margin: 0;
                padding: 200px 0 0;
                text-align: center;
                font: normal 18pt/18pt Georgia, serif;
            }
            PRE {
                text-align: left;
                font: normal 10pt/12pt monospace;
                margin: 50px 200px 0;
            }
        </style>
    </head>
    <body>
        Internal server error, program!
        <pre>Traceback (most recent call last):
  File &quot;/app/.heroku/python/lib/python2.7/site-packages/algorithm.py&quot;, line 288, in run
    new_state = function(**deps.as_kwargs)
  File &quot;/app/.heroku/python/lib/python2.7/site-packages/aspen/algorithms/website.py&quot;, line 115, in get_response_for_resource
    return {'response': resource.respond(state)}
  File &quot;/app/.heroku/python/lib/python2.7/site-packages/aspen/http/resource.py&quot;, line 59, in respond
    content_type, body = super(Dynamic, self).respond(accept, state)
  File &quot;/app/.heroku/python/lib/python2.7/site-packages/aspen/simplates/__init__.py&quot;, line 169, in respond
    exec(self.pages[1], context)
  File &quot;/app/www/v1.spt&quot;, line 22, in &lt;module&gt;
    image = Image.open(fp)
  File &quot;/app/.heroku/python/lib/python2.7/site-packages/PIL/Image.py&quot;, line 2349, in open
    % (filename if filename else fp))
IOError: cannot identify image file &lt;cStringIO.StringI object at 0x7f6b803082d8&gt;
</pre>
    </body>
</html>
```

# Steps To Reproduce

1. Conduct the POST request attached above to the `http://gip.rocks/v1` using Burp, Charles, or 
https://www.hurl.it/ with correct Content-Type header:
{F174337}
{F174336}
2. Check the response.

# Patch
I think you need just some exception handling block when perform image load at `https://github.com/gratipay/gip.rocks/blob/master/www/v1.spt` on line 19
```
# Load the image.
fp = StringIO(request.raw_body)
fp.seek(0)
image = Image.open(fp)
```



## Attachments
- z1.JPG
- z.JPG
