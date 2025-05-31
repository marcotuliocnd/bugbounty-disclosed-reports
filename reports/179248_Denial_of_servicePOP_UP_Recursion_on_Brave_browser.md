# Denial of service(POP UP Recursion) on Brave browser

## Report Details
- **Report ID**: 179248
- **URL**: https://hackerone.com/reports/179248
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-11-01T00:19:57.268Z
- **Disclosed**: 2016-11-07T07:00:53.060Z

## Reporter
- **Username**: sahiltikoo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information


## Summary:

Basically I have found a denial of service attack on brave browser in Linux platform.In this bug when we open the __html file or visiting (www.tiks.host-ed.me)__ then click on __pop up dos.html__ ,(which contains a recurring pop up code),the Pop up freezes the entire browser window except for minimize button  and on maximizing it hangs, we can't close any tabs neither using (Ctrl+w) to close current tab that is causing recursion. This is a known issue and in past has been already addressed in browsers such as _Google Chrome_, however Brave Browser is still affected by the issue.And in _safari browser_ Pop up's come after some time delays that allows user to stop the running process by clicking on (X) in URL.

##Attack Scenario :-

This can be exploited by an attacker just by sending this __html file or visiting (www.tiks.host-ed.me)__ to victim through email or any other source and when victim will open the html file in his/her Brave browser their window will freeze and they would need to kill the process in Linux(kill -9 pid) or (End Task) in windows. So to avoid such misuse of the issue some patches must be made. 

>The vulnerability occurred due to mishandling of location.reload function, as it keeps reloading the >document, however the issue more likely is present inside of not limiting the pop ups or simply offering no >way to ignore further prompts. 


## Products affected:
 
_Brave browser(0.11.6) on Linux platform_

## Steps To Reproduce:

1.) Got o www.tiks.host-ed.me then click on __pop up dos.html__ file or You can open the html code i have attached below on brave browser.
2.) You will see pop up like :-

{F131446}

And while in Google chrome this effect is limited by offering a checkbox to prevent the current document from creating additional dialogs. Like as shown below :-

{F131451}





## Supporting Material/References:

I have attached POC images and html code that you will require in resolving the above issue.

Thanks
sahiltikoo


## Attachments
- pop_up(dos).png
- pop_up_dos.html
- google.png
