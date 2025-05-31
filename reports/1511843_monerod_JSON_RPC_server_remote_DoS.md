# monerod JSON RPC server remote DoS

## Report Details
- **Report ID**: 1511843
- **URL**: https://hackerone.com/reports/1511843
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-15T00:16:28.790Z
- **Disclosed**: 2022-09-12T21:50:10.819Z

## Reporter
- **Username**: m31007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
Monero daemon (monerod)  does not limit Content-length variable when processing incoming HTTP requests.
We can force monerod to allocate arbitrary amount of memory.


How to reproduce:
1) compile monero https://github.com/monero-project/monero
2) run it:
$ ulimit -Sv 1000000000
$ ./bin/monerod --rpc-login test:test  --rpc-bind-ip 0.0.0.0 --confirm-external-bind

3) run attached script m1.py
$ python2 ./m1.py 192.168.1.34

4) after some time OOM killer will stop monerod

## Impact

monerod process can be stopped remotely, no authentication is required. 
An access to JSON RPC port is enough.

## Attachments
- m1.py
