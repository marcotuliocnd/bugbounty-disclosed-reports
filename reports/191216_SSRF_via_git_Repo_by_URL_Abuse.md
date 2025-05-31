# SSRF via git Repo by URL Abuse

## Report Details
- **Report ID**: 191216
- **URL**: https://hackerone.com/reports/191216
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-14T19:59:53.158Z
- **Disclosed**: 2017-11-28T18:11:33.802Z

## Reporter
- **Username**: oroborus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi team ,

First things first, awesome work with <3 Gitlab 

######Description :
When creating a repository there is an option to pull existing repo from github by providing your github repos url endpoint, then a request is made to that url endpoint to fetch data and create repo on github fair enough till here. But the issue i wanna address here is that you are **not validating that the URL provided by user** this lets any malicious user request any arbitrary url on the internet and use gitlabs server to connect back to him.

######Steps to Reproduce : 

1. Create a repo
2. Click on git repo by url option 
3. Enter url of your public server and create a repo
4. Now if you access your servers access logs you will find 

``` http
 40.84.0.225 - - [14/Dec/2016 11:36:33] "GET /info/refs?service=git-upload-pack HTTP/1.1" 404 - 
```  
Which is requested by gitlab when creating the repo.

######POC:

>>As a poc i simply port forwarded port  **4444** on my router and started simple HTTP server and listened on 4444 to check for incoming connections, by doing the steps mentioned above i got a GET request from **40.84.0.225**  , images for the same are attached for reference.


######Impact:

Successful attack on this issue can lead to the following:

* Port scan intranet and external Internet facing servers
* Fingerprint internal (non-Internet exposed) network aware services
* Perform banner grabbing
* Run code on reachable machines
* Enumerate and attack services that are running on these hosts

Although i have not tested for any of these yet, this issue can still be misused to use this endpoint to initiate port scans or dos on other servers on the internet, as the hits will be going from your endpoint.


**Cheers!** 
####*Siddhu*

## Attachments
- 1.PNG
- 2.PNG
