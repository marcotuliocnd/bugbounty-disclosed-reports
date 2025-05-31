# test.zba.se is vulnerable to SSL POODLE  

## Report Details
- **Report ID**: 201520
- **URL**: https://hackerone.com/reports/201520
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-27T10:49:07.396Z
- **Disclosed**: 2017-02-27T10:50:34.423Z

## Reporter
- **Username**: hackerhero
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information

 test.zba.se is vulnerable to ssl poodle
 Steps to reproduce:
 1.nmap -sV --version-light --script ssl-poodle -p 443 example.com

 2.curl -v3 -X HEAD https://www.example.com<br> 
  3.or script given at https://access.redhat.com/node/1232123/40/0<br> 
  command: ./poodle.sh example.com 
  Result from these all 3 commands proves that test.zba.se is vulnerable to ssl poodle issue. 


Attack scenario:
It was discovered by researchers at Google itself and announced on Google’s online security blog.<br> read here for more information and attack scenario:<br> https://security.googleblog.com/2014/10/this-poodle-bites-exploiting-ssl-30.html.




## Attachments
No attachments
