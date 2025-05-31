# WordPress Plugin Update Confusion at trafficfactory.com

## Report Details
- **Report ID**: 1364851
- **URL**: https://hackerone.com/reports/1364851
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-10-10T10:59:43.670Z
- **Disclosed**: 2021-11-25T09:11:00.772Z

## Reporter
- **Username**: vavkamil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: trafficfactory

## Vulnerability Information
Hi,

I'm currently researching a "novel" supply chain attack affecting WordPress plugins, and I believe your website might be vulnerable.

The way it works is similar to a recent [Dependency Confusion](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610) attack, where a malicious actor can take over internal packages unclaimed on PyPI / npm registry.

If you use an internally developed WordPress plugin not present in WordPress Plugin Directory, an attacker might upload it there. That would introduce the "[Confused deputy problem](https://en.wikipedia.org/wiki/Confused_deputy_problem)" attack scenario, where the privileged user, instructed to update all plugins regularly, inadvertently infects the instance with malware.

I wrote a custom scanner, which passively detects plugins on a front page (JS/CSS assets), and searches the slug name in the WP SVN registry. It found "tf-elementor" plugin installed at "trafficfactory.com":

`https://www.trafficfactory.com/wp-content/plugins/tf-elementor/assets/css/tf9d3a.css?ver=5.6.5`

currently not present in:

`https://plugins.svn.wordpress.org/tf-elementor`

## Steps To Reproduce:

The WordPress approval process for new plugins is automated and [open-source](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/shortcodes/class-upload-handler.php), so it's possible to see which checks needs to pass:

- Slug must only contain lowercase alphanumeric characters and dash.
- Slug can't have a reserved name like wp-admin (`has_reserved_slug()`)
- Slug can't be on a list of protected trademarks (`has_trademarked_slug()`)
- Slug can't be installed on more than 100 websites (`wporg_stats_get_plugin_name_install_count`)

The whole flow looks like this:

1. An attacker submits a plugin with the same name you use for a review
2. It will pass the review process, and the attacker gets access to the SVN repository
3. The attacker uploads the plugin files, and it's added to the WordPress Plugin Directory for anyone to use
4. The attacker adds a backdoor and bumps the plugin version
5. You will get a notification that a new update is available; when you update, your website gets compromised

I did not attempt to claim your plugin, as the update would inadvertently break the website (old plugin files will get deleted), but I simulated the attack with [my custom plugin](https://wordpress.org/plugins/xml-rpc-settings/), and it works.

## How to mitigate

There is no easy way to defend yourself because it's by design, and WordPress doesn't allow you to upload a "dummy" version of your plugin. You can either add the plugin you use in the WordPress Plugin Directory or change the plugin name to prevent the review process from succeeding.
The plugin slug can only contain lower case alphanumeric characters and dash as a delimiter. Some of the keywords are prohibited as well, which could help us in this case. That means that you can rename your custom plugins in the following ways:

- `internal_plugin_name`
- `InternalPluginName`
- `wp-internal-plugin-name`

It is also possible to leverage a [hook](https://developer.wordpress.org/reference/hooks/upgrader_package_options/) and write a custom update function, blocking the internal WP API call and replacing it with your own, similar to how a paid plugin offers custom updates from their servers.

Some plugins do that for you, for example, [Easy Updates Manager](https://wordpress.org/plugins/stops-core-theme-and-plugin-updates/), which allows you to block updates for specific plugins.

## Supporting Material/References:

I wrote a custom scanner in Python, a WordPress Docker container to simulate the Plugin update process, a custom plugin to pass the review for the SVN registry, and an extensive write-up describing everything in more detail.

I plan to publish everything soon, but let me know, and I will share a draft with you beforehand. Feel free to requests any additional info from me, as I understand it sounds more like a theoretical vulnerability without a valid PoC.

Thank you!

Kind regards,
@vavkamil

## Impact

An attacker can hijack your plugin, currently not available in the WordPress Plugin Directory (SVN registry). If that happens and you update the plugin, it can introduce a backdoor or RCE, essentially giving keys to the kingdom to the attacker.

## Attachments
No attachments
