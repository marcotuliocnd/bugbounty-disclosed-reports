# Reflected XSS in Step 2 of the Installation

## Report Details
- **Report ID**: 170156
- **URL**: https://hackerone.com/reports/170156
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-18T05:04:27.335Z
- **Disclosed**: 2017-08-02T05:59:06.669Z

## Reporter
- **Username**: pavanw3b
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: revive_adserver

## Vulnerability Information
**"Cricetinae"** :)

### Short Description
The **dbName** parameter in Step 2 of Installation Wizard is vulnerable to Cross-Site Scripting vulnerability when the form is returned with error.

### Vulnerability Details
Cross-Site Scripting issue let's one to run a javascript of choice. It helps most of the client side risks including but not limited to phishing, temporary deface, browser key-logger and others. Exploitation frameworks like BeEF eases the offensive attack.

### Attack Vector
Though this may be treated as a Self-XSS, the place where the issue is affecting is sensitive. If the user who is going to set up the Revive Adserver, follows an untrusted malicious guide which contains specially crafted XSS payload, can help in gaining access to the database by tricking him to enter the credential in attacker's site by redirecting or any other way.
	
### Dependency
1. Occurs at the time of installation when the Database Name contains invalid characters.
2. Chrome's default XSS Protection blocks simple XSS payloads. Please use firefox for reproduction.

### Steps to Reproduce
1. Navigate to Installation
2. Agree to the terms and condition in the first step
3. In the second step, please enter  `something<script>alert('xss');</script>` for Database Name field
4. Note the javascript alert box triggered from the above payload entered in dbName parameter

### HTTP Request
`POST /revive-adserver/www/admin/install.php HTTP/1.1
..
..
Connection: close`

`_qf__install-db-form=&action=database&moreFieldsShown=&dbName=something<script>alert('xss');</script>&dbUser=root&dbPassword=roots&dbHost=localhost&dbType=mysql&dbLocal=0&dbPort=3306&dbTableType=MYISAM&dbTablePrefix=rv_&save=Continue+%C2%BB`
`

###HTTP Response
`HTTP/1.1 200 OK
`
..
`<span id='errorMessages'>
                          Database names cannot contain "/", "\", ".", or characters that are not allowed in filenames <br/>                          Installation failed to create the database something<script>alert('xss');</script></span>`
        
###Test Environment Details
**Version**: Latest as on Sept 17: revive-adserver-3.2.4 downloaded from official website
**Setup type**: local
**Browser**: Firefox 47.0
**OS**: Mac OS X

Cheers,
Pavan

## Attachments
- revive_adserver_xss.png
