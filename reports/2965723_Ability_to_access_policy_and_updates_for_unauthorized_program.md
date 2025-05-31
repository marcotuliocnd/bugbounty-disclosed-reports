# Ability to access policy and updates for unauthorized program

## Report Details
- **Report ID**: 2965723
- **URL**: https://hackerone.com/reports/2965723
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2025-01-30T01:27:16.344Z
- **Disclosed**: 2025-05-08T16:11:35.842Z

## Reporter
- **Username**: light3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
#Description:
In an organization with two programs, a user who is only part of one program can still access the policy and updates of the unauthorized program using an API key.  

## **Steps to Reproduce**  

1. In an organization with two programs, navigate to:  
   **[HackerOne Organization Settings](https://hackerone.com/organizations/askcmsakmdfksqa_demo/settings/users)**  
2. Add a new user.  

█████████  

3. Create a low-permission group for one of the two programs, as shown below:  

   ![Low Permissions Group](F4003557)  

4. As shown above, the user should only have access to **askcmsakmdfksqa_h1r**.  
5. Verify the low-permission account access:  

{F4003563}  
{F4003565}

6. Using the low-permission account, navigate to:  
 [HackerOne API Token Settings](https://hackerone.com/settings/api_token/edit)
7. Generate a **HackerOne API key**, then make the following request:  

   ```bash
   curl "https://api.hackerone.com/v1/hackers/programs/askcmsakmdfksqa_h1b/" \
     -X GET \
     -u "██████=" \
     -H 'Accept: application/json'
   ```  

8. The unauthorized user is able to retrieve the policy and updates of the restricted program:  

{F4003567} 

9. If changes or updates occur, they are also accessible:  

   {F4003570}

10. The user can retrieve these updates as well:  

{F4003571}

## Impact

The unauthorized user or have a low permissions can get access to restricted program policy and updates which is contains a sensitive data also the user is unauthorized

## Attachments
- Screenshot_2025-01-30_at_3.07.11_AM.png
- Screenshot_2025-01-30_at_3.09.42_AM.png
- Screenshot_2025-01-30_at_3.13.51_AM.png
- Screenshot_2025-01-30_at_3.16.50_AM.png
- Screenshot_2025-01-30_at_3.18.39_AM.png
- Screenshot_2025-01-30_at_3.20.10_AM.png
