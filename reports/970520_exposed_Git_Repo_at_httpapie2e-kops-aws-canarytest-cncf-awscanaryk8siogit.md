# exposed Git Repo at http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/

## Report Details
- **Report ID**: 970520
- **URL**: https://hackerone.com/reports/970520
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-08-30T03:34:57.629Z
- **Disclosed**: 2021-01-07T18:33:23.911Z

## Reporter
- **Username**: zevfw5pp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Dear Security team,

If this report is out of scope,  please let me know and I will close the report myself

I found a git repository on http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/.git. This endpoint allows an attacker to retrieve much of the source code and git history for this service which could potentially reveal sensitive information, it all depends what is stored there.

Example:
http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/logs/HEAD
http://api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io/.git/config
Mitigation
The restrict access (403 forbidden) are enabled only on /.git and not their subfolders. You just need to add all the git subfolders to the same rule.


Best Regards,
Daniel

## Impact

An attacker can get information just dumping data using  .git repository.

## Attachments
No attachments
