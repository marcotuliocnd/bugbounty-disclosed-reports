# Netlify Authentication Token Exposed in Public Mozilla CI Logs

## Report Details
- **Report ID**: 2915647
- **URL**: https://hackerone.com/reports/2915647
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-12-27T21:52:44.033Z
- **Disclosed**: 2025-05-13T09:35:01.798Z

## Reporter
- **Username**: samirsec0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
A critical vulnerability was discovered involving the exposure of a Netlify authentication token within publicly accessible logs. This token provided full access to the `Mozilla IT Web SRE` Netlify account, bypassing all restrictions. The token’s permissions encompassed roles such as Owner, Developer, Billing Admin, Reviewer, Publisher, and Content Editor, granting complete control over site management, deployments, billing, and content configurations. This exposed API key posed significant security risks, enabling unauthorized users to manipulate the account and its associated assets freely.

---

### **Key Information:**
- **Exposed Token:** `███`
- **Source of Exposure:**
  - **Public URL:** [Mozilla CI Logs](https://firefox-ci-tc.services.mozilla.com/tasks/d5NRF8FdQamV9XdPO_mTBQ/runs/0/logs/public/logs/live.log)
  - **File:** `live.log`
- **API Used for Verification:** [Netlify API Documentation](https://open-api.netlify.com/)
- **Website at Risk:** `https://crash-pings.mozilla.org`
- **Account at Risk:** `Mozilla IT Web SRE`

---

### **Steps to Reproduce:**

1. **Access Public Log:**
   - Open the following URL in a browser: [Mozilla CI Logs](https://firefox-ci-tc.services.mozilla.com/tasks/d5NRF8FdQamV9XdPO_mTBQ/runs/0/logs/public/logs/live.log).

2. **Locate the Exposed Token:**
   - Search for the keyword `auth:` in the log file.
   - Extract the Netlify token (e.g., `███`).

3. **Verify Token Validity:**
   - Use the token to query the Netlify API. For example:

```bash
curl -X GET https://api.netlify.com/api/v1/accounts -H "Authorization: Bearer ████" -s | jq
```

   - Observe the response containing sensitive information about the Netlify account's sites.

```json
[
  {
    "name": "Mozilla IT Web SRE",
    "slug": "mozilla-it",
    "role": "Developer",
    ...
    ...
    "selected_access_site_ids": [
      "5a05c659-aa54-4184-bdbe-7faa4dd497b5"
    ],
    "billing_name": "it-sre",
    "billing_email": "it-sre@mozilla.com",
    "billing_details": null,
    ...
    ...
    "roles_allowed": [
      "Owner",
      "Developer",
      "Billing Admin",
      "Reviewer",
      "Publisher",
      "Content Editor"
    ],
    "created_at": "2019-06-26T13:57:19.242Z",
    "updated_at": "2024-07-08T18:56:21.541Z",
    "has_site_password": false,
    "site_sso_login": false,
    "site_sso_login_context": "all",
    "site_jwt_secret": null,
    "saml_config": {
      "idp_entity_id": "urn:auth.mozilla.auth0.com",
      "idp_sso_target_url": "https://auth.mozilla.auth0.com/samlp/hj3jYIhcrgvPWTpnFoHWLPx57t6KKqhA",
      "idp_slo_target_url": "https://auth.mozilla.auth0.com/samlp/hj3jYIhcrgvPWTpnFoHWLPx57t6KKqhA/logout",
      "idp_cert_fingerprint": "2F:C4:72:FC:FE:1C:69:A6:6E:8B:A7:FA:72:AA:3D:08:B0:A0:6A:F8"
    },
    "saml_session_expiration": 604800,
    "deploy_notifications_per_repo": true,
    "payments_gateway_name": "zuora_production",
    "lifecycle_state": "active",
    "lifecycle_state_reason": null,
    "weeks_past_due": null,
    "days_until_disabled": null,
    "current_billing_period_start": "2024-12-26T00:00:00.000-08:00",
    "next_billing_period_start": "2025-01-26T00:00:00.000-08:00",
    "current_usage_period_start": "2024-12-01T00:00:00.000-08:00",
    "next_usage_period_start": "2025-01-01T00:00:00.000-08:00",
    ...
    ...
    "type_name": "Enterprise",
    "type_id": "58f792a3d6865d698b6879bd",
    "type_slug": "enterprise",
    "monthly_seats_addon_dollar_price": "0.0",
    "owner_ids": [
      "60be48126deb9594c56ad4a0",
      "60c285a4fa8ef00f41b7a171",
      "60eda0538f4cf6540569b4b5",
      "62548540b51a811561330ed7",
      "62c5e063fe09d502f8dc2519",
      "62f22a000c27a1187e2be65b",
      "62ffe60780a012285fb7d36f",
      "63b429858592e6679549e622",
      "650deaef51dc692b41f8b3f2",
      "658210e2646ba26e2d050ff4"
    ],
    "saml_enabled": true,
    "org_saml_enabled": false,
    "org_mfa_enabled": false,
    "default": false,
    "cancellable": false,
    "has_builds": true,
    "enforce_saml": "enforced_strict",
    "team_logo_url": null,
    "can_start_pro_trial": false,
    "on_pro_trial": false,
    "can_start_enterprise_trial": false,
    "on_enterprise_trial": false,
    "security_contacts": [],
    "gitlab_self_hosted_config": null,
    "github_enterprise_config": null,
    "bitbucket_self_hosted_config": null
  }
]
```

4. **Confirm Full Access:**
   - Perform other API requests, such as deploying, deleting, or modifying sites.
   - For example, access sensitive logs, environment variables, or site configurations.
   - You can test all endpoints in Netlify api docs: https://open-api.netlify.com

---

## **Proof of Concept (PoC):**
I have created a POC video:
███

---

### **Recommendations:**

1. **Revoke the Token:**
   - Revoke the exposed token immediately and notify all affected stakeholders.

2. **Audit Logging Practices:**
   - Review all CI/CD pipelines to ensure sensitive data (e.g., authentication tokens) are masked.

3. **Enhance Token Security:**
   - Implement OAuth scopes or IP whitelisting to restrict token usage.
   - Monitor for suspicious API usage to detect possible exploitation.

---

## **Thank You!**
I appreciate the opportunity to report this critical issue and assist in securing your systems.

---

## Impact

The leaked authentication token provides **full access** to the Netlify account, leading to the following risks:

	1.	**Financial Theft:**
	-	Change the `billing_email` to divert all payouts to an attacker-controlled account.
	2.	**Site Compromise:**
	-	Modify, delete, or deploy malicious content on the associated site (https://crash-pings.mozilla.org).
	3.	**Data Exposure:**
	-	Access environment variables, logs, and other sensitive configuration data.
	4.	**Reputation Damage:**
	-	Use the compromised account to host malicious content or phishing attacks.
	5.	**Permanent Loss of Control:**
	-	Delete all sites and configurations, causing irreversible damage.

## Attachments
No attachments
