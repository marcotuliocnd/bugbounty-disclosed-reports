# Race condition in faucet when using starport

## Report Details
- **Report ID**: 1438052
- **URL**: https://hackerone.com/reports/1438052
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-12-30T08:45:02.218Z
- **Disclosed**: 2022-07-26T17:47:40.549Z

## Reporter
- **Username**: cyberboy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cosmos

## Vulnerability Information
Hi team, 
I and Aditya sent this bug over email on Wed, 29 Dec, 17:45 IST. Later we noticed that security reports are accepted via the HackerOne program. So, I am sending a copy of the bug report here. 

## Summary:
We were testing an application and we found a race condition bug in the faucet Implementation of Starport. 
https://github.com/tendermint/starport

## Steps To Reproduce:
1. Start a starport with the below configuration. Note the "coins_max" has been set to 11 tokens and hence a user cannot fetch more after the 11 token limits.

```
accounts:
  - name: alice
    coins: ["0token", "200000000stake"]
  - name: bob
    coins: ["500token", "100000000stake"]
validator:
  name: alice
  staked: "100000000stake"
client:
  openapi:
    path: "docs/static/openapi.yml"
  vuex:
    path: "vue/src/store"
faucet:
  name: bob
  coins: ["5token", "100000stake"]  
  coins_max: ["11token", "100000stake"]
```

2. Now call the request manually  with 5 tokens per request as in our configuration after 2 requests and 10 tokens in total Alice won't be able to fetch more tokens from the faucet

```
POST / HTTP/1.1
Host: 172.105.41.242:4500
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://172.105.41.242:4500/
Content-Type: application/json
Origin: http://172.105.41.242:4500
Content-Length: 63
Connection: close
{
  "address": "ALICE_ADDRESS"}

```

Now we can confirm Alice cannot have more than 11 tokens. 

3.  Now regenerate the server and instead of sending a single request send a concurrent request to fetch tokens in Alice address.  We used 50 requests concurrently.

{F1563051}

4. Now when we check Alice balance it is 30 which should have not been more than 11

{F1563052}

We believe the root cause of the issues is the go mapping which is not advised for concurrency 
https://github.com/tendermint/starport/blob/develop/starport/pkg/cosmosfaucet/transfer.go#L59

## Supporting Material/References:
https://cwe.mitre.org/data/definitions/362.html

## Impact

A malicious user can send concurrent requests to fetch more tokes from faucets than the "max-credit limit" which allows.

## Attachments
- Screenshot_2021-12-29_at_5.41.56_PM.png
- Screenshot_2021-12-29_at_5.43.09_PM.png
