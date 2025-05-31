# Unauthorized access

## Report Details
- **Report ID**: 1669176
- **URL**: https://hackerone.com/reports/1669176
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-14T23:06:00.908Z
- **Disclosed**: 2022-08-25T14:14:31.613Z

## Reporter
- **Username**: mega7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hello Gents,
I would like to report an issue where attackers are able to:
1. List `about.gitlab.com` GS bucket.
2. Access all resales through https://about.gitlab.com/all-releases.xml & https://about.gitlab.com/security-releases.xml, which contains undisclosed HackerOne reports.
> For Example:
```
<p>This vulnerability has been discovered internally by the GitLab team.</p> <h2 id="pipeline-subscriptions-trigger-new-pipelines-with-the-wrong-author">Pipeline subscriptions trigger new pipelines with the wrong author</h2> <!-- https://gitlab.com/gitlab-org/security/gitlab/-/issues/642 -->
 <p>A critical issue has been discovered in GitLab affecting all versions starting from 14.0 prior to 14.10.5, 15.0 prior to 15.0.4, and 15.1 prior to 15.1.1 where an authenticated user authorized to import projects could import a maliciously crafted project leading to remote code execution. This is a critical severity issue (<code>CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H</code>, 9.9). It is now mitigated in the latest release and is assigned <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2185">CVE-2022-2185</a>.</p> <p>Thanks <a href="https://hackerone.com/vakzz">vakzz</a>
```
3. Access https://about.gitlab.com/mindmap.txt which contains this internal Google Documents link:
https://docs.google.com/document/d/e/2PACX-1vSNzTLkZMqILVYoey4dnSLYdk0Jmsd8pFu7ygLJ57RQ1c8XlZDbzaG45rQMOrDbHRWCQa5LN7DZid8s/pub
> I didn't dig in so much , but I was able to edit a document like this one: 
> [GitLab_MessageGuide](https://docs.google.com/document/d/14APaSKwYpwutujISnkbLOnjdQ5RG-hIQXulasZT7h6s/edit)
4. list All Gitlab Staff full names through https://about.gitlab.com/roulette.json
5. All JavaScript files using `gsutil ls gs://about.gitlab.com/javascripts/`, there are many other files too.
> Also please take a look at this json file: https://storage.googleapis.com/about.gitlab.com/_nuxt/content/db-0881eaf3.json, it contains phone numbers, tokens, and more than 1000 URLs could be useful for attackers.

### Steps to reproduce:
+ Please visit https://storage.googleapis.com/about.gitlab.com, or you can install [gsutil](https://cloud.google.com/storage/docs/gsutil_install). then list the bucket using the following command: 
+ `gsutil ls gs://about.gitlab.com/`.

### Proof of concept
+ {F1867120}
+ {F1867121}
+ {F1867122}
+ {F1867125}

## Impact

Unauthorized access & Information disclosure.

Thanks and have a nice day!

## Attachments
- Screenshot_(57).png
- Screenshot_(58).png
- Screenshot_(59).png
- Screenshot_(60).png
