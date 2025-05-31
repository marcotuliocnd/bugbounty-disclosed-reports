# Container scanning and Dependency scanning report leaked to unauthorized users

## Report Details
- **Report ID**: 676976
- **URL**: https://hackerone.com/reports/676976
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-19T22:30:30.193Z
- **Disclosed**: 2019-12-13T14:53:19.423Z

## Reporter
- **Username**: xanbanx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi GitLab Security team

### Summary

GitLab makes the container scanning and dependency scanning information available as part of a JSON endpoint for merge requests. These reports are output of the CI job and should only be displayed if the visiting user has access to CI. However, right now GitLab displays the the container scanning and dependency scanning reports regardless of this permission, making it available to whoever has access to the merge request.

For public projects, GitLab allows to restrict CI pipelines to project members only (public pipelines disabled). However, in this case, the merge request widget still renders the scanning reports result, which is the outcome of a CI pipeline.

### Steps to reproduce

This is reproducible on gitlab.com. It requires at least a gold plan to have the container scanning and dependency scanning feature available.

1. Create a public project, restrict CI pipeline access to project members, and disable public pipelines
2. Push a  new branch and add .gitlab-ci.yml file with the following content:

```yml
test:
  script: |
    echo '{"image": "registry.gitlab.com/groulot/container-scanning-test/master:5f21de6956aee99ddb68ae49498662d9872f50ff","unapproved": ["CVE-2017-18269","CVE-2017-16997","CVE-2018-1000001","CVE-2016-10228","CVE-2018-18520","CVE-2010-4052","CVE-2018-16869","CVE-2018-18311"],"vulnerabilities": [{ "featurename": "glibc", "featureversion": "2.24-11+deb9u3", "vulnerability": "CVE-2017-18269", "namespace": "debian:9", "description": "SSE2-optimized memmove implementation problem.", "link": "https://security-tracker.debian.org/tracker/CVE-2017-18269", "severity": "Defcon1", "fixedby": "2.24-11+deb9u4"},{ "featurename": "glibc", "featureversion": "2.24-11+deb9u3", "vulnerability": "CVE-2017-16997", "namespace": "debian:9", "description": "elf/dl-load.c in the GNU C Library (aka glibc or libc6) 2.19 through 2.26 mishandles RPATH and RUNPATH containing $ORIGIN for a privileged (setuid or AT_SECURE) program, which allows local users to gain privileges via a Trojan horse library in the current working directory, related to the fillin_rpath and decompose_rpath functions. This is associated with misinterpretion of an empty RPATH/RUNPATH token as the \"./\" directory. NOTE: this configuration of RPATH/RUNPATH for a privileged program is apparently very uncommon; most likely, no such program is shipped with any common Linux distribution.", "link": "https://security-tracker.debian.org/tracker/CVE-2017-16997", "severity": "Critical", "fixedby": ""},{ "featurename": "glibc", "featureversion": "2.24-11+deb9u3", "vulnerability": "CVE-2018-1000001", "namespace": "debian:9", "description": "In glibc 2.26 and earlier there is confusion in the usage of getcwd() by realpath() which can be used to write before the destination buffer leading to a buffer underflow and potential code execution.", "link": "https://security-tracker.debian.org/tracker/CVE-2018-1000001", "severity": "High", "fixedby": ""},{ "featurename": "glibc", "featureversion": "2.24-11+deb9u3", "vulnerability": "CVE-2016-10228", "namespace": "debian:9", "description": "The iconv program in the GNU C Library (aka glibc or libc6) 2.25 and earlier, when invoked with the -c option, enters an infinite loop when processing invalid multi-byte input sequences, leading to a denial of service.", "link": "https://security-tracker.debian.org/tracker/CVE-2016-10228", "severity": "Medium", "fixedby": ""},{ "featurename": "elfutils", "featureversion": "0.168-1", "vulnerability": "CVE-2018-18520", "namespace": "debian:9", "description": "An Invalid Memory Address Dereference exists in the function elf_end in libelf in elfutils through v0.174. Although eu-size is intended to support ar files inside ar files, handle_ar in size.c closes the outer ar file before handling all inner entries. The vulnerability allows attackers to cause a denial of service (application crash) with a crafted ELF file.", "link": "https://security-tracker.debian.org/tracker/CVE-2018-18520", "severity": "Low", "fixedby": ""},{ "featurename": "glibc", "featureversion": "2.24-11+deb9u3", "vulnerability": "CVE-2010-4052", "namespace": "debian:9", "description": "Stack consumption vulnerability in the regcomp implementation in the GNU C Library (aka glibc or libc6) through 2.11.3, and 2.12.x through 2.12.2, allows context-dependent attackers to cause a denial of service (resource exhaustion) via a regular expression containing adjacent repetition operators, as demonstrated by a {10,}{10,}{10,}{10,} sequence in the proftpd.gnu.c exploit for ProFTPD.", "link": "https://security-tracker.debian.org/tracker/CVE-2010-4052", "severity": "Negligible", "fixedby": ""},{ "featurename": "nettle", "featureversion": "3.3-1", "vulnerability": "CVE-2018-16869", "namespace": "debian:9", "description": "A Bleichenbacher type side-channel based padding oracle attack was found in the way nettle handles endian conversion of RSA decrypted PKCS#1 v1.5 data. An attacker who is able to run a process on the same physical core as the victim process, could use this flaw extract plaintext or in some cases downgrade any TLS connections to a vulnerable server.", "link": "https://security-tracker.debian.org/tracker/CVE-2018-16869", "severity": "Unknown", "fixedby": ""},{ "featurename": "perl", "featureversion": "5.24.1-3+deb9u4", "vulnerability": "CVE-2018-18311", "namespace": "debian:9", "description": "Perl before 5.26.3 and 5.28.x before 5.28.1 has a buffer overflow via a crafted regular expression that triggers invalid write operations.", "link": "https://security-tracker.debian.org/tracker/CVE-2018-18311", "severity": "Unknown", "fixedby": "5.24.1-3+deb9u5"},{ "featurename": "foo", "featureversion": "1.3", "vulnerability": "CVE-2018-666", "namespace": "debian:9", "description": "Foo has a vulnerability nobody cares about and whitelist.", "link": "https://security-tracker.debian.org/tracker/CVE-2018-666", "severity": "Unknown", "fixedby": "1.4"}]}' > gl-container-scanning-report.json
    echo '{"version": "1.3","vulnerabilities": [{"category": "dependency_scanning","name": "io.netty/netty - CVE-2014-3488","message": "DoS by CPU exhaustion when using malicious SSL packets","cve": "app/pom.xml:io.netty/netty@3.9.1.Final:CVE-2014-3488","severity": "Unknown","solution": "Upgrade to the latest version","scanner": {"id": "gemnasium","name": "Gemnasium"},"location": {"file": "app/pom.xml","dependency": {"package": {"name": "io.netty/netty"},"version": "3.9.1.Final"}},"identifiers": [{"type": "gemnasium","name": "Gemnasium-d1bf36d9-9f07-46cd-9cfc-8675338ada8f","value": "d1bf36d9-9f07-46cd-9cfc-8675338ada8f","url": "https://deps.sec.gitlab.com/packages/maven/io.netty/netty/versions/3.9.1.Final/advisories"},{"type": "cve","name": "CVE-2014-3488","value": "CVE-2014-3488","url": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3488"}],"links": [{"url": "https://bugzilla.redhat.com/CVE-2014-3488"},{"url": "http://netty.io/news/2014/06/11/3.html"},{"url": "https://github.com/netty/netty/issues/2562"}],"priority": "Unknown","file": "app/pom.xml","url": "https://bugzilla.redhat.com/CVE-2014-3488","tool": "gemnasium"},{"category": "dependency_scanning","name": "Django - CVE-2017-12794","message": "Possible XSS in traceback section of technical 500 debug page","cve": "app/requirements.txt:Django@1.11.3:CVE-2017-12794","severity": "Unknown","solution": "Upgrade to latest version or apply patch.","scanner": {"id": "gemnasium","name": "Gemnasium"},"location": {"file": "app/requirements.txt","dependency": {"package": {"name": "Django"},"version": "1.11.3"}},"identifiers": [{"type": "gemnasium","name": "Gemnasium-6162a015-8635-4a15-8d7c-dc9321db366f","value": "6162a015-8635-4a15-8d7c-dc9321db366f","url": "https://deps.sec.gitlab.com/packages/pypi/Django/versions/1.11.3/advisories"},{"type": "cve","name": "CVE-2017-12794","value": "CVE-2017-12794","url": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-12794"}],"links": [{"url": "https://www.djangoproject.com/weblog/2017/sep/05/security-releases/"}],"priority": "Unknown","file": "app/requirements.txt","url": "https://www.djangoproject.com/weblog/2017/sep/05/security-releases/","tool": "gemnasium"},{"category": "dependency_scanning","name": "nokogiri - USN-3424-1","message": "Vulnerabilities in libxml2","cve": "rails/Gemfile.lock:nokogiri@1.8.0:USN-3424-1","severity": "Unknown","solution": "Upgrade to latest version.","scanner": {"id": "gemnasium","name": "Gemnasium"},"location": {"file": "rails/Gemfile.lock","dependency": {"package": {"name": "nokogiri"},"version": "1.8.0"}},"identifiers": [{"type": "gemnasium","name": "Gemnasium-06565b64-486d-4326-b906-890d9915804d","value": "06565b64-486d-4326-b906-890d9915804d","url": "https://deps.sec.gitlab.com/packages/gem/nokogiri/versions/1.8.0/advisories"},{"type": "usn","name": "USN-3424-1","value": "USN-3424-1","url": "https://usn.ubuntu.com/3424-1/"}],"links": [{"url": "https://github.com/sparklemotion/nokogiri/issues/1673"}],"priority": "Unknown","file": "rails/Gemfile.lock","url": "https://github.com/sparklemotion/nokogiri/issues/1673","tool": "gemnasium"},{"category": "dependency_scanning","name": "ffi - CVE-2018-1000201","message": "ruby-ffi DDL loading issue on Windows OS","cve": "ffi:1.9.18:CVE-2018-1000201","severity": "High","solution": "upgrade to \u003e= 1.9.24","scanner": {"id": "bundler_audit","name": "bundler-audit"},"location": {"file": "sast-sample-rails/Gemfile.lock","dependency": {"package": {"name": "ffi"},"version": "1.9.18"}},"identifiers": [{"type": "cve","name": "CVE-2018-1000201","value": "CVE-2018-1000201","url": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000201"}],"links": [{"url": "https://github.com/ffi/ffi/releases/tag/1.9.24"}],"priority": "High","file": "sast-sample-rails/Gemfile.lock","url": "https://github.com/ffi/ffi/releases/tag/1.9.24","tool": "bundler_audit"}]}' > gl-dependency-scanning-report.json
  artifacts:
    reports:
      container_scanning: gl-container-scanning-report.json
      dependency_scanning: gl-dependency-scanning-report.json

```
3. Create a merge request with those changes
4. As an unauthorized user, visit the page `https://example.gitlab.com/<namespace>/<public-project-name>/merge_requests/1/merge_requests/1/container_scanning_reports` and `https://example.gitlab.com/<namespace>/<public-project-name>/merge_requests/1/merge_requests/1/dependency_scanning_reports`

These two endpoints are now leaking the container scanning dependency scanning information to unauthorized users, who do not have access to CI. 

### Impact

Unauthorized users have access to critical information like the container scanning or dependency scanning report, thus have a lot of insight of an application. By knowing the found vulnerabilities (or still existing), they could attack the target application.

### Examples

This happens on gitlab.com. I've setup a test project, where the CI pipeline access is restricted to project members. However, you can access the container scanning and dependency scanning report from CI via the following endpoints:

* https://gitlab.com/test-group-wter/test-reports/merge_requests/1/container_scanning_reports
* https://gitlab.com/test-group-wter/test-reports/merge_requests/1/dependency_scanning_reports

### What is the current *bug* behavior?

Container scanning and dependency scanning reports are leaked on merge requests endpoints. 

### What is the expected *correct* behavior?

Container scanning and dependency scanning report endpoints on merge requests require proper access control to avoid leaking it to unauthorized users.

Best regards,
Xanbanx

## Impact

See above

## Attachments
No attachments
