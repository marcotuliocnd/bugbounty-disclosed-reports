# HTML injection and information disclosure in support panel

## Report Details
- **Report ID**: 634312
- **URL**: https://hackerone.com/reports/634312
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-03T08:15:19.173Z
- **Disclosed**: 2019-07-09T13:43:59.828Z

## Reporter
- **Username**: xaleraf4ra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hello Weblate Team!

I found HTML injection and information disclosure in support panel

###Description
There is a form to ```weblate.org``` and ```hosted.weblate.org``` to send to support
I poisoned the request, where I inserted such payload in all fields:
```
"><img src="[SERVER]">
```

After that, when my payload got into the support panel, it was reproduced and the picture was uploaded, after that requests were sent to my server

#####So HTML injection is there
Further, having examined in detail the requests that came to me on the server, I saw (private) ip addresses of administrators or employees (support panel)

###### IP Adresses
```
37.9.65.65
89.187.189.240
95.108.197.9
178.154.167.78
```

###### User Agent
```
User-Agent: Mozilla/5.0 (iPad; CPU OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Canary
```

## Impact

The vulnerability allows you to execute HTML code in the support panel, also steal personal data of administrators, employees, for example: IP Addresses, which browsers employees use, and so on.


Best regards Bogdan

## Attachments
- _________________2019-07-03_11-14-51.png
- _________________2019-07-03_11-14-59.png
