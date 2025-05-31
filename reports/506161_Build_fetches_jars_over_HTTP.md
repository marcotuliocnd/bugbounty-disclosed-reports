# Build fetches jars over HTTP

## Report Details
- **Report ID**: 506161
- **URL**: https://hackerone.com/reports/506161
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-07T16:24:48.110Z
- **Disclosed**: 2019-06-10T19:01:06.838Z

## Reporter
- **Username**: jlleitschuh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: portswigger

## Vulnerability Information
[CWE-829: Inclusion of Functionality from Untrusted Control Sphere](https://cwe.mitre.org/data/definitions/829.html)
[CWE-494: Download of Code Without Integrity Check](https://cwe.mitre.org/data/definitions/494.html)

PortSwigger maintains several Open Source Projects under the [PortSwigger GitHub organization](https://github.com/PortSwigger). Some of these projects contain build files that indicate that some of these projects are resolving dependencies over HTTP instead of HTTPS. This allows these artifacts to be potentially MITMed to maliciously compromise them and infect the build artifacts that are produced. Additionally, if any of these JARs or other dependencies were compromised, any developers or production servers using these could continue to be infected past updating to fix this.

**Description:**

This attack leverages the build infrastructure loading dependencies over HTTP without any other sort of integrity check to allow them to be maliciously compromised.

### This isn't just theoretical
POC code has existed since 2014 to maliciously compromise a JAR file inflight.
See:
* https://max.computer/blog/how-to-take-over-the-computer-of-any-java-or-clojure-or-scala-developer/
* https://github.com/mveytsman/dilettante

### MITM Attacks Increasingly Common
See:
* https://serverfault.com/a/153065
* https://security.stackexchange.com/a/12050
* [Comcast continues to inject its own code into websites you visit](https://thenextweb.com/insights/2017/12/11/comcast-continues-to-inject-its-own-code-into-websites-you-visit/#) (over HTTP)

### Source Locations

#### Insecure Download

##### TeamCity Integration
- https://github.com/PortSwigger/burp-teamcity-integration/blob/4fc37ab14575ab9b54cf27e8ecac0923fa1ed3e0/pom.xml#L11-L22

##### Jenkins Integration

- https://github.com/PortSwigger/burp-jenkins-integration/blob/0151b131807d46ef0b55b172a1f23f988cd27bac/pom.xml#L17-L29

#### Insecure Upload

Insecure upload of artifacts is pretty much always accompanied by credentials. Since these credentials are sent over HTTP, they are transmitted in plaintext and should be considered compromised.

##### Jenkins Integration
 - https://github.com/PortSwigger/burp-jenkins-integration/blob/0151b131807d46ef0b55b172a1f23f988cd27bac/pom.xml#L61-L66

### Fix and Public Disclosure

At a minimum, all of these code locations where artifacts are downloaded from an untrusted source needs to be fixed. Previous releases should be rebuilt with the fix applied. The checksum of the released artifacts and artifacts built in a trusted environment should be made. If the checksums match, you can be certain that they weren't compromised.

If the checksums don't match, indicating a compromised artifact, CVE numbers need to be issued for the potentially malicious artifacts.

The ability to check if checksums match assume that these projects have [reproducible builds](https://en.wikipedia.org/wiki/Reproducible_builds).

## Steps To Reproduce:

  1. Cone the Impacted Project
  2. Change this line in Dilettante so it is targeting the repository used in the build.
       https://github.com/mveytsman/dilettante/blob/master/dilettante.py#L143
  3. Start Dilettante on your local machine.
  4. Proxy the HTTP traffic for the build through Dilettante
  5. Execute the Build's tests.
  6. You should be greeted with the image of a cat.


## Other Places to Look

Given how widely I'm finding this vulnerability externally, I'd advise that the Port Swigger Security team take some time to also analyze their internal infrastructure for similar vulnerabilities.

**This responsible disclosure follows [Google's 90-day vulnerability disclosure policy](https://www.google.com/about/appsecurity/) (I'm not an employee of Google, I just like their policy).**

## Impact

By insecurely downloading code over an untrusted connection HTTP and executing the untrusted code inside of these JAR files as part of the unit/integration tests before a release opens these artifacts up to being maliciously compromised.

Remote code execution on a production server. Malicious compromise of build artifacts.

## Attachments
No attachments
