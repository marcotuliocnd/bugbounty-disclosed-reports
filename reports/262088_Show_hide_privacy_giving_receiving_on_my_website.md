# Show hide privacy giving receiving on my website 

## Report Details
- **Report ID**: 262088
- **URL**: https://hackerone.com/reports/262088
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-08-21T22:49:34.266Z
- **Disclosed**: 2017-09-09T17:23:33.680Z

## Reporter
- **Username**: test99767
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hi team ..
I found show hide privacy settings on website ... nobody can see  on my profile but i put code on my website anybode can see my total giving .. 

Step reprodence ..

1- go to https://gratipay.com/~demo/settings/ click turn on (  hide total to giving other) and (hide my self from search result ) this way nobody can see my profile it .
2- go to https://gratipay.com/~demo/widgets/
3- copy code to your website then preview your test site look show all your privacy before now you hide it

* GIVING & TAKING WIDGETS

Use this code to add a Gratipay "receiving" widget on your website:

<script data-gratipay-username="demo"
        src="//grtp.co/v1.js"></script>

Or, if you'd like to include a "giving" widget, you can add the

data-gratipay-widget="giving"
attribute:
<script data-gratipay-username="demo"
        data-gratipay-widget="giving"
        src="//grtp.co/v1.js"></script>


##Poc
 Screenshot 

## Attachments
- 11.png
- 22.png
- 44.png
- 33.png
