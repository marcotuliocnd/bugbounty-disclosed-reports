# Development configuration file

## Report Details
- **Report ID**: 231267
- **URL**: https://hackerone.com/reports/231267
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-05-23T21:21:30.618Z
- **Disclosed**: 2018-01-18T10:18:17.634Z

## Reporter
- **Username**: protector47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pushwoosh

## Vulnerability Information
Hello,
I found an **Sensitive Information Disclosure**.
A configuration file (e.g. Vagrantfile, Gemfile, Rakefile, ...) was found in this directory. This file may expose sensitive information that could help a malicious user to prepare more advanced attacks. It's recommended to remove or restrict access to this type of files from production systems.

#POC
https://go.pushwoosh.com/composer.json
https://go.pushwoosh.com/composer.lock

Open these URLs a configuration file will become download and these files contains very sensitive data.

###IMPACT:
These files may disclose sensitive information. This information can be used to launch further attacks.

###PATCH
Remove or restrict access to all configuration files accessible from internet.

Thanks,



## Attachments
No attachments
