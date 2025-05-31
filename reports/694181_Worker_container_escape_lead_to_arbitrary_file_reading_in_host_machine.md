# Worker container escape lead to arbitrary file reading in host machine

## Report Details
- **Report ID**: 694181
- **URL**: https://hackerone.com/reports/694181
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-09-13T02:39:39.780Z
- **Disclosed**: 2019-10-16T12:34:13.387Z

## Reporter
- **Username**: testanull
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semmle

## Vulnerability Information
## Summary:
Because lack of security, attacker will be able to remove original log file and replace it will a symlink to other file, 
After finishing job, host machine copy file from docker container.
Because the original log file has been removed, the host machine will copy the symlink file.
But the problem is it doesn't copy the linked file in container, it copys the linked file in the HOST MACHINE.

## Steps To Reproduce:
The attack is very simple, just remove the original build.log file and replace with a symlink file,
I used this configuration to read the ``/etc/passwd``:
```extraction:
  cpp:
    after_prepare:
      - rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd /opt/out/snapshot/log/build.log
```

## PoC
Content of ``/etc/passwd`` is attached below

## Impact

Give attacker ability to explore the host machine, expose more sensitive informations from it.

## Attachments
- docker_escape_read_file.PNG
