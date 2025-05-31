# Development Application Credentials + Information Exposed

## Report Details
- **Report ID**: 1018413
- **URL**: https://hackerone.com/reports/1018413
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-25T17:47:13.351Z
- **Disclosed**: 2020-12-03T19:01:21.042Z

## Reporter
- **Username**: lmhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
**Issue Description**
When I browsed through all the JS files on prow.k8s.io I came across a link called **/config** which contains a configuration disclosure for the development files

**URL Vulnerabilities**
https://prow.k8s.io/config

**Proof On Concept**
```javascript
- continuous-integration/travis-ci
kubespray:
required_status_checks:
contexts:
- Kubespray CI Pipeline
required_status_checks:
contexts:
- cla/linuxfoundation

- kubernetes-security
  rerun_auth_configs:
    '*':
      github_team_ids:
      - 2009231
      - 2460384
  spyglass:
    gcs_browser_prefix: https://gcsweb.k8s.io/gcs/
    gcs_browser_prefixes:
      '*': https://gcsweb.k8s.io/gcs/
    lenses:
    - lens:
        name: metadata
      optional_files:
      - ^(?:podinfo|prowjob)\.json$
      remote_config:
        endpoint: http://127.0.0.1:1234/dynamic/metadata
        hide_title: true
        priority: 0
        static_root: ""
        title: Metadata
      required_files:
      - ^(?:started|finished)\.json$
    - lens:
        config:
          highlight_regexes:
          - timed out
          - 'ERROR:'
          - (FAIL|Failure \[)\b
          - panic\b
          - ^E\d{4} \d\d:\d\d:\d\d\.\d\d\d]
          - '^INFO: Analyzed \d+ targets'
        name: buildlog
      remote_config:
        endpoint: http://127.0.0.1:1234/dynamic/buildlog
        hide_title: false
        priority: 10
        static_root: ""
        title: Build Log
      required_files:
      - ^.*build-log\.txt$
```

## Impact

Information Exposed + File Configuration Disclosure

## Attachments
No attachments
