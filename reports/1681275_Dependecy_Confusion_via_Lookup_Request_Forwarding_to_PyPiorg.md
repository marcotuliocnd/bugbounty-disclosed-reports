# Dependecy Confusion via Lookup Request Forwarding to PyPi.org

## Report Details
- **Report ID**: 1681275
- **URL**: https://hackerone.com/reports/1681275
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-08-26T12:09:55.451Z
- **Disclosed**: 2022-11-21T03:49:27.733Z

## Reporter
- **Username**: usd-responsible-disclosure
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary

*pip* is probably the most popular *Python* package manager and can be used to install packages from the publicly
available *Python Package Index* (*PyPi*) at [pypi.org](https://pypi.org) or form internal package repositories. In the beginning of 2021,
a vulnerability type called *Dependency Confusion* attracted some attention in the information security scene. Several
high profiled companies were identified to accidentally load internal dependencies from the public available index
at *PyPi*. This could have allowed any *PyPi* user to register packages with the accidentally requested names
and to achieve remote code execution on the affected systems.

The underlying reason for the vulnerability was the usage of the `--extra-index-url` parameter when installing packages
via *pip*. This parameter adds additional packages sources where *pip* checks for the desired installation candidate. That
being said, the publicly available index at *PyPi* remains within the sources and will be used if the requested version
of the desired package can be found. In case of no version was specified, *pip* installs the most recent version it finds
among all configured repositories.

After the *Dependency Confusion* got publicly known, the general recommendation was to use `--index-url` instead of
`--extra-index-url`, which replaces [pypi.org](https://pypi.org) as the default package registry. *GitLab*, however, still advises it's
users to use `--extra-index-url` within the web overview of a projects package registry. Therefore, users that are not
aware of *Dependency Confusion*, might accidentally install internal *GitLab* packages from the publicly available index
at *PyPi*.

Moreover, with version `14.2`, *GitLab* made even usage of `--index-url` not fail save. According to the
[documentation](https://docs.gitlab.com/ee/user/admin_area/settings/continuous_integration.html#pypi-forwarding):

> In GitLab 14.2 and later, when a PyPI package is not found in the Package Registry, the request is forwarded to pypi.org.

This configuration can lead to dangerous side effects when installing  internal packages with other internal dependencies
or when using `--index-url` with another internal URL in the `--extra-index-url` parameter. *GitLab* defines package registries on
the project and group level. If package dependecies cross these project or group boundaries, dependecy confusion is possible.

### Steps to reproduce

First, we create a simple python project `usd-example-package` and make it available over the projects package
registry within *GitLab*. Viewing the webpage of the newly created package, it shows the following installation command:

{F1885321}

As one can see, the suggested install command uses the `--extra-index-url` by default, which makes it vulnerable to
dependency confusion.

Now lets go one step further. Within our example package, we add an internal dependency `usd-example-dependecy`. This
dependency is contained within another project and we add `--extra-index-url` to include this within the repository sources.
The installation command now looks like this:

```console
$ pip install usd-example-project --index-url https://gitlab.example.com/api/v4/projects/10/packages/pypi/simple --extra-index-url https://gitlab.example.com/api/v4/projects/11/packages/pypi/simple
```

Since `--index-url` was used, [pypi.org](https://pypi.org) should not be considered when searching for packages and the installation command
should be safe, right? Well, after launching the command, *pip* first loads `usd-example-project` from the URL specified
as `--index-url`:

```http
GET /api/v4/projects/10/packages/pypi/simple/usd-example-dependecy/ HTTP/1.1
Host: gitlab.example.com
```

Afterwards, the `--extra-index-url` is checked as described above, but since it belongs to our internal
trusted *GitLab* instance, this should be fine:

```http
GET /api/v4/projects/11/packages/pypi/simple/usd-example-project/ HTTP/1.1
Host: gitlab.example.com
```

However, since `usd-example-package` is only distributed within the project
with ID 10, the registry for project ID 11 will not find the requested package and forward the request to *PyPi*:

```http
HTTP/1.1 302 Found
Location: https://pypi.org/simple/usd-example-project/
```

Now, although we used `--index-url`, we are again vulnerable to dependency confusion.

### Fix

The reported issue should be fixed by making the following adjustments:

1. The insecure installation command suggested by the repository webpages should be replaced. Instead of `--extra-index-url`,
   the `--index-url` command line option should be chosen.
2. Forwarding of requests for unknown packages to [pypi.org](https://pypi.org) should be disabled by default. This setting can have dangerous side
   effects and should not be enabled by default. Administrators that understand the consequences could still enable the feature
   for their instance.

We are aware that automatic forwarding of unknown packages to *PyPi* increases the usability of internal package registries
quite a lot. Installation of internal tools and dependencies usually also requires installation of packages that are available
on *PyPi*. Restricting the index to an internal repository makes automatic installation of these external dependencies fail,
which creates some additional installation effort. That being said, the accidental installation of potentially malicious software
from a public package registry represents a high security risk for organisations and should be classified as more important as
usability.

Another possible solution would be to only allow forwarding requests to *PyPi* for packages that are not available within the
whole internal *GitLab* instance.

### References

* https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610
* https://docs.gitlab.com/ee/user/packages/pypi_repository/
* https://docs.gitlab.com/ee/user/admin_area/settings/continuous_integration.html#pypi-forwarding

### Credits
This security vulnerability was identified by [Tobias Neitzel](https://twitter.com/qtc_de) of [usd AG](https://www.usd.de/).

## Impact

Dependency Confusion can lead to remote code execution (RCE) on systems that use the insecure installation command. This usually affects developer machines or GitLab runners, but also endusers can be affected.

## Attachments
- usd-2022-0042.png
