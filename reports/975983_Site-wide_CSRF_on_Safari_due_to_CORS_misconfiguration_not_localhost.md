# Site-wide CSRF on Safari due to CORS misconfiguration (not localhost)

## Report Details
- **Report ID**: 975983
- **URL**: https://hackerone.com/reports/975983
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-07T06:27:53.837Z
- **Disclosed**: 2020-10-27T19:25:44.977Z

## Reporter
- **Username**: nnez
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Description
Hello there, on `new.cs.money` or `cs.money`, there is anti-CSRF mechanism, which is `Referer` header check.
However, I discovered that regex logic for checking `Referer` header is flawed.

I found that adding `{` or `}` at the end of the domain pass the validation.
Therefore, if a request comes from `new.cs.money{.attacker.com` it would pass validation.
And because there is no other protective mechanisms in place (SameSite flag, Origin check, Content-Type check), thus allowing attacker to perform CSRF attack on victim.

According to this research, https://www.corben.io/advanced-cors-techniques/
Unlike other browsers, Safari will load the domain with weird characters like `{` or `}` in it.

You can try this by accessing `new.cs.money{.withgoogle.com` on Safari and Chrome then see the differences.

## Steps To Reproduce
These steps are gonna demonstrate how an attacker can perform CSRF attack forcing user to `change_email` on this endpoint `https://new.cs.money/change_email`
1.Open Safari on MacOS, login on `new.cs.money` (you also need steam account to do this)
2.Open new tab on safari, and navigate to `new.cs.money{.withgoogle.com`

*I want to note that `new.cs.money{.withgoogle.com` can be hosted on attacker site like, `new.cs.money{.attacker.com`. However, I'm still on the process of buying new domain, so I'm gonna come back and provide you with another way to exploit this with my domain. But I think that these steps are also enough for PoC*

3.Inspect element to bring up javascript console (To enable dev tool, please refer to https://stackoverflow.com/questions/40234993/how-to-inspect-element-using-safari-browser)
4.Go to JS console, paste below code and hit enter
```
var FormEl = `
<form action="https://new.cs.money/change_email" method="POST">
        <input type="hidden" name="email" value="nnez+attacker@wearehackerone.com" />
        <button type="submit" style="font-size:28pt;z-index:99999">Submit</button>
    </form>
`;
var Div = document.createElement('div');
Div.innerHTML = FormEl;
document.body.appendChild(Div);
```
5.Click submit button
6.Go back to https://new.cs.money/th/csgo/personal-info and see that the email is changed

## Video Demonstration
{F978459}

## Impact

Because `new.cs.money` and `cs.money` implement anti-CSRF mechanism the same way, and use it in all endpoints, therefore, it could lead to site-wide CSRF attack on any endpoints. I can't test `Cash Out` function yet because I can't access it, but I set the severity to high because of this.

I can't access https://hackerone_sellmode.zaebumba.com/ despite the new credentials you updated.

## Attachments
- new-cs-money-csrf-site-wide-safari.mp4
