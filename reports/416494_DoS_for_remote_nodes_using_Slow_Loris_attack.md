# DoS for remote nodes using Slow Loris attack

## Report Details
- **Report ID**: 416494
- **URL**: https://hackerone.com/reports/416494
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-30T14:16:46.633Z
- **Disclosed**: 2019-02-21T17:44:52.823Z

## Reporter
- **Username**: sobhraj_charles
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
**Summary:** 

Using the slow loris attack it's possible to make the the daemon unresponsive to all RPC requests without at least a restart.

**Description:** 

I used this node.js application (https://www.npmjs.com/package/sloww) to perform the attack on one of my remote nodes, but any other implementation of the attack should also work fine.

## Releases Affected:

  * Ubuntu 16.04 x64 - Monero v0.12.3.0 was affected so all releases before should be affected as well.
  
## Steps To Reproduce:

  1. Start the daemon with standard remote node parameters like `./monerod --rpc-bind-ip 0.0.0.0 --confirm-external-bind`
  2. Start the slow loris attack, I tested with 1000 sockets opened and 700 milliseconds as rate at which 
      packets should be sent.
  3. Try sending a normal RPC command like `curl -X POST http://IP:18089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_block_count"}' -H 'Content-Type: application/json'` there will not be any response from the RPC a few seconds after the attack was started.

## Impact

An attacker could target a large number of remote nodes for example the ones under https://moneroworld.com/, with just a single PC.

## Attachments
No attachments
