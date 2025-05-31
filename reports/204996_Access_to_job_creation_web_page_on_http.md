# Access to job creation web page on http://████████

## Report Details
- **Report ID**: 204996
- **URL**: https://hackerone.com/reports/204996
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-02-09T15:55:40.961Z
- **Disclosed**: 2019-12-02T18:38:43.772Z

## Reporter
- **Username**: reptou
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**

Hi DoD Team ! It looks like we may access to an ASP form on http://███ which enables any unauthenticated web user to create new jobs in the website database without any control. Furthermore, it seems that asp files are created with txt extensions too that enable the files to be readable from the Internet. 

**Description:**

The following web page http://██████████/html/sql/jobannouncement/jobinput.asp shows an ASP form which enables any user to create a new job in the database of the website. By checking http://██████/html/sql/jobannouncement/jobinput.txt, we may see all the code of the asp file and check that the data filled in the previous form are injected into an Access Database (which is not directly reachable). 

## Impact

It seems that the changes done through the form are not reflected on the web site as it seems to wait for a DOC file containing all the information about the job itself. However, when trying to record a new job, the data seem to be inserted into the database without any issue. An attacker could try to perform a Denial Of Service attack by inserting a lot of records into it for eample  At this moment, I do not see any other impact and I prefer reporting this issue before going further. 

## Step-by-step Reproduction Instructions

1. Go there : http://█████/html/sql/jobannouncement/jobinput.asp
2. Fill all the fields 
3. You will be redirected to jobconf.asp (which code source may be read too by using jobconf.txt file in URI)

## Suggested Mitigation/Remediation Actions

This form should not be reachable from the Internet without any proper authentication and authorization). 

Please let me know your thoughs on this,

Thanks !

Reptou

## Attachments
No attachments
