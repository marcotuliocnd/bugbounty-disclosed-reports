# Django debug enabled showing information about system, database, configuration files

## Report Details
- **Report ID**: 1561377
- **URL**: https://hackerone.com/reports/1561377
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-06T12:35:02.908Z
- **Disclosed**: 2022-05-31T21:28:33.107Z

## Reporter
- **Username**: omarelfarsaoui
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glovo

## Vulnerability Information
## Summary:
Hi team,
This subdomain `pulpo.it.glovoint.com` is a Django application running with debug mode turned on (DEBUG = True ).
One of the main features of debug mode is the display of detailed error pages to help developers.
If your app raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings.py file.

## Steps To Reproduce:
it's not complicated and needs some user interaction, using  Burpsuite I send the POST request to `https://pulpo.it.glovoint.com/admin` path and I got 500 response. 

The information leaked includes the following:
Django Version.
python Version
IP addresses
S3_URL
database (username, URL, type, port )
email addresses


## Supporting Material/References:
███

## Remediation:
Never deploy with DEBUG turned on.
To disable debug mode, set DEBUG=False in your Django settings.py file.

## Impact

An attacker can obtain information such as:
Django & Python version.
Used database type, database user name, and current database name.
Details of the Django project configuration.
Internal file paths.
Exception-generated source code, local variables and their values.
This information might help an attacker gain more information and potentially to focus on the development of further attacks on the target system.

## Attachments
No attachments
