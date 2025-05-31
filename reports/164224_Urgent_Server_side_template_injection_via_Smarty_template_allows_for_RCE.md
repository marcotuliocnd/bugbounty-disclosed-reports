# Urgent: Server side template injection via Smarty template allows for RCE

## Report Details
- **Report ID**: 164224
- **URL**: https://hackerone.com/reports/164224
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-29T17:27:44.749Z
- **Disclosed**: 2017-08-17T18:25:41.763Z

## Reporter
- **Username**: yaworsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: unikrn

## Vulnerability Information
Hi All,
I've found an issue which has allowed me to execute file_get_contents and extract your /etc/passwd file.

##Description
It appears as though you are using smarty on the backend for templating. Entering a malicious payload as my firstname, lastname and nickname and then inviting a user to join the site results in the code being executed.

To start, I began with the payload {7*7} and received a template error in the email I received {F115749} Recognizing the injection, I then was able to confirm the version of smarty used via {$smarty.version} {F115750} Next I was able to test {php} tags by using ```{php}print "Hello"{/php}``` {F115751}. Finally I used file_get_contents to begin extracting the etc/pass file ```{php}$s = file_get_contents('/etc/passwd',NULL, NULL, 0, 100); var_dump($s);{/php}``` {F115752}

##Steps to reproduce
1. Edit your profile
2. Add the payload ```{php}$s = file_get_contents('/etc/passwd',NULL, NULL, 0, 100); var_dump($s);{/php}``` as your first name, last name and user name (I'm not sure which field is vulnerable)
3. Invite a friend using another email of yours
4. View the email and you will see part of the etc file dumped

##Vulnerability
Since the {php} tags are being parsed and executed, we can execute php functions. In this case, you'll see I'm able to extract the etc/passwd file. While I haven't tried, an attacker can more than likely create a shell on the server.

Please let me know if you have any questions.
Pete

## Attachments
- ssti_rce_initial_payload_error.png
- ssti_rce_etc_passwd.png
