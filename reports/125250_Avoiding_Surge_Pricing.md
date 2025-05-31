# Avoiding Surge Pricing

## Report Details
- **Report ID**: 125250
- **URL**: https://hackerone.com/reports/125250
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-03-23T05:48:58.498Z
- **Disclosed**: 2016-08-11T18:44:11.333Z

## Reporter
- **Username**: nikhil_patil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Please have a look at the video in this [video link](https://drive.google.com/file/d/0B5uOIs56rbZkeDlxRG9TVDdKWkU/view?usp=sharing) which shows the bug and helps you reproduce the same following the steps. 

As you can see, there is surge of 1.3x in that area. But with this bug, one can avoid the surge. 

To explain the video in brief
First I selected Uber Go with the pickup location as "Prestige Shantiniketan" and destination as "Big Brewsky". Now the **"Share your car" fare is 249.91** and **"Get your own car" fare is 277.68.**
Now I go back to the map screen, and I scroll to the area which has no surge. And then I click on "set pickup location". 
In the confirmation screen, I change the pickup location to "Prestige Shantiniketan" (the location with surge) and use the same Destination "Big Brewsky". Ta-Da !! Now you can see the price without surge even though there is surge in that area (you can see surge symbol on "Request Pool" button). The **"Share your car" fare is 191.48** and **"Get your own car" fare is 212.76**. 
Since the UberPool fare is pre-decided, if one has booked using this bug will end up paying the non-surge price for UberPool.

PS: I've personally tried this loophole once for "Share your car" in the UberGo screen and it worked for me. 
This bug might even work for "Get you own car" or UberX, where the bill generated is considering non-surge price, but I haven't tried it. Although in the fare estimate, it shows the non-surge price in surge areas using the above trick.

## Attachments
No attachments
