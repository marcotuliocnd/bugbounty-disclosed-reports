# Secret API Key is logged in cleartext 

## Report Details
- **Report ID**: 1662194
- **URL**: https://hackerone.com/reports/1662194
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-08-07T20:49:40.671Z
- **Disclosed**: 2022-12-23T09:25:17.056Z

## Reporter
- **Username**: sim4n6
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
## Summary:

While code-reviewing the repository <https://github.com/omise/omise-python/>, I have found that you log in clear-text some sensitive data. 

## Steps To Reproduce:

  1. Check here [omise/request.py#L88](https://github.com/omise/omise-python/blob/bfcf283378a823139b9f19f10e84d42a98c5b1ac/omise/request.py#L88) and here [omise/request.py#L111](https://github.com/omise/omise-python/blob/bfcf283378a823139b9f19f10e84d42a98c5b1ac/omise/request.py#L111)
 1. The code source explicitly logs in debugging mode the secret API key.
```
logger.debug('Authorization: %s', self.api_key)
```

 1. Activate logging level debug and run the following sample.py file 
```
import omise
omise.api_secret = 'skey_test_5sqdfyjv0rtqzs9f2x2'

customer = omise.Customer.create(
   description='John Doe',
   email='john.doe@example.com'
)
```

You will get:

{F1857247}

## Impact

- sensitive data logged in clear text may end up in unusual places: recorded demonstrations, copied logs, etc.

## Remediation

- I suggest you log at least a partial part of the secret API key if not remove the L88 and L111 in whole.

## Attachments
- Screenshot_at_2022-08-07_21-39-21.png
