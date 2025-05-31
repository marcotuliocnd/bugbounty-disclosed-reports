# Friend Request Flow Exposes User Data 

## Report Details
- **Report ID**: 1245741
- **URL**: https://hackerone.com/reports/1245741
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-27T15:01:39.109Z
- **Disclosed**: 2022-01-12T10:25:58.416Z

## Reporter
- **Username**: yetanotherhacker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zenly

## Vulnerability Information
## Summary:
When submitting a friend request to a user, Zenly will allow access to their phone number regardless of whether the friend request is accepted or not. To obtain this information, a malicious actor only needs to know their username. 
## Steps To Reproduce:
To reproduce this issue, an environment that enables intercepting and decoding network requests is required. Once this environment is set up, we are able to gain visibility over network activity.
{F1355295}
The vulnerability makes use of the **“Add by Username”** flow, which starts by searching a known username.
{F1355316}
The interceptor that was previously set up can be used to view the requests that occurred during this search. Note that the “Add as Friend” button was never pressed, meaning a friend request was never sent.
███████
By observing the response of the request that was executed on the `/UserPublicFriends` endpoint, a list of friends can be seen, although it is not displayed on the UI of the application. This list contains every friend of the user, one of them is **Bogus_CEO** (bogus CEO of Zenly, for demonstration purposes). Note that the response also contains their username, which could in turn be used to repeat this process and obtain their friends' list instead.
Once we obtain the username of the target user, we can obtain their phone number through a flow that is almost identical. On the **“Add by Username”** view, we search for their username and complete the flow by tapping the **ADD AS FRIEND** button.
{F1355328}
This friend invitation will trigger a request to the `/FriendRequestCreate` endpoint, whose response contains specific information regarding both our user (items 3, 5, and 6 in the image below) and the target user (items 4, 7, and 8 in the image below).
████████
Note that the response contains both our phone number and the phone number of the target user, even though our friend request **was never accepted by the target user**.

## Impact

Exposure of user data can be used by attackers for malicious purposes. Obtaining this data can put at risk not only the users of the application but also Zenly’s brand image.
Consider a scenario where a malicious actor wants to attack a company by targeting its CEO. An attacker can make use of this vulnerability and employ the following attack vector:
1. Search the web for an employee of the company and try to obtain their social media handle e.g., Twitter. (Best targets are employees who work in communications or marketing fields since they are typically more exposed and represent easier targets)
2. Validate their handle is valid on Zenly.
3. Access their list of friends through Zenly, obtain the handle of the CEO.
4. Retrieve the phone number of the CEO through their username. <- This is already a privacy violation, but the scenario can go on...
5. Carry out a spear-phishing attack, using the phone number of the CEO.
An attacker can also repeat these steps to obtain the phone number of other employees and thus prepare a more credible attack.
Note that, according to the documentation provided by Zenly, present at [this link][1], it should not be possible to retrieve the phone number of a user unless we are already friends with them.
The following screenshot was obtained from this documentation:
{F1355287}

[1]: https://community.zen.ly/hc/en-us/articles/360001404288-View-or-call-my-Zenly-friend-s-phone-number

## Attachments
- Picture1.png
- Picture2.png
- Picture3.png
- Picture5.png
