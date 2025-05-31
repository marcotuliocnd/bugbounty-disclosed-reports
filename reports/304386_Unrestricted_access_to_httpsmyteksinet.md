# Unrestricted access to https://██████.█████myteksi.net/

## Report Details
- **Report ID**: 304386
- **URL**: https://hackerone.com/reports/304386
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-12T22:26:21.523Z
- **Disclosed**: 2018-02-12T07:09:58.517Z

## Reporter
- **Username**: reptou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: grab

## Vulnerability Information
Hello again Grab Security Team !

Following my previous research, it seems that your Microservices architecture you are currently running on *.█████myteksi.net is publicly exposed on another endpoint : https://█████████.█████myteksi.net. 

**Summary:** 

When researching and starting a new enumeration of your different subdomains, I found that https://███.████████myteksi.net is related to your Eureka / Zuul environment and is reachable without any filtering. 

**Description:**

This is a quite complex architecture, but I think that it reveals a lot of debug information that could help an attack find a vector, and certainly enables him to do some actions on this infrastructure without any control (this has to be confirmed as I do not want to perform any modification on your curent environment). 

In order to understand the way this infrastructure works, I read the following documentation to discover some endpoints and see what could be achieved : http://cloud.spring.io/spring-cloud-static/Finchley.M5/single/spring-cloud.html#_health_indicator_2

Regarding information gathering, there are different endpoints reachable for example :

* https://█████.███████myteksi.net/info
* https://████.██████myteksi.net/dump
* https://███████.█████████myteksi.net/trace
* https://████████.██████████myteksi.net/configprops
* https://████████.███myteksi.net/env (from this one you got the eureka username and I guess the password too even if this is hidden ;-))
* https://█████.████myteksi.net/beans
* https://█████.█████myteksi.net/metrics
* https://███.████myteksi.net/autoconfig
* https://███.█████████myteksi.net/routes
* https://██████████.█████████myteksi.net/features

For the action to be done, we may notice the following (extract from the documentation) :

```
For a Spring Boot Actuator application there are some additional management endpoints:

* POST to /env to update the Environment and rebind @ConfigurationProperties and log levels
* /refresh for re-loading the boot strap context and refreshing the @RefreshScope beans
* /restart for closing the ApplicationContext and restarting it (disabled by default)
* /pause and /resume for calling the Lifecycle methods (stop() and start() on the ApplicationContext) 
```
As stated previously, I did not try these actions, but I have a good confidence that it will be executed without any restriction. 

From my point of view, this is an internal infrastructure that should not be exposed to any Internet user (as for the eureka endpoint previously reported). 

## Browsers Verified In:

N/A

## Steps To Reproduce:

  1. Just try previous URL with correct HTTP Verb if necessary (GET / POST...)

Please let me know your thoughts on this,

Thank you !

Reptou

## Impact

This is quite difficult to know exactly what could be achieved as the infrastructure is complex. However, I would say that it could first enable an attacker to understand better your infrastructure and identify weaknesses. The other point is that if the attacker is able to perform some actions, this could lead to DoS of this service in some cases and, of course, unexpected behaviour (modfying env properties ...)

## Attachments
No attachments
