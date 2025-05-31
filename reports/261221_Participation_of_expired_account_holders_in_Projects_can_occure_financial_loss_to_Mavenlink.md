# Participation of expired account holders in Projects can occure financial loss to Mavenlink 

## Report Details
- **Report ID**: 261221
- **URL**: https://hackerone.com/reports/261221
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-18T00:03:13.820Z
- **Disclosed**: 2018-09-09T09:18:00.636Z

## Reporter
- **Username**: rashedhasan007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mavenlink

## Vulnerability Information
I think I have found a security issue . 

Summery:
---------------------
Inviting a person to Project who has an expired account can participate in project activity via email address , Which is against Mavenlink's business policy , As after an account has been expired after trial period they need to buy a plan to access all the features . 


Issue Background:
---------------------
As we know on signing up , Mavenlink Offers a Trial account of a limited period , where users can check out all the features and gets a basic understanding how Mavenlink works . However after the trial period is over for a free account , Upon logging in to the actors account he gets a message like this and it's not possible to access anything at all as this comes every time . 

F213824 

So , If user does not chooses a plan he actually can not access this account now , Trying to navigate to any section brings to 

```
https://app.mavenlink.com/settings/account/subscription?showPlansPricing=true
```

Where Mavenlink prompts user to select a plan to continue using the features of the application . However If someone creates a project and invites the expired account holder , he receives and email that he has been invited to the project . when he tries to open it he can not access this as I have mentioned the application lands to the same page and prompts to buy a plan . however if the expired account owner replies the email , a comment is placed at the project . particularly  when any post is made on the project timeline that expired account holder receives an email , and replying that email he can participate  in the conversation without any problem  . wheres if the expired account holder tries to access the project with direct link he can not and land on the same page again where he needs to choose a plan to move forward with Mavenlink . 

So , an actor can post comment/ participate in conversations  via email when he actually does not have access to that due to Mavenlink's business policy via the application . Which seems the actor is getting more access / privilege more than he should get , and that is why I belief this is a security issue . 

Proof Of Concept:
---------------------

- Create a project with your Mavenlink Account . 
- Invite the person whose account status is expired . 
-  Add him as a consultant
- He will receive an email which is associated to his Mavenlink account . 
- He will try to navigate for the link received via email to see the project . 
- The attempt would be unsuccessful due to Mavenlink's policy .
- As the application will not let the actor to access before he selects a paid plan . 
- Now create a post from your account 
- An email will go to that expired users address . 
- he replies the email 
- and comment gets posted on behalf of him . 
- But he actually cannot get access . 

How can it  affect Mavenlink :
---------------------
The user is getting the privilege to participate in a project what he could have after selecting a paid plan , he can make comments by simply replying the email he received , unethical actors may take advantage of this current behavior which will eventually affect Mavenlink financially . As the user can perform this action without selecting a paid plan . 

I am attaching a video demonstration . Hope you will investigate this and get back with an update , 

Sincerely  , 
Rashed 




## Attachments
- Screenshot_462.png
- mv_prive.webm
