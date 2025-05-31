# Arbitrary escape sequence injection in docker-machine from worker nodes

## Report Details
- **Report ID**: 1916285
- **URL**: https://hackerone.com/reports/1916285
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-03-23T20:28:55.804Z
- **Disclosed**: 2023-06-02T02:00:16.264Z

## Reporter
- **Username**: mehmil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hi,

This bug report is specific to docker-machine and its utilization by Gitlab as preferred tool to allow autoscaling across different providers (https://docs.gitlab.com/runner/configuration/autoscale.html). I am  not sure if it fits the scope here but wanted to reach out regarding this before I post it publicly in an upcoming blog post about general topic of escape sequence injection as it might still be relevant for you.

I know that in future docker-machine will be replaced by native support but currently this is the preferred tool to allow autoscaling. (https://gitlab.com/groups/gitlab-org/-/epics/2502)

Attack requirements and description:

1. `docker-machine` reports information like version number in use by worker nodes.

2. worker nodes may be running with a docker socket mounted in container to allow CI builds (of course alternatives like kaniko can be used but using docker socket is still a common approach)

3. Using such an approach with docker-machine and docker executor with mounted docker socket basically means that ci/cd jobs have root access to worker nodes.

4. Now a malicious ci/cd job can overwrite locally running docker daemon with a malicious docker daemon which will still be contacted by `docker-machine` to retrieve information like version, ip etc. Running commands like `docker-machine ls` on the bastion host would inject that malicious information in a window on Bastion node.

PoC:

1. Launch a worker instance using docker-machine and any driver.

2. On the worker node, modify docker daemon to report following string in version response:

```
"\033]2;\033[21t \033[1;32m\033[21t\033[Jroot@host$ \v\033[0m View all output? hit enter to continue: \v\033[A?\033[0\033[2AA\033[0",
```

This can be done by compiling docker from source and modifying the version information in `info.go` (https://github.com/moby/moby/blob/23.0/daemon/info.go#L104). Use this docker daemon to overwrite already running docker daemon on the worker node.

3. Now run `docker-machine ls` or `docker-machine version worker_machine_name` and it will:

- change window title by injecting escape sequence using `\033[2;`
- Inject arbitrary input in user's prompt i.e. `ll` and try to trick user into hitting enter and executing the input buffer as a command.

4. Using a more malicious input, it will also be possible to crash the bastion node completely.

`docker-machine` is executed with high privilege users and letting it output potentially malicious content can have a high impact not just with escape code injection but also if such an output is used for monitoring or automation scripts assuming that whatever it reports is validated content and not arbitrary information. `docker-machine` should validate this information especially for things like `version`

More about escape sequences which can be injected in terminals:  https://marc.info/?l=bugtraq&m=104612710031920&w=2

Please review if this fits into the scope here or if it would be alright to publish it as part of a public blog post regarding such attack vectors. 

Thanks!

## Impact

Escape code injection
Denial of Service

## Attachments
No attachments
