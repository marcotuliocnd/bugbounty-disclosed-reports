# Bypassing Access control, changing owner's name in a private leaderboard

## Report Details
- **Report ID**: 245340
- **URL**: https://hackerone.com/reports/245340
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-02T14:19:26.869Z
- **Disclosed**: 2017-07-31T21:24:02.631Z

## Reporter
- **Username**: tikoo_sahil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hello, 

I would like to mention a bug here that is regarding changing the name of the owner of a leaderboard by a member that is first shown forbidden but when you again try to change owner's name you can see the changes to name made in the pop up that appears.
Basically when I created a private leaderboard  named test1 on my account ███ then in the next step I sent invitation to ████ so as this email was also mine I accepted the request to join the leaderboard and then I visited the members section  of the leaderboard through my ████████ account (owner account)

There I saw an edit option for the name of the member of leaderboard test1 that was the member with email ███ , so before that I opened a new settings page and made the member with email ████ the owner and made my account role as member , see below 

{ ███████} 

Then on the editing page when i tried to edit the name of the user to testing  with email █████ which had now become the owner and I was a member so I got the below forbidden error 

{ ████████}

But when I clicked on edit button again I saw the pop up saying 'Enter new name for testing ' see below pic 

{ ████} 

So clearly I was able to bypass the access control set for the members of a leaderboard.
So please patch it .

Regards
Sahil tikoo

## Attachments
No attachments
