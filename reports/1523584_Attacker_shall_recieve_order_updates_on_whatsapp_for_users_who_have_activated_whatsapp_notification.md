# Attacker shall recieve order updates on whatsapp for users who have activated whatsapp notification

## Report Details
- **Report ID**: 1523584
- **URL**: https://hackerone.com/reports/1523584
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-27T18:18:46.607Z
- **Disclosed**: 2022-04-06T06:00:20.037Z

## Reporter
- **Username**: schutzx0r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
H

Summary:
1. Order ID are IDOR ( Insecure Direct Object Reference )
2. When users activated whats app notification an attacker would start receiving the notification without user interaction about their order.

Proof Of Concept:-

When an user order on a restaurant he/she can start whatsapp notification on their order.

██████████

Steps to Reproduce:-

1. When the user activates whats app notification by sending the message with order id. His order notification's vulnerable.

2. Now the attacker sends the message with above vulnerable order id ( Order id is IDOR - eg:15625383 )

3. He will get the error notification, though he will start receiving the updates.

{F1670097}

3.1 the updates would be
3.1.1 delivery partner assigned.
3.1.2 when he will reach
3.1.2 once he delivered the order.

## Impact

business logic error.

## Attachments
- order_notification_hack.png
