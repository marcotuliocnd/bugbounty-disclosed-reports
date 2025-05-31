# XSSI (Cross Site Script Inclusion)

## Report Details
- **Report ID**: 118631
- **URL**: https://hackerone.com/reports/118631
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-24T23:00:33.343Z
- **Disclosed**: 2017-08-22T22:38:07.744Z

## Reporter
- **Username**: paulos__
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: coinbase

## Vulnerability Information
Hi,

https://www.coinbase.com/pusher/auth returns sensetive  a json auth-token response that can be parsed by 
```javascript
JSON.parse()
```
from external site. this can easily be mitigated by putting /**/ or // chars at the beginning of the json response and thus making functions like JSON.parse unable to get the data extracted because of parsing errors.

I do know the url takes 2 post parameters and one of them being a **channel name** to properly get the json response. but if an attacker get access to that parameter, just once. he will forever be able to use it. 

for instance:
```html
<form action="https://www.coinbase.com/pusher/auth?callback=tothis" method="POST">
<input type="hidden" name="socket_id" value="1.266427">
<input type="hidden" name="channel_name" value="private-549850166bb03f3b19000147-QPCIGVGojmUh1w">
<input type="submit">
</form>
```
if I visit that URL I will get the json response, now persumably the channel_name would reset over time or when I log out. unfortunatly, that isn't true. if I log back in, that private channel_name would still result a token, in other words, never expiring and reusable. combining this with json parsing, it is possible for an attacker who knows the channel_name to steal the tokens, over and over.

Thanks,


## Attachments
No attachments
