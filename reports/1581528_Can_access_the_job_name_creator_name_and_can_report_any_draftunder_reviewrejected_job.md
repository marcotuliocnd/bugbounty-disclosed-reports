# Can access the job name, creator name and can report any draft/under review/rejected job

## Report Details
- **Report ID**: 1581528
- **URL**: https://hackerone.com/reports/1581528
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-05-26T01:37:10.580Z
- **Disclosed**: 2022-07-20T18:08:56.474Z

## Reporter
- **Username**: sachin_kr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
The application has a functionality using which a user can report a job if he found the job is misleading/spam or fraud. Using this feature, an attacker can do report any unlisted (draft/under review/rejected) job. After reporting the job the victim will receive an email from 'LinkedIn Trust & Safety Team' saying 'We reviewed your report. Here's what we did.'  This also discloses the name of the user and his profile link who posted the job. Once you click on the 'view your report' button of the email, it will redirect you to the reports page at = 'https://www.linkedin.com/safety/reports/:reportId' This will disclose the name of the rejected/draft/under review job.

### Steps to reproduce:
1. Log in to an account and go to any posted job - `https://www.linkedin.com/jobs/view/3084381086/`
3. Now open any (rejected/draft or under review job using the job id) - https://www.linkedin.com/jobs/view/3086447496/. The application will give ` Something went wrong ` error message.
2. Report the posted job and intercept the vulnerable request.
{F1744522}
4. Forward the job using the draft, rejected jobId - 3086447496. The report will get submitted without any error. And after some time (1hr) you will receive an email in the social tab of the email from `Linkedin Trust and Safety`. This email includes the name of the job creator and his profile link and when u click on the `View your Report` button. It will disclose the name of the job including the location.
{F1744530}{F1744531}{F1744532}

###Vulnerable request:
```
POST /lite/flag-content?contentUrn=urn:li:jobPosting:3086455454&reason=OFFENSIVE&contentSource=JOBS_PREMIUM_OFFLINE&authorProfileId=0&trk=report-content HTTP/2
Host: www.linkedin.com
Cookie: XXX
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Csrf-Token: ajax:3198904967979491318
X-Isajaxform: 1
Origin: https://www.linkedin.com
Referer: https://www.linkedin.com/jobs/view/3084381086/?refId=%EF%BF%BD%2F%EF%BF%BD%21d%EF%BF%BD%27%EF%BF%BDe%1A_s%EF%BF%BD%16%EF%BF%BD%EF%BF%BD&trk=d_flagship3_company
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Content-Length: 0
Te: trailers
```

## Impact

An attacker can report any unlisted job and can access the name of the creator, name of the job name of the company, etc details.

## Attachments
- Screenshot_2022-05-26_at_6.52.08_AM.png
- Screenshot_2022-05-26_at_7.03.28_AM.png
- Screenshot_2022-05-26_at_7.03.38_AM.png
- Screenshot_2022-05-26_at_7.03.57_AM.png
