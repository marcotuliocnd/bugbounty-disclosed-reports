# Cross-domain linkability when system time changed in Tor Browser

## Report Details
- **Report ID**: 282339
- **URL**: https://hackerone.com/reports/282339
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-24T08:59:56.241Z
- **Disclosed**: 2017-10-26T11:30:53.199Z

## Reporter
- **Username**: newfunction
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
This report is inspired by #257942. That report uses `languagechange` event as an indicator for different tabs to link multiple visits to a single user. This report uses another trick to achieve the same thing.

Malicious websites keeps reading `Date.now()` inside a `setInterval` loop with a short interval (the PoC uses 3000 ms). Normally, the values of `Date.now()` between two consecutive iterations should differ by around 3000 ms (i.e. 2900 ms - 3100 ms). However, if the user's system time changes (either by user's manual modification or by some program's auto clock synchronization), the websites can detect this change, because the time difference between two iterations are likely to be larger than 3000 ms. In this case the script can send a log to the malicious server with the current and previous timestamp. Since it is very unlikely that two users change their system clocks at the same time and with the same old/new time pair, it is possible to link the same user on different domains.

PoC:
1. Open https://xiaoyinl.github.io/dds24f/tals.html and https://jsfiddle.net/a4faupwj/ on two different tabs in Tor Browser.
2. Change the computer's system time to more than 4 seconds later or a few seconds earlier.
3. Check the output from the two websites.

I think this issue is probably more severe than #257942, because the time change can happen without user action. There is a paper describing how major operating systems synchronize the system time and that most of the time synchronization protocol is vulnerable to MITM attacks.[1] The frequency of clock synchronization ranges from minutes to hours. The fact that Tor decreases timing precision to 100 ms doesn't really matter. Although I didn't test, I feel that if the user's clock lags more than 0.3 second right before a clock synchronization, using `setInterval(100ms)` should be able to detect that.

To fix this, the only feasible way I can think of is to prohibit non-active tabs from calling `Date.now()`.

[1] https://www.blackhat.com/docs/eu-14/materials/eu-14-Selvi-Bypassing-HTTP-Strict-Transport-Security-wp.pdf

## Attachments
No attachments
