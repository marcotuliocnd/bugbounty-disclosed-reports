# Attachment object in GraphQL continues to grant access to files, even if they are removed from rendering

## Report Details
- **Report ID**: 1132606
- **URL**: https://hackerone.com/reports/1132606
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-23T09:45:05.510Z
- **Disclosed**: 2021-08-24T04:15:36.337Z

## Reporter
- **Username**: haxta4ok00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Hi team,

Our team noticed that you(program) can attach files to the policy page. These files can be anything, images, text, archive, etc.In other words, these files may or may not contain sensitive information.  Our team believes that the data that can be attached in different vectors is high . Therefore, in the CVSS calculator, we set Confidentiality: `High`. 

Also, the HackerOne platform slightly confuses customers in this situation. When the client tries to delete a file from the tab where the file is attached, the page shows that the file was deleted, and after clicking the "Update policy page" button, it shows that it was successfully updated. But the page does not reload, and the client sees that the file was indeed deleted. We also tested this on the endpoint, and indeed. The update takes place without the involvement of the Attachment file. But after you refresh the policy edit page, this file will appear again. But visually, the client initially believes that the file was deleted, until he refreshes the page and sees it. We believe this is misleading to the customer


{F1239141}
{F1239140}
{F1239142}
{F1239139}

In any case, we believe that when a client deletes a file from the page rendering(`{F_number_file}`), it deletes the path (link) to that file, i.e. it believes that it is not possible for other people to get it.






## Steps To Reproduce:

1. Customer create private program on platform HackerOne
2. Customer attached some file that has sensitive data (for example while the program is private)
3. Customer  decided to open their program and become public
4. Removes rendering to a file on a page (`{F_number_file}`) / Also decides to delete from the attachments tab
5. The program goes public

Next, any unauthorized user can make a GraphQL request


```http
https://hackerone.com/graphql
POST:
{"query":"query {team(handle:\"security\"){attachments{_id,content_type,created_at,expiring_url,file_name,file_size,id,long_lasting_url}}}"}
```
Change the handle to the desired one
 

## Recommendation:
Review the relationship to deleting files for the policy page, or change access to the Attachment object in GraphQL if rendering was removed

## Impact

Granting access to files even if they are removed from rendering

## Attachments
- after_update_page.png
- delete_file.png
- file_1.png
- have_not_attachment.png
