# Full access to internal Gitlab instances at redash.gitlab.com, dashboards.gitlab.com, prometheus.gitlab.com

## Report Details
- **Report ID**: 498964
- **URL**: https://hackerone.com/reports/498964
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-02-21T00:34:23.084Z
- **Disclosed**: 2019-04-19T09:46:26.556Z

## Reporter
- **Username**: rijalrojan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
**Summary:**
Lack of proper ticket trick security leads to internal access on Gitlab instances. **I did not use support.gitlab.com instead just using support@gitlab.com email was suffice. 

**Description:**

*Getting a support@gitlab.com Google Account*

After the Ticket Trick attack that Inti reported and disclosed, many companies including Gitlab added proper security measures to prevent this kind of attack. What companies did not realize is that Zendesk has a feature that can be exploited by attackers other than the CC feature. 

In this case, Gitlab has blocked sending emails to support+*@gitlab.com which prevents Ticket Trick that Inti came up with. However, the CC feature along with the Zendesk's feature can lead to further exploitation. 

To begin with, I sent an email to support@gitlab.com. After this, an automated reply was sent by Gitlab with confirmation that my ticket went through. Next, I went to accounts.google.com and registered support@gitlab.com. For the firstname and last name I copied a special hash for the ticket. Zendesk as a feature has a special hash for each ticket that is generated in the system This hash is like the key in a dictionary and can be used to add more content to the ticket. So by getting that hash and sending the request, Google allegedly sends an email to verify.

What happened here was due to Zendesk's own security measures, the first email from Google will be set as private because they are not CCed to my ticket. So then, I replied to the support ticket from Gitlab and in CC put noreply@google.com. Once this was done, I replayed the request in Google and again tried to verify `support@gitlab.com` this time the ticket had the verification code public. 

{F427388}

If you check the image on the top right corner you can see the hash repeated twice because I put that as a first and last name. 

Once this was done, I had a verified support@gitlab.com email. 

{F427390}

Next, I went to crt.sh to search for gitlab.com domains and found 3 domains that stood out: 

* prometheus.gitlab.com
{F427391}

* redash.gitlab.com 
{F427393}

* dashboards.gitlab.com
{F427395}

## Impact

Getting access to internal applications.

## Attachments
- grafana.PNG
