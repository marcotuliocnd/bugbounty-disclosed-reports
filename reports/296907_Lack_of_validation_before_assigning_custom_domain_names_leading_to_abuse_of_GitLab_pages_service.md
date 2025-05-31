# Lack of validation before assigning custom domain names leading to abuse of GitLab pages service

## Report Details
- **Report ID**: 296907
- **URL**: https://hackerone.com/reports/296907
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-12-11T08:14:59.603Z
- **Disclosed**: 2018-02-01T23:26:02.414Z

## Reporter
- **Username**: badshah_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
One way to add a custom domain name for GitLab pages is to create a new DNS A record pointing to the IP of GitLab Pages server i.e. `52.167.214.135`. A person who owns the domain name, could then add the domain name in the Pages settings (at `https://gitlab.com/<username>/<repo>/pages`). GitLab then assigns the domain name mentioned in the Pages settings to that repository if no other repository uses the domain name. All the visitors of the site will be delivered the HTML content in that repository.

An attacker who finds any domain name with DNS records pointing to the above mentioned IP, could take over it for malicious purposes. The domain name will be locked to the attackers repository and the legitimate owner cannot claim it until it is released by the attacker.

There are currently 1953 unique domain names with DNS records pointing to the above mentioned IP, and 115 domains could be taken over.

## Steps To Reproduce:

There are websites which provide data about DNS records. One such website is DNSTrails.com.

**Automated method to get all the domains pointing their DNS to `52.167.214.135`**:
```python
import requests
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Referer': 'https://dnstrails.com/',
    'Origin': 'https://dnstrails.com',
    'DNT': '1',
}

page_no = 1

while page_no <= 1000:
  params = (
      ('page', page_no),
  )
  print "Page : " + str(page_no)
  raw_data = requests.get('https://app.securitytrails.com/api/search/by_type/ip/52.167.214.135', headers=headers, params=params, verify=False)
  data = json.loads(raw_data.text)
  for s in data["result"]["items"]:
    with open('gitlab_domains.txt', 'a') as file:
      file.write(s["domain"] + '\n')
  page_no = page_no + 1
#  print "Sleeping for 5"
#  time.sleep(5)
```

Get the unique domain names using: `sort gitlab_domains.txt | uniq > unique_domains.txt`

**Python code to check if the domain names are vulnerable:**
```python
import requests

with open('unique_domains.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

for s in content:
  print '*'
  try:
    req = requests.get('http://' + s, timeout=10)
    if req.status_code == 404 and "The page you're looking for could not be found" in req.text:
      with open("vuln_websites.txt", "a") as myfile:
        myfile.write(s + '\n')
  except Exception as e:
    with open("error.txt", "a") as m:
      m.write(s + '\n')
```

This script creates two files - `vuln_websites.txt` and `error.txt`. The domain names in `vuln_websites.txt` is vulnerable to domain name take overs on GitLab.

Count of the vulnerable domain names: `wc -l vuln_websites.txt`. The output is : 115

## Simple mitigation technique

When the domain is added in the settings, get the whois data of the domain name. Check the DNS records and if it contains GitLab's above mentioned IP, request the OTP sent to the registered email address.

A basic python implementation would be:

```python
# pip install python-whois

import whois
w = whois.whois('domain.com')
print w["emails"]
# The OTP could be sent to that email
```

## Impact

Attacker can create fake GitLab account(s) using the email(s) from temporary/anonymous email services. Configure fake email addresses with git for further code commits. Create multiple repositories and add domain name from the vulnerable list. The attacker can then:

- Use the static websites as Command and Control centers for their malware / for other malicious intents
- Phish the customers / visitors of the legitimate domain owners, abusing both the GitLab user's rights and GitLab's Terms of Use.

## Attachments
No attachments
