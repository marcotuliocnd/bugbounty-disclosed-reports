# DNS rebinding in --inspect via invalid octal IP address

## Report Details
- **Report ID**: 1710652
- **URL**: https://hackerone.com/reports/1710652
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-09-23T19:28:01.957Z
- **Disclosed**: 2022-12-07T19:11:53.956Z

## Reporter
- **Username**: haxatron1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
## Summary
The Node.js rebinding protector for --inspect still allows invalid IP address, specifically, the octal format.
An example of an octal IP address is 1.09.0.0, the 09 octet is invalid because 9 is not a number in the base 8 number system.
Browsers such as Firefox (tested on latest version m105) will still attempt to resolve this invalid octal address via DNS. When combined with an active --inspect session, such as when using VSCode, an attacker can perform DNS rebinding and execute arbitrary code

## Steps To Reproduce:
1. Add entry to /etc/hosts
```````
127.0.0.1       1.09.0.0
```````
2. Start `node --inspect`
3. Visit http://1.09.0.0:9229/json on Firefox (tested on m105) 
4. JSON file shows. This proves Firefox is resolving 1.09.0.0 to 127.0.0.1 via DNS. Additionally, you may use Wireshark to see that Firefox is sending DNS requests to 1.09.0.0 (without the /etc/hosts entry of course!)

## Impact

Bypass the DNS rebinding protection for --inspect and execute arbitrary code

## Attachments
No attachments
