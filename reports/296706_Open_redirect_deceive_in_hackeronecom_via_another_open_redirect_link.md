# Open redirect deceive in hackerone.com via another open redirect link.

## Report Details
- **Report ID**: 296706
- **URL**: https://hackerone.com/reports/296706
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-10T18:38:12.956Z
- **Disclosed**: 2017-12-13T15:57:07.675Z

## Reporter
- **Username**: abidbaseer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
1. The open redirect feature in hackerone does not work properly
2. When users submit a report. They can also use links in the report. 
3. An attacker can deceive other users by using another website redirect link in hackerone.com
For example consider the links below
[https://l.facebook.com/l.php?u=https://evil.com/&h=ATMJdQSbOgLxx8kkZxvuz8D9mq0OTPfZ5OHToxZGQXr6M-ylbKvZxQ9p2xJv4TswF-pv2Nr75TIXzp1369GuPe3cmETf46pXKfIHlw]

when you click on the link the proceed button will appear and the facebook.com domain will be highlighted. When you click the proceed button you will be redirected to evil.com.

Similarly consider this link as an example
[https://www.google.com.pk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjx8qv0iYDYAhUIVhQKHe-pCGUQFggkMAA&url=https%3A%2F%2Fevilzone.org%2F&usg=AOvVaw36yGjkBQ68CeL5hPUPT7cp]

When you click the link google.com.pk will be highlighted and the proceed button will appear. By clicking the proceed button you will be redirected to the evilzone.org.
Just like the above examples other websites open redirects link can be used to deceive users. The open redirect feature of hackerone need attention to detect hosts specially when there are multiple hosts in the link. Thanks

## Impact

This vulnerability could redirect users to the attackers websites for phishing attacks.

## Attachments
No attachments
