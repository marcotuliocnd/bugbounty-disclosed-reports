# Improper input validation in projects leads to fully deny access to project resources

## Report Details
- **Report ID**: 1237700
- **URL**: https://hackerone.com/reports/1237700
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-18T14:41:27.848Z
- **Disclosed**: 2021-09-01T20:11:37.712Z

## Reporter
- **Username**: a_d_a_m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
#INTRODUCTION

**Accounts used to search for this vulnerability:**
- **id:** █████████ **email:**███
- **id:** █████████ **email:** █████████

**Most of the requests made to test the vulnerability were made with the "X-hackerone:  a_d_a_m"  header**

**IP used:**
████ / ███

**Endpoint URL:**
https://fr.semrush.com/projects/api/projects/tags/PROJECT_ID/?key=API_KEY

#EXPLOITATION
**Description of Security Issue:**

According to SEMrush documentation:
>Semrush Projects allow you to set up 11 different tools analyzing all aspects of a business's online visibility.

As shown below these projects can include tags:
{F1343556}

The problem stems from the fact that the input which contains the name of the tag is not validated correctly, an attacker has the possibility of setting the name of a tag to null, which is contrary to the logic of the application. Giving the value null to a tag name causes a critical bug in the front-end. If a person has a tag in their project list that has a null name, then the person will no longer be able to manage their projects, see their project list or access a project. The victim does not even have the option to delete the project with the sabotaged tag, since he can no longer manage his projects. A blank page will appear as shown in the video below:

{F1343572}

*However, this is not a security issue. For this to be considered as such, a vector would have to be found that would allow an attacker to impact other users.*

According to the documentation:
>Project sharing is also available to make collaboration between teams and agencies easy.

Through this tool I have found 2 ways to impact an external user:

- The first is to have been invited by someone to a project with "can edit" rights. Thus, the attacker will be able to modify the labels of the project and impact the owner and all the participants of the project. (with interaction and privileges)

{F1343606}

*Steps needed to reproduce 1st bug:*
{F1343639}

- The second way is to invite someone with their email to a project that we created with a sabotaged tag, so our project will be directly present in the victim's project list and will be directly impacted without interaction of the victim.  (**without interaction and privileges**)

*Steps needed to reproduce 2nd bug:*
{F1343659}

#RESOLUTION

In my opinion, the best solution would be to validate the type of the tag names entered in the request (forbid the null type).






The type of the bug is "Improper Input Validation (CWE-20)" but I couldn't find it in the list of weakness, it's weird given that it is available in other programs when I make a report. Given that I did not find any other type of weakness in the list which could come close to what I found, I didn't put the name of the weakness.Can you try to put it if you can ?

## Impact

**There is total loss of availability, resulting in the attacker being able to fully deny access to resources in the impacted component without any interaction from the victim.**

**exploitation scenarios:**
- We can take the email addresses of the most important semrush clients (agencies, companies, etc.) and paralyze all their projects

*From what I heard in the documentation, agencies working on online visibility use SEMrush with this tool to have a project for each client, we can imagine that a malicious person can impact agencies specializing in online visibility by inviting their email address to a sabotaged project.
This will have the effect of preventing these agencies from accessing their clients' projects and managing them just with their email address.*

- A guest of a project (employee / client / ...) with editing rights can paralyze all projects of the owner and collaborators on the project

To find the email of an individual/company that you are targeting, *you can search on google or on social networks/request the email from the company by inventing x or y reason/we can also know the target's email address for other reasons (former employee / collaborator, close to the company, etc ...). Another very good tool: hunter.io, which allows you to extract email addresses from a domain name.*

{F1343710}

Once a wordlist of victims' email addresses has been created, an attacker can format these emails in json format to invite them to the sabotaged project.

## Attachments
- tag_overview.PNG
- front-end-bug.webm
- share-project.PNG
- first-case.webm
- second-case.webm
- hunter-io.PNG
