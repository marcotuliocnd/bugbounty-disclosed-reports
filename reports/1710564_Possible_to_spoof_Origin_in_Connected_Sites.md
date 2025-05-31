# Possible to spoof Origin in "Connected Sites"

## Report Details
- **Report ID**: 1710564
- **URL**: https://hackerone.com/reports/1710564
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-23T18:24:46.167Z
- **Disclosed**: 2023-04-13T09:15:29.034Z

## Reporter
- **Username**: renniepak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: metamask

## Vulnerability Information
Hi MetaMask Team!

I have been experimenting with trying to spoof the origin of the site that is trying to interact with MetaMask. Being able to recognize the origin is an important mechanism in the Web3 ecosystem, because signing anything from a malicious origin could result a loss of funds for example. 

I have found that it is possible to partly spoof the origin in the `Connect Sites` menu , which seems to be caused by a bit of CSS that sets the origin domain name direction to ["right-to-left"](https://www.w3schools.com/cssref/pr_text_direction.asp)

## Reproduction

1. Install the latest MetaMask Chrome Extension (10.18.4) in the latest Chrome version (105.0.5195.127).
2. Navigate to https://0-a.nl/metamask23rh23f923f.html
3. Accept the request to connect to 0-a.nl

████ █████

4. Sign the message (although I believe this is not necessary)

{F1948691}

5. Open the Extension again and click `Expand view`

{F1948694}

6. Click the 3 dots and then `Connected Sites`

{F1948696}

## Result

What we see now is that not `0-a.nl` is shown as a connected site but `a.nl-0`

{F1948697}

## Vulnerable code:

This behavior is caused by the fact that our domain name starts with a number and is followed by a hyphen, in combination with the following style sheet:

https://github.com/MetaMask/metamask-extension/blob/753666d9c2a0cb2be89e885629dfa6f3ded5703b/ui/components/ui/site-origin/index.scss#L21
```
   direction: rtl;
```

This specific combination of "English" letters, numbers and hyphens and the "right-to-left" direction in the stylesheet, will cause for the order of the characters in the domain name to be messed up, displaying an incorrect domain name.

## Exploitation

I understand `a.nl-0` is a weird looking domain and might cause some suspicions. But to demonstrate more impact we will pretend I own the domain:
`4-metamask.io` or more specifically the subdomain https://10.18.4-metamask.io

I didn't purchase this domain so to simulate this, go back to step 6 from the reproduction.

Right click the `a.nl-0` and select `Inspect Element`. Select the  line saying `<span>0-a.nl</span>` and replace it with `<span>10.18.4-metamask.io</span>`. **To emphasize, this is not self-exploitation, we merely do this so we don't need to buy the `4-metamask.io` domain to POC this.**

Now go back to the browser tab and the result should look like this:

{F1948706}

We now spoof the domain metamask.io and use the version number to distract from the fact that a hyphen follows the .io TLD.

## Impact

Connecting to a website allows that website to see your MetaMask wallet address and balance, and send transaction approval requests etc. For privacy and safety concerns you might want to disconnect your MetaMask wallet from a malicious website.

As seen in Steps 3 and 4, initially we are not able to spoof the origin in the MetaMask popups. However even if you took those steps by mistake, it should be easily identifiable which website to "Disconnect" should you want so to. 

What I've demonstrated in this POC is that we can register a similar looking domain and make it difficult for the victim to distinguish which website to Disconnect from their wallet, with our domain hiding in plain sight. 

Like stated in my introduction, the mechanism to manually recognize which Origin is making requests to Metamask is a vital part of the Web3 ecosystem and a secure implementation of the screens to accommodate this should be caried out to all the applicable user interfaces.

## Attachments
- image.png
- image.png
- image.png
- image.png
- image.png
