# Improper authorization on `/api/as/v1/credentials/` for  Dev Role User with Limited Engine Access

## Report Details
- **Report ID**: 1218680
- **URL**: https://hackerone.com/reports/1218680
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-06-06T19:56:04.315Z
- **Disclosed**: 2021-08-03T17:12:41.321Z

## Reporter
- **Username**: superman85
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
**Summary:**
Dear Team,

Since  #1168528 was resolved. I have checking again for other roles. At Dev Role with Limited Engine Access, an user still can access API endpoint 
`/api/as/v1/credentials/` to get all API keys (private-key, search-key ... )

## Steps To Reproduce:

1 - Log in Kibana with the admin (elastic) user and go to the Stack Management > Users page (/app/management/security/users/)
2 - Choose an username , password and role for this user. For example you can choose username: **dev**
3 - Log in App Search with the admin (elastic) user and go to the Users & roles page (/as#/role-mappings/)
4 - Click Add mapping
5 - External Attribute choose **username** , in the Attribute value field enter **dev**
6 - In the Role box select Dev
7 - In Engine Access select Limited Engine Access, no need to select any engine
8 - Login to App Search with user **dev**
9 - Go to endpoint https://your_app_search_instance/api/as/v1/credentials/
10 - You still can get all api keys 

I have attached video PoC
█████████

## Impact

Privilege escalation. The default App Search install has a Private API Key with read/write access to all engines. If a Private Admin Key has been created before. the attacker can use it to create new API keys or delete existing ones.

With Limited Engine Acess, an user should create and managed their own api keys

## Attachments
No attachments
