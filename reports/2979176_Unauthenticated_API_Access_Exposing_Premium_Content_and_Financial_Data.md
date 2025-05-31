# Unauthenticated API Access Exposing Premium Content and Financial Data

## Report Details
- **Report ID**: 2979176
- **URL**: https://hackerone.com/reports/2979176
- **State**: Closed
- **Severity**: none
- **Submitted**: 2025-02-06T19:05:15.270Z
- **Disclosed**: 2025-02-09T21:31:04.293Z

## Reporter
- **Username**: mcblockchamp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
# **Security Report: Unauthenticated API Access Exposing Premium Content and Financial Data**

## **Issue Summary**  
A critical security flaw has been identified on **xvideos.red**, allowing unrestricted access to premium channels and videos without requiring a paid membership. Normally, these resources should be behind a paywall, but due to an open API vulnerability, unauthorized users can retrieve detailed financial and video-related data, including direct access to premium content.  

## **Affected Endpoints**  
- **API Endpoints Exposing Financial and Video Data:**  
  - `https://www.xvideos.red/channels/bangbros-network/fan-club/rating/1`  
  - `https://www.xvideos.red/channels/barebackstudios/fan-club/best/0`  

- **Direct Access to Premium Channels and Videos Without Membership:**  
  - `https://www.xvideos.red/channels/barebackstudios/`  
  - `https://www.xvideos.red/channels/barebackstudios/#gallery`  
  - Example Video: `https://www.xvideos.red/video.umkcobd36ea/nikki_brooks_free_family_use_vol_4_backpedaling`  

## **Vulnerability Details**  

1. **Unauthorized Video and Channel Access**  
   - Normally, premium videos and channels require a paid membership.  
   - However, users can now directly access these without authentication by using specific URLs.  

2. **Exposed Financial Data Per Video**  
   - The API returns earnings per video (`pmp` field), revealing revenue generation per transaction.  
   - Example:  
     ```json
     "pmp": "$24,99"
     ```
   - This data can be scraped and analyzed for competitive insights.  

3. **Video Metadata Exposure**  
   - Unauthorized users can retrieve details such as:  
     - Video ID, URL, duration, and title.  
     - Private access status.  
     - Views, likes, and other engagement metrics.  
   - Example JSON Response:  
     ```json
     {
       "id": 950497,
       "status": "PUBLISHED",
       "is_private": false,
       "timestamp": 1695600641,
       "videos": [
         {
           "id": 74696125,
           "u": "/video.umkcobd36ea/nikki_brooks_free_family_use_vol_4_backpedaling",
           "c": 10,
           "tf": "Nikki Brooks Free Family Use Vol 4 Backpedaling",
           "d": "45 dk",
           "pmp": "$24,99",
           "p": "barebackstudios",
           "pn": "Bare Back Studios",
           "ch": true,
           "pm": true
         }
       ]
     }
     ```  
   - This confirms that financial information, video details, and premium access flags are openly available.  

## **Reproduction Steps**  

1. Access the API endpoints:  
   - `https://www.xvideos.red/channels/bangbros-network/fan-club/rating/1`  
   - `https://www.xvideos.red/channels/barebackstudios/fan-club/best/0`  

2. Observe the JSON response containing sensitive data.  
3. Use the provided `u` field (video URL) to directly access premium videos.  
4. Access `https://www.xvideos.red/channels/barebackstudios/` or `https://www.xvideos.red/channels/barebackstudios/#gallery` to browse premium content without a subscription.  

This vulnerability allows unrestricted access to **both premium channels and individual premium videos**, effectively bypassing paywalls.


{F4031235}

{F4031237}

## Impact

- **Revenue Loss:** Users can bypass payment requirements and access premium content for free.  
- **Privacy Risks:** Financial data of video creators and studios is exposed.  
- **Content Theft:** Videos can be indexed, scraped, and redistributed illegally.  
- **Competitive Intelligence:** Earnings per video and overall channel revenue can be analyzed by third parties.

## Attachments
- image.png
- image.png
