# Unauthenticated WordPress Database Repair DoS

## Report Details
- **Report ID**: 2786591
- **URL**: https://hackerone.com/reports/2786591
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-10-17T06:12:26.877Z
- **Disclosed**: 2024-10-18T13:01:54.056Z

## Reporter
- **Username**: wshadow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Summary:

The WordPress Database Repair feature, accessible via the `/wp-admin/maint/repair.php` endpoint, is vulnerable due to improper access control and insecure design. When `WP_ALLOW_REPAIR` is set to `true` in the `wp-config.php` file, the repair page becomes publicly accessible without requiring any authentication. This vulnerability arises from two main issues: the absence of authentication for accessing the repair endpoint and the insecure nature of the WordPress repair feature, which lacks any limits or restrictions on access frequency or user verification. Consequently, an attacker can repeatedly trigger resource-intensive database repair operations, overwhelming server resources and resulting in a Denial of Service (DoS) condition. 
This vulnerability can be categorized under these two CWE's as it fails to impose necessary restrictions on who can access this critical functionality.

**CWE-306: Missing Authentication for Critical Function** 
 **CWE-400: Uncontrolled Resource Consumption**

## Platform(s) Affected:

Wordpress Core  <6.6
https://core.svn.wordpress.org/branches/6.6/

## Steps To Reproduce:

1. Ensure that `WP_ALLOW_REPAIR` is set to `true` in the `wp-config.php` file of the target WordPress installation.
   ```php
   define('WP_ALLOW_REPAIR', true);
   ```
2. Access the database repair endpoint directly by visiting the URL: `http://target-site.com/wp-admin/maint/repair.php`.
3. Note that the page allows access without authentication. Select either the "Repair Database" or "Repair and Optimize Database" button.
4. To exploit this vulnerability, repeatedly send GET requests to `http://target-site.com/wp-admin/maint/repair.php?repair=1` to trigger the database repair process.
   - You can use a simple bash script or a tool like `cURL` to automate the requests:
     ```bash
     while true; do curl -X GET "http://target-site.com/wp-admin/maint/repair.php?repair=1"; sleep 1; done
     ```
   - To be more practical, I have weaponized it with a simple python script that can bring the site down for as long as the attacker desires. The script is hosted at https://raw.githubusercontent.com/smaranchand/wreckair-db/refs/heads/main/wreckair-db.py?token=GHSAT0AAAAAACZBPSANBXQSCUVHV6JYC2LUZYQVXVQ

      Note: Let me know if it is not accessible.
5. Observe that the repeated requests will eventually exhaust server resources, causing the site to become unresponsive, results in a Denial of Service (DoS) condition, impacting the availability of the target WordPress site.

## Supporting Material/References:
{F3684807}

## Impact

The impact of this vulnerability is severe, as it allows an unauthenticated attacker to make the target WordPress site unresponsive through repeated use of the database repair functionality. This Denial of Service (DoS) condition disrupts the availability of the website, rendering it inaccessible to legitimate users. The lack of authentication and rate limiting on a critical function makes it easy for attackers to exploit, resulting in significant downtime, potential loss of business, and damage to the reputation of the affected website. Additionally, this vulnerability has been active for a long time, going unreported and unnoticed, making it a persistent threat to WordPress installations that enable the repair feature without proper security measures.

## Mitigations

To mitigate this vulnerability, the following actions are recommended:

1. **Require Authentication**: WordPress should require authentication for accessing the `/wp-admin/maint/repair.php` endpoint, even when `WP_ALLOW_REPAIR` is set to `true`. This would ensure that only authorized users can initiate database repair operations.

2. **Restrict Access**: Implement IP-based access control to limit access to the repair page only to trusted IP addresses. This would prevent unauthorized users from accessing the endpoint.

3. **Use a One-Time Token Mechanism**: Introduce a secure one-time token mechanism to allow temporary access to the repair page. This token should expire after a short period, reducing the risk of exploitation.

4. **Rate Limiting**: Apply rate limiting to the `/wp-admin/maint/repair.php` endpoint to restrict how frequently repair requests can be made. This will help mitigate the risk of resource exhaustion through repeated requests.

By implementing these mitigations, the risk associated with this vulnerability can be significantly reduced, ensuring that the database repair functionality is only used by authorized personnel and cannot be abused to create a DoS condition.

## Attachments
- Screen_Shot_2024-10-17_at_11.01.30_AM.png
