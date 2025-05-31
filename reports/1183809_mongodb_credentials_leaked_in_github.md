# mongodb credentials leaked in github

## Report Details
- **Report ID**: 1183809
- **URL**: https://hackerone.com/reports/1183809
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-05-04T14:01:08.027Z
- **Disclosed**: 2021-05-07T16:58:12.038Z

## Reporter
- **Username**: makuzo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Go to [values.yaml file](https://github.com/Sifchain/sifnode/blob/740331dad061ee0f5a3cf3798d429f294b70f0ae/deploy/helm/block-explorer/values.yaml) file.

  2.Check from line 23:
```
blockExplorer:
  args:
    mongoUsername: "mongodb"
    mongoPassword:
    mongoDatabase: "block_explorer"
  env:
    rootURL: "http://localhost:3000"
    chainnet: ""
    genesisURL: ""
    remote:
      rpcURL: ""
      apiURL: ""
```

{F1288433}
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]
F1288433

## Impact

I believe that this database has the data of  https://blockexplorer.sifchain.finance/blocks ,so an attacker can access the database and control it.

## Attachments
- sif.png
