# Response Manipulation lead to bypass verification code while making appointment at `█████████`

## Report Details
- **Report ID**: 1943252
- **URL**: https://hackerone.com/reports/1943252
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-12T06:46:56.679Z
- **Disclosed**: 2023-08-30T15:46:47.850Z

## Reporter
- **Username**: mo3giza
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mars

## Vulnerability Information
## Steps To Reproduce:

1. Go to this URL ███
2. Make an appointment
3. Choose send verification code to email
4. Enter random code 
5. Intercept the request using burp
4. Click do intercept response and forward
5. Change false to true

## Impact

bypass verification code

## Attachments
No attachments
