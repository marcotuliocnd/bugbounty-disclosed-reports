# Backup Source Code Detected

## Report Details
- **Report ID**: 389454
- **URL**: https://hackerone.com/reports/389454
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-08-01T21:44:46.808Z
- **Disclosed**: 2018-09-21T22:49:57.381Z

## Reporter
- **Username**: linkks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Impact

Depending on the nature of the source code disclosed, an attacker can mount one or more of the following types of attacks:•Access the database or other data resources. With the privileges of the account obtained, attempt to read, update or delete arbitrary data from the database.
•Access password protected administrative mechanisms such as "dashboard", "management console" and "admin panel" potentially leading to full control of the application.
•Develop further attacks by investigating the source code for input validation errors and logic vulnerabilities.

Actions to Take


Remove all temporary and backup files.

Required Skills for Successful Exploitation

This is dependent on the information obtained from source code. Uncovering these forms of vulnerabilities does not require high levels of skills. However, a highly skilled attacker could leverage this form of vulnerability to obtain account information for databases or administrative panels, ultimately leading to control of the application or even the host the application resides on.

## Impact

GET /howto/store/order.html~ HTTP/1.1
Host: www.starbucks.co.jp
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-us,en;q=0.5
Cache-Control: no-cache
Cookie: PHPSESSID=██████; registerParams[0]=card; registerParams[1]=https%3A%2F%2Fcard.starbucks.co.jp%2Fmystarbucks%2Fcard%2FregisterMsc%2F
Referer: http://www.starbucks.co.jp/howto/store/order.html~
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36

<?php
include_once($_SERVER['DOCUMENT_ROOT']."/config.inc.php");

// ãƒšãƒ¼ã‚¸ãƒ—ãƒãƒ‘ãƒ†ã‚£è¨å®š
$pageProperties['title'] = "How to ã‚ªãƒ¼ãƒ€ãƒ¼";
$pageProperties['description'] = "ã‚¹ã‚¿ãƒ¼ãƒãƒƒã‚¯ã‚¹ã§ã¯ãŠå®¢æ§˜ã®ã”å¸Œæœ›ã«å¿œãˆã‚‰ã‚Œã‚‹ã‚ˆã†ã€æ§˜ã€…ãªã‚ªãƒ¼ãƒ€ãƒ¼ã‚·ã‚¹ãƒ†ãƒ ã‚’ã”ç”¨æ„ã—ã¦ã„ã¾ã™ã€‚";
$pageProperties['keyword'] = _BASE_META_KEYWORD_.",ä½¿ã„æ–¹,how,ã‚ªãƒ¼ãƒ€ãƒ¼,æ³¨æ–‡,order,ãƒ“ãƒãƒ¬ãƒƒã‚¸,beverage,ãƒ¡ãƒ‹ãƒ¥ãƒ¼,menu,ã‚µã‚¤ã‚º,size";
$pageProperties['ogImage'] = "http://www.starbucks.co.jp/images/og/howto-order.jpg";
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title><?php echo $pageProperties['title']; ?>ï½œã‚¹ã‚¿ãƒ¼ãƒãƒƒã‚¯ã‚¹ ã‚³ãƒ¼ãƒ’ãƒ¼ ã‚¸ãƒ£ãƒ‘ãƒ³</title>
<?php include(_SB_DIR_INCLUDE_."/common/meta.html"); ?>
<link type="text/css" rel="stylesheet" href="/common/css/contents.css" media="screen,print">
<link type="text/css" rel="stylesheet" href="/howto/store/css/index.css" media="screen,print">
<link type="text/css" rel="stylesheet" href="/howto/css/howto.css" media="screen,print">
<?php include(_SB_DIR_INCLUDE_."/common/css-pc.html"); ?>
<?php include(_SB_DIR_INCLUDE_."/common/js-old.html"); ?>
</head>
<body>
<noscript>
<p class="noscript">å½“ã‚µã‚¤ãƒˆã‚’ã”è¦§ã„ãŸã ãã«ã¯ãƒ–ãƒ©ã‚¦ã‚¶ã®è¨å®šã§<strong>JavaScriptã‚’æœ‰åŠ¹ã«è¨å®š</strong>ã™ã‚‹å¿…è¦ãŒã”ã–ã„ã¾ã™ã€‚</p>
</noscript>
<?php include(_SB_DIR_INCLUDE_."/common/welcome.html"); ?>
<?php include(_SB_DIR_INCLUDE_."/common/header.html"); ?>
<?php include(_SB_DIR_INCLUDE_."/common/title-scroll.html"); ?>
<div class="mainContents static migration withLocalNav">
<article>
<header class="local">
<h2><?php echo $pageProperties['title']; ?></h2>
<?php include(_SB_DIR_INCLUDE_."/common/sns.html"); ?>
<ul class="backLinks">
<li><a href="/howto/">
<div><p>How to STARBUCKS</p></div>
</a></li>
</ul>
</header>
<div class="mainArea typeWithSideA">
<div id="contentsMainIn" class="newContents">
<div class="container">
<h3 class="order mT0">1.ãƒ“ãƒãƒ¬ãƒƒã‚¸ã‚’é¸ã³ã¾ã—ã‚‡ã†ã€‚</h3>
<p>ã‚³ãƒ¼ãƒ’ãƒ¼ã‚„ãƒ•ãƒ©ãƒšãƒãƒ¼ãƒŽã®ä»–ã‚‚ã€ã‚³ã‚³ã‚¢ã‚„ã‚¸ãƒ¥ãƒ¼ã‚¹ã‚‚ã”ç”¨æ„ã—ã¦ã„ã¾ã™ã€‚</p>
<ul class="listInline becerage mB35">
<li><img src="/howto/store/images/img-order-coffee.jpg" width="159" height="218" alt="ã‚³ãƒ¼ãƒ’ãƒ¼ é«˜å“è³ªã®ã‚¢ãƒ©ãƒ“ã‚«ç¨®ã‚³ãƒ¼ãƒ’ãƒ¼è±†ã‚’ä½¿ç”¨ã—ãŸå®šç•ªãƒ“ãƒãƒ¬ãƒƒã‚¸ã€‚"></li>
<li><img src="/howto/store/images/img-order-espresso.jpg" width="160" height="218" alt="ã‚¨ã‚¹ãƒ—ãƒ¬ãƒƒã‚½ ãƒ“ãƒãƒ¬ãƒƒã‚¸ å®Œç’§ã«æŠ½å‡ºã•ã‚ŒãŸã‚¨ã‚¹ãƒ—ãƒ¬ãƒƒã‚½ã‚’ä½¿ç”¨ã—ãŸãƒ“ãƒãƒ¬ãƒƒã‚¸ã€‚"></li>
<li><img src="/howto/store/images/img-order-frappuccino.jpg" width="159" height="218" alt="ãƒ•ãƒ©ãƒšãƒãƒ¼ãƒŽÂ® ä¸€å¹´ã‚’é€šã—ã¦ç¾Žå‘³ã—ãæ¥½ã—ã‚ã‚‹ã€ãƒ•ãƒãƒ¼ã‚ºãƒ³ãƒ“ãƒãƒ¬ãƒƒã‚¸ã€‚"></li>
<li class="lastChild"><img src="/howto/store/images/img-order-tea.jpg" width="155" height="218" alt="ãƒ†ã‚£ãƒ¼ãƒ“ãƒãƒ¬ãƒƒã‚¸ãƒ»ãã®ä»– ãƒ†ã‚£ãƒ¼ã€ã‚³ã‚³ã‚¢ã€100ï¼…ã‚¸ãƒ¥ãƒ¼ã‚¹ãªã©ã‚‚ã‚ã‚Šã¾ã™ã€‚"></li>
</ul>
<div class="listWithTypeA">
<p class="mB15">å®šç•ªãƒ“ãƒãƒ¬ãƒƒã‚¸ã®ã»ã‹ã«ã‚‚ã€å£ç¯€ã«åˆã‚ã›ãŸãŠã™ã™ã‚ã®ãƒ“ãƒãƒ¬ãƒƒã‚¸ã‚‚ã”ç”¨æ„ã—ã¦ã„ã¾ã™ã€‚</p>
<ul class="links mB30">
<li><a href="/beverage/">ãƒ“ãƒãƒ¬ãƒƒã‚¸ãƒ¡ãƒ‹ãƒ¥ãƒ¼ä¸€è¦§</a></li>
</ul>
<p class="lightFontS mB0">My Starbucksä¼šå“¡ã®çš†æ§˜ã«ã¯ã€å£ç¯€é™å®šã®ãƒ“ãƒãƒ¬ãƒƒã‚¸ã‚’ã„ã¡æ—©ãç¢ºèªã§ãã‚‹å…ˆè¡Œå‘ŠçŸ¥ã‚’è¡Œã£ã¦ãŠã‚Šã¾ã™ã€‚</p>
<p class="itemNotes mB15">ç™»éŒ²ã¯ç„¡æ–™ã§ã™</p>
<ul class="links">
<li><a href="/register/mystarbucks/input/#input">My Starbucksä¼šå“¡ç™»éŒ²</a></li>
</ul>
<!-- /.listWithTypeA --></div>
<!-- /.container --></div>
<div class="container">
<h3 class="order">2.ã‚µã‚¤ã‚ºã‚‚ã„ã‚ã„ã‚ã€‚</h3>
<p>é£²ã¿ãŸã„é‡ã‚’é£²ã¿ãŸã„ã ã‘ã€‚ã‚µã‚¤ã‚ºã¯4ç¨®é¡žã‹ã‚‰ãŠé¸ã³ãã ã•ã„ã€‚</p>
<ul class="listInline size">
<li><img src="/howto/store/images/index-img-short.jpg" width="155" height="205" alt="ã‚·ãƒ§ãƒ¼ãƒˆ Shortï¼ˆ240mlï¼‰"></li>
<li><img src="/howto/store/images/index-img-tall.jpg" width="155" height="205" alt="ãƒˆãƒ¼ãƒ« Tallï¼ˆ350mlï¼‰"></li>
<li><img src="/howto/store/images/index-img-grande.jpg" width="155" height="205" alt="ã‚°ãƒ©ãƒ³ãƒ‡ Grandeï¼ˆ470mlï¼‰"></li>
<li class="lastChild"><img src="/howto/store/images/index-img-venti.jpg" width="155" height="205" alt="ãƒ™ãƒ³ãƒ†ã‚£ VentiÂ®ï¼ˆ590mlï¼‰"></li>
</ul>
<ul class="notes light fontS">
<li><span class="mark">â€»</span>å„ã‚µã‚¤ã‚ºã®å®¹é‡ã¯ã€ç›®å®‰ã§ã™ã€‚</li>
<li><span class="mark">â€»</span>ã‚¢ã‚¤ã‚¹ãƒ‰ãƒªãƒ³ã‚¯ã®ã‚·ãƒ§ãƒ¼ãƒˆã‚µã‚¤ã‚ºã¯300mlã§ã™ã€‚</li>
</ul>
<!-- /.container --></div>
<div class="container last">
<h3 class="order">3.ãƒ“ãƒãƒ¬ãƒƒã‚¸ã‚’è‡ªåˆ†å¥½ã¿ã®å‘³ã‚ã„ã«ã€‚</h3>
<p>ãƒ“ãƒãƒ¬ãƒƒã‚¸ã¯ãŠå¥½ã¿ã«åˆã‚ã›ã¦ã€è‡ªç”±ã«ã‚«ã‚¹ã‚¿ãƒžã‚¤ã‚ºã™ã‚‹ã“ã¨ãŒã§ãã¾ã™ã€‚</p>
<div class="col">
<div class="col2">
<h4 class="order">ãƒ¬ã‚¸ã§ <span>at Cash register</span></h4>
<p class="mB20"><img src="/howto/store/images/img-order-arrange.jpg" alt="ãƒŸãƒ«ã‚¯ã‚’é¸ã‚“ã ã‚Š ã‚·ãƒãƒƒãƒ—ã‚„ã‚½ãƒ¼ã‚¹ã‚’è¿½åŠ ã—ãŸã‚Š ã‚¨ã‚¹ãƒ—ãƒ¬ãƒƒã‚½ã‚·ãƒ§ãƒƒãƒˆã‚’è¿½åŠ ã—ã¦é¢¨å‘³ã‚’ã‚ˆã‚Šæ·±ã" width="318" height="154"></p>
<p class="tasteTxt mB0">ã‚ªãƒ¼ãƒ€ãƒ¼æ™‚ã«ã€ãƒãƒªã‚¹ã‚¿ã«ãŠå°‹ããã ã•ã„ã€‚<br>
ãŠå¥½ã¿ã®å‘³ã‚’è¦‹ã¤ã‘ã‚‹ãŠæ‰‹ä¼ã„ã‚’ã•ã›ã¦ã„ãŸã ãã¾ã™ã€‚<br>
è‡ªåˆ†ã«ã´ã£ãŸã‚Šã®å‘³ã«å‡ºä¼šãˆã‚‹ã‹ã‚‚ã—ã‚Œã¾ã›ã‚“ã€‚</p>
<!-- /.col2 --></div>
<div class="col2">
<h4 class="order">ã‚³ãƒ³ãƒ‡ã‚£ãƒ¡ãƒ³ãƒˆãƒãƒ¼ã§ <span>at Condiment bar</span></h4>
<p class="mB20"><img src="/howto/store/images/img-order-bar.jpg" alt="" width="318" height="154"></p>
<p class="tasteTxt mB0">ã‚³ãƒ³ãƒ‡ã‚£ãƒ¡ãƒ³ãƒˆãƒãƒ¼ã§ãŠå¥½ã¿ã®å‘³ã‚ã„ã«ã€‚<br>
ã‚³ãƒ¼ãƒ’ãƒ¼ã‚„ç´…èŒ¶ã«åŠ ãˆã‚‹ãƒŸãƒ«ã‚¯ã¯2ç¨®é¡žã€‚ãŠç ‚ç³–ã¯3ç¨®é¡žã€‚é¦™ã‚Šè±Šã‹ã«ãªã‚‹ãƒ‘ã‚¦ãƒ€ãƒ¼ãªã©ã‚‚ã”ç”¨æ„ã—ã¦ã„ã¾ã™ã€‚</p>
<!-- /.col2 --></div>
<!-- /.col --></div>
<div class="withImgCol listWithTypeB mB45">
<ul class="btns row imgR mT3">
<li><a href="/howto/customize/index.html">How to ã‚«ã‚¹ã‚¿ãƒžã‚¤ã‚º</a></li>
</ul>
<p class="txtL">ã‚«ã‚¹ã‚¿ãƒžã‚¤ã‚ºã«ã¤ã„ã¦è©³ã—ãã¯ã“ã¡ã‚‰ã§ã€‚</p>
<!-- /.withImgCol.listWithTypeB.mB45 --></div>
<div class="arrangeBorderWrap">
<div class="arrangeBorder pT30 pB10">
<div class="withImgCol">
<p class="imgL"><img src="/howto/store/images/img-order-lid.jpg" alt="" width="160" height="97"></p>
<div class="txtR">
<h4 class="order">ã“ã®ãƒ•ã‚¿ã€å–ã‚‰ãšã«é£²ã‚“ã§ã¿ã¦ã€‚</h4>
<p>æ©ããªãŒã‚‰ã‚³ãƒ¼ãƒ’ãƒ¼ã‚’æ¥½ã—ã‚“ã ã‚Šã€æ¸©ã‹ãä¿ã¤åŠ¹æžœã¯ã‚‚ã¡ã‚ã‚“ã€<br>
ã“ã®ãƒ•ã‚¿ã«é–‹ã„ãŸå°ã•ãªé£²ã¿å£ã‹ã‚‰ç›´æŽ¥é£²ã‚€ã¨ã€ãƒ•ã‚©ãƒ¼ãƒ ãƒŸãƒ«ã‚¯ã‚„ãƒ›ã‚¤ãƒƒãƒ—ã‚¯ãƒªãƒ¼ãƒ ãŒç¨‹ã‚ˆãæ··ã–ã‚Šåˆã„ã€æœ€å¾Œã¾ã§ãŠã„ã—ãå‘³ã‚ãˆã¾ã™ã€‚ãœã²ãŠè©¦ã—ãã ã•ã„ã€‚</p>
<!-- /.txtR --></div>
<!-- /.withImgCol --></div>
<!-- /.arrangeBorder.pT30.pB10 --></div>
<div class="arrangeBorder last pT30">
<div class="withImgCol">
<p class="imgL"><img src="/howto/store/images/img-order-bring.jpg" alt="" width="160" height="119"></p>
<div class="txtR">
<h4 class="order">Bring My Cup</h4>
<p class="mB15">ãƒ‰ãƒªãƒ³ã‚¯ã‚’ã”è³¼å…¥ã®éš›ã€ã”è‡ªåˆ†ã®ã‚¿ãƒ³ãƒ–ãƒ©ãƒ¼ã‚„ãƒžã‚°ã‚«ãƒƒãƒ—ã‚’ãŠæŒã¡ã„ãŸã ãã¨ã€<br>
è³‡æºã®ç¯€ç´„ã«ã”å”åŠ›ã„ãŸã ã„ãŸãŠç¤¼ã¨ã—ã¦ã€ç¨ŽæŠœæœ¬ä½“ä¾¡æ ¼ã‹ã‚‰20å††å€¤å¼•ã—ã¾ã™ã€‚<br>
<ul class="links mB30">
<li><a href="http://www.starbucks.co.jp/csr/environment/green_stores.html">ã‚¹ã‚¿ãƒ¼ãƒãƒƒã‚¯ã‚¹ç’°å¢ƒã¸ã®å–ã‚Šçµ„ã¿</a></li>
</ul>
<p class="txtR">ãŠæ°—ã«å…¥ã‚Šã®ãƒ‰ãƒªãƒ³ã‚¯ã‚’ã€ãŠæ°—ã«å…¥ã‚Šã®ã‚¿ãƒ³ãƒ–ãƒ©ãƒ¼ã«å…¥ã‚Œã¦ã€‚<br>
ä¿æ¸©æ€§ã«å„ªã‚ŒãŸã‚¿ãƒ³ãƒ–ãƒ©ãƒ¼ãªã‚‰ã€å¥½ããªã¨ãã«å¥½ããªå ´æ‰€ã§ãŠã„ã—ãå‘³ã‚ãˆã¾ã™ã€‚</p>
<!-- /.txtR --></div>
<!-- /.withImgCol --></div>
<!-- /.arrangeBorder.last.pT30 --></div>
<!-- /.arrangeBorderWrap --></div>
<!-- /.container.last --></div>
<!-- /.newContents --></div>
<ul class="backLinks">
<li><a href="/howto/">
<div><p>How to STARBUCKS</p></div>
</a></li>
</ul>
<!-- /.mainArea.typeWithSideA --></div>
<nav class="localNav">
<div class="sideBar">
<ul class="backLinks">
<li><a href="/howto/">How to STARBUCKS</a></li>
</ul>
<ul class="navList">
<li class="is-located">
<p>ãƒ“ãƒãƒ¬ãƒƒã‚¸ã‚’é¸ã¶<span>How to ã‚ªãƒ¼ãƒ€ãƒ¼</span></p>
</li>
<li><a href="/howto/customize/">
<p>ã‚«ã‚¹ã‚¿ãƒžã‚¤ã‚ºã«ãƒˆãƒ©ã‚¤<span>How to ã‚«ã‚¹ã‚¿ãƒžã‚¤ã‚º</span></p></a></li>
<li class="linkParent">
<p>ã‚¹ãƒžãƒ¼ãƒˆã«æ¥½ã—ã‚€</p>
</li>
<li class="lower"><a href="/howto/store/tumbler.html">
<p><span>ã‚¿ãƒ³ãƒ–ãƒ©ãƒ¼</span></p></a></li>
<li class="lower"><a href="/howto/card/">
<p><span>ã‚¹ã‚¿ãƒ¼ãƒãƒƒã‚¯ã‚¹ ã‚«ãƒ¼ãƒ‰</span></p></a></li>
<li><a href="/howto/food/">
<p>ãƒ•ãƒ¼ãƒ‰ã¨ã‚³ãƒ¼ãƒ’ãƒ¼ã‚’æ¥½ã—ã‚€</p></a></li>
<li><a href="/customize/">
<p>ãŠæ°—ã«å…¥ã‚Šã®ä¸€æ¯ã‚’ã•ãŒã™</p></a></li>
<li><a href="/howto/coffee/">
<p>è‡ªå®…ã§æ¥½ã—ã‚€<span>at Home</span></p></a></li>
<li class="lower"><a href="/howto/coffee/beans.html">
<p><span>ã‚³ãƒ¼ãƒ’ãƒ¼è±†ã‚’é¸ã¶</span></p></a></li>
<li class="lower"><a href="/howto/coffee/passport.html">
<p><span>ã‚³ãƒ¼ãƒ’ãƒ¼ãƒ‘ã‚¹ãƒãƒ¼ãƒˆï¼†ãƒ“ãƒ¼ãƒ³ã‚ºã‚«ãƒ¼ãƒ‰</span></p></a></li>
<li class="lower"><a href="/howto/coffee/skill.html">
<p><span>ãŠã„ã—ã„ã‚³ãƒ¼ãƒ’ãƒ¼ã‚’ã„ã‚Œã‚‹ã‚³ãƒ„</span></p></a></li>
<li class="lower"><a href="/howto/coffee/seminar-kigu.html">
<p><span>ã‚³ãƒ¼ãƒ’ãƒ¼ã‚»ãƒŸãƒŠãƒ¼/ã‚³ãƒ¼ãƒ’ãƒ¼å™¨å…·</span></p></a></li>
<li><a href="/howto/office/">
<p>ã‚ªãƒ•ã‚£ã‚¹ã§æ¥½ã—ã‚€<span>at Office</span></p></a></li>
<li><a href="/howto/mystarbucks/">
<p>My Starbucksã§æ¥½ã—ã‚€<span>ä¼šå“¡ç™»éŒ²</span></p></a></li>
<li><a href="/howto/index.html#andMore">
<p>ä¾¿åˆ©ãªã‚µãƒ¼ãƒ“ã‚¹</p></a></li>
</ul>
<!-- /.sideBar --></div>
</nav>
<?php include(_SB_DIR_INCLUDE_."/common/sns-footer.html"); ?>
</article>
<!-- /.mainContents.static.migration.withLocalNav --></div>
<?php include(_SB_DIR_INCLUDE_."/common/footer.html"); ?>
<?php include(_SB_DIR_INCLUDE_."/common/nav-os.html"); ?>
</body>
</html>

## Attachments
No attachments
