# Exposed Prometheus instance at prometheus.qa.r3.com

## Report Details
- **Report ID**: 1200583
- **URL**: https://hackerone.com/reports/1200583
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-18T05:32:37.367Z
- **Disclosed**: 2021-07-12T08:40:26.437Z

## Reporter
- **Username**: ian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: r3

## Vulnerability Information
## Summary
Hi there, just wanted to note that all of your assets are listed as out of scope on HackerOne right now, which is a bit confusing. Nevertheless, I noticed that your Prometheus server at prometheus.qa.r3.com is exposed to the internet, which appears to let you view all of the internal metrics of all of your QA systems. This seems to be connected to your Kubernetes API server, so it seems pretty concerning.

I don't think this is incredibly concerning, as after all Prometheus is just metrics. But I don't think they are intended to be publicly exposed. :)

{F1305158}
{F1305159}

## Steps To Reproduce:
Visit https://prometheus.qa.r3.com/.

## Impact

Disclosure of normally private metrics

## Attachments
- Screen_Shot_2021-05-17_at_10.30.46_PM.png
- Screen_Shot_2021-05-17_at_10.30.17_PM.png
