# Exposes a series of other private credentials

## Report Details
- **Report ID**: 289189
- **URL**: https://hackerone.com/reports/289189
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-11-10T14:54:49.455Z
- **Disclosed**: 2017-11-13T20:00:45.306Z

## Reporter
- **Username**: 4w3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hi,

I found a `Javascript` file where have many private credentials.

# JS File
* `https://app.legalrobot.com/meteor_runtime_config.js`

# Code
```
__meteor_runtime_config__ = {"meteorRelease":"METEOR@1.5.2.2","meteorEnv":{"NODE_ENV":"production","TEST_METADATA":"{}"},"PUBLIC_SETTINGS":{"analyticsSettings":{"Google Analytics":{"trackingId":"UA-62872512-1"},"Intercom":{"appId":"nmyyq5i5"},"Keen IO":{"projectId":"556cb72a2fd4b162515c7ef8","writeKey":"dc0bfcfdeb1073312ebf28588828f224162ce8a2de411bbb563909191bfe4f6fc2f89749d64bc29ef1326e6f9520a7eec85ac68d1631abd3a211fea234f0b8f1d211bcd1a4f89d1a2ca7bdd5393dcc616155ba2eb65f0f26c14ecff30cef6958"}},"aws":{"files":{"region":"us-west-2"}},"contact":{"siteName":"Legal Robot","SMS":"(877) 413-4380","email":"hello@legalrobot.com","logo":"https://www.legalrobot.com/assets/img/logo.png","url":"https://www.legalrobot.com","shortUrl":"LegalRobot.com","address":"548 Market Street, Suite 28970, San Francisco, CA 94104","phone":"(415) 894-0240","facebook":"https://www.facebook.com/LegalRobot/","twitter":"https://twitter.com/legalrobot","instagram":"https://www.instagram.com/legalrobot/","googlePlus":"https://plus.google.com/+LegalRobot","linkedIn":"https://www.linkedin.com/company/legal-robot","fbAppId":"365463763640085"},"intercom":{"id":"nmyyq5i5"},"domain":"legalrobot.com","persistent_session":{"default_method":"temporary"},"stripe":{"publishableKey":"pk_live_aa7H8nClyv2IIShaDJGqDs9A"}},"ROOT_URL":"https://app.legalrobot.com","ROOT_URL_PATH_PREFIX":"","kadira":{"appId":"fqm5S7o42sAL2eD8T","endpoint":"https://apm-engine.meteor.com","clientEngineSyncDelay":10000,"enableErrorTracking":true},"appId":"zivmvxxevpdg1xu8kc5","accountsConfigCalled":true,"autoupdateVersion":"b63bfae847acb9cfe642ce499c53741902219d35","autoupdateVersionRefreshable":"6bb469fad9a6afa3ba3eb9dfb4e11067a35116ca","autoupdateVersionCordova":"325d666b7e9b79c77b59f2c48bc20ad9ed61033a"};
```

# Private Data

{F238410}

```
"PUBLIC_SETTINGS":{"analyticsSettings":{"Google Analytics":{"trackingId":"UA-62872512-1"}`
* `Intercom":{"appId":"nmyyq5i5"}
```

#### Keen IO project id writeKey 
```
Keen IO":{"projectId":"556cb72a2fd4b162515c7ef8","writeKey":"dc0bfcfdeb1073312ebf28588828f224162ce8a2de411bbb563909191bfe4f6fc2f89749d64bc29ef1326e6f9520a7eec85ac68d1631abd3a211fea234f0b8f1d211bcd1a4f89d1a2ca7bdd5393dcc616155ba2eb65f0f26c14ecff30cef6958"}}
```

#### Facebook App ID
```
"fbAppId":"365463763640085"}
```

#### Intercom id
```
intercom":{"id":"nmyyq5i5"}
```

#### Stripe PublishKey
`stripe":{"publishableKey":"pk_live_aa7H8nClyv2IIShaDJGqDs9A"}`

#### PublishKey 
```
"publishableKey":"pk_live_aa7H8nClyv2IIShaDJGqDs9A"}},"ROOT_URL":"https://app.legalrobot.com","ROOT_URL_PATH_PREFIX":""
```

### kadira
```
"kadira":{"appId":"fqm5S7o42sAL2eD8T","endpoint":"https://apm-engine.meteor.com"
```
#### App ID
```
"appId":"zivmvxxevpdg1xu8kc5"
```

### See also on a report #124100
{F238415}


Looking forward to hearing from @legalrobot security team.

Warm Regard,
@4w3

## Attachments
- private_data.PNG
- report.PNG
