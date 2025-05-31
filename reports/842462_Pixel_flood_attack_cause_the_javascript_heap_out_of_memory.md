# Pixel flood attack cause the javascript heap out of memory

## Report Details
- **Report ID**: 842462
- **URL**: https://hackerone.com/reports/842462
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-07T11:02:53.744Z
- **Disclosed**: 2020-05-21T08:18:00.595Z

## Reporter
- **Username**: mayaseven
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Pixel flood attack in jimp
It allows flooding the memory and causing DoS by uploading a crafted image (5kb image), and the Jimp module will tries to allocate 4128062500 pixels into memory.

# Module

**module name:** jimp
**version:** <=0.10.1
**npm page:** `https://www.npmjs.com/package/jimp`

## Module Description

> An image processing library for Node written entirely in JavaScript, with zero native dependencies.

## Module Stats

1,053,700 Weekly Downloads

# Vulnerability

## Vulnerability Description

> The jimp module will load the pixel from the image file to the memory, and processing the image in order to get a new image file such as resize, rotate, blur, etc. The jimp using EXIF data for picture orientation, which was causing run out of memory in the system. The attacker could manipulate the exif data in the image file such as change the image pixel to 64250x64250pixels. If the jimp module loaded the crafted image, it tries to allocate 4128062500 pixels into memory. 

## Steps To Reproduce:

1. First, install the jimp module : `npm install --save jimp`
2. Second, download a crafted image from the attachment (lottapixel.jpg).
3. Finally, create index.js file as the PoC code below and execute. 

```
var Jimp = require('jimp');

Jimp.read('lottapixel.jpg', (err, lenna) => {
  if (err) throw err;
  lenna
    .resize(256, 256) // resize
    .quality(60) // set JPEG quality
    .greyscale() // set greyscale
    .write('image-small-bw.jpg'); // save
});
```

The output will display the error message like below when the memory is exhausted.
>FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory

## Patch

> Disable ImageMagick's EXIF orientation.

## Supporting Material/References:

- Pixel flood attack `https://hackerone.com/reports/390`
- Nodejs v13.12.0

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

Denail of Service

## Attachments
- lottapixel.jpg
