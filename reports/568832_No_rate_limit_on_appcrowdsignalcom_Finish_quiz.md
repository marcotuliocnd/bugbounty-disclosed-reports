# No rate limit on app.crowdsignal.com (Finish quiz)

## Report Details
- **Report ID**: 568832
- **URL**: https://hackerone.com/reports/568832
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-05-06T14:58:23.144Z
- **Disclosed**: 2019-07-27T09:01:50.681Z

## Reporter
- **Username**: yusuf_furkan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hello team
[https://hackerone.com/reports/488923 ]--> vulnerability resolved maybe you can compare the report to start this, but this vulnerability has been closed.this is a separate no-rate limit error.this is not a duplicate bug.
No rate limit on app.crowdsignal.com (Finis quiz)
POC step:
1.https://app.crowdsignal.com/quizzes/new
2.example (https://testedtestsdasad1404.survey.fm/untitled-quiz-1)
3.Finish quiz send it to Intruder.(Burp suite)
4.get the payloads ready. Attack with null payloads.
5.POC video and screenshot:

## Impact

an attacker could send a large number of requests to terminate the victim. there is a limit.(quiz finish)
solution:
a limit must be added.

## Attachments
- No_rate_limit_POC_quiz.png
- No_rate_limit_on_crowdsignal.mp4
