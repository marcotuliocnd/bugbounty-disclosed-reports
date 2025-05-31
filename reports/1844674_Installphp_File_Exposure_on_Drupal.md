# Install.php File Exposure on Drupal

## Report Details
- **Report ID**: 1844674
- **URL**: https://hackerone.com/reports/1844674
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-24T01:15:53.787Z
- **Disclosed**: 2023-02-24T19:06:54.384Z

## Reporter
- **Username**: carpc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
In the security assessment, it was discovered that the install.php file located at ██████/core/install.php is accessible and returns a 200 status code. Since the installation process is not possible, it is essential to address the vulnerability of the install.php file as soon as possible to prevent potential attacks and ensure the availability of the website. It is important to take measures to remove or secure the file to prevent it from being accessed by attackers and causing a denial of service attack. This is crucial to prevent the website from crashing and overwhelming the system, which can lead to serious problems for the website and its users.

Obs:
* Use the drupwn tool, found at https://github.com/immunIT/drupwn
* Run the command: python3 ./drupwn --mode enum --target ██████/
* The tool will reveal the install.php script with a status of  **200 OK**.

████

## Summary
The install.php file, which is meant to be removed after the initial installation of Drupal, has been left in place and is accessible to attackers. This file can be used to reinstall the website, potentially leading to data loss or other issues. Additionally, it was observed that the website encountered an unexpected error of Drupal\Component\Plugin\Exception\PluginNotFoundException: Unable to determine class for field type 'comment' which can be used to escalate privilege and access sensitive information.

## Proof Of Concept 
Proof of Concept: A screenshot demonstrating the install.php file being accessible and the error is displayed
█████████

**My IP Report:**
████ 

## References

## Impact

By accessing the install.php file, an attacker could potentially reinstall the website, leading to data loss or other issues. Additionally, the error displayed may also be used to escalate privilege and access sensitive information.

## System Host(s)
█████████

## Affected Product(s) and Version(s)
Drupal 8 or  >

## CVE Numbers


## Steps to Reproduce
1. Open a web browser and navigate to █████/core/install.php
2. Observe that the install.php file is accessible and returns a 200 status code

## Suggested Mitigation/Remediation Actions
The install.php file should be removed from the website to prevent unauthorized access and the error should be fixed to prevent privilege escalation. Additionally, it is recommended to review all the configurations and modules to verify if there are any misconfigurations or vulnerabilities.

It is important to note that an attacker could use this vulnerability to cause a significant amount of stress on the website by repeatedly accessing the install.php file, potentially causing the website to crash. This is why it's important to report this vulnerability and fix it as soon as possible.



## Attachments
No attachments
