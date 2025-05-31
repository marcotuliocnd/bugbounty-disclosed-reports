# unauth mosquitto ( client emails, ips, license keys exposure )

## Report Details
- **Report ID**: 1578574
- **URL**: https://hackerone.com/reports/1578574
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-23T07:23:09.118Z
- **Disclosed**: 2022-07-18T11:39:34.544Z

## Reporter
- **Username**: second_grade_pentester
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hi team

## Summary
connect.acronis.com ( ip 88.99.142.45:1883 ) has unauth mosquitto mqtt, anyone can connect and read\write messages

## Steps To Reproduce
[add details for how we can reproduce the issue]

  1. https://github.com/bapowell/python-mqtt-client-shell
  1. python3 mqtt_client_shell.py
  1. connection
  1. host 88.99.142.45
   1. connect
   1. subscribe "#" 1


```
Payload (str): b'{"host":"nusite", "tag":"nusite-licenser", "level":"debug", "msg":" response: {\'commands\': [],
 \'license_info\': {\'licensee_name\': \'██████████\',
 \'license_key\': \'█████████\', \'support_exp_date\': \'2021-11-30\',
 \'licensed_actions\': [{\'names\': [\'*\'], \'rules\': [{\'ops\': [{\'action\': \'allow\'}]}]}]}, \'signature\': \'\'}"}'
```

█████


## Recommendations
enable authentication

Thanks

## Impact

access to client data, possibility to write messages to unauth mqtt

## Attachments
No attachments
