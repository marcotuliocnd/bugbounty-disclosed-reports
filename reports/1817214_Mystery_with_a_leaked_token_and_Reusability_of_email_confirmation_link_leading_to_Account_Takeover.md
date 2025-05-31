# Mystery with a leaked token and Reusability of email confirmation link leading to Account Takeover

## Report Details
- **Report ID**: 1817214
- **URL**: https://hackerone.com/reports/1817214
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-12-26T20:08:14.892Z
- **Disclosed**: 2023-02-03T14:41:14.518Z

## Reporter
- **Username**: gokulsk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sorare

## Vulnerability Information
Hi Team, 
First of all hope you are well and belated christmas wishes! Sorry for this long report. I need to write it long because many things happened during the testing and the report wont be complete if I didnt mention each and everything. During the test I end up modifying another user's profile. I'm sorry for that and I trust your safe harbor policy. 

If you dont want to read everything, please read the first part and must watch the Video POCs.

So here I'm with a mystery bug and I have a long story to tell. Please listen carefully. I was fed up not getting any bugs and was thinking to try my luck using google dorking. I tried many dorks and finally I came up with this one:

site:sorare.com inurl:token
=====================
{F2092332}

Here, as you can see there are two search results:

1. A random user's Email-confirmation link
2. A device confirmation link.
Both these links consists of tokens respective of the aim of these links. 

So, as I said earlier I was fed up and surfing without hope through these links. 
Now:
1. I opened up the second result which is of a confirm_device link with a token for a random user.
2. Initially the site said me the link is no longer valid and redirected to me to a settings option which asked me to upload profile picture.
3. Initially I thought that link was invalid and it got redirected me to my Sorare profile.
4. But it wasnt my profile.
5. The link brought me to a person named JACK3422's profile. Here I'd like to say thanks to Safe Harbor policy. Because I accidently changed the profile picture and some game settings the app asked me to do. Honestly I thought it is my profile.
=====================
6. So this leaked device confirmation link allowed me to get into a random person's profile.
7. Now I forgot to take a POC of this issue and was desparate. I logout from his profile and I tried to use that link again and it wasn't working again. :(
So I was about to quit. Before explaining further let me point out the steps worked here:

A. Google dorking using site:sorare.com inurl:token
B. Go to the second link, i.e; https://sorare.com/confirm_device?token=N04J3Zczv1GaFrniJisN1QgsisoJHQ
C. Click OK. It redirected me to that persons profile settings.

Unfortunately, the above link doesn't work anymore. So I decided to leave that sadly.
=====================

Then I opened the first link which is of a email confirmation link. You can guess its result. It was an expired confirmation link. But I have a behavior of trying IDOR everywhere even if it is a random encoded string.

Here  I'd like to mention the flow of Sorare sign up process:
A user enters email, username and password and on next step sorare sends a confirm email link to the entered email. Only if the mail is confirmed a user can sign in to his new account. 

On clicking email confirmation link after going to mail provider, the user directly enters into his/her account. i.e, this confirmation link signs in users and there is no need to enter credentials again.
=====================
Since there is no need to enter credentials again and a email confirmation link can sign in users, imagine if these links are leaked like our google dork results? Anyone can enter in to anyone's account using these email confirmation links right?So the best part is the email confirmation link can be only used once.  That's why when I opened that link it showed the profile is already verified. But what if an attacker can bypass this expired links and get into anyone's account without password? That's what the bug I observed here:
=====================
How I bypassed the confirm link I got using google dorks.

A. Google dork: site:sorare.com inurl:token
B. Open the first link which is an email confirmation link:(Remember to logout from your sorare account)

https://sorare.com/confirm_email?token=Jt7S7WS_4EphEyiDn6z_&redirectUrl=https%3A%2F%2Fsorare.com%2F

C. Now it will show like this: 
Errors: was already confirmed, please try signing in

D. So you may think "Oh, the link is not valid anymore, we should try some other bugs." NO!

Just observe this confirmation link:

Already used link: https://sorare.com/confirm_email?token=Jt7S7WS_4EphEyiDn6z_&redirectUrl=https%3A%2F%2Fsorare.com%2F  (Invalid)
=====================
 
Now here is a token parameter in this URL:

token=Jt7S7WS_4EphEyiDn6z_ (invalid token)
=====================

Now focus on the numbers in this token. So what to do to reuse this link is token is to concentrate on the numbers that stays freely and not in between the alphabets. I mean '4'. Because 4 is not in between those strings but it starts after an underscore. So chage this 4 to 6 or5.

Now the token manipulated to: 

token=Jt7S7WS_6EphEyiDn6z_  (Valid)
=====================

And the URL changes to: 

 https://sorare.com/confirm_email?token=Jt7S7WS_6EphEyiDn6z_&redirectUrl=https%3A%2F%2Fsorare.com%2F (Valid)
=====================


E. Do not open this link directly. You need to go through the above steps. Open the link in step B and modify 4 to 6 from the address bar as shown in video poc.
=====================

{F2092372}

F. So those two google dork results are of same person. Somehow it got leaked and anyone can use it now from Google. What happens if more people's confirmation links and device confirmation links are leaked like this?

Now to check if it is valid for all email confirmation link I created a new account and tested the confirmation link I got.

The link I got:

https://sorare.com/confirm_email?redirectUrl=https%3A%2F%2Fsorare.com%2F&token=qvQfgPqvWV-2FiM5k2f7(Invalid link)

Here I observed the token and changed the number 2(after hyphen) to 5 or something:

https://sorare.com/confirm_email?redirectUrl=https%3A%2F%2Fsorare.com%2F&token=qvQfgPqvWV-5FiM5k2f7

Bang! Got access to my account without password.

Again do not open this link directly. First open the invalid link and modify the url from address bar. Then only it works.

{F2092373}

So that's it.

## Impact

Even though the email confirmation links shows theyre expired they can be reused using this method. Since these links directly sign in users an attacker who got such a leaked link didnt want to know the password to sign in. So this is a highly dangerous bug. Leakage of these links can end up in account takeover easily. (As I did here using Google Dork)

## Attachments
- Screenshot_2022-12-27_00_15_22.png
- Accidental_takeover.mkv
- My_Sorare.mkv
