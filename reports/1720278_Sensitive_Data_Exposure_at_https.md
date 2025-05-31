# Sensitive Data Exposure at https://█████████

## Report Details
- **Report ID**: 1720278
- **URL**: https://hackerone.com/reports/1720278
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-10-02T23:45:22.173Z
- **Disclosed**: 2023-02-24T18:58:25.839Z

## Reporter
- **Username**: 0r10nh4ck
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

I found in the endpoint https://███/api/getEnvVars, 
sensitive data of environment variables containing: AWS S3 credentials, PATH, IP and PORTs.

## References

https://www.tenable.com/plugins/was/113164
https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html
https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html

## Impact

By using leaked AWS credentials or abusing credentials with misconfigured permissions, 
an attacker could try to gain access to sensitive information on the AWS account 
or perform arbitrary modification on the AWS resources.

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Enable a HTTP interception proxy, such as Burp Suite or OWASP ZAP
2. Use a browser to navigate to: https://█████████
3. Find the HTTP POST to https://█████████/api/getEnvVars
4. See the response.

POC:

```json
{"PORT":"8080","PATH":"/home/vcap/app/node_modules/.bin:/home/vcap/node_modules/.bin:/home/node_modules/.bin:/node_modules/.bin:/home/vcap/deps/0/node/lib/node_modules/npm/node_modules/@npmcli/run-script/lib/node-gyp-bin:/home/vcap/deps/0/bin:/usr/local/bin:/usr/bin:/bin:/home/vcap/app/bin:/home/vcap/deps/0/node_modules/.bin","APP_SUB_DOMAIN":"██████","DEPLOY_ENV":"test","CF_INSTANCE_ADDR":"████████:61069","CF_INSTANCE_IP":"█████████","CF_INSTANCE_PORT":"61069","HOME":"/home/vcap/app","MEMORY_LIMIT":"125m","PWD":"/home/vcap/app","TMPDIR":"/home/vcap/tmp","USER":"vcap","VCAP_APP_HOST":"0.0.0.0","VCAP_APP_PORT":"8080","VCAP_APPLICATION":"{\"application_id\":\"█████████\",\"application_name\":\"████████\",\"application_uris\":[\"███\"],\"application_version\":\"███████\",\"cf_api\":\"https://api.system.██████\",\"host\":\"0.0.0.0\",\"instance_id\":\"█████████\",\"instance_index\":0,\"limits\":{\"disk\":3072,\"fds\":16384,\"mem\":125},\"name\":\"█████\",\"organization_id\":\"█████\",\"port\":8080,\"process_id\":\"███████\",\"process_type\":\"web\",\"space_id\":\"f28c5898-2473-4bf8-90e4-24d77a930603\",\"space_name\":\"CDN2-0_test\",\"uris\":[\"█████\"],\"version\":\"████\"}","VCAP_SERVICES":"{\"aws-s3\":[{\n  \"label\": \"aws-s3\",\n  \"provider\": null,\n  \"plan\": \"standard\",\n  \"name\": \"██████\",\n  \"tags\": [\n\n  ],\n  \"instance_guid\": \"█████████\",\n  \"instance_name\": \"█████\",\n  \"binding_guid\": \"██████████\",\n  \"binding_name\": null,\n  \"credentials\": {\n    \"access_key_id\": \"██████\",\n    \"bucket\": \"███-████████\",\n    \"region\": \"███\",\n    \"secret_access_key\": \"████\"\n  },\n  \"syslog_drain_url\": null,\n  \"volume_mounts\": [\n\n  ]\n},{\n  \"label\": \"aws-s3\",\n  \"provider\": null,\n  \"plan\": \"standard\",\n  \"name\": \"█████\",\n  \"tags\": [\n\n  ],\n  \"instance_guid\": \"█████████\",\n  \"instance_name\": \"███████\",\n  \"binding_guid\": \"██████████\",\n  \"binding_name\": null,\n  \"credentials\": {\n    \"access_key_id\": \"█████\",\n    \"bucket\": \"██████████-████\",\n    \"region\": \"██████████\",\n    \"secret_access_key\": \"████████\"\n  },\n  \"syslog_drain_url\": null,\n  \"volume_mounts\": [\n\n  ]\n}]}","s3_env_params":{"s3":{"config":{"credentials":{"expired":false,"expireTime":null,"refreshCallbacks":[],"accessKeyId":"████"},"credentialProvider":{"providers":[null,null,null,null,null,null,null],"resolveCallbacks":[]},"region":"████","logger":null,"apiVersions":{},"apiVersion":null,"endpoint":"https://s3.amazonaws.com","httpOptions":{"timeout":120000,"agent":null},"maxRedirects":10,"paramValidation":true,"sslEnabled":true,"s3ForcePathStyle":false,"s3BucketEndpoint":false,"s3DisableBodySigning":true,"s3UsEast1RegionalEndpoint":"legacy","computeChecksums":true,"convertResponseTypes":true,"correctClockSkew":false,"customUserAgent":null,"dynamoDbCrc32":true,"systemClockOffset":0,"signatureVersion":"v4","signatureCache":true,"retryDelayOptions":{},"useAccelerateEndpoint":false,"clientSideMonitoring":false,"endpointDiscoveryEnabled":false,"endpointCacheSize":1000,"hostPrefixEnabled":true,"stsRegionalEndpoints":"legacy","useFipsEndpoint":false,"useDualstackEndpoint":false},"endpoint":{"protocol":"https:","host":"s3.amazonaws.com","port":443,"hostname":"s3.amazonaws.com","pathname":"/","path":"/","href":"https://s3.amazonaws.com/"},"_events":{"apiCallAttempt":[null],"apiCall":[null]},"_clientId":10},"s3_bucket":"██████-███","user_url":"████"}}
```

## Suggested Mitigation/Remediation Actions
- Implement access control.
- Properly configure the API.
- Block requisition exposure.



## Attachments
No attachments
