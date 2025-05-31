# Not using Binary::safe* functions for substr/strlen function

## Report Details
- **Report ID**: 181315
- **URL**: https://hackerone.com/reports/181315
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-11-10T12:50:45.937Z
- **Disclosed**: 2016-11-13T00:43:30.432Z

## Reporter
- **Username**: e3amn2l
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Several places in the code don't use Binary::safe* or CryptoUtil::safe* functions, but use raw functions instead (strlen/substr) which can act as mb_funcname instead (not count bytes for strlen/etc...)

1\. https://github.com/paragonie/airship/blob/4be7ac0f16b1744255a876a38dbe13fb1c09731a/src/Engine/Security/CSRF.php#L87
```
            $lockTo = substr($lockTo, 0, strlen($lockTo) - 1);
```

2\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/Engine/Security/Util.php#L98
can be changed to use self::subString which use  Binary::safeSubstr
```
                        \substr($mimeType, $p),
```

3\. https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/tools/audit_helper.php#L30
```
    if (\substr($print, 0, 3) === 'tmp' || \substr($print, 0, 5) === 'files') {
```

4\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/tools/hangar/src/SessionCommand.php#L23-L24
```
            $x = \strlen($this->session['dir']);
            return \substr($current, $x + 1);
```

5\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/tools/hangar/src/SessionCommand.php#L46-L47
```
            $x = \strlen($this->session['dir']);
            return \substr($file, $x + 1);
```

6\. https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/tools/random_audit.php#L28
```
echo \substr($fileList[$choice], $l), "\n";
```

7\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/CommandLine/installer.php#L39
8\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/CommandLine/manual_update.php#L40
9\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/symlinks.php#L48
10\. https://github.com/paragonie/airship/blob/4aa579c564383355ad3de111a746f14a07164dba/src/config/logger.php#L28
11\. https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/tools/hangar/src/Commands/Add.php#L62
12\. https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/tools/hangar/src/Commands/Add.php#L62
13\. https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/tools/hangar/src/hangar.php#L68
14\. https://github.com/paragonie/airship/blob/7bb8d24487e127b2210ac7f1153df8153208c3b9/tools/hangar/src/Command.php#L168


strlen usage:

1\. https://github.com/paragonie/airship/blob/ef2d4f725e5af2eae27fd919533d01b625d020b1/src/Cabin/Hull/Blueprint/Blog.php#L1080
2\. https://github.com/paragonie/airship/blob/ef2d4f725e5af2eae27fd919533d01b625d020b1/src/Cabin/Hull/Blueprint/Blog.php#L1098
3\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/Cabin/Hull/Landing/IndexPage.php#L43
4\. https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/tools/hangar/src/Commands/Help.php#L100
5\. https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/tools/hangar/src/Commands/Add.php#L60
6\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/Cabin/Hull/Landing/BlogPosts.php#L85
7\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/Cabin/Hull/Landing/BlogPosts.php#L147
8\. https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/tools/hangar/src/Commands/Autorun.php#L61
9\. https://github.com/paragonie/airship/blob/0e9289553cdc538556d362faaee63be6cc534a0c/tools/hangar/src/Commands/Autorun.php#L81
10\. https://github.com/paragonie/airship/blob/4aa579c564383355ad3de111a746f14a07164dba/src/config/logger.php#L26
11\. https://github.com/paragonie/halite/blob/8980974467cd54c6d2bb4dd98b2f0e9838570549/autoload.php#L13


fix:
1. change strlen usage to CryptoUtil::safeStrlen or Util::safeStrlen or Binary::safeStrlen or Util::stringLength across the codebase.
2. change substr usage to Util::safeSubstr or CryptoUtil::safeSubstr or Binary::safeSubstr across the codebase.

## Attachments
No attachments
