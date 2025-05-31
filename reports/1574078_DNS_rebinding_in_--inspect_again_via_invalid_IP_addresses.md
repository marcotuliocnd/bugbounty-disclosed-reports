# DNS rebinding in --inspect (again) via invalid IP addresses 

## Report Details
- **Report ID**: 1574078
- **URL**: https://hackerone.com/reports/1574078
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-05-18T05:48:02.207Z
- **Disclosed**: 2023-08-11T16:38:13.629Z

## Reporter
- **Username**: haxatron1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
The IsAllowedHost check in https://github.com/nodejs/node/blob/fdf0a84e826d3a9ec0ce6f5a3f5adc967fe99408/src/inspector_socket.cc#L580 can easily be bypassed because IsIPAddress does not properly check if an IP address is invalid or not. When an invalid IPv4 address is provided (for instance 10.0.2.555 is provided), the browser will make a DNS requests to the DNS server, providing a vector for an attacker-controlled DNS server to perform a rebinding attack and hence access the JSON file containing the WebSocket file.

## Steps To Reproduce:
The steps to reproduce is mostly the same as https://hackerone.com/reports/1069487, but replace localhost6 with 10.0.2.555, I am copying it here for reference.

1. Victim runs node with --inspect option
2. Victim visits attacker's webpage
3. The attacker's webpage redirects to http://10.0.2.555:9229 
4. 10.0.2.555 is not a valid IP address so the browser asks the malicious DNS server and gets <attacker's-IP> with a short TTL.
5. Victim loads webpage http://10.0.2.555:9229 from <attacker's-IP>.
6. The webpage http://10.0.2.555:9229 tries to load http://10.0.2.555:9229/json from attacker's server. 
7. Due to a short TTL, the DNS server will be soon asked again about an entry for “10.0.2.555”. This time, the DNS server responds “127.0.0.1”.
The http://10.0.2.555:9229 website (i.e., the one hosted on <attacker's IP>) will retrieve http://10.0.2.555:9229/json from 127.0.0.1, including webSocketDebuggerUrl. Now, the attacker knows the webSocketDebuggerUrl and can connect to is using WebSocket. Note that WebSocket is not restricted by same-origin-policy. By doing so, they can gain the privileges of the Node.js instance.
8. In https://github.com/nodejs/node/blob/fdf0a84e826d3a9ec0ce6f5a3f5adc967fe99408/src/inspector_socket.cc#L164L175, the debugger does not recognise that 10.0.2.555 is not a valid IP address and so will allow disclosure of /json file.

To confirm this issue, I will just show two things (let me know if this is not enough):
A) That when 10.0.2.555 is keyed into the browser (Firefox used), a DNS resolution request will be made by a browser to a DNS server, (thus, allowing the DNS rebinding vector to occur,
1. Open Wireshark 
2. Add a redirector
````
<?php

header("Location: http://10.0.2.555:9229/json");
````
3: In the browser visit the the redirector
4. In Wireshark, see that DNS resolution request is being made for 10.0.2.555

B) That when 10.0.2.555 is resolved, the browser will send a Host: 10.0.2.555 which the NodeJS debugger accepts and exposes the /json file.
1. Modify /etc/hosts file
````
10.0.2.555      127.0.0.1
````
2. Visit the redirector in A) to get redirected to the /json file.

## Impact: 
Attacker can gain access to the Node.js debugger, which can result in remote code execution.

## References:
https://hackerone.com/reports/1069487
https://nodejs.org/en/docs/guides/debugging-getting-started/

## Recommended Fix
The isIPAddress() check in https://github.com/nodejs/node/blob/fdf0a84e826d3a9ec0ce6f5a3f5adc967fe99408/src/inspector_socket.cc#L164L175 should be more stricter in validation.

## Impact

Attacker can gain access to the Node.js debugger, which can result in remote code execution.

## Attachments
No attachments
