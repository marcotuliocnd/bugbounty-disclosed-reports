# chainning bugs to get full disclosure of Users addresses 

## Report Details
- **Report ID**: 1398905
- **URL**: https://hackerone.com/reports/1398905
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-12T15:07:35.256Z
- **Disclosed**: 2021-11-16T08:57:37.498Z

## Reporter
- **Username**: spaceboy20
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glovo

## Vulnerability Information
Summary:
I was able to disclose any address that was used by the customers. 
The only barrier that came across that I need to put my visa on. 
On seeing that I managed to bypass it .
just after bypassing that, my order was accepted and the price was set to free So i don't know actually if there is an order that will be sent on that address.
I got a confirmation mail from the website confirming that my order was accepted and included an address which belongs to other user ! :D 


## Steps To Reproduce:


  1. Go to  https://glovostore.com/ and log in
  2. Select any product then proceed in putting an address.
  3. proceed to check out and capture that request using burpsuite as screenshot_1
 4. We will find that the address that belongs to me has a number in the parameter "customerAddress" and that  parameter is exploitable as i can change that number which results that i can reach other users' addresses. * we will know how after a minute *
  5. We now can send a post request now that contain our modified customer address.
 6. we will see that  we received a payment link that will eventually make it horrible for me if i want to see all useres' addresses. however, that's a way in getting the addresses. after payment we will find an email sent to us on our email which will contain an address to an existing user.
  7.  If we want to make that attack more easy and harmful, we return to the burp to the request we captured earlier.
8. We will find "products" parameter that consists of an array,  we will set the "qt" value = -1 
9. Now we send the request to find that our order now has no cost !! + a confirmation mail was sent to me that contains the address.
10. finally, we can send that request to intruder and add a list of numbers  as payloads to get as much addresses as we can as demonstrated on Screenshot_2

Supporting Material/References:
CustomerAddresses  to test  [3038813,3038817,3038821]

Screenshot_3 shows a sample of the address sent to the email.

Please note: I don't know if i have to submit multiable bugs as bypassing the paying site leads to flooding team responseable for accepting the orders with false positives which is an issue. and the information disclosure is a different bug.

## Impact

1. Disclose addresses of glovostore users
2. bypass the paying Site that leads to accepted orders without charge

## Attachments
- Screenshot_1.png
- Screenshot_2.png
- Screenshot_3.png
