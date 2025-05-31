# Brute-Forcing invite codes  in partners.uber.com 

## Report Details
- **Report ID**: 144616
- **URL**: https://hackerone.com/reports/144616
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-14T02:21:34.661Z
- **Disclosed**: 2016-07-26T00:47:09.173Z

## Reporter
- **Username**: mefkan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi,

//We are going to use this link : https://partners.uber.com/join/?invite_code=xxxxx with GET method.

There are  options to customize codes,

We can do it with only numbers 
https://partners.uber.com/join/?invite_code=1 to 10000

Or we can use some words with numbers
https://partners.uber.com/join/?invite_code=uber1 to uber10000

If the source code of  page matches with  <p class="delta flush">  that means the invite code exists.Or you can use other working matches.I used the <p class="delta flush"> in the examples.

So we can brute-force.There are no limits for tries.No captchas no errors

Example links that includes money :

https://partners.uber.com/join/?invite_code=547kkgvcv $500
https://partners.uber.com/join/?invite_code=6w3wt2b8z $300

With no money:

https://partners.uber.com/join/?invite_code=mza5cmjtue
https://partners.uber.com/join/?invite_code=9cy316h6ue
https://partners.uber.com/join/?invite_code=4u8kyjxtue
https://partners.uber.com/join/?invite_code=15xvj

And I will add some examples to attachments.

So an attacker or a hacker could use it for free rides or getting money with uber,can create many accounts with every  invite code.

//The other thing about this vulnerability is you are getting some informations about members.

For example Go that page or request a GET method 

GET https://partners.uber.com/join/?invite_code=uber3958

You'll see in the source code //in Turkish uber version)

<img src="https://d297l2q4lq2ras.cloudfront.net/nomad/2014/11/27/20/480x480_id_6dae6e16-0990-4cef-ad6b-1ddf3497d1b4.jpeg">
        </div>
          <h1 class="flush--bottom">ignacio alejandro, sizi arabanızla para kazanmanız için davet etti.</h1>

Member Informatins:

ignacio alejandro > This is the name of user who has the invite code.
And you can see the user's image in "<img src =".And probably she or he uploaded his/her photo on "2014/11/27" which is in the image link.



## Attachments
- example1.png
- example2.png
- information.png
- information2.png
- information3.png
- request.png
- bruteforce.png
