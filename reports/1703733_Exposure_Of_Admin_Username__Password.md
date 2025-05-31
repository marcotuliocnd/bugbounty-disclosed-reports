# Exposure Of Admin Username & Password

## Report Details
- **Report ID**: 1703733
- **URL**: https://hackerone.com/reports/1703733
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-09-18T10:24:40.552Z
- **Disclosed**: 2022-12-25T10:48:00.481Z

## Reporter
- **Username**: coyemerald
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hello Team, 
Ther an exposure of your username and password on this    subdomain https://engage2.mtnonline.com/nc/


Exposed Credentials

    uid: "mtnng",
        passwd: "bd31568138edbfc0552a1ecc6886ea5c",



Steps To Reproduce:

Visit https://engage2.mtnonline.com/nc/ 

Now, press CTRL+U to view the source code of this page,


Look for this code




       console.log(message);
    }
}

    (function (){
    const plid = 73;

    const mtnContainer = document.getElementById("mtn20238");
    const mtnUri = mtnContainer.childNodes[0].getAttribute("href");
    mtnContainer.addEventListener("click", ()=>fetch(mtnUri).catch(()=>{}));

    window.mobucksApi.placeAd({
        containerElementId: "mtn20238",
        uid: "mtnng",
        passwd: "bd31568138edbfc0552a1ecc6886ea5c",
        plid:plid,
        }, () => { 
            typeof mtnNoBanner == "function" && mtnNoBanner(plid,mtnContainer);

## Impact

The exposed password is in md5 which I was able to decrypt easily

uid: mtnng
hash = bd31568138edbfc0552a1ecc6886ea
plain password: v0d@c0mS@

And as an attacker, this can be abused in lots of ways such as exposing some client's info

https://adsmobucks.mtnbusiness.com.ng/feed?uid=mtnng&passwd=bd31568138edbfc0552a1ecc6886ea5c&plid=8

## Attachments
- mtnb.JPG
- mtnb2.JPG
