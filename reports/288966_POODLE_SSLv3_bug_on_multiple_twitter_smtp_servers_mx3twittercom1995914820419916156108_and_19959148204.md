# POODLE SSLv3 bug on multiple twitter smtp servers (mx3.twitter.com,199.59.148.204,199.16.156.108 and 199.59.148.204)

## Report Details
- **Report ID**: 288966
- **URL**: https://hackerone.com/reports/288966
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-09T21:44:16.746Z
- **Disclosed**: 2018-02-22T00:11:25.195Z

## Reporter
- **Username**: omespino
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information

**Summary:** POODLE SSLv3 bug on multiple twitter smtp servers

**Description:** CVE-2014-3566: The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other products, uses nondeterministic CBC padding, which makes it easier for man-in-the-middle attackers to obtain cleartext data via a padding-oracle attack, aka the "POODLE" issue.


## Steps To Reproduce:

Hi Twitter Sec team here is the POC

  1. get a nmap installation and twitter_smtp_ssl_servers.txt file (attached)  
  2. run this command :
"nmap -sV --version-light -Pn --script ssl-poodle -p 25 -iL twitter_smtp_ssl_servers.txt | grep -B 5 VULNERABLE"
  3. See the results 

## Supporting Material/References:

  * An output screentshot  and the twitter_smtp_ssl_servers.txt are attached.


## Attachments
- POODLE_SSLv3_twitter_smtp_servers.png
- twitter_smtp_ssl_servers.txt
