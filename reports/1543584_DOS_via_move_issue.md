# DOS via move_issue

## Report Details
- **Report ID**: 1543584
- **URL**: https://hackerone.com/reports/1543584
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-18T14:11:34.089Z
- **Disclosed**: 2022-11-04T03:44:34.198Z

## Reporter
- **Username**: legit-security
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
Moving an issue with a specially-crafted description results in high CPU usage for 60 seconds (request timeout).
Multiple requests can be issued in parallel to create a larger impact.

### Steps to reproduce
1. Given an authorized user (on GitLab.com - anyone can self-register. On EE - depends on instance configuration).
2. Create an issue with the following description (provided a one-line python script to avoid bloating):
3. Once created, move the issue to a different project.

The script:
```python -c "print('![l' * 100000 + '\n')"```
Note: works with a lower number of repetitions too.


### Impact
After 60 seconds (timeout) - the request fails.
Meanwhile, on the server end, (a single) CPU is burnt out (verified against a local EE instance).
Issuing multiple requests in parallel (on multiple GitLab issues) results in multiple CPUs burn out.
Using the DockerHub image, the entire server is completely unavailable by repeatedly sending a small number of requests repeatedly.

### Examples
The bug is instance-independent, works on latest versions. Since GitLab.com is open-core - it would work on GitLab too.

### What is the current *bug* behavior?
The HTTP request fails for timeout while the server is burning CPU.

On the code side:
lib/gitlab/gfm/uploads_rewriter.rb / module Gitlab/Gfm / class UploadsRewriter / function files:
```@text.scan(@pattern)```
Where FileUploader::MARKDOWN_PATTERN is assigned to the pattern data member.

MARKDOWN_PATTERN is: 
```\!?\[.*?\]\(/uploads/(?<secret>[0-9a-f]{32})/(?<file>.*?)\)```
The pattern is of a polynomial complexity, thus, the scan results in high CPU utilization.

### What is the expected *correct* behavior?
Instead of using Ruby’s default Regex engine, use the RE2 engine (or the wrapped version at lib/gitlab/untrusted_regexp.rb), with the following pattern:
```\!?\[.*\]\(/uploads/([0-9a-f]{32})/(.*)\)```
As RE2 does not go beyond O(n), this scan becomes linear.
Note: since RE2 does not support named captures, all references should be fixed - assigning the results to secret/identifier local variables.### Relevant logs and/or screenshots

### Output of checks

#### Results of GitLab environment info

## Impact

A complete denial of service of a GitLab EE instance.
As this vulnerability impacts GitLab.com, we assume that this vulnerability opens the door for a DDOS attack.

## Attachments
No attachments
