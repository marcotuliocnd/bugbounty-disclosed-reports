# Underrepresentation Bias through Twitter's Cropping Algorithm

## Report Details
- **Report ID**: 1294062
- **URL**: https://hackerone.com/reports/1294062
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-08-06T17:29:25.375Z
- **Disclosed**: 2021-09-08T22:50:24.592Z

## Reporter
- **Username**: cyberqueenmeg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: twitter-algorithmic-bias

## Vulnerability Information
Bounty Hunter Name:
CyberQueenMeg

About You:
Megan, also known as CyberQueenMeg, is a passionate rising cybersecurity professional who is interested in programming, cybersecurity, and web development. Megan is a high school senior in a rigorous computer science program at her high school where she has to take an advanced CS course every year and complete a 200-hour internship. Megan founded the Computer Science Club at her school, which is committed to providing CS education to all in a safe learning environment. Megan works as a freelance bug bounty hunter for HackerOne and Bugcrowd and is particularly focused on hunting for web security vulnerabilities. Megan is a nationally recognized cybersecurity scholar and has earned industry-recognized certifications through ETA and Microsoft. Megan is a 2021 National Cyber Scholar, 2021 NCWIT National Honorable Mention, and a member of a SkillsUSA top 5 team in cybersecurity. As a female student in technology, Megan also shares her perspective on cybersecurity and diversity in technology with audiences worldwide. Megan is also a member in good standing in many national organizations, including NCWIT, WiCyS, ETA International, SkillsUSA, CyberPatriot, NHS, and CSHS. After graduating high school in May 2022, Megan plans to attend Grand Canyon University in Phoenix, Arizona to earn a Bachelor of Science in Cybersecurity. Megan is also an avid violinist, pianist, and guitarist and is the concertmaster of her school orchestra. When Megan is not working, she enjoys competing in CTFs, reading, baking, playing music, geocaching, and being with her family and friends.

Readme:
The harm I have identified in Twitter's cropping algorithm is Under-representation Bias. The example I am providing is of two canines, one lighter and one darker who are separated in the photo slightly. In the example of how the image appeared on Twitter, the lighter color canine is centered and that darker color canine is cut off and barely shown because of the cropping algorithm.

This under-representation bias in dogs is a crucial finding because it proves that the saliency algorithm is biased against darker colored living beings of different species, not just humans. It proves the need to change the algorithm to not determine cropping based on color, as noted in the Twitter research paper.

Evidence/Reproducibility:
This GitHub link contains the original graphic and the cropped graphic I used as my bounty example; https://github.com/mhowell11/twitter-crop-bias-bounty

Supporting Material/References:
All supporting material is contained in the GitHub link in Evidence/Reproducibility

## Impact

## Self-Grading Recommendation: 
Description of Harm: This harm is an under-representation bias against living beings of darker colors.
Decision to grade as intentional or unintentional harm: This is an unintentional harm as the poster of this picture (who I know) intended for both dogs to be shown in the cropped version.
**- Harm Base Score:** 20: This is an unintentional under-representation bias, which has been assigned a base score of 20.
**- Harm Damage/Impact:** 1.3: This bias affects multiple darker communities that transcend species (1.4). and could have a moderate impact on a dark skinned person's well being (1.2)
**- Affected Users:** 1.2: This bias is a common bias that occurs commonly on Twitter per the Twitter research paper and therefore impacts millions of people.
**- Likelihood or Exploitability:** 1.3: This bias occurs on Twitter daily and will do so until the saliency algorithm is fixed.
**- Justification:** 1.5: This bias is culturally relevant and shows a different perspective that provides valuable information on why the saliency algorithm is favoring lighter-skinned individuals over darker-skinned ones.
**- Clarity:** 1.5: My response meets all of the requirements for the bias challenge and is culturally situated.
**- Creativity:** 1.5: This is a very creative take on skin color bias that shows that the saliency algorithm is biased based on color across species.
**- Total Score:** 20 * (1.3 + 1.2 + 1.3 + 1.5 + 1.5 + 1.5) = 166.0

## Attachments
No attachments
