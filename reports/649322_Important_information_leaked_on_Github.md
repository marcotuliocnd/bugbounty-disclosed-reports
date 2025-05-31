# Important information leaked on Github

## Report Details
- **Report ID**: 649322
- **URL**: https://hackerone.com/reports/649322
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-07-18T15:45:59.893Z
- **Disclosed**: 2019-08-22T12:52:28.011Z

## Reporter
- **Username**: mohanaddobal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: equifax

## Vulnerability Information
While searchin on Github about Equifax i found some juicy information like a username and password of this subdomain (https://transport5.ec.equifax.com/), internal ip of the database and its username & password 
 In the following link (https://github.com/ajiththorali/Testing/blob/49025b364451fb2076f85ad009a0dc50a941c5ce/target/classes/API_Equifax/propertiesHandle.properties) you could find this info 
*******
XML_URL = https://transport5.ec.equifax.com/ists/stspost?require_security= HTTP/1.1
Username = 50404
Password = ny5b2MuswjrFq3J2P9
service_name = acroxmltest
Content_Type = application/xml
*******
jdbc_driver = com.mysql.jdbc.Driver
db_url = jdbc:mysql://192.168.84.225:3700/EquiFax
db_username = root
db_password = redhat
*********

You should change passwords of the leaked account and remove this info from github

## Impact

any attacker can login to this sub domain and do unauthorized actions
If any one was able to be inside the network he would connect to the leaked database ip and steal important information

## Attachments
No attachments
