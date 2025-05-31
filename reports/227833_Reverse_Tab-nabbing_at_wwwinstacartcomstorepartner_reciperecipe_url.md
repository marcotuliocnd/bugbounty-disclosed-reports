# Reverse Tab-nabbing at www.instacart.com/store/partner_recipe?recipe_url=

## Report Details
- **Report ID**: 227833
- **URL**: https://hackerone.com/reports/227833
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-12T05:17:05.825Z
- **Disclosed**: 2017-05-30T17:24:39.002Z

## Reporter
- **Username**: ak1t4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
### Summary 

Instacart at ```/store/partner_recipe?recipe_url=``` endpoint is vulnerable to reverse tabnabbing, since the injected link use ```target="_blank"``` , this means the page that opens in a new tab can access the initial tab and change its location using the window.opener property.

example: ```<a href="https://s3-eu-west-1.amazonaws.com/some-evil-host/evil2.html" target="_blank" class="">```

#### Reproduction Steps & PoC

__POC A__

1) Go to https://www.instacart.com/store/partner_recipe?recipe_url=https://s3-eu-west-1.amazonaws.com/some-evil-host/evil2.html&partner_name=&ingredients[]=apples&ingredients[]=butter&ingredients[]=Splenda+Brown+Sugar+Blend&ingredients[]=cinnamon&ingredients[]=nutmeg&title=Example-Reciper-with-Evil-Link&description=&image_url=x
2) Click on "Example-Reciper-with-Evil-Link"
3) You see that new page show 404 error and the principal page is change by a fake login page of instacart

**Evil link**
{F183925}
**New open Page**
{F183924}
**Principal page changed for a phishing page**
{F183923}

__POC B__

1)Go to https://www.instacart.com/store/partner_recipe?recipe_url=https://s3-eu-west-1.amazonaws.com/some-evil-host/evil.html&partner_name=&ingredients[]=apples&ingredients[]=butter&ingredients[]=Splenda+Brown+Sugar+Blend&ingredients[]=cinnamon&ingredients[]=nutmeg&title=%22Barb%27s+Fried+Apples+-Diabetic-Low+Fat&description=&image_url=x
2) Click on "Example-Reciper-with-Evil-Link"
3) You see alert popup in instacart principal page

{F183926}

(**Tested on all latest version browser: safari / chrome / firefox**)

### FIX & MITIGATION

To  mitigate this issue we need to use rel="nofollow noopener noreferrer" as follows:

```<a target="_blank" class="btn external-url" href="https://evil.com" rel="nofollow noopener noreferrer"><i class="fa fa-external-link"></i>
</a>```

Now when you click on this link, the attacker cannot access the initial tab.

#### References

**https://www.jitbit.com/alexblog/256-targetblank---the-most-underestimated-vulnerability-ever/**

Let me know if more info needed or anything else,

kind regards,
@ak1t4



## Attachments
- Captura_de_pantalla_2017-05-12_a_las_2.04.50.png
- Captura_de_pantalla_2017-05-12_a_las_2.04.34.png
- Captura_de_pantalla_2017-05-12_a_las_2.04.28.png
- Captura_de_pantalla_2017-05-12_a_las_2.07.16.png
