# Stealing data from customers.gitlab.com without user interaction

## Report Details
- **Report ID**: 674195
- **URL**: https://hackerone.com/reports/674195
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-15T00:14:09.831Z
- **Disclosed**: 2020-08-26T14:02:00.620Z

## Reporter
- **Username**: rpadovani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

An attacker can link her own customers.gitlab.com account to the one of the victim, and these give access to 3 different vulnerabilities:
- destroying subscriptions of the victim
- buying new subscriptions using victim credit card for its own groups
- some (minor) information disclosure about what is over Gitlab.com

### Steps to reproduce

The attacker registers herself on customers.gitlab.com, logging in using her Gitlab.com account. 
After that, she updates her customers.gitlab.com account and link it to the victim's Gitlab account through the victim's account userId (they are sequential and they are not secret, so no problem retrieving it).

This update is quite easy, attacker needs only to copy how "Update Account" HTTP request, and change the `customer%5Buid%5D` field, like this:

```
await fetch("https://customers.gitlab.com/customers", {
    "credentials": "include",
    "referrer": "https://customers.gitlab.com/customers/edit",
    "body": "utf8=%E2%9C%93&_method=patch&authenticity_token=YOquJGc9evhkHMfLOZljuw9OcDn0gtJw8AHPb0yVhyml9q1TISGHa%2FK57DAlg8jB%2BEqvJYYob26BRgx4sZbRzg%3D%3D&customer%5Bfirst_name%5D=Riccardo&customer%5Blast_name%5D=Padovani&customer%5Baddress_1%5D=&customer%5Baddress_2%5D=&customer%5Bcity%5D=Munich&customer%5Bzip_code%5D=81479&customer%5Bcountry%5D=DEU&customer%5Bstate%5D=BY&customer%5Bvat_code%5D=&customer%5Bcompany%5D=Riccardo+Padovani&customer%5Bemail%5D=hackerone1%40rpadovani.com&customer%5Bprovider%5D=gitlab&customer%5Buid%5D=VICTIM_ID",
    "method": "POST",
    "mode": "cors"
});
```

The backend will validate the input, and now the two accounts are somehow linked.

### Impact

- When the victim will login again, all his subscriptions will be lost
- If the victim updates his data after the attack, the attacker account will be updated with the same data, INCLUDING CREDIT CARD. The attacker can now purchase plans using victim's credit card
- Attacker has also a list of teams victim is owner, when she purchases a new plan.

If attacker wants to purchase a plan for her own group, she can nominate victim owner, so now attacker's group will be in the dropdown, buy the plan, remove the victim.

### Examples

I attached a video with all these attacks, sorry but it is a bit messy.
On the left there is victim's browser, on the right attacker's browser. When it appears a console, is for the attacker's browser. The attacker's is in a private session, so it is completely separated from the victim.

0:00-0:10: we see victim has a subscription, and attacker no. They also have different data
0:10-0:40: attacker does a first attack, changing both uid and email, and it doesn't work
0:40-1:10: attacker does a proper attack, changing only uid. Notice how bottom right the Gitlab.com account changes
1:10-1:30: nothing else has changed
1:30-1:50: victim does log out and login again and ALL DATA AND SUBSCRIPTIONS ARE GONE

You can skip to
2:30-2:40: victim updates his data, also attacker's data are updated accordingly
2:40-4:30: victim buys a new subscription 
4:30-5:00: attackers can use victim's credit card

### What is the current *bug* behavior?

customers.gitlab.com user can update its link to Gitlab.com without any verification

### End notes:

I'd like you also reset my customers.gitlab.com accounts, now they are all a bit a mess.

Also, while testing I think I associated my customers.gitlab.com account with Gitlab's account with UID 1 due an error in copy-paste. I removed immediately the link, but maybe you should check if the link is indeed being delete, and say sorry on my behalf to Sid!

I noticed that in the video it appears my CC data - so please do not disclose the issue, also on the Gitlab.com issue tracker, without removing the video first, please!

## Impact

Attackers can steal victim's data, including last 4 numbers of CC, and use victim's CC to buy subscriptions

## Attachments
No attachments
