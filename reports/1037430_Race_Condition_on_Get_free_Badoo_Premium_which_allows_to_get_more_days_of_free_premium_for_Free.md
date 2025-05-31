# Race Condition on "Get free Badoo Premium" which allows to get more days of free premium for Free. 

## Report Details
- **Report ID**: 1037430
- **URL**: https://hackerone.com/reports/1037430
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-11-18T10:21:16.116Z
- **Disclosed**: 2020-12-07T17:36:23.599Z

## Reporter
- **Username**: th4nu_0x0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
##Summary: 
On Badoo when a user wants to delete his account it prompts for a Free 3 days premium or the user can proceed to delete his account. But when user choose to get free 3 day premium he can click `Get free Badoo Premium` and can enjoy free premium for three days, Here i found a race condition vulnerability through which i was able to get more than three days of premium. 

On the time of testing I  got  3 successful request  which got me 9 days of premium instead of  3 (where 1 week of premium costs about 5$) . And by increasing Number of connections an attacker can get even more days of premium. 
█████

## POC Video: 
█████████

##Steps To Reproduce: 
  1. Create a account on badoo.com 
  2. Go to  badoo.com/settings and click `Delete account` which is available on bottom > Delete your account > I’m looking for something different > I don't want to pay, After these steps you'll see this prompt. 
        ██████████

  3. Before clicking `Get free Badoo Premium` turn intercept On in your burp suite and then click `Get free Badoo Premium` intercept this `POST /webapi.phtml?SERVER_PROMO_ACCEPTED ` select any parameter value > right click > send it to turbo inturer. 
  4. Copy this script from this link https://raw.githubusercontent.com/PortSwigger/turbo-intruder/master/resources/examples/race.py and paste it in code section of turbo intruder and click attack and  after completion you'll see more than 1 sucessfull responses .

After seeing 3 successful █████ requests i conformed from the settings that it was successful where it showed `it will stop on 27 November 2020` 9 days from today `18 November`
████████

##Vulnerable HTTP Request: 
```
POST /webapi.phtml?SERVER_PROMO_ACCEPTED HTTP/1.1
Host: eu1.badoo.com
Connection: close
Content-Length: 190
X-Session-id: s1:77:████
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
X-Message-type: 402
X-User-id: █████████
Content-Type: json
Accept: */*
Origin: https://eu1.badoo.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://eu1.badoo.com/settings
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie:  {cookie here}

{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":402,"p_string":{"value":"delete_account_trial_spp_new_flow"}}],"message_id":101,"message_type":402,"version":1,"is_background":false}
```

##Supporting Material/References:
- https://pandaonair.com/2020/06/11/race-conditions-exploring-the-possibilities.html

## Impact

- As an attacker i can get Free premium access for more days without paying any money.

## Attachments
No attachments
