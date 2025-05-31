# Google storage bucket takeover which is used to load JS file in dashboard.html in "github.com/kubernetes/release" which can lead to XSS

## Report Details
- **Report ID**: 1398706
- **URL**: https://hackerone.com/reports/1398706
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-12T12:02:55.146Z
- **Disclosed**: 2021-12-16T21:56:53.423Z

## Reporter
- **Username**: codermak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Kubernetes have a github repository [github.com/kubernetes/release](https://github.com/kubernetes/release)
In the repository there is code for dashboard.
The  dashboard have a html file `dashboard.html` which is using a JS file from a google storage bucket.
The bucket was not registered on google cloud. So I was able to takeover the bucket and host PoC

## Kubernetes Version:
NA

## Component Version:
NA

## Steps To Reproduce:

  1. Go to https://github.com/kubernetes/release/blob/master/cmd/vulndash/dashboard.html#L6
  2. You will see this google storage bucket `storage.googleapis.com/k8s-artifacts-prod-vuln-dashboard` getting used at line 6
  3. Try accessing the bucket using this url https://storage.googleapis.com/k8s-artifacts-prod-vuln-dashboard/takeover.html
  4. You will see a base64 string, try decoding the string you will see takeover message.
  5. Bucket is also getting used to load some data from JSON file here https://github.com/kubernetes/release/blob/master/cmd/vulndash/dashboard.js#L1

## Supporting Material/References:

- https://storage.googleapis.com/k8s-artifacts-prod-vuln-dashboard/takeover.html
- https://github.com/kubernetes/release/blob/master/cmd/vulndash/dashboard.html#L6
- https://github.com/kubernetes/release/blob/master/cmd/vulndash/dashboard.js#L1

```
curl -s https://storage.googleapis.com/k8s-artifacts-prod-vuln-dashboard/takeover.html | base64 --decode
```

{F1511738}

{F1511740}

## Impact

An attacker can takeover the bucket and host maliicous JS file on it, when the js file will get loaded on the dashboard, it will run the malicious JS code which can also lead to XSS attacks.
Also, when the dashboard.js file tries to call the storage bucket to get the json data, that attacker will be able to control and can return malicious or misguiding or misleading information

## Attachments
- Screenshot_from_2021-11-12_17-29-02.png
- Screenshot_from_2021-11-12_17-32-10.png
