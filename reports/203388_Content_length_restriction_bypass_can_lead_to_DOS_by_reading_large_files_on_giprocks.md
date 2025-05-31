# Content length restriction bypass can lead to DOS by reading large files on gip.rocks

## Report Details
- **Report ID**: 203388
- **URL**: https://hackerone.com/reports/203388
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-04T11:27:50.436Z
- **Disclosed**: 2017-03-31T14:50:05.910Z

## Reporter
- **Username**: a0xnirudh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hello team,

## Introduction

Since you mentioned in the rules that all libraries listed on your github repositories are in scope, I decided to take a look at http://gip.rocks

## Problem:

The application reads an image file and convert it into smaller formats, zip it and let the users to download the updated file. But the problem here is the condition check before reading the file to the variable:

File: https://github.com/gratipay/gip.rocks/blob/master/www/v1.spt

```python
if int(request.headers['Content-Length']) > 256 * 1024:
    raise Response(413)

image_type = request.headers['Content-Type']
if image_type not in ('image/png', 'image/jpeg'):
    raise Response(415)

# Load the image.
fp = StringIO(request.raw_body)
fp.seek(0)
image = Image.open(fp)

```

Here you can see that you are calculating the length of the incoming file from the `content-length` HTTP header and if it is less than `256 * 1024`, you will accept the request. But this is not a correct way to check size of the incoming file.

## POC:

1) Initiate a system wide proxy with burp suite

2) Try to send a curl request with a huge file and see the request in curl

3) The content length will be obviously greater than the max value application accepts but modify the `content-length` header to a value which is less than `256 * 1024`.

4) Forward the request and you can see that the server will read the files to a variable and if the file is large enough, this is more than enough to DOS the server.

Now since this deals with DOS, I haven't actually tried out this attack but we can easily confirm this from the source code that this can be bypassed in the way I explained above. I also tried deploying locally but I had a hard time making the software run locally and I don't have enough free time to debug what is happening.

But I think the bug is very clear from the source code itself, which is why I really didn't test it but thought to report it.

## Mitigation:

Putting your trust on HTTP headers may not be a good idea. But I am not really sure what is a solid method to find the proper length of the string in this case.

## Attachments
No attachments
