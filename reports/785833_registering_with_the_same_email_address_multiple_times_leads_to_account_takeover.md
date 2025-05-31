# registering with the same email address multiple times leads to account takeover 

## Report Details
- **Report ID**: 785833
- **URL**: https://hackerone.com/reports/785833
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-29T21:59:34.917Z
- **Disclosed**: 2022-03-14T21:13:24.623Z

## Reporter
- **Username**: whitehacker18
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
##i'm not sure if this issue is in scope or not or if it's intended , kindly if you don't accept this issue please close it as informative , thanks in advance

## Summary:
the ability of the user to register many times using the same mail address can lead to account take over 

## Steps To Reproduce:

  1. attacker goes to https://www.reddit.com/register/?dest=https%3A%2F%2Fwww.reddit.com%2F and signup by email for ex account@gmail.com and username attacker1 
  2. attacker goes to his email and verify it 
  3. attacker logs out 
  4. user goes to https://www.reddit.com/register/?dest=https%3A%2F%2Fwww.reddit.com%2F and signup by email for ex account@gmail.com and username user1
  5. attacker goes to his email and verify it 
  6.  user logs out 
  now since registering an account via the same email multiple times , the attacker can do the following 
  7.  go to https://www.reddit.com/username and type your email then click submit 
  8. all list of usernames registered on the attacker email will be sent to his mail 
  9. attacker gets the username of the victim user <user1>
 10. attacker request password reset on the victim by entering his name <user1> and the attacker email <account@gmail.com> by going to https://www.reddit.com/password
 11. the password of the victim is sent to the attacker email 
 12. the attacker takeovers the victim account by changing his password via reset link

## Supporting Material/References:
https://hackerone.com/reports/767829

 
##if you need any help please tell me , if you need any extra info or a video as a poc please tell me and i'll provide it 

##fix:
allow the user to register using the email only once.

## Impact

acoount takeover , disclosing of private info and chats 

if a user registers with an attacker email without knowing (as the application allows multiple registration email) then the attacker can takeover any account

## Attachments
No attachments
