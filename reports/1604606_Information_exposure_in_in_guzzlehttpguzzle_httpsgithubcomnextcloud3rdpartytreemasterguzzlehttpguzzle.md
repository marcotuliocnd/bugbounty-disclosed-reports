# Information exposure in in guzzlehttp/guzzle (https://github.com/nextcloud/3rdparty/tree/master/guzzlehttp/guzzle)

## Report Details
- **Report ID**: 1604606
- **URL**: https://hackerone.com/reports/1604606
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-16T21:19:11.689Z
- **Disclosed**: 2022-09-16T02:52:19.205Z

## Reporter
- **Username**: ro0t_elqayser
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:

Affected versions of this package are vulnerable to Information Exposure which fails to strip the Authorization header on HTTP downgrade, this depency is out of date and it can leat to still authorization header.
## Steps To Reproduce:

(https://github.com/nextcloud/3rdparty/tree/master/guzzlehttp/guzzle)
  Introduced through: guzzlehttp/guzzle@7.4.0, aws/aws-sdk-php@3.184.6, php-http/guzzle7-adapter@1.0.0, php-opencloud/openstack@3.1.0, microsoft/azure-storage-blob@1.5.2
  From: guzzlehttp/guzzle@7.4.0
  From: aws/aws-sdk-php@3.184.6 > guzzlehttp/guzzle@7.4.0
  From: php-http/guzzle7-adapter@1.0.0 > guzzlehttp/guzzle@7.4.0

##Fix:
You can update to 7.4.4, 6.5.7 to fix this information exposure.

## Impact

Affected versions of this package are vulnerable to Information Exposure which fails to strip the Authorization header on HTTP downgrade.

## Attachments
No attachments
