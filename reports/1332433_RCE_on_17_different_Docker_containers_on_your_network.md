# RCE on 17 different Docker containers on your network

## Report Details
- **Report ID**: 1332433
- **URL**: https://hackerone.com/reports/1332433
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-09-07T16:45:45.843Z
- **Disclosed**: 2021-10-20T15:07:37.818Z

## Reporter
- **Username**: 0x0luke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
I was able to get RCE on 17 different docker containers, ranging from postgres and some prod enviroments

## Steps To Reproduce:
I found that there was a unconfigured portainer.io service running on http://spreed-demo.nextcloud.com:9000

  1. I created an administrator account with the login creds admin:password (please change these credentials!!!)
  2. The site redirected me to the portainer backend, which displayed the docker containers running on the box, see first screen shot
  3. I was able to fully interact with the docker containers running, the site also allows me to execute arbitrary bash commands on the boxes, See second screenshot

Other info that was disclosed to me from the panel:
Internal IP addresses,
Docker disk volumes
Docker images,
The docker stacks

## Supporting Material/References:

{F1439949}
{F1439951}

## Impact

An attacker can directly take over each docker container on this system to deploy his own malware, run DDoS attacks etc from inside Nextclouds services.

## Attachments
- RCE.PNG
- RCE2.PNG
