# Public and secret api key leaked via omise github repo(owned by omise)

## Report Details
- **Report ID**: 508024
- **URL**: https://hackerone.com/reports/508024
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-03-11T18:10:36.138Z
- **Disclosed**: 2019-03-25T09:41:37.301Z

## Reporter
- **Username**: noobwalid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: omise

## Vulnerability Information
Found secret key of particular omise accounts!
Functionality of the public and secret keys are described below:

Public key

The public key can be used to create tokens via javascript from your customers browsers. This key can be safely exposed to the outside world.

Secret key

The secret key can be used to create customers, cards and charges and to retrieve information about your account, such as its balance. You must keep this key from prying eyes.

I have got both public and secret key on omise github repo.**But not sure if they were created only for testing purpose**

##Go to :
https://github.com/omise/omise-php/blob/1158aeceb83c55d4b2188b75ae0f899d7af3881a/README.md
scroll down.and you will see leaked keys!!

```
<?php
require_once dirname(__FILE__).'/vendor/autoload.php';

define('OMISE_PUBLIC_KEY', 'pkey_test_54ot96fkr3i2op60cng');
define('OMISE_SECRET_KEY', 'skey_test_54ot96fkr3i2op60cng');
define('OMISE_API_VERSION', '2017-11-02');
```

thank you

## Impact

Attacker can use the secret key to create customers,cards and charges and to retrieve info about the particular account,such as its balance.

## Attachments
No attachments
