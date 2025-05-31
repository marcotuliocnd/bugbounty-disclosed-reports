# @nextcloud/logger NPM package brings vulnerable ansi-regex version

## Report Details
- **Report ID**: 1607601
- **URL**: https://hackerone.com/reports/1607601
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-06-20T14:31:09.150Z
- **Disclosed**: 2022-07-29T10:18:43.439Z

## Reporter
- **Username**: ro0t_elqayser
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Affected versions of this package are vulnerable to Regular Expression Denial of Service (ReDoS) due to the sub-patterns [[\\]()#;?]* and (?:;[-a-zA-Z\\d\\/#&.:=?%@~_]*)*.

## Details: 
Denial of Service (DoS) describes a family of attacks, all aimed at making a system inaccessible to its original and legitimate users. There are many types of DoS attacks, ranging from trying to clog the network pipes to the system by generating a large volume of traffic from many machines (a Distributed Denial of Service - DDoS - attack) to sending crafted requests that cause a system to crash or take a disproportional amount of time to process.
The Regular expression Denial of Service (ReDoS) is a type of Denial of Service attack. Regular expressions are incredibly powerful, but they aren't very intuitive and can ultimately end up making it easy for attackers to take your site down.

## Steps To Reproduce:

  1. First I download the code (https://github.com/nextcloud/password_policy) I usual cat files and See the technologies that the site use and its versions I Found that You use `ansi-regex`
  2. then I cat every file and find in package-lock.json has the version I have the versions of the ansi-regex with a lot of versions there some of some vulnerable and other update to the latest version and the vulnerable paths is  
```json
},
				"strip-ansi": {
					"version": "3.0.1",
					"resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz",
					"integrity": "sha1-ajhfuIU9lS1f8F0Oiq+UJ43GPc8=",
					"requires": {
						"ansi-regex": "^2.0.0"
					}
				}

					"has-ansi": {
			"version": "2.0.0",
			"resolved": "https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz",
			"integrity": "sha1-NPUEnOHs3ysGSa8+8k5F7TVBbZE=",
			"requires": {
				"ansi-regex": "^2.0.0"
			},

			"dependencies": {
				"ansi-regex": {
					"version": "2.1.1",
					"resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz",
					"integrity": "sha1-w7M6te42DYbg5ijwRorn7yfWVN8="
				}

				"node_modules/babel-code-frame/node_modules/ansi-regex": {
			"version": "2.1.1",
			"resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz",
			"integrity": "sha1-w7M6te42DYbg5ijwRorn7yfWVN8=",
			"engines": {
				"node": ">=0.10.0"
			}
		},
		"node_modules/babel-code-frame/node_modules/strip-ansi": {
			"version": "3.0.1",
			"resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz",
			"integrity": "sha1-ajhfuIU9lS1f8F0Oiq+UJ43GPc8=",
			"dependencies": {
				"ansi-regex": "^2.0.0"
			}
			"node_modules/has-ansi/node_modules/ansi-regex": {
			"version": "2.1.1",
			"resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz",
			"integrity": "sha1-w7M6te42DYbg5ijwRorn7yfWVN8=",
			"engines": {
				"node": ">=0.10.0"
			}
		},
```
3. then I found that every version of ansi-regex before 4.1.1 as you see in the code you use 2.11,2.0.0,3.0.1 and these versions are vulnerable to Regular Expression Denial of Service (ReDoS) as every policy that Denial of service attack is out of scope so I didn't try anything to not make any damage to your work but I want to report it to you to investigate on that and update to the fixed version to denied this attack from happening. 
4. this is a poc that attacker can use to 

#POC
```
import ansiRegex from 'ansi-regex';

for(var i = 1; i <= 50000; i++) { var time = Date.now(); var attack_str = "\u001B["+";".repeat(i*10000); ansiRegex().test(attack_str) var time_cost = Date.now() - time; console.log("attack_str.length: " + attack_str.length + ": " + time_cost+" ms") 
```
# Fix: 
update to these (4.1.1, 5.0.1, and 6.0.1)  like you do in most of your code. 

## Supporting Materials:

this useful links that can you check on this vuln
1. https://www.cve.org/CVERecord?id=CVE-2021-3807
2. https://cwe.mitre.org/data/definitions/400.html
3. https://security.snyk.io/vuln/SNYK-JS-ANSIREGEX-1583908

## Impact

the attacker aimed at making a system inaccessible to its original and legitimate users. There are many types of DoS attacks, ranging from trying to clog the network pipes to the system by generating a large volume of traffic from many machines (a Distributed Denial of Service - DDoS - attack) to sending crafted requests that cause a system to crash or take a disproportional amount of time to process.

## Attachments
No attachments
