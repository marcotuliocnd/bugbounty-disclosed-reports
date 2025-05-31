# Elasticsearch is currently open without authentication on  https://██████l

## Report Details
- **Report ID**: 2231261
- **URL**: https://hackerone.com/reports/2231261
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-29T16:51:21.847Z
- **Disclosed**: 2023-12-21T17:30:51.917Z

## Reporter
- **Username**: roland_hack
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

The vulnerability lies in insecure access to an Elasticsearch instance accessible at the URL "https://███████l". Currently, access to Elasticsearch is open without the need for authentication, exposing data stored on this instance to the risk of unauthorized disclosure.


## References

https://www.acunetix.com/vulnerabilities/web/elasticsearch-service-accessible/
https://medium.com/@D0rkerDevil/3k-bounty-for-elastic-search-takeover-70c0847d2e40
https://infosecwriteups.com/haystack-hackthebox-writeup-7dfd8a6fed5
https://book.hacktricks.xyz/network-services-pentesting/9200-pentesting-elasticsearch

## Impact

Insecure access to Elasticsearch on the https://████████l  site has serious security implications. The consequences of this vulnerability include
Sensitive Data Leakage: Sensitive data stored in Elasticsearch, including confidential information, personal data and other sensitive information, may be exposed and compromised.
Risk of Data Modification or Deletion: Unauthorized access may enable malicious actors to modify or delete data, disrupting the integrity of stored information.
Privacy Violation: The vulnerability may lead to violations of the privacy of users whose data is stored on the Elasticsearch instance, which may have legal consequences.
Service disruption: Attackers can disrupt services by accessing Elasticsearch without authorization, which can lead to service interruptions and performance degradations.
Unknown security risks: Unauthorized access can expose the system to unknown security risks, including potential attacks or malicious activity.
It is essential to take immediate action to correct this vulnerability and reduce these potential risks. The security of the Elasticsearch instance must be strengthened to protect data and guarantee confidentiality.

## System Host(s)
████l

## Affected Product(s) and Version(s)
Elasticsearch 2.7.0

## CVE Numbers


## Steps to Reproduce
To reproduce the Elasticsearch insecure access vulnerability on the "https://███l" instance, follow these steps:
Open a web browser and access the URL "https://███l".
Use a tool such as "estk" to list the Elasticsearch indexes available on the site by executing the command estk --url=https://█████████l list.
You can also use : https://github.com/elasticsearch-dump/elasticsearch-dump

- Output 

estk --url=https://█████l list

2023/10/29 17:24:51 Detecting version...
2023/10/29 17 :24:51 Trying elasticsearch
2023/10/29  17:24:53 Found elasticsearch, major version 2
Indices: 3, document count: 2212, size: 5.9 MB
Found index aim_high with 2211 documents (5.9 MB)
Found index .opensearch-observability with 0 documents (208 B)
Found index .kibana_1 with 1 documents (5.3 kB)

To extract data from a specific index (for example, the "aim_high" index), run the command
estk dump --url=https://███████l --index=aim_high.
The index data will be displayed in JSON format on standard output, confirming insecure access.
These steps describe how a potential attacker could access Elasticsearch data without the need for authentication, thus exposing the vulnerability.

## Suggested Mitigation/Remediation Actions
The "Suggested Mitigation/Remediation Actions" section of a vulnerability report offers recommendations for remediating the vulnerability or mitigating its effects. Here's how you can formulate it for the Elasticsearch insecure access vulnerability:
Suggested Mitigation/Remediation Actions:
To remediate the Elasticsearch insecure access vulnerability on the "https://██████l" instance, the following actions are recommended:
Set up authentication: Configure Elasticsearch to require authentication before granting access to data. Use robust authentication methods, such as SSL certificates, usernames and passwords.
Set up authorization: Define appropriate authorization policies to limit access to data according to user roles and privileges. Ensure that only authorized persons have access to sensitive data.
Updates and patches: Make sure your Elasticsearch instance is up to date with the latest security patches. Perform regular updates to correct known vulnerabilities.



## Attachments
No attachments
