# Create an account on auth-sandbox.elastic.co with email @elastic.co or any other @domain.com

## Report Details
- **Report ID**: 837510
- **URL**: https://hackerone.com/reports/837510
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-04-02T19:00:10.940Z
- **Disclosed**: 2020-12-28T16:23:52.187Z

## Reporter
- **Username**: superman85
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
**Summary:** 
Dear Team,

Today when doing some recon steps and found this subdomain 
>https://54.246.136.164/

Its not loaded correctly and viewing the source code exposed some other links interesting

>https://elasticsandbox.docebosaas.com/pages/14/learner-dashboard
https://auth-sandbox.elastic.co

Go to https://elasticsandbox.docebosaas.com/learn and using **SIGNIN WITH SAML SSO** leading to 

>https://staging.found.no/login?fromURI=https%3A%2F%2Fauth-sandbox.elastic.co%2Fapp%2Felasticcoexternal_docebo_1%2Fexkigtmda9ejVUCM70h7%2Fsso%2Fsaml%3FSAMLRequest%3DnVJNb9swDP0rhu6O%252FBE3sRBnyBIMC9BuQZ32sEsgy0yjTZY0Ud68fz%252FFSbH2ksNOAim%252B9%252FhILpB3yrJV70%252F6EX72gD4aOqWRjR8V6Z1mhqNEpnkHyLxg9erhnmWThFlnvBFGkTeQ2wiOCM5Lo0m03VTk0DTzMj%252B2YlYWjeDHpk3zsiggnxfibppnWXonoMyKNM9I9AwOA7IigSjAEXvYavRc%252B5BKsiROpnGS7dM5m%252BasmH4j0Sa4kZr7EXXy3iKjlAerMXLdNmaYgOKhREyEodxaeg2FgcGD01wdWiOgMYeUwvBDvviu5SV8f35aP8yS04wiGno2TaLVq7G10dh34Gpwv6SAp8f7f9JX%252BlfxCzdyjkG%252Fo6pDKnULw8Se7AdX1bKzCupAvwqtvY860%252FYKcBSnaMc3i7nAM5a2cOS98jFaEu2uO%252FoYqKV%252Bub2e5lKE7PN%252Bv4t3X%252Bs9WS7O3Gwct1v%252Bh5MFfUuwuNzblyC93eyMkuJP9Mm4jvvbnZ0zso2PYynzjmuUoH0YvFLm99oB91AR73ogdHmRfH%252FVy78%253D%26RelayState%3Dhttps%253A%252F%252Felasticsandbox.docebosaas.com%252Flms%252Findex.php%253Fr%253Dsite%252Fsso%2526sso_type%253Dsaml

At the website https://staging.found.no/ use **Signup** function allow me to register 2 accounts below
>superman85@wearehackerone.com
support@elastic.co

After login https://auth-sandbox.elastic.co/app/UserHome my account dashboard from superman85@wearehackerone.com is different with support@elastic.co.

On account support@elastic.co I can view some interesting apps like Elastic Cloud Admin (QA-Canary) etc ...

I have tried to launch apps and successful authorization this 
>https://adminconsole-qa-eu-west-1.aws.qa.cld.elstc.co/deployments

I do not do anything after logged in adminconsole. My IP address is **█████**

{F771084}
## Steps To Reproduce:

  1. Go to https://staging.found.no/ and Signup an account with email @elastic.co 
  1. Go to https://auth-sandbox.elastic.co and login with email/password you have registered
{F771085}
  1. After logged in, you are able to see the apps 
{F771083}

## Impact

With this vulnerability an attacker was allowed to view apps only visible to employees with email @elastic.co

## Attachments
- auth-sandbox_dashboard.png
- admin_console_dashboard.png
- auth-sandbox_profile.png
