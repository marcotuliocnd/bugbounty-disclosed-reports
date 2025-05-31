# Submitted reports state logs leakage

## Report Details
- **Report ID**: 306733
- **URL**: https://hackerone.com/reports/306733
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-01-19T01:21:47.485Z
- **Disclosed**: 2018-01-19T21:55:57.732Z

## Reporter
- **Username**: 666reda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi team,

Summary
----------
The endpoint `https://hackerone.com/<hacker>` returns a JSON response containing some informations about the `<hacker>`, the parameter signal is returned as a high precision float number (up to 14 digits after the comma), the fractional part of this JSON parameter can be used to disclose some informations including the exact number of Resolved, Informative, and N/A reports submitted by the researcher as demonstrated in the following of the report.


Descpription
---------------------
The signal is calculated server-side by applying `(-5*N/A + 0*Informative + 7*Resolved) / (N/A+Informative+Resolved)`, self-closed reports and Duplicates are not included in signal calculations, I also ignored Spam reports because it's very rarely submitted by actif researchers. After the calculation is done, the signal value is returned as it is in `https://hackerone.com/<hacker>` even if only 2 digits after the comma is shown in the hacker profile, for instance, the following GET request to @fransrosen profile 
`curl -H 'X-Requested-With: XMLHTTPRequest' -H 'Accept: application/json' https://hackerone.com/fransrosen` will give us `..."signal":6.47740667976424`.


{F255410}


Keeping in mind that the number of Resolved reports are publicly disclosed in the `report_count` JSON parameter, it's enough to know Informative and N/A reports to have all the details about the hacker. To proceed, one should calculate *x* and *y* with `signal = x*(-5)+y*(0)+report_count*7 / x+y+report_count`, note that the signal is a high precision float number so the equation won't have more than solution, especially if we designate an estimation of the max number of submitted reports, and that's what I did in my exploit.

While this cannot not be accomplished mathematically (AFAIK), it can be easily done brue-force.


Exploitation
---------------------
I wrote a small python program to exploit this issue, the script can be used with the syntax : `python H1-signal.py <hacker> <max-reports>`
with `<hacker>` is the hacker to attack, and `<max-reports>` is an estimation of the max number of reports submitted by him, the estimation can be made depending on the hacker profile, the script will make a call to `https://hackerone.com/<hacker>` then recover the necessary parameters, then start the brute-force process, if `<hacker>` has really submitted less than `<max-reports>` reports, we will get the exact number of every submitted report by state.


POC
---------------------
Let's test on my own profile @██████

1- make an estimation of the max report number submitted by @███████, he has only 3 found bugs with 1.35 signal, so let's say 15 reports.

2- lunch `python H1-signal.py ███████ 15`
3- after a few moments we got :


{F255408}


And that's my exact log, because `2 N/A`, `3 Informatives` and `3 Resolveds` is the only combination which produce the signal `1.375`


POC 2
---------------------
Another test with ███████ and ████████ (sorry for this, please redact the names if you plan to publicly disclose the report, I already redacted them from the screenshot)

1- make an estimation of the max report number submitted the researchers.

2- lunch `python H1-signal.py ███ 25 && python H1-signal.py █████ 20`

3- after a few moments we got :


██████


these will be their submitted reports logs, because they are the only possibilities that can result the returned signal.


Testing Environment
---------------------
**Linux kali 4.9.0** with **Python 2.7.13** and **curl 7.55.1**.

## Impact

Information Disclosure via knowing the exact log of submitted reports with no user interation.


Limitations
---------------------
It takes much time when it's about more that 30 reports, especially if we took into consideration Spam reports, so of course, not all hackers can be targeted by exploiting this bug.
However, hundreds of H1 users has submitted less than 30 reports, and can be easily targeted, so I guess you still want to fix this, right ?


Mitigation
---------------------
Do everything server-side and send back only the signal with 2 digits after the comma which will be directly displayed in the hacker profile, or include Duplicate reports in the signal calculation.


References
---------------------
https://support.hackerone.com/hc/en-us/articles/207377903-What-are-Signal-and-Impact-
https://support.hackerone.com/hc/en-us/articles/205624695-What-are-the-states-of-a-report-


Let me know if you have any additional questions,
Regards.

## Attachments
- H1-signal.py
- poc1.png
- signal_ex.png
