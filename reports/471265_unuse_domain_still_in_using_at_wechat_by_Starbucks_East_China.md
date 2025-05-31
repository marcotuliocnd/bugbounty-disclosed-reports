# unuse domain still in using at wechat by Starbucks East China

## Report Details
- **Report ID**: 471265
- **URL**: https://hackerone.com/reports/471265
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-12-22T18:27:37.298Z
- **Disclosed**: 2019-01-22T23:17:14.214Z

## Reporter
- **Username**: k3mlol
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:** 
spcc.mobi is still using at wechat offical account by Starbucks East China. but this domain is **on sale**.

**Description:**
I had reported this at report_id=433843，bu your gays had ignored, because they said the domain is unused.

In fact, spcc.mobi still having an interface using at wechat offical account by Starbucks East China

wechat offical account name is **星巴克江浙沪**

endponit request below:

``` html
GET /v5/bind.html HTTP/1.1
Host: coupon.ec-starbucks.cn
User-Agent: Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MOB31E; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044405 Mobile Safari/537.36 MMWEBID/157 MicroMessenger/6.7.3.1360(0x260703EC) NetType/WIFI Language/zh_CN Process/tools
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,image/tpg,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: PHPSESSID=ip1f71qqak3kvakksu28bensjlapsh9a; Hm_lvt_b7c2e12efc764f8179148ddbece8211f=1545489448; Hm_lpvt_b7c2e12efc764f8179148ddbece8211f=1545489448
Connection: close

```
reponse is below:

``` html
....
<script>
	$(function(){
		$.get('http://weixin.spcc.mobi/oauth/_jssdk.html',{url:location.href.split('#')[0]},function(data){
			 wx.config($.extend({
			    debug: false,
			    jsApiList: ['onMenuShareTimeline','onMenuShareAppMessage','onMenuShareQQ','onMenuShareWeibo','hideMenuItems','showMenuItems','hideOptionMenu','showOptionMenu',]
			},data));
		},'jsonp');
	})
	
	wx.ready(function () {	
		wx.hideOptionMenu();
	});

</script>
....
```

**Platform(s) Affected:**
- coupon.ec-starbucks.cn(Starbucks East China in using)

## Steps To Reproduce:

#### plan A(easy)
1. request the endpoint I offer
2. you will find the reponse contain "weixin.spcc.mobi"
3. visit the **weixin.spcc.mobi** you will find that this domain is on sale

#### plan B(complicated)
1. register a wechat account(download the app(name is wechat) from app store or play store)
2. search wechat offical account **星巴克江浙沪** then follow
3. click my card
4. you can find the requests as the I had mention.

## Recommendations for fix
remove the the unused **weixin.spcc.mobi** endpoint

## Impact

the domain is on sale, if attacker buy  this domain, can full control this domain for(Phishing Attack and etc.)

## Attachments
- burp_request.jpg
- ec-sbux-china.jpg
- ec-sbux.jpg
- wechat2.jpg
- wechat_you_click.jpg
