# Exfiltrating a victim's exact location (to within 5m)

## Report Details
- **Report ID**: 1234406
- **URL**: https://hackerone.com/reports/1234406
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-06-15T08:44:18.137Z
- **Disclosed**: 2021-07-21T18:41:34.974Z

## Reporter
- **Username**: robertheaton
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
I used Bumble's distance feature to exfiltrate the exact location (to within approx 5m) of a victim. I did this by using the Bumble API to move my attacker account's location around the approximate area of the victim. I was able to obtain the exact distance between attacker and victim at 3 separate locations, and I then used trilateration (https://gis.stackexchange.com/questions/17344/differences-between-triangulation-and-trilateration) to combine these 3 distances into a single, precise location.

This is not a new vulnerability; Tinder was found to be vulnerable to a version of it in 2014 (https://blog.includesecurity.com/2014/02/how-i-was-able-to-track-the-location-of-any-tinder-user/). What is new is the circumvention of Bumble's attempted mitigations for the Tinder attack. Tinder was trivially vulnerable to trilateration because their API returned the exact distance between attacker and victim, to 15 decimal places, and the client was responsible for rounding it. Bumble attempts to mitigate this by rounding the distance on the server, and returning only this rounded distance to the client. Simple trilateration is still possible using these rounded values, but this only gives us an accuracy of the nearest square mile or so.

However, we can massively increase the precision to the nearest few metres by hypothesising that Bumble performs server-side rounding using code like the following:

```
def calculate_rounded_distance():
  exact_distance = calculate_exact_distance()
  rounded_distance = math.floor(exact_distance)
  return rounded_distance
```

This means that we can have our attacker slowly "shuffle" around the vicinity of the victim, looking for the precise location where a victim's distance from us flips from (say) 1.0 miles to 2.0 miles. We can infer that this is the point at which the victim is exactly 1.0 miles from the attacker. We can find 3 such "flipping points" (to within arbitrary precision, say 0.001 miles), and use them to perform trilateration as before.

To reproduce:

1. Create 2 accounts - a victim and an attacker. I don't believe that they need to be made to match with each other in order to exploit this vulnerability.
2. Use Burp Suite or similar to grab the victim and attacker session IDs so that we can control them programatically via the Bumble API
3. Use the Bumble API to put the victim in a fixed, target location
4. Put the attacker in a random location in the vicinity of the victim. The attack does not require any special knowledge of the victim's location beyond the summary shown in the UI (eg. "Lambeth")
5. Step the attacker in a random direction in small increments (smaller increments take longer but give more precise locations). After each step, check the distance between attacker and victim. If it has changed, record the average of the current and previous location as being exactly the smaller of the 2 distances away from the victim.
6. If desired, repeat step 5 with a smaller step size in the vicinity of the known distance flip in order to increase precision
7. Repeat steps 4-6 3 times starting in different positions
8. Draw 3 circles, 1 for each distance found. The radius should be the distance between victim and attacker, the centre should be the point at which the distance flipped. (KML viewed in Google Earth is convenient for this step)
9. Confirm that all 3 circles cross at the same point - you should have been able to identify the victim's location to within approx 5m

I've included a Python POC with this report, and a screenshot of trilateration results produced using this script where the victim is placed at 10 Downing Street, UK. Depending on precision desired it takes approximately 10 seconds to find a victim's location.

## Impact

The Bumble API does not appear to restrict the users about whom an attacker can pull information. This means that an attacker could use this vulnerability to find the exact location of any user whose user ID they know. This includes:

* Current matches
* Past matches who have since broken up with them
* Any user whose profile the attacker has been shown in an encounter

The only restriction I've found is that sometimes the API does not return the numerical distance between the attacker and victim. I speculate that this occurs when the victim hasn't checked in for a period of time.

To mass exfiltrate the locations of a large swathe of Bumble users, an attacker could use multiple accounts with wide filters to cycle through large numbers of encounters, collecting large numbers of user IDs and then using trilateration to find all of their locations.

Revealing the exact location of Bumble users presents a grave danger to their safety, so I have filed this report with a severity of "High".

## Attachments
No attachments
