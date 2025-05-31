# Hide download previews are accessible without a watermark

## Report Details
- **Report ID**: 1745755
- **URL**: https://hackerone.com/reports/1745755
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-10-21T13:47:15.866Z
- **Disclosed**: 2023-05-04T07:56:47.425Z

## Reporter
- **Username**: juliushaertl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Initial report from https://github.com/nextcloud/richdocuments/issues/2561

**Describe the bug**
The secure watermarked view announced for Nextcloud 25 / Hub 3 can be hacked. See reproduction steps below.

**To Reproduce**

1. Go to Nextcloud Office Admin Settings and set the watermark options to have a custom watermark in read-only shares, without a download button.
2. For example, create a read-only public share link without a download button.
3. Go to the created public URL and see that there is as expected a watermark on the read-only document and no download button. For now, everything is OK.
4. Then notice that there is the close document cross at the top right. IMO, this cross should not exist because when you click on it, the document reappears behind, without the watermark. Even though the document appears smaller, I think this is risky and goes against the privacy purpose of this feature shown in Berlin.

**Expected behavior**
The close button should not appear at the top right in order to keep the recipient of the share captive in this view of the document. I go further in my explanation by saying that if the share is a single file share and not a folder share, the close button should never appear, because the share recipient is not supposed to access an upstream folder, but just be able to view the file (and edit it if he has write permission), nothing else.

**Screenshots**
Here is the closing button : 
![2022-10-21_14-29](https://user-images.githubusercontent.com/33763786/197195931-1e55f569-de6c-4527-be30-6e584a847468.png)
Here is what we get after clicking on it : 
![2022-10-21_14-39](https://user-images.githubusercontent.com/33763786/197197843-fb0eba78-17f7-4b71-8eca-0254b0e80af1.png)

## Impact

While the download should be hidden and the watermark should get applied the preview is still visible without

## Attachments
No attachments
