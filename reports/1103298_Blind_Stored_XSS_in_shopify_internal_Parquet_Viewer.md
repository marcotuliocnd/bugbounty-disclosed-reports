# Blind Stored XSS in shopify internal Parquet Viewer

## Report Details
- **Report ID**: 1103298
- **URL**: https://hackerone.com/reports/1103298
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-14T18:44:29.624Z
- **Disclosed**: 2024-02-08T15:10:03.594Z

## Reporter
- **Username**: testingforbugs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
##Summary:
Hey, hope you are doing well, I have found that one of my blind xss payload fired in one of your internal tool `Parquet viewer` on 14th feb 11:23 PM IST

I don’t know the entry point were I put my bXSS payload, But this is fired in one of your employee ( `[██████` ) computer.

##Details:
I am attaching all the details here.

* Vulnerable Page URL
`file://localhost/private/var/folders/4m/pdc_bjcj17dcxbtlllqqq81w0000gp/T/parquet-viewer-6296239398097329598.html`

* User IP Address
`█████████`

* User-Agent
`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36`

You can see the name of Shopify employee `████████` at `gs://starscream-adhoc/user/███/shop_dimension/part-00039-4039dc30-6a7a-4108-838d-fb1daec9a216-c000.snappy.parquet`
* ███████

* Open the dom.html and go o the `Sample Data` ███████
████

## Impact

████

Kind Regards
Aman

## Attachments
No attachments
