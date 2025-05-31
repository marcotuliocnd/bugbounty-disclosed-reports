# Worker container escape lead to arbitrary file reading in host machine [again]

## Report Details
- **Report ID**: 697055
- **URL**: https://hackerone.com/reports/697055
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-09-18T09:34:52.929Z
- **Disclosed**: 2019-10-21T01:32:16.250Z

## Reporter
- **Username**: testanull
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semmle

## Vulnerability Information
## Summary:
After a successful build, LGTM allow user to view the file list.
By default, only source code files and build config files are reserved (``lgtm.yml`` and ``.lgtm.yml``).
If there are both files in folder, LGTM will process ``lgtm.yml`` file and skip ``.lgtm.yml``, but it still keeps both of files in directory.
By making symlink to ``.lgtm.yml`` file, after successful build, it will point to HOST MACHINE file!

## Steps To Reproduce:

1. Create a simple project which LGTM can build successful.
In this report, I use this project (https://github.com/testanull/test11)
2. Create file: ``lgtm.yml``  with a valid config content, for example:

```
extraction:
  java:
    index:
      build_command:
      - ./custom-build
```

3. Make a symlink point to a HOST MACHINE file/directory with name: ``.lgtm.yml``
4. After successful build, ``.lgtm.yml`` file will contain the host machine file content!

##PoC of reading ``/etc/passwd`` is attached below

## Impact

Give attacker ability to explore the host machine, expose more sensitive informations from it.

## Attachments
- docker_escape_read_passwd_2.PNG
