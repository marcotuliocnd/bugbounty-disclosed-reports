# Internal loop going to infinite for cb.setTimeout(func, msecs) for broadcast app.

## Report Details
- **Report ID**: 388215
- **URL**: https://hackerone.com/reports/388215
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-07-29T10:19:58.129Z
- **Disclosed**: 2018-10-01T23:06:24.890Z

## Reporter
- **Username**: hackaccinocraft
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hi There, 

I am not sure about that this is vulnerability for @chaturbate or not but in my seeing i thought it can be vulnerable and attacker can use this vulnerability for exploitation on @chaturbate website with normal user so finally i decide to report. 

As i was just playing with ```Broadcast app``` and i found some of the script which provide from @chaturbate it's totally wrong because by modifying script malicious user can make nonsense on website with normal user. 

#Step of POC
>Step 1 : Go to https://chaturbate.com/apps/upload_app/?slot=0
>Step 2 : Make app and give all details as it is what they asked but in ```JavaScript code``` insert below code and lunch app. 
```
function callme() {
    cb.chatNotice("hello world");
    cb.setTimeout(callme, 10)
}
cb.setTimeout(callme, 10)
```
Now particular this code make infinite call in website and loop will also going to round infinite time which make lots of buffer on website + also make irritation to normal user who visit live broad cast. 

#POC video 
{F325793} 

#Prevention
If you allow to make auto call for loop code then please make validation on creating app like put minimum value which you put in token code like if we are making any app for token then website always give notification like put 1 token at list. 

Please let me know if you want more information then, 

Cheers, 
Ninjan

## Impact

>1) Attacker make infinite buffer on website. 
>2) Irritate normal users by broadcasting their self and running those kind of app.

## Attachments
- Video_20180729_201125.mp4
