# [Twitter Open Source] Releases were & are built/executed/tested/released in the context of insecure/untrusted code

## Report Details
- **Report ID**: 505007
- **URL**: https://hackerone.com/reports/505007
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-05T03:05:54.116Z
- **Disclosed**: 2019-12-13T21:08:47.178Z

## Reporter
- **Username**: jlleitschuh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:**

[CWE-829: Inclusion of Functionality from Untrusted Control Sphere](https://cwe.mitre.org/data/definitions/829.html)
[CWE-494: Download of Code Without Integrity Check](https://cwe.mitre.org/data/definitions/494.html)

Twitter maintains several Open Source Projects under the [Twitter GitHub organization](https://github.com/twitter). These projects contain build files that indicate that some of these projects are resolving dependencies over HTTP instead of HTTPS. This allows these artifacts to be potentially MITMed to maliciously compromise them and infect the build artifacts that are produced. Additionally, if any of these JARs or other dependencies were compromised, any developers or production servers using these could continue to be infected past updating to fix this.

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

##### Scrooge
  - https://github.com/twitter/scrooge/blob/b8fb8b563cb152b5d46c2ec8a24c9c134cdde140/project/plugins.sbt#L1-L6
 
##### Tormentia
 - https://github.com/twitter/tormenta/blob/50cf4773fd188a6ae82ab87e306a58c064cced1e/project/plugins.sbt#L1-L3

##### Scalding
 - https://github.com/twitter/scalding/blob/19429900e9fcdaa5c38160f0b68b579aac3f4604/project/plugins.sbt#L1-L7

##### Diffy
 - https://github.com/twitter/diffy/blob/7894459430d27d184d3663e0570f535a93fa61c6/project/plugins.sbt#L3

##### Bijection
 - https://github.com/twitter/bijection/blob/11c8325bb734bb3bd36d8d7ac6dd1dd48d82f7e3/project/plugins.sbt#L2

##### Algebird
 - https://github.com/twitter/algebird/blob/01f989f4ad534c1450ab0982669393ba1817a6d1/project/plugins.sbt#L1-L5

##### Hdfs-Du
 - https://github.com/twitter/hdfs-du/blob/5caaa0cf117ed1ebbe873ec1e8302a535bd0bc5d/pom.xml#L64-L75

##### Iago
 - https://github.com/twitter/iago/blob/019a4adfbfa913e6307cdc5a589089e95cfb6285/examples/echo/pom.xml#L17-L28

##### Ambrose
- https://github.com/twitter/ambrose/blob/da7bcb932c418c157d9c372a4ca5f1884b874d78/cascading/pom.xml#L14-L19
- https://github.com/twitter/ambrose/blob/da7bcb932c418c157d9c372a4ca5f1884b874d78/scalding/pom.xml#L22-L27

###### BookKeeper
 - https://github.com/twitter/bookkeeper/blob/91c85ab8350dfc00c2bc07f0bed338ce4d87b2f6/bookkeeper-stats-providers/twitter-finagle-provider/pom.xml#L48-L53

###### Elephant-Bird

- https://github.com/twitter/elephant-bird/blob/62642c935198aa0ff968f48669c7e654b42dfbf0/cascading3/pom.xml#L13-L18

###### JOAuth
- https://github.com/twitter/joauth/blob/b4f6afb6be79ecb0bb8d04c76b17cfa51de4ffab/project/plugins/Plugins.scala#L10-L16

###### Ect...

This list is not exaustive, I just wanted to come up with examples so the Twitter security team could get a general sense of what they are looking for.

Here are the GitHub queries I used to find these:
 - [SBT Builds with Resolvers over HTTP](https://github.com/search?q=org%3Atwitter+resolvers+http%3A%2F%2F&type=Code)
 - [Maven POM files with Repositories over HTTP](https://github.com/search?l=Maven+POM&p=2&q=org%3Atwitter+repositories+http%3A%2F%2F&type=Code)

**WARNING!** If any of these builds are using a shared or reused `~/.gradle`, `~/.m2` or whatever SBT uses as an artifact cache between builds and any of these downloads were maliciously compromised, the compromised jar may remain inside of cache directory and continue to be used in future builds.

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

Given how widely I'm finding this vulnerablity externally to Twitter, I'd advise that the Twitter Security team take some time to also analize their internal infrastructure for similar vulnerabilities.

**This responsible disclosure follows [Google's 90-day vulnerability disclosure policy](https://www.google.com/about/appsecurity/) (I'm not an employee of Google, I just like their policy).**

## Impact

By insecurely downloading code over an untrusted connection HTTP and executing the untrusted code inside of these JAR files as part of the unit/integration tests before a release opens these artifacts up to being maliciously compromised.

Remote code execution on a production server. Malicious compromise of build artifacts.

## Attachments
No attachments
