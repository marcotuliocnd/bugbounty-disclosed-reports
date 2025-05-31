# remote access to localhost daemon, can issue jsonrpc commands

## Report Details
- **Report ID**: 303390
- **URL**: https://hackerone.com/reports/303390
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-01-08T23:33:57.253Z
- **Disclosed**: 2018-02-22T00:08:19.199Z

## Reporter
- **Username**: bugbound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** [Remotely use jsonrpc on localhost wallets]

**Description:** [its possible to execute jsonrpc calls as monerod does not pay strict attention to origin or content-type client headers]

## Releases Affected:

  * [monerod] port 18081

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

1. run monerod
2. visit http://bugbound.co.uk/test42/bert.html for POC (html form)
3. Click submit and view request/response


## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

## Impact

potentially empy wallet by calling jsonrpc sendrawtransaction

## Attachments
- demo1.html
