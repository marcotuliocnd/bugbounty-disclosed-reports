# ABLE TO TRICK THE VICTIM INTO USING A CRAFTED EMAIL ADDRESS FOR A PARTICULAR  SESSION AND THEN LATER TAKE BACK THE ACCOUNT 

## Report Details
- **Report ID**: 1357013
- **URL**: https://hackerone.com/reports/1357013
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-01T22:47:09.041Z
- **Disclosed**: 2022-01-05T05:15:51.283Z

## Reporter
- **Username**: at11zt00
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
Hi
I have found a vulnerability in your website using which i can trick the victim into using a specific email address to login in into the website and him thinking that he is using his own email address and continuing the session and then later we can take back the account and check what are the chats he made
UNDER SOME CIRCUMSTANCES

HOW TO REPRODUCE:-
scenarios - a team admin sends you and the victim a joining link to his team.
it looks like this:-
https://hackerone.cloud.mattermost.com/signup_user_complete/?d={"display_name":"\u003ch1\u003ea","email":"██████████","name":"main"}&t=cqtkyznxn8e43yagt9fjcsrc4nh6yoqq914in3zg4ykj1jkjbc9bippckjikj4cw

now we can see that there is an Email value and a token value. here the email value doesn't matter because even if we change it .  you will be login as the 
email to which the link was send. the token is assigned according to a particular email value
but interesting thing happens when we remove the email value and keep it blank (REFER TO THIS EMAIL)

https://hackerone.cloud.mattermost.com/signup_user_complete/?d={"display_name":"\u003ch1\u003ea","email":"","name":"main"}&t=cqtkyznxn8e43yagt9fjcsrc4nh6yoqq914in3zg4ykj1jkjbc9bippckjikj4cw

IF we go to the first link it asks us for name and password
BUT if we go to the second link it ask's for username password and email(HERE things get interesting)
even if we give a different email address to it . you will be signed as the attacker email id and the you can continue the session thinking that its your own email id you are using

## Impact

the attacker can use his own invite link and then remove the email value from it and send it to the victim. when the victim clicks he sees 3 fields he give his own email id password and username and continue the session when done he log's out then the attacker can use forget password to take back his account and look through all of his private messages

STEPS TO REPRODUCE :-
1. go to the first link you will be asked for username and password(DON'T SUBMIT JUST SEE THE CONTENTS)
2.go to the second link you will be also asked for email(ENTER ALL THE VALUES )
3.now if you check the email address it will be different from the original email address (you are using a forged email id) of the attacker

NOW I HAVE RATED IT HIGH BECAUSE USING THIS WE CAN  SEE ALL THE CONVERSATION'S HE DID FOR A PARTICULAR SESSION
I WILL ATTACH THE POC BELOW

## Attachments
- value_not_set_to_email_field.png
