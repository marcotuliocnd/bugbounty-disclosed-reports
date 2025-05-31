# Unsafe yaml load can lead to remote code execution

## Report Details
- **Report ID**: 2467232
- **URL**: https://hackerone.com/reports/2467232
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-04-17T13:32:57.671Z
- **Disclosed**: 2024-05-04T11:50:22.497Z

## Reporter
- **Username**: tarun_sec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
TL;DR
Yaml.load() has the ability to construct an arbitrary Python object. This is dangerous if you receive a YAML document from an untrusted source.


Proof of concept 
https://github.com/liberapay/liberapay.com/blob/master/liberapay/testing/vcr.py#L40

How do I fix it?
Always use yaml.safe_load(). This function limits this ability to simple Python objects like integers or lists. 

If you have any questions 
please comment on the report 

best regards
mrrobot2050

## Impact

Yaml.load() has the ability to construct an arbitrary Python object. This is dangerous if you receive a YAML document from an untrusted source.

## Attachments
- Screenshot_2024-04-17_at_7.02.27_PM.png
