# Acquisition on broken link listed on the page "https://docs.doppler.com/docs/removal-deprecated-packages-scripts in [scheduling a call]

## Report Details
- **Report ID**: 2418210
- **URL**: https://hackerone.com/reports/2418210
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-03-15T17:59:09.042Z
- **Disclosed**: 2024-05-22T14:09:18.348Z

## Reporter
- **Username**: zig_shark
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: doppler

## Vulnerability Information
Summary:

 Docs doppler has an unclaimed broken link on its doc page which can be claimed by any malicious user.  

 Steps to reproduce: 

 1.Visit https://docs.doppler.com/docs/removal-deprecated-packages-scripts 
 2.Click on scheduling a call. 
 {F3122702}

 3. The scheduling a call page points to https://calendly.com/doppler-ryan/onsite-install , but the URL gives 404. 

 4.So, I impersonated his identity by forming a fake account called 'Page Acquisition by Joao Gomes' at this link.  Here, just for PoC purposes, I assumed the broken link by creating an account with this name doppler-ryan 

  {F3122718}

 Reference: https://hackerone.com/reports/2399386

{F3122743}

## Impact

The product violates well-established principles for safe design. 

 A malicious user can create a fake account on that broken redirect link and trick users who arrive at that link.

## Attachments
- Screenshot_2024-03-15_at_18-55-15_Removal_of_Deprecated_Clients.png
- Screenshot_2024-03-15_at_19-02-10_-_Jo_o_Gomes_(zig_shark)_acquisition_of_doppler-ryan.png
- Screenshot_2024-03-15_at_19-04-02_Doppler_disclosed_on_HackerOne_Github_app(link)_Takeover_Listed_on.png
- Screenshot_2024-03-15_at_19-12-54_Doppler_-_Bug_Bounty_Program_HackerOne.png
