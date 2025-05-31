# Zomato Map server going out of memory while resizing map image

## Report Details
- **Report ID**: 751904
- **URL**: https://hackerone.com/reports/751904
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-12-05T11:20:34.840Z
- **Disclosed**: 2019-12-05T12:00:35.394Z

## Reporter
- **Username**: mchinmoy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Go to

https://maps.zomato.com/php/staticmap?center=0,0&size=240x150&maptype=zomato&markers=180,180,pin_res32&sensor=false&scale=%&zoom=eval(2147483647+1)&language=en

a map will be displayed

Now increase the map size by 10x

https://maps.zomato.com/php/staticmap?center=0,0&size=2400x1500&maptype=zomato&markers=180,180,pin_res32&sensor=false&scale=%&zoom=eval(2147483647+1)&language=en

It will always timeout after waiting from 1-15 minutes

POC video is attached.

## Impact

Zomato Map servers can be bought down making map feature completely non functional and causing millions of dollars loss for Zomato.

## Attachments
- Zomato_Map_Server_Going_Out_Of_Memory.mp4
