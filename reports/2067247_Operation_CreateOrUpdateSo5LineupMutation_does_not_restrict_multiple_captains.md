# Operation CreateOrUpdateSo5LineupMutation does not restrict multiple captains

## Report Details
- **Report ID**: 2067247
- **URL**: https://hackerone.com/reports/2067247
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-12T17:33:40.976Z
- **Disclosed**: 2023-08-01T15:41:17.293Z

## Reporter
- **Username**: fixenet
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sorare

## Vulnerability Information
## Summary:
By tampering with the POST request to the endpoint CreateOrUpdateSo5LineupMutation while editing a team you can change all football players to have the captain attribute to 'true'.  This goes against the UI enforced logic of having only one captain per team, as this attribute gives the football player a 50% score bonus disrupting game logic. 

## Steps To Reproduce:
  1. Go to https://sorare.com/football
  2. Edit a team you own.
  3. Press "Confirm" button.
  4. Intercept the request made to /federation/graphql with the "operationName":"CreateOrUpdateSo5LineupMutation"
{F2493465}
  5. Change all the players attribute "captain":true

## Result:
Confirmed team of all captains:
{F2493464}

## Impact

An attacker could get an unfair advantage vs other users that are following the expected game logic, since the API does not check for multiple captains.

## Attachments
- fullCaptain.png
- request.png
