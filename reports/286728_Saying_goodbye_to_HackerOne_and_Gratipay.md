# Saying goodbye to HackerOne and Gratipay.

## Report Details
- **Report ID**: 286728
- **URL**: https://hackerone.com/reports/286728
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-02T21:06:42.798Z
- **Disclosed**: 2017-11-02T21:08:48.437Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
# Thank you, HackerOne

I would like to make this the final report to Gratipay and thank everyone that was involved in this amazing journey. Gratipay is shutting down at the end of the year (https://gratipay.news/the-end-cbfba8f50981) and to finish on a happy note we closed all of our reports as resolved.

We launched our bug bounty program on July 17th, 2015 after having received reports via our [security.txt](https://github.com/gratipay/gratipay.com/commits/master/www/security.txt) file. I joined the team one year ago after submitting this report: https://hackerone.com/reports/190373. @whit537 invited me and I immediately received a warm welcome. The experience and amount of knowledge I gained from a year triaging reports means so much to me. No matter the quality or severity of the report, there was always something new to learn.

Over the course of this time we received a total of 481 reports: 

{F235849}

I would like to thank every single one of you that reported an issue to us and wish you the best of luck with future reports.

{F235846}

# Notable Moments

The following are some of the most notable moments of working with Gratipay and all of you.

### 1) "Sub domain takeover" by @b3nac

Link to report: https://hackerone.com/reports/221133

@b3nac reported what they believed to be a sub-domain takeover. It turned out it was not an issue, but since @b3nac had invested so much time and effort into that report we decided to award them some points. @b3nac has come so far and is now reporting amazing issues on HackerOne. Remember to keep encouraging newcomers.

{F235855}

---

### 2) "Reflected XSS - gratipay.com" by @tungpun

Link to report: https://hackerone.com/reports/262852

@tungpun reported the first ever reflected XSS in gratipay.com. I could not believe my eyes when I saw this report land in my inbox. We managed to fix the issue in 17 minutes.

{F235856}

---

### 3) "Gratipay rails secret token (secret_key_base) publicly exposed in GitHub" by @nuii

Link to report: https://hackerone.com/reports/262620

@nuii reported a leaked Rails secret token in our codebase. The amazing thing was they found it thanks to one of [my write-ups](https://edoverflow.com/2017/github-for-bugbountyhunters/).

{F235857}

---

### 4) "POODLE SSLv3.0" by @wazehell

Link to report: https://hackerone.com/reports/219499

@wazehell reported an invalid POODLE attack, but it was a great opportunity to explain what the POODLE attack is and help them maybe report a valid issue in the future.

{F235860}

---

### 5) "Content length restriction bypass can lead to DOS by reading large files on gip.rocks" by @a0xnirudh

Link to report: https://hackerone.com/reports/203388

Thanks to @a0xnirudh's report I was able to escalate the issue to something that could have potentially caused more damage.

{F235862}

---

### 6) "Sub domain take over in gratipay.com" by @anshad

Link to report: https://hackerone.com/reports/257331

Lesson learned here is, even if the report is invalid remember to always encourage the hacker to keep on looking, because they are human (hopefully) and can learn from their mistakes.

{F235864}

# Conclusion

Once again thank you for everything.

{F235865}

Happy hacking!
Ed

## Attachments
- Screenshot_from_2017-11-02_21-32-36.png
- Screenshot_from_2017-11-02_21-35-10.png
- Screenshot_from_2017-11-02_21-40-45.png
- Screenshot_from_2017-11-02_21-44-13.png
- Screenshot_from_2017-11-02_21-46-47.png
- Screenshot_from_2017-11-02_21-49-52.png
- Screenshot_from_2017-11-02_21-54-22.png
- Screenshot_from_2017-11-02_21-58-22.png
- d94c24e8e51209ca6f1a397295f465cc726c904f_xtralarge.jpg
