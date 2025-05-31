# [nextcloud/server] Moment.js vulnerable to Inefficient Regular Expression Complexity

## Report Details
- **Report ID**: 1712329
- **URL**: https://hackerone.com/reports/1712329
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-09-26T11:16:15.511Z
- **Disclosed**: 2022-12-09T05:17:34.177Z

## Reporter
- **Username**: mik-patient
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Describe the bugs: 🐛
moment is a lightweight JavaScript date library for parsing, validating, manipulating, and formatting dates. affected versions of this package are vulnerable to Regular Expression Denial of Service (ReDoS) via the preprocessRFC2822() function in from-string.js, when processing a very long crafted string (over 10k characters).

**PoC:**
```javascript
moment("(".repeat(500000))
```
Denial of Service (DoS) describes a family of attacks, all aimed at making a system inaccessible to its original and legitimate users. There are many types of DoS attacks, ranging from trying to clog the network pipes to the system by generating a large volume of traffic from many machines (a Distributed Denial of Service - DDoS - attack) to sending crafted requests that cause a system to crash or take a disproportional amount of time to process.

The Regular expression Denial of Service (ReDoS) is a type of Denial of Service attack. Regular expressions are incredibly powerful, but they aren't very intuitive and can ultimately end up making it easy for attackers to take your site down.

Let’s take the following regular expression as an:
```javascript
regex = /A(B|C+)+D/
```
This regular expression accomplishes the following:
  * `A` The string must start with the letter 'A'
  *  `(B|C+)+` The string must then follow the letter A with either the letter 'B' or some number of occurrences of the letter 'C' (the `+` matches one or more times). The `+` at the end of this section states that we can look for one or more matches of this section.
  * `D` Finally, we ensure this section of the string ends with a 'D'

It most cases, it doesn't take very long for a regex engine to find a match:
```javscript
$ time node -e '/A(B|C+)+D/.test("ACCCCCCCCCCCCCCCCCCCCCCCCCCCCD")' 0.04s user 0.01s system 95% cpu 0.052 total
```
The entire process of testing it against a 30 characters long string takes around ~52ms. But when given an invalid string, it takes nearly two seconds to complete the test, over ten times as long as it took to test a valid string. The dramatic difference is due to the way regular expressions get evaluated.

Most Regex engines will work very similarly (with minor differences). The engine will match the first possible way to accept the current character and proceed to the next one. If it then fails to match the next one, it will backtrack and see if there was another way to digest the previous character. If it goes too far down the rabbit hole only to find out the string doesn’t match in the end, and if many characters have multiple valid regex paths, the number of backtracking steps can become very large, resulting in what is known as catastrophic backtracking.

Let's look at how our expression runs into this problem, using a shorter string: "ACCCX". While it seems fairly straightforward, there are still four different ways that the engine could match those three C's:


**Workarounds**
In general, given the proliferation of ReDoS attacks, it makes sense to limit the length of the user input to something sane, like 200 characters or less. I haven't seen legitimate cases of date-time strings longer than that, so all moment users who do pass a user-originating string to constructor are encouraged to apply such a rudimentary filter, that would help with this but also most future ReDoS vulnerabilities.

**Details/References**
The issue is rooted in the code that removes legacy comments (stuff inside parenthesis) from strings during rfc2822 parsing. `moment("(".repeat(500000))` will take a few minutes to process, which is unacceptable. There is an excellent writeup of the issue here: [moment/moment#6015 (comment)](https://github.com/moment/moment/pull/6015#issuecomment-1152961973)

## Impact

CVE-2022-31129
`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`
[GHSA-wc69-rhjr-hc9g](https://github.com/moment/moment/security/advisories/GHSA-wc69-rhjr-hc9g)

  * using string-to-date parsing in moment (more specifically rfc2822 parsing, which is tried by default) has quadratic (N^2) complexity on specific inputs
  * noticeable slowdown is observed with inputs above 10k characters
  * users who pass user-provided strings without sanity length checks to moment constructor are vulnerable to (Re)DoS attacks

## Attachments
No attachments
