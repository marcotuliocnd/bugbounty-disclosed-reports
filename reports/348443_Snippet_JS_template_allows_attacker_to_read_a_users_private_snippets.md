# Snippet JS template allows attacker to read a user's private snippets

## Report Details
- **Report ID**: 348443
- **URL**: https://hackerone.com/reports/348443
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-05-08T03:09:57.685Z
- **Disclosed**: 2019-03-03T03:03:14.355Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
These days snippets can be embedded in a site other than the GitLab instance. An embed link is only generated for public snippets, as can be seen in the `app/views/shared/snippets/_header.html.haml`:

```haml
  - if public_snippet?
    .embed-snippet
      .input-group
        .input-group-btn
          %button.btn.embed-toggle{ 'data-toggle': 'dropdown', type: 'button' }
            %span.js-embed-action= _("Embed")
            = sprite_icon('angle-down', size: 12)
          %ul.dropdown-menu.dropdown-menu-selectable.embed-toggle-list
```

When visiting a public snippet, the embed link is shown at the top of the page, as such:

{F294865}

As you can see, there's no entropy other than the snippet ID, which is an auto incrementing ID. It turns out that the controller itself doesn't limit the user to generate a JS template for a private snippet though. When appending `.js` to a private snippet, it'll return the JavaScript template, which contains the contents of a private snippet. This can be used to access a private snippet the attacker doesn't have access to from a 3rd party website.

To reproduce, sign in on gitlab.com and create a private snippet. For the sake of the PoC, let's create global snippet (not one that is tied to a project). It also works with a project, but in that case the attacker has to know the namespace and project path. Here's a PoC that'll call the `alert` function with the first line of a private snippet:

```html
<html>
<head>
<style>
.gitlab-embed-snippets {
  display: none;
}
</style>
<script src="https://gitlab.com/snippets/1714319.js"></script>
</head>
<body>
  <script>
    alert(document.getElementById('LC1').innerHTML);
  </script>
</body>
</html>
```

Simply replace the snippet ID in the `script` tag with whichever snippet ID the private snippet has. Save the HTML and load it from any other location, e.g. localhost or some domain. You'll notice that it'll alert the first line of the contents:

{F294866}

## Impact

An attacker could enumerate IDs and inject multiple `script` tags to try to determine the contents of private snippets. Not knowing which snippet IDs belong to a user increases the attack complexity, which lowers the overall severity of the vulnerability. Private snippets may contain sensitive information that is not supposed to be viewable to anyone outside of the creator itself.

## Attachments
- Screen_Shot_2018-05-07_at_8.01.10_PM.png
- Screen_Shot_2018-05-07_at_8.05.10_PM.png
