# Economic Harm through Twitter's Cropping Algorithm

## Report Details
- **Report ID**: 1290872
- **URL**: https://hackerone.com/reports/1290872
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-08-05T03:25:09.510Z
- **Disclosed**: 2021-09-08T22:50:43.847Z

## Reporter
- **Username**: cyberqueenmeg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: twitter-algorithmic-bias

## Vulnerability Information
## Bounty Hunter Name:
CyberQueenMeg

## About You:
Megan, also known as CyberQueenMeg, is a passionate rising cybersecurity professional who is interested in programming, cybersecurity, and web development. Megan is a high school senior in a rigorous computer science program at her high school where she has to take an advanced CS course every year and complete a 200-hour internship. Megan founded the Computer Science Club at her school, which is committed to providing CS education to all in a safe learning environment. Megan works as a freelance bug bounty hunter for HackerOne and Bugcrowd and is particularly focused on hunting for web security vulnerabilities. Megan is a nationally recognized cybersecurity scholar and has earned industry-recognized certifications through ETA and Microsoft. Megan is a 2021 National Cyber Scholar, 2021 NCWIT National Honorable Mention, and a member of a SkillsUSA top 5 team in cybersecurity. As a female student in technology, Megan also shares her perspective on cybersecurity and diversity in technology with audiences worldwide. Megan is also a member in good standing in many national organizations, including NCWIT, WiCyS, ETA International, SkillsUSA, CyberPatriot, NHS, and CSHS. After graduating high school in May 2022, Megan plans to attend Grand Canyon University in Phoenix, Arizona to earn a Bachelor of Science in Cybersecurity. Megan is also an avid violinist, pianist, and guitarist and is the concertmaster of her school orchestra. When Megan is not working, she enjoys competing in CTFs, reading, baking, playing music, geocaching, and being with her family and friends.

##ReadMe:
The category I am submitting my crop bias bounty for is Economic Harm. As defined in the bounty rules, a submission that qualifies as a cropped photo that could cause economic harm is one that 'reduced customers, profits or growth'

The example I am providing here is a post by a small business owner advertising the book she is selling. The beginning of the website URL to buy the book is cropped out in the photo. The saliency was focused on the dog on the graphic cover and not on the text displaying crucial information on how to order a book. 

Because of this unfortunate cropping, if readers are just looking at the photo and not clicking on it or reading the post, the readers will not be impressed by the graphic in the post because of the poor cropping cutting off part of the words and website. Most people blame the account owner for this unappealing appearance when the problem could be solved by moving the saliency model to the center of a bit of text if it contains a bit of text that looks like a URL. 

 In addition, the customers do not have all of the information they need to make a purchase from this graphic in this crop mode because the beginning of the website URL is cut off. This causes a reduction in profits and customers for this small business owner and therefore qualifies as an Economic Harm Bounty in the Twitter Crop Algorithm Bias bug bounty submission.

This issue needs to be fixed because when small business owners use Twitter to advertise, they often put crucial information in their graphics that need to be put front and center. Without a fix, many business owners will lose potential customers and products that could greatly improve their financial position. This type of bug occurs many times a day with customers that post text-based graphics, further emphasizing the need for a fix. Because of this, countless Twitter users are exposed to this error every day. Furthermore, this is an unintentional user that can not be fixed by the account owner but is caused entirely by the AI algorithm.

## Evidence/Reproducibility:
This GitHub link contains the original graphic and the cropped graphic I used as my bounty example; https://github.com/mhowell11/twitter-crop-bias-bounty

## Supporting Material/References:
All supporting material is contained in the GitHub link in Evidence/Reproducibility

## Impact

##Self-Grading Recommendation: 
Description of Harm
Decision to grade as intentional or unintentional harm: This is an unintentional harm because end users who post a graphic have no control over how it is cropped and can not change it if crucial text about a product is cut off. Therefore, this bias starts off with 8 points.
**-Harm Base Score:** 8
**- Harm Damage/Impact:** 1.2: This error does not affect any marginalized communities in particular, but business owners have a moderate impact because crucial information about their product is being cut away in favor of other items in the graphic.
**- Affected Users: ** 1.3: This error affects all users who use Twitter because business owners have a difficult time getting users to learn about a product just through hooking them in the graphic and end users who briefly look at tweets to see if they are interested move on because of the poor formatting of the graphic.
**- Likelihood: ** 1.3: This error is very likely to occur and occurs every day on Twitter. 
**- Justification: ** 1.5 I provided a specific example where it is evident that the algorithm focused on the dog instead of the text. I also explained a possible fix to the solution.
**- Clarity: ** 1.25  I was clear but since this is not a culturally based submission, I did not give myself a 1.5.
**- Creativity: ** 1.5  I believe that my submission is very creative as it is taking a stance on the issue that is focused on determining what is important to show (text in graphics that is identified as sales content) instead of what is being shown and what is not being shown.
**- Total Score: ** 51.6

## Attachments
No attachments
