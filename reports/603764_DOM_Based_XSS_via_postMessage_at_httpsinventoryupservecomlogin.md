# DOM Based XSS via postMessage at https://inventory.upserve.com/login/

## Report Details
- **Report ID**: 603764
- **URL**: https://hackerone.com/reports/603764
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-06-08T02:00:23.696Z
- **Disclosed**: 2019-06-25T13:56:46.607Z

## Reporter
- **Username**: gamer7112
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: upserve

## Vulnerability Information
#Description
DOM based XSS is possible at https://inventory.upserve.com/login/ due to insecure origin checking when receiving a postMessage.

#POC
1. Visit https://hq.upserve.com.████████/upserve_xss.html
2. Click link
3. View alert on https://inventory.upserve.com

#Vulnerable Code
```javascript
window.addEventListener("message", function(e) {
  if (~e.origin.indexOf("https://hq.upserve.com")) {
    if (e.data && typeof e.data == "object") {
      try {
        if (e.data["exec"]) {
          eval(e.data["exec"]);
        }
      } catch (err) {
        console.log(err);
      }
    } else {
      console.log("Non-object passed");
    }
  } else {
    console.log("Incorrect origin: " + e.origin.toString());
    return;
  }
});
```
The origin check simply determines if "https://hq.upserve.com" is anywhere in the origin so an origin like "https://hq.upserve.com.mydomain.com" will pass this check just fine.

## Impact

Due to the page being a login page, login credentials could be logged and stolen when a victim goes to login.

## Attachments
No attachments
