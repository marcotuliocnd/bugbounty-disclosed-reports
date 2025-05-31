# IDOR - Delete technical skill assessment result & Gained Badges result of any user

## Report Details
- **Report ID**: 1592587
- **URL**: https://hackerone.com/reports/1592587
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-06T18:46:45.681Z
- **Disclosed**: 2022-10-05T19:29:11.476Z

## Reporter
- **Username**: sachin_kr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
The web app is vulnerable to IDOR at `DELETE /voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/urn%3Ali%3Afsd_skillAssessmentAttemptReport%3A(urn%3Ali%3Afsd_profile%███%2Curn%3Ali%3Askill%3A280%2C1)` HTTP request. Allows an attacker to delete the skill assessment result of any user's technical skill. This can be done by replaying the request using the victim's 'profileId' which can be obtained from the page source of the victim's public profile and the skill id which is a numeric identifier that can be brute-forced.

###The Profile UUID can be obtained from the page source of the victim's public LinkedIn profile and the skill id can be brute-forced with the threshold of 3 requests in burp intruder.

###Steps to reproduce:
1. log in to an account.
3. Give an assessment say HTML or PowerPoint.
4. After completing the assessment go to - https://www.linkedin.com/skill-assessments/hub/quizzes/?channel=JOBS_HOME_NAVIGATION_BAR
5. If the assessment is successful then click on the `Badge` button of your assessment else click on the `to retake ``button(https://www.linkedin.com/skill-assessments/hub/reports/?channel=JOBS_HOME_NAVIGATION_BAR&resultType=TO_RETAKE).
6. Click on the Kebab menu icon and then click on the delete results button.
7. Intercept the vulnerable request.
8. Change the 'fsd_profile' profile parameter value with the victim's profile UUID `(this can be obtained from the page source of the victim's public profile page as shown in video POC)` and send the request to the intruder.
9. Now brute-force the value of 'skill id' (Keep frequency 3). The victim's skill will get deleted.
████

###Video POC:
███████

###Vulnerable Request:
```
DELETE /voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/urn%3Ali%3Afsd_skillAssessmentAttemptReport%3A(urn%3Ali%3Afsd_profile%███████%2Curn%3Ali%3Askill%3A280%2C1) HTTP/2
Host: www.linkedin.com
```

## Impact

An attacker can delete the badges and skill assessment results from any public LinkedIn profile by replaying the request using the victim's UID and skill id. The UID is publically available in the page source.

## Attachments
No attachments
