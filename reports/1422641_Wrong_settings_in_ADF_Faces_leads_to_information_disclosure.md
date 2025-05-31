# Wrong settings in ADF Faces leads to information disclosure

## Report Details
- **Report ID**: 1422641
- **URL**: https://hackerone.com/reports/1422641
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-12-10T14:36:48.517Z
- **Disclosed**: 2022-01-19T19:28:18.141Z

## Reporter
- **Username**: h3xr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hello, Team.

Found some interesting links which leads to information disclosure in █████
Link 1: [██████████]███
Link 2: [████████]██████████
Link 3: [██████████]███

Every link goes through https://██████to https://████
**For Link 3 is possible to change data in the fields: First Name, Last Name, Phone Number. Just click "██████".**

Viewing the code gives us some more info about the system:
```
██████
```

ADF ███████ is outdated
The [Ref. Page](https://docs.oracle.com/cd/E41362_01/web.1111/b31973/ap_config.htm) says:
*A.2.3.16 Version Number Information
Use the oracle.adf.view.rich.versionString.HIDDEN parameter to determine whether or not to display version information an a page's HTML. When the parameter is set to false, the HTML of an ADF Faces page contains information about the version of ADF Faces and other components used to create the page as shown in Example A-2.
When you create a new application, the parameter is set to true. It should also be set to true in a production environment. Set the parameter to false to display this version information for debugging information.
Note:
In a production environment, set this parameter to true to avoid security issues. It should be set to false only in a development environment for debugging purposes.*

[This Ref.](https://imlive.s3.amazonaws.com/Federal%20Government/ID188660931371312277217448460962608356160/Attachment_E_███S_Request_for_Role_Guide.pdf) points us that Link 3 is:
*██████S lists any █████s waiting for your approval. If there are none, there will be a message like the one in ███████. Click the Logout button to exit ██████████S.  You can use the link in your email to return to the ██████████.*

But we see the Logout button and can modify some data - so **perhaps** we are logged in.

## Impact

Sensitive information disclosure
Information modification
Privacy Violation

## System Host(s)
███████

## Affected Product(s) and Version(s)
Oracle ADF Faces

## CVE Numbers


## Steps to Reproduce
In the Desc. section

## Suggested Mitigation/Remediation Actions
Update Oracle ADF
Close sensitive information from unauthenticated users



## Attachments
No attachments
