# Improper handling of untypical characters in domain names

## Report Details
- **Report ID**: 1178337
- **URL**: https://hackerone.com/reports/1178337
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-04-28T14:07:26.814Z
- **Disclosed**: 2021-09-10T17:51:58.124Z

## Reporter
- **Username**: philippjeitner
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs

## Vulnerability Information
# Description

Missing input validation of host names returned by Domain Name Servers in node's `dns` library can lead to output of wrong hostnames (leading to Domain Hijacking) and injection vulnerabilities in applications using the library (leading to Remote Code Execution, XSS, Applications crashes, etc.).

# Discoverer(s)/Credits

Philipp Jeitner, Fraunhofer SIT

# References

Injection Attacks Reloaded: Tunnelling Malicious Payloads over DNS
https://www.usenix.org/conference/usenixsecurity21/presentation/jeitner
(Available starting from August 11, 2021)

# Steps To Reproduce

Using the example application (`main.js`) which does dns lookups via node.

```
const dns = require('dns');

if (process.argv[2] == "-x") {
	var host = process.argv[3];

	dns.reverse(host, (err, result) => {
		
		if (result){
			for (var i = 0; i < result.length; i++)
			{
				console.log("node".padEnd(8), "reverse".padEnd(16), host.padEnd(30), "-".padEnd(80), "-".padEnd(10), "IN".padEnd(5), "PTR".padEnd(5), result[i]);
			}
		} else {
			console.log("node".padEnd(8), "reverse".padEnd(16), host.padEnd(30), "-".padEnd(80), "-".padEnd(10), "-".padEnd(5), "ERROR".padEnd(5), err.errno);
		}
	});
	
} else {
	var host = process.argv[2];
	dns.lookup(host, (err, result) => {
		if (result) {
			console.log("node".padEnd(8), "lookup".padEnd(16), host.padEnd(30), "-".padEnd(80), "-".padEnd(10), "IN".padEnd(5), "A".padEnd(5), result);
		} else {
			console.log("node".padEnd(8), "lookup".padEnd(16), host.padEnd(30), "-".padEnd(80), "-".padEnd(10), "-".padEnd(5), "ERROR".padEnd(5), err.errno);
		}
	});
	
	dns.resolve(host, (err, result) => {
		if (result) {
			for (var i = 0; i < result.length; i++) {
				console.log("node".padEnd(8), "resolve".padEnd(16), host.padEnd(30), "-".padEnd(80), "-".padEnd(10), "IN".padEnd(5), "A".padEnd(5), result[i]);
			}
		} else {
			console.log("node".padEnd(8), "resolve".padEnd(16), host.padEnd(30), "-".padEnd(80), "-".padEnd(10), "-".padEnd(5), "ERROR".padEnd(5), err.errno);
		}
	});
	
	dns.resolveCname(host, (err, result) => {
		if (result) {
			for (var i = 0; i < result.length; i++) {
				console.log("node".padEnd(8), "resolveCname".padEnd(16), host.padEnd(30), "-".padEnd(80), "-".padEnd(10), "IN".padEnd(5), "CNAME".padEnd(5), result[i]);
			}
		} else {
			console.log("node".padEnd(8), "resolveCname".padEnd(16), host.padEnd(30), "-".padEnd(80), "-".padEnd(10), "-".padEnd(5), "ERROR".padEnd(5), err.errno);
		}
		
	});
	
}
```

Run the code with the example domains provided by us:

```
$ node main.js cnamezeroweb.test.xdi-attack.net

node     resolveCname     cnamezeroweb.test.xdi-attack.net - -  IN    CNAME zero.longtxtrecord.ml

$ node main.js cnamexss.test.xdi-attack.net

node     resolveCname     cnamexss.test.xdi-attack.net  - -  IN    CNAME <img/src=''/onerror='alert&#x28&#x22xss&#x22&#x29'>.a.cnamexss.test.xdi-attack.net
```

Compare with the output of a well-behaving stub resolver library (glibc) and/or dig:

```
$ dig dig cnamezeroweb.test.xdi-attack.net

cnamezeroweb.test.xdi-attack.net. 284 IN CNAME  zero.longtxtrecord.ml\000cnamezeroweb.test.xdi-attack.net.
zero.longtxtrecord.ml\000cnamezeroweb.test.xdi-attack.net. 284 IN A 1.2.3.4

$ dig cnamezeroweb.test.xdi-attack.net

cnamezeroweb.test.xdi-attack.net. 300 IN CNAME  zero.longtxtrecord.ml\000cnamezeroweb.test.xdi-attack.net.
zero.longtxtrecord.ml\000cnamezeroweb.test.xdi-attack.net. 299 IN A 1.2.3.4

$ getent hosts cnamezeroweb.test.xdi-attack.net
$ getent hosts cnamexss.test.xdi-attack.net

(no output, return code = 2 because name is filtered)
```

The first issue (cnamezeroweb) is a clear error in zero-byte handling and can potentially lead to DNS-cache injections in case an application implements a cache based on the library.

The second (cnamexss) shows that this can be used to tunnel all kinds of injection payloads, and we argue that applications do not typically expect other characters than [a-z0-9-.] in hostnames. We are aware of applications which can be exploited via this second attack vector (stub dns resovlers which does not filter special characters from hostnames) and argue that stub-resolver libraries should only allow hostnames containing [a-z0-9-.], as it is implemented by glibc's gethostbyname, etc. functions. See the Section 'More information' below on standardization of stub resolver functionality.

Note: One might argue that underscores (_) should also be allowed, since they are used for many application like DMARC, SRV, etc. Actually the underscore was chosen exactly because it is a character not allowed in "hostnames" and thus dmarc records (_dmarc.example.com) does not conflict with "normal" hostnames (See RFC8552, Section 1.1).

The same exploits also apply to reverse-dns records via node's `dns.reverse` function, and probably functions for other record types as well (not tested). You can test this by setting up a nameserver with the following records, in bind9 this requires disabling the `check-names` option in the configuration.

```
1.1.1.1.in-addr.arpa.   300     IN      PTR     t\000.example.com.
3.3.3.3.in-addr.arpa.   300     IN      PTR     <img/src=''/onerror='alert&#x28&#x22xss&#x22&#x29'>.example.com.
```

Then run `node main.js -x 1.1.1.1` and observe the misinterpreted/unfiltered result.

*Note*: I selected CWE-170 "Improper Null Termination" as a weakness, however this only applies to the first issue.  You might want to consider this two seperate issues (zero-byte handling and missing filtering).

# More information

The POSIX Standard for Information Technology defines interfaces for DNS lookups in systems standard C libraries. This Standard includes functions for forward lookups (gethostbyname, getaddrinfo) as well as backward-lookups (gethostbyaddr, getnameinfo). These funtions cannot only return IP addresses but can also contain host names of aliases (CNAME) of the requested host name in case of forward-lookups, or the primary host name of that ip address in the case of backward-lookups (PTR). The POSIX Standard defines the data format of these host names as a null-terminated C-String containing a "hostname" or "nodename", which are typically expected by developers and defined by RFC952 [2] and RFC1123 [3] to only contain alphanumeric characters (a-z,A-Z,0-9), hyphens ("-") and periods (".") to split labels. This creates a mismatch of allowed characters between "hostnames" and "domain names" as defined by the DNS standard [4] which defines "domain names" as a series of "text labels" which are textually represented by concatenating all "text labels" and joining them together with period signs. However, "text labels" can contain any octet value, even zero-bytes ("\x00") and period signs (".") and recursive DNS resolvers are required by the DNS standard to support any of these characters in DNS records, thus not implementing any sanitiy checks on domain names.

When DNS responses are parsed by the stub DNS resolver implemented by stub resolver library as part of the `gethostbyname()`, `getaddrinfo()`, `gethostbyaddr()` and `getnameinfo()` functions, these functions must therefore ensure that the returned, null-terminated C-Strings must be valid domain names as defined by the POSIX standard, else applications which use these values might include that information in contexts where malicious data can included inside the domain name and used for command injection attacks like Cross-Site-Scripting, SQL-injections, etc. Furthermore, if domain names contain text labels with periods (".") or zero-bytes ("\x00") and the stub resolver library does naively decode these domain names into strings, attackers can create malicious domain names which are misinterpreted by the naive decoding logic to look like different domain names than they actually are. When these misinterpreted domain names are than cached by applications using the stub resolver, this allows for domain hijacking by poisoning of the applications DNS cache which uses the vulnerable stub resolver library.

*Note*: node does not implement a stub resolver as standardized by POSIX, so the rules about allowed vs. non-allowed characters do not directly apply. However, we argue that developers do not know about the specifics of the "hostname" vs. "domain name" consideration, so any library which implements dns lookups should ideally behave in the same way to reduce vulnerabilities caused by developers switching from another language/stub resolver library.

## Impact

Impact depends on the application triggering the DNS lookup, see description.

## Attachments
- main.js
