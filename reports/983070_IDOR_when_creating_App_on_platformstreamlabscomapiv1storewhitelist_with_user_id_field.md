# IDOR when creating App on [platform.streamlabs.com/api/v1/store/whitelist] with user_id field

## Report Details
- **Report ID**: 983070
- **URL**: https://hackerone.com/reports/983070
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-16T00:34:56.010Z
- **Disclosed**: 2020-11-26T10:04:51.433Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: logitech

## Vulnerability Information
## Summary:
Hi team,
There is a IDOR when applying to platform.streamlabs.com after loginning.

If you login to platform.streamlabs.com and click `Create App`. You will see the "apply form". And if you submit it, you will see the `user_id` parameter in JSON data of the apply request. (api/v1/store/whitelist). This parameter is vulnerable for IDOR, you can apply to platform as another accounts.

Also these `user_id`s are sequential, so any attacker can apply this form with a lot of accounts with random values. Attacker can force the victims' apply forms to be rejected.
## Steps To Reproduce:

  1. Sign-up to platform.streamlabs.com with 2 different accounts (Make sure you didn't apply the apply form before.)
  1. Click `Create App` and turn on the proxy
  1. Fill in the form and click  `Apply`
  1. Change the `user_id` on the JSON data of the request to your another account's ID.
  1. Forward the request.

`user_id`'s are sequential, for finding your user_id you can go to https://platform.streamlabs.com/api/v1/s/user/me

If you see `200 OK` in response, that means you submitted the form as victim.

{F989441}

Now, the victim can't apply the form again. And if you fill the form with random values. Streamlabs will probably reject the victim's form because of random values.

## Impact

Any attacker can apply the platform form with a lot of accounts with random values. So attacker can force the victims' apply forms to be rejected.
I don't know the full impact because I didn't get response for my Platform request yet. Maybe there is more serious impact on this issue but I can't figure it out for now.

Thanks,
Bugra

## Attachments
- 200.PNG
