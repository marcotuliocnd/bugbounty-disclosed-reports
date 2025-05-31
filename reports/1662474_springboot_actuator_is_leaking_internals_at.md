# springboot actuator is leaking internals at ██████████

## Report Details
- **Report ID**: 1662474
- **URL**: https://hackerone.com/reports/1662474
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-08-08T08:11:58.468Z
- **Disclosed**: 2022-09-14T20:29:17.123Z

## Reporter
- **Username**: thpless
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
### Proof of Concept

If you go to https://█████████/actuator you'll get a complete overview of all the endpoints that are accessable 
(Suggestion: Use a Firefox Browser if possible, its json representation is well formed and the links are clickable )

██████████

## Impact

Information Disclosure 

* https://████/actuator/beans
Displays a complete list of all the Spring beans in your application.

* https://██████████/actuator/caches
Exposes available caches. For ███ it is empty

* https://███████/actuator/health
The actual status of the actuator is displayed
```
status	"UP"
components	
diskSpace	
status	"UP"
details	
total	1167859712
free	1167810560
threshold	10485760
exists	true
ping	
status	"UP"
```

* https://███/actuator/info
version and  built time are displayed
```	
build	
version	"1.2.1-SNAPSHOT"
artifact	"unregister-file-endpoint"
name	"UnregisterFileEndpoint"
group	"com.hexusfed"
time	"2022-06-30T14:44:23.879Z"
```

* https://██████████/actuator/conditions
Shows the conditions that were evaluated on configuration and auto-configuration classes and the reasons why they did or did not match.

* https://█████/actuator/configprops
Displays a collated list of all configuration properties.

* https://█████/actuator/env
contains internal paths, ports, version numbers etc.

* https://███/actuator/loggers
configuration of loggers in the application

* https://███/actuator/heapdump *** (CRITICAL)***
Downloads a complete  heap dump file (about 30 MBs). This file has a  PHD-format and can be analyzed with a heapdump analyzer tool.

* https://█████████/actuator/threaddump
Performs a thread dump.

* https://████████/actuator/metrics
internal metrics

* https://█████/actuator/scheduledtasks
For this system there are no scheduled tasks running

* https://█████/actuator/mappings
Displays a collated list of all request paths (mapped to the coresponding internal software module).

## System Host(s)
████

## Affected Product(s) and Version(s)
spring-boot.actuator.v3

## CVE Numbers


## Steps to Reproduce
If you use the link https://███████/actuator, you'll see all the leaked endpoints in a json file

## Suggested Mitigation/Remediation Actions
By default, all endpoints except for shutdown are enabled. To configure the enablement of an endpoint, use its management.endpoint.<id>.enabled property.

Normally /actuator/health and /actuator/info are enabled the rest is disabled .



## Attachments
No attachments
