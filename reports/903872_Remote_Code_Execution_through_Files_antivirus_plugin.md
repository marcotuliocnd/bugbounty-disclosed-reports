# Remote Code Execution through "Files_antivirus" plugin

## Report Details
- **Report ID**: 903872
- **URL**: https://hackerone.com/reports/903872
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-20T16:18:49.190Z
- **Disclosed**: 2021-06-21T12:28:19.922Z

## Reporter
- **Username**: pabl00nicarres
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owncloud

## Vulnerability Information
Hi,
I would like to report a Remote Code Execution in OwnCloud. 
The flaw is exploitable as an authenticated user and level of privileges required is "Administrator".
Vulnerable component is the plugin "files_antivirus", freely downloadable via the market and available in owncloud github repository at  
+ https://github.com/owncloud/files_antivirus.

Environment used: LAMP stack . Owncloud version:  10.4.1.3.
Considerations: In owncloud separation between application/database/system layer is cleary a (good) design choice and neither an Administrator user in a default configuration scenario is supposed to upload custom code if not provided with shell access level.
POC: Below the steps to reproduce the issue and get code execution:
+ Login in owncloud as Administrator.
+ If not installed, go to marketplace and install the aforementioned "files_antivirus" plugin.
+ Download the config report from the general menu. {F875798}
+ Open the report, all sensitive infos are stripped but absolute paths are still there. We're mostly interested in the config value "datadirectory" in order to understand where exactly the uploaded files are. Other interesting values are in the "enviroment structure, where we can get the php interpreter path (just an example, this can be done with bash etc.). {F876062}
+ Go to "Files" and upload a file with php code, extension is not relevant.
{F876139}
+ Go to "Protection" and, using the previously obtained path from the config report, set the clamscan av path with the PHP interpreter path. The first argument will be the file with php code we just uploaded (the use of escapeshellarg function is not relevant here, we're not injecting shell arguments/commands). {F876153}
+ Save the new config, ignore the error about the scan that cannot be executed and verify that the PHP code was successfully executed.

Kind Regards
Paolo Serracino

## Impact

Depends from the environment, an attacker who is able to get admin creds could use this flaw to move laterally, steal cloud metadata infos and so on.

## Attachments
- Screenshot_(174).png
- Screenshot_(178).png
- Screenshot_(180).png
- Screenshot_(182).png
