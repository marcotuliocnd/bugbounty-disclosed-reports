# Manipulate Uneditable Messages in Support

## Report Details
- **Report ID**: 995969
- **URL**: https://hackerone.com/reports/995969
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-01T15:37:47.558Z
- **Disclosed**: 2020-10-27T19:28:43.629Z

## Reporter
- **Username**: ahmd_halabi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
Hello,

The support section has a validation on all the posted messages where it doesn't allow you to edit your messages after some minutes from posting them.
I was able to bypass this protection and edit successfully the previous messages that can't be edited.

After further investigation, I found that whenever you create/send a message, there is a date value made of numbers generated in the response which indicates the timestamp or the date that the message was created.
And when you edit that message, the same value is used as a date parameter in the edit request.

The bug is that the date parameter is still active for the unedited messages, so when you perform an editable request having the old unedited message's date value as a date parameter, the request will be successful and the new edit text will be successfully applied.

## Steps To Reproduce:
1. So first you need to identify the message initial date, send a message in the support section, intercept its request and see the response containing the target date.

```
█████████
Host: support.cs.money

{"user_steamid":"id-number","text":"test","settings":{"skin_exterior":0,"eco":0,"unavailable":1,"hints_in_trade":1,"lock_skin":0,"popup_skin":1,"reserved_skin":1,"save_filter":0,"virtual_trade":0,"skins_ticker":1,"beautiful_pics":1,"skins_float":0,"rarity":0,"collection":0,"conveyor":1,"block_red_points":0,"sourcePay":"scrill"},"bot_mode":"trade","user_mode":"trade"}
```

██████

'2. Say that you no longer are able to edit the above message created by you. So now create another message. Click edit, send the message and intercept its request.
'3. Add the date value from the step 1 response in the `date` value, and add the new message content in the `new_message` value.

```
███████
Host: support.cs.money

{"date":"date-value","new_message":"Hackerone edited message changed successfully === bug"}
```

'4. Forward the request and see the response code id 200 OK, Reload the page and see that the message is edited successfully.

## Supporting Material/References:
Please see the video below where I explained the bug step-by-step.

█████

## Impact

Users are able to edit their old messages that are not supposed to be editable anymore. This can lead to serious issues because they are being edited on the server too.
Also this is a bypass for the application validation and violation of its protection.
I think this can lead to serious problems if malicious users edit the messages to bad or harmful content.

Best Regards.

## Attachments
No attachments
