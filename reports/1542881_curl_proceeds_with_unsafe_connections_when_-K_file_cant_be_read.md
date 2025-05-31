# curl proceeds with unsafe connections when -K file can't be read

## Report Details
- **Report ID**: 1542881
- **URL**: https://hackerone.com/reports/1542881
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-04-17T03:11:27.320Z
- **Disclosed**: 2022-04-21T15:38:25.221Z

## Reporter
- **Username**: medianmedianstride
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
I'm using curl 7.82.0 on Linux. When the file specified by the -K option can't be read, curl sends network traffic as specified by the other options that are explicitly included on the command line (in other words, there's only a warning and I'd like it to be a fatal error). This behavior occurs even if those other options result in an action that's often considered unsafe, such as use of cleartext passwords. It's fine for curl to be capable of sending cleartext passwords, but this shouldn't happen unintentionally.

I feel that this is a vulnerability in curl because curl is able to recognize that the user's intended set of options was not specified correctly, but curl still decides to send network traffic corresponding to the known subset of those options. One might argue that, philosophically, curl prefers to send network traffic even if the user's input is underspecified; however, this isn't true elsewhere in curl. For example, if the user misspells one of the options on the command line, curl doesn't simply ignore that one, and do whatever is specified by the remaining, correctly spelled options. Instead, any misspelled option is a fatal error, and curl sends no network traffic at all. My suggestion is to make this -K situation consistent with that, i.e., if the file specified by -K can't be read, then that is a fatal error and no network traffic is sent.

## Steps To Reproduce:
  1. Begin typing a curl command line that uses the -K option followed by a filename.
  2. Create the file with that filename.
  3. Within the file, include a curl option that is typically regarded as making network traffic more safe, e.g., the --ssl-reqd option.
  4. Ensure that the curl process cannot read this file.
  5. Enter the curl command.
  6. Observe that curl does **not** exit with an error message stating that the file can't be read.
  7. Observe that curl makes the network connection without the safety measure chosen in step 3.

## Supporting Material/References:
A fatal error is the approach taken by many other programs in analogous cases, i.e., the program allows a security-relevant user-specified configuration file on the command line, and that file can't be read, e.g.,
```
  % ssh -F /home/user/my-safe-ssh-options/not-exist.config example.com
  Can't open user config file /home/user/my-safe-ssh-options/not-exist.config: No such file or directory

  % tar -X /home/user/list-of-my-private-key-files/not-exist.config -c -f public.tar .
  tar: /home/user/list-of-my-private-key-files/not-exist.config: No such file or directory
  tar: Error is not recoverable: exiting now
```
In other words, ssh realizes it would be wrong to simply use the system-wide SSH client configuration when the user is clearly trying to use a different configuration. The tar program realizes it would be wrong to simply place every file into a public archive, when the user is clearly trying to use -X to exclude specific files. With curl, the user is clearly trying to add some options, which may perhaps be critical for security in that user's use case.

Here's an example in which a curl user wishes to send secret credentials to an FTP server only if the FTP server supports SSL, analogous to the ==curl --ssl-reqd ftp://example.com== example on the https://curl.se/docs/manpage.html page. The user chooses to use only a filename (named my-curl-ftp-options.config below), not a full pathname, with the -K option, just as in the ==curl --config file.txt https://example.com== example on that page.

This example includes a user mistake, but the vulnerability is also relevant without any user mistake.

SSL detection works fine if the user's current working directory contains the my-curl-ftp-options.config file. However, the user then makes the realistic mistake of changing to a different working directory without changing the -K value. (Here, the user goes to the /mnt/LargeVolume/user directory because it has much more disk space for storing the large FTP downloads.) Indeed, curl warns the user, but then immediately sends the unsafe network traffic.

For purposes of the example, ftp.dlink.de is used (it always demands a password, but all combinations of usernames and passwords succeed). 

### Part 1
```
% /usr/bin/curl -L -s -S -o /home/user/curl https://github.com/moparisthebest/static-curl/releases/download/v7.82.0/curl-i386
% chmod +x /home/user/curl
% /home/user/curl --version
curl 7.82.0 (x86_64-pc-linux-muslx32) libcurl/7.82.0 OpenSSL/1.1.1l zlib/1.2.11 libssh2/1.9.0 nghttp2/1.43.0
Release-Date: 2022-03-05
Protocols: dict file ftp ftps gopher gophers http https imap imaps mqtt pop3 pop3s rtsp scp sftp smb smbs smtp smtps telnet tftp 
Features: alt-svc AsynchDNS HSTS HTTP2 HTTPS-proxy IPv6 Largefile libz NTLM NTLM_WB SSL TLS-SRP UnixSockets
% pwd
/home/user/ftp
% cat my-curl-ftp-options.config
--ssl-reqd
% /home/user/curl -K my-curl-ftp-options.config -u secretu:secretp --no-progress-meter ftp://ftp.dlink.de 2>&1 | head -6
curl: (64) Requested SSL level failed
```
### Part 2
```
% cd /mnt/LargeVolume/user
% ls -1
001-huge-file-from-ftp-server.dat
002-huge-file-from-ftp-server.dat
% /home/user/curl -K my-curl-ftp-options.config -u secretu:secretp --no-progress-meter ftp://ftp.dlink.de 2>&1 | head -6
Warning: error trying read config from the 'my-curl-ftp-options.config' file
drwxrwxrwx   1 user     group           0 Mar 16  2016 @archive
drwxrwxrwx   1 user     group           0 Jul 03  2020 anleitungen
drwxrwxrwx   1 user     group           0 Mar 16  2016 ant24
drwxrwxrwx   1 user     group           0 Mar 16  2016 ant70
drwxrwxrwx   1 user     group           0 Nov 20 14:40 aspnet_client
```
In Part 2, the cleartext network traffic exchanged begins with:
```
220 D-Link FTP Server.ready ...
USER secretu
331 Password required for secretu.
PASS secretp
230-Willkommen auf dem D-Link FTP-Server
```
In Part 1, the network traffic exchanged is the following. The cleartext password is never sent:
```
220 D-Link FTP Server.ready ...
AUTH SSL
534 AUTH command is disabled.
```
As mentioned above, if the user had underspecified the desired network traffic by misspelling an option (e.g., the wrong spelling --ssl-required instead of the correct spelling -ssl-reqd), then there would be a fatal error, and no network traffic (such as a cleartext password) would be sent:
```
% /home/user/curl --ssl-required -u secretu:secretp --no-progress-meter ftp://ftp.dlink.de 2>&1 | head -6
curl: option --ssl-required: is unknown
curl: try 'curl --help' for more information
```
In a more realistic case, the user would not use ftp.dlink.de, but would instead use a series of FTP servers that are normally intended to support SSL. The user would want to place --ssl-reqd in a configuration file because it applies to every server. However, the user would want to place the username and password on the command line because they are different for every server.

An exploitation scenario (protocol downgrade attack) without a user mistake is:
1. The victim user has a midnight cron job that is supposed to use curl for FTP with SSL. It has "-K /home/user/ftp/my-curl-ftp-options.config" on the command line; that file exists and contains a --ssl-reqd line.
2. The curl binary is on local disk, but the user's home directory (including the /home/user/ftp/my-curl-ftp-options.config file) is on an NFS file server.
3. The attacker is already able to disrupt availability (e.g., flood the NFS server for a few minutes at midnight to make it unresponsive) but has no way to disrupt the confidentiality or integrity of curl's use of SSL.
4. Because /home/user/ftp/my-curl-ftp-options.config can't be read, curl doesn't know that SSL was desired, and thus sends the password in cleartext.
5. The attacker can read the password off of the wire.

This vulnerability report is not specific to FTP or SSL. There are many other scenarios in which a missing option makes the network traffic less safe, and they add motivation for introducing a fatal error when the -K file can't be read. Some of the other scenarios are:

* the user intended to have --digest in that file, and curl instead makes an HTTP request with a cleartext password
* the user intended to have --append in that file, and curl instead overwrites the target file
* the user intended to have --proxy (followed by the name of an anonymizing proxy server) in that file, and curl instead reveals the user's endpoint IP address to the server operator

## Impact

In the main example above, the attacker can discover a cleartext password. More generally, the attacker can achieve any security impact that **any** curl option was trying to prevent. For example, the victim's source IP address may be leaked if the curl option was to use a proxy server. The connection may honor a revoked certificate if the curl option was to specify a local file with a Certificate Revocation List. Several others may also be relevant depending on the protocols and threat model.

## Attachments
No attachments
