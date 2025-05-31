# Verifying email bypass

## Report Details
- **Report ID**: 1121896
- **URL**: https://hackerone.com/reports/1121896
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-10T00:15:54.085Z
- **Disclosed**: 2023-03-03T18:27:43.741Z

## Reporter
- **Username**: fisjkars
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripe

## Vulnerability Information
During an assessment made on a separate web-application using theirs customers to use Stripe for their payments, I detected a different behavior between account created using the standard interface and the account created using the connect portal.

## Classic User creation.

Users can create their account using the classic interface on https://dashboard.stripe.com

![](./classicAccountCreation.png)

By analyzing the traffic, we can see that the user is created with a POST request made on https://dashboard.stripe.com/ajax/register.

![](./ClassicRegisterAccountRequest.png)

The new user can directly access to the dashboard without verify the email address entered in the creation form. However till the user has not verified the email, all features were limited to test data.

![](./LimitedAccountWithClassicCreation.png)
![](./LimitedAccountWithClassicCreation2.png)

These restrictions did not allowed to generate invoices or payments on behalf of **not verified mail** the mail entered during the creation process.

## Connect User creation.

Stripe API proposed some Oauth features described in this article (https://stripe.com/docs/connect/oauth-reference).

The workflow begin with this type of url : https://connect.stripe.com/oauth/authorize?response_type=code&client_id={{CLIENT_ID}}****

Once the user reached this page, he has two options :
 * Sign-in with an existing account.
 * Create a new account.

 The second option asked to the users several informations such as 

 * Personnal details (name, last name, adress)
 * Business details (website, activities, company adress etc)
 * Email adress
 * Bank details

 Second factor with SMS is required and verified for the account creation.

![](./CreateWithConnect.png)
![](./CreateWithConnect2.png)
![](./CreateWithConnect3.png)
![](./CreateWithConnect4.png)

Once all required informations has been filled and validated, the account is created using the API endpoint and the users is redirected to the client page with the access token generated.

![](./accountCreatedUsingApi.png)

By the way, by browsing the dashboard website, the user is connected with the new account.

## Vulnerabilty.

Instead of the user created with the standard interface, the account created with the API can access to all Stripe feature such as :

* Creating invoices and send them by email.
* Creating subscriptions.
* Managing customers.
* etc...

The main concern is the email adress is not verified at this moment, it means that an attacker can impersonate a real company by spoofing the emails address.

## Impact

In the POC scenario, I created the account superadmin@michelin.com for Michelin Group company. Even if I don't have access to this email, I was able to spoof invoices for Michelin. 

The invoices received by customers are valid because sent by Stripe and saying that superadmin@michelin.com generated the invoice.

![](./NotVerifiedAccountButActive.png)
![](./branding.png)
![](./InvoicesCreated.png)
![](./createinvoice2.png)
![](./invoiceReceived.png)

The generated invoice cannot be considered a spam as it was sent by Stripe...

To complete the report, I generated some little invoices to validate the payment and the payout to the attacker bank.

![](./balance.png)
![](./paymentsMade.png)

## Attachments
- classicAccountCreation.png
- ClassicRegisterAccountRequest.png
- LimitedAccountWithClassicCreation2.png
- LimitedAccountWithClassicCreation.png
- CreateWithConnect4.png
- CreateWithConnect.png
- CreateWithConnect2.png
- CreateWithConnect3.png
- accountCreatedUsingApi.png
- invoiceReceived.png
- InvoicesCreated.png
- NotVerifiedAccountButActive.png
- paymentsMade.png
- branding.png
- createinvoice2.png
