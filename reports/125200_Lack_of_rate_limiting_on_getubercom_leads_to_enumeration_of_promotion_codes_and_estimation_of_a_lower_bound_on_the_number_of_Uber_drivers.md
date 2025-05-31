# Lack of rate limiting on get.uber.com leads to enumeration of promotion codes and estimation of a lower bound on the number of Uber drivers

## Report Details
- **Report ID**: 125200
- **URL**: https://hackerone.com/reports/125200
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-23T01:41:53.615Z
- **Disclosed**: 2016-08-12T17:16:04.890Z

## Reporter
- **Username**: ddworken
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Invite codes are 5 alphanumeric (lower case) characters. This means there are 36 (26 + 10) possible options for each space in the invite code. In total this means there are 36^5 or 60,466,176 possible invite codes. Through enumerating through all possible invite codes, one can find the total number of Uber accounts and the first name associated with each of the uber accounts. 

When loading ```https://get.uber.com/invite/[Invite Code]```, one will see one of two possible messages. If you see only ```Create your account and get moving in minutes.``` then there is no account associated with that invite code. If you see ```Sign up now to claim your free gift from [First Name] ($15 off first ride)*.```, then there is an account associated with that invite code. 

For an example of each of the possible responses, see the two below links: 

`https://get.uber.com/invite/v1m8a`

`https://get.uber.com/invite/v1m8u`

A simple (but inefficient) way of exploiting this is with a simple python program like this (I have not tested the below code): 

``` python
import requests

characters = '0123456789abcdefghijklmnopqrstuvwxyz' # 

def isAccount(code):
    if "free gift from" in requests.get("https://get.uber.com/invite/"+code).content:
        return True
    return False

numAccounts = 0

for firstChar in characters:
    for secondChar in characters: 
        for thirdChar in characters:
            for fourthChar in characters:
                for fifthChar in characters:
                    if isAccount(firstChar + secondChar + thirdChar + fourthChar + fifthChar):
                        numAccounts += 1
```

Furthermore, one does not need to actually test all 60,466,176 invite codes. Since the invite codes are distributed randomly, one can simply test a subset of that and extrapolate. For example, if I test 1 million invite codes and find 3% are valid, then I know that approximately 3% of the 60,466,176 possible invite codes are valid (only an estimate). 

Thanks,
David Dworken

## Attachments
No attachments
