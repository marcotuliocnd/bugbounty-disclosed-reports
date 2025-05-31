# Compromising the user ID

## Report Details
- **Report ID**: 358007
- **URL**: https://hackerone.com/reports/358007
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-27T00:46:59.723Z
- **Disclosed**: 2018-10-07T00:51:49.026Z

## Reporter
- **Username**: jarvis0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
Vulnerability allows to compromise the user ID in the "Dating" menu. This is a serious vulnerability that violates the logic of the site and allows the attacker to write a message to the user he likes before the user responds reciprocally.

In order to play the vulnerability, you need to go to the page [Dating](https://badoo.com/encounters), and use all available ones for the current account. While the husky is not over, such a request is sent:

{F302185}

In response comes this:

{F302186}

So far, nothing interesting in the answer. Next, you need to use all available hounds. If you need to do this quickly, you can press the "1" key quickly on the keyboard. When the husky is over, such a window will be displayed.

 {F302183}

We need to close this window. Next, the implementation of the vulnerability on the real profile will be demonstrated. The following profile is displayed:

{F302198}

You must press the "1" key. Then look in Burp Suite which request was sent:

{F302197}

Here is the answer:

{F302201}

The response comes with a link:

`pr4eu.badoocdn.com/p34/133/0/0/5/631317204/d1341450/t1527356459/c_JfzIrrpMHtw3mgp4-aHsvV7EuPiN5pF-uR22VRsu9Zc/1341450309/dfs_180x180/sz___size__.jpg`

In the link you can find ID: 631317204

Then just go to the link

`https://badoo.com/profile/631301611` 

And the real profile of the girl will be received.

{F302205}

You can write her a message.

This vulnerability can be automated. To do this, you need to get a "Premium", you can use a free two-day version. You need to go to the [Settings] page (https://badoo.com/settings) and delete your profile. When deleting, several windows will be highlighted, one of which will offer Premium for 2 days. Premium status allows you to change "like" to "dislay" and vice versa. Next, you need to return to[Знакомства](https://badoo.com/encounters) and click on the cross. When the next page appears, you can decide whether you like the profile of a person or not. If you like - click on "Laik", look at the query response, identify the ID, then click on the cross on the page, going to the next profile. Then go to this person's page by ID, change the "dislay" to "like" and then write a private message.


This method can be automated programmatically through python + selenium, pumping out pictures of avatars of girls in the folder, giving them names in the form {ID} .png. This will quickly select the girls you like and write them.

## Impact

The attacker can scroll the profiles of users in the "Dating" menu and determine the ID of a particular user who he liked. Knowing ID, you can write to the user, without waiting until he responds with the interaction.

## Attachments
- badoo1.png
- badoo2
- badoo3.png
- badoo6.png
- badoo5.png
- badoo7.png
- badoo8.png
