# Able to see location coordinates in any event without permission to do so

## Report Details
- **Report ID**: 2610467
- **URL**: https://hackerone.com/reports/2610467
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-07-18T14:54:40.939Z
- **Disclosed**: 2024-09-25T10:59:43.344Z

## Reporter
- **Username**: ezzra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fetlife

## Vulnerability Information
Hi Fetlife team!

You can see the **location coordinates** in endpoint ``https://fetlife.com/events/{event-id}`` **response** even though the host event has blocked non-RSVP users (users don't attend the event) from seeing the exact address.

If the event host does not hide the address via privacy setting or the attacker has already attended the event, there's a Google Map link on the right event detail tab.

{F3448703}

If you check the coordinates from Google Map link, you will see that it is approximately the same as the coordinates you see in the response.

The coordinates in the response are reversed, so when entering them on Google Map you need to reverse them. 

``131.04425, -12.496252 -> -12.496252, 131.04425``

{F3448636}

Attack condition/Limitation:
=====================
Attackers are not being banned from the event.

Step to Reproduce:
=====================
1. Open Burp and proxy all HTTP requests.
2. Prepare 2 accounts. In this case, I use my 2 accounts: Ezzra1 (attacker), Ezzra2 (victim).
3. Victim creates event and goes to the privacy setting, ticks the box ``Address & Name of Location`` and clicks ``Update Event Privacy`` to hide the exact address.
4. Attacker goes to the event ``https://fetlife.com/events/{event-id}`` 
5. Check HTTP history. You will see the **Request** ``GET /events/{event-id}``
6. In **Response** tab, type in the search box **location** and now you can see the location coordinates.

## Impact

Attackers can see/guess the exact location of the event.

## Attachments
- PoC.png
- google-map.png
