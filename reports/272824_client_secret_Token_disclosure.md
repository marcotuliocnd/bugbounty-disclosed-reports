# client_secret Token disclosure 

## Report Details
- **Report ID**: 272824
- **URL**: https://hackerone.com/reports/272824
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-28T20:16:49.764Z
- **Disclosed**: 2017-09-28T21:07:49.028Z

## Reporter
- **Username**: yumi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: aspen

## Vulnerability Information
Greetings, 

I think I've discovered a ```client_secret``` token disclosure. 

**_Proof of concept:_**

**1.** Go to https://github.com/AspenWeb/experimental-javascript-version/blob/master/www/blog/index.html


**2.** At the line 6, a client_secret token it's disclosed. 

```
request('https://api.github.com/repos/zetaweb/aspen/issues?client_id=f58e3c865648d1eae132&client_secret=b1e49a627a30e3d41568ecaf976436f4bfbbefba', function (error, response, body) {
```

Thanks for your attention and let me know if you need anything. 
Regards, Yumi

## Attachments
No attachments
