# Users able to set video url for unpublished words and able to see the name of unpublished words

## Report Details
- **Report ID**: 486837
- **URL**: https://hackerone.com/reports/486837
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-27T07:17:15.865Z
- **Disclosed**: 2019-03-02T02:24:12.643Z

## Reporter
- **Username**: d3f4u17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: urbandictionary

## Vulnerability Information
**Summary**

Users will be able to set youtube video URL to unpublished words and will be able to see names of an unpublished word.

**Description**

Once a user publishes a word and later unpublish it, others user still would be able to set the youtube video URL for it and will be able to see the name of the unpublished words.

##Steps to reproduce

1. Go to your account and create a new definition and see the URL to get the definition_id.
2. Go to definitions page and unpublish it.
3. Now visit the following URL [https://www.urbandictionary.com/video.new.php?defid=your_def_id](https://www.urbandictionary.com/video.new.php?defid=your_def_id)
4. Now you will be able to set the youtube video URL and will be able to see the name of the unpublished word.

In my case i have used the following **defid**  *12504202*

* To check whether the word is unpublished or not I used the urbandictionary's api and used the following URL [http://api.urbandictionary.com/v0/define?defid=12504202](http://api.urbandictionary.com/v0/define?defid=12504202) and it returned me an empty list, showing that no data exists for the given defid.
>see poc-1

* Then I passed the samedefid to the URL defined at step 3 [https://www.urbandictionary.com/video.new.php?defid=12504202](https://www.urbandictionary.com/video.new.php?defid=12504202) and after visiting it I was able to see the name and was able to set the youtube video for it.
>see poc-2

##POC/Screenshots
* POC-1
{F413241}

* POC-2
{F413242}

## Impact

* Information disclosure

## Attachments
- Screenshot_from_2019-01-27_12-41-51.png
- Screenshot_from_2019-01-27_12-42-16.png
