# Multiple Path Disclosure

## Report Details
- **Report ID**: 9485
- **URL**: https://hackerone.com/reports/9485
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-04-24T05:43:26.433Z
- **Disclosed**: 2016-07-16T06:44:03.836Z

## Reporter
- **Username**: anant
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hi Ian,

I have downloaded all the latest version's of plugin's from your wp profile and did a quick check for FPD. I know you may point out that WP does'nt consider it as a issue however i personally for plugin i look at it as a miss on best practice from plugin developers part.

I do not expect a reward for this but informing so that issue could be corrected.

List of FPD spotted (I know some of these you have already stated you may not be able to modify : but putting it out as its not a big risk however its good to know such error exists).

http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/basic-google-maps-placemarks.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/unit-tests.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/views/front-end-head.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/views/message.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/views/meta-address.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/views/meta-re-abolish-slavery.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/views/meta-z-index.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/views/settings-marker-clusterer.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/views/settings.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/views/shortcode-bgmp-list-marker.php
 http://localhost/wpcheck/wp-content/plugins/basic-google-maps-placemarks.1.10.3/basic-google-maps-placemarks/views/shortcode-bgmp-map.php
 http://localhost/wpcheck/wp-content/plugins/camptix-network-tools.0.1/camptix-network-tools/camptix-network-tools.php
 http://localhost/wpcheck/wp-content/plugins/camptix-network-tools.0.1/camptix-network-tools/includes/class-camptix-network-attendees-list-table.php
 http://localhost/wpcheck/wp-content/plugins/camptix-network-tools.0.1/camptix-network-tools/includes/class-camptix-network-dashboard-list-table.php
 http://localhost/wpcheck/wp-content/plugins/camptix-network-tools.0.1/camptix-network-tools/includes/class-camptix-network-log-list-table.php
 http://localhost/wpcheck/wp-content/plugins/camptix-network-tools.0.1/camptix-network-tools/network-dashboard.php
 http://localhost/wpcheck/wp-content/plugins/email-post-changes.1.7/email-post-changes/class.email-post-changes.php
 http://localhost/wpcheck/wp-content/plugins/email-post-changes.1.7/email-post-changes/email-post-changes.php
 http://localhost/wpcheck/wp-content/plugins/email-post-changes.1.7/email-post-changes/unified.php
 http://localhost/wpcheck/wp-content/plugins/google-authenticator-encourage-user-activation.0.1/google-authenticator-encourage-user-activation/bootstrap.php
 http://localhost/wpcheck/wp-content/plugins/google-authenticator-encourage-user-activation.0.1/google-authenticator-encourage-user-activation/views/force-notice.php
 http://localhost/wpcheck/wp-content/plugins/google-authenticator-encourage-user-activation.0.1/google-authenticator-encourage-user-activation/views/nag-notice.php
 http://localhost/wpcheck/wp-content/plugins/google-authenticator-encourage-user-activation.0.1/google-authenticator-encourage-user-activation/views/requirements-error.php
 http://localhost/wpcheck/wp-content/plugins/google-authenticator-encourage-user-activation.0.1/google-authenticator-encourage-user-activation/views/settings-fields.php
 http://localhost/wpcheck/wp-content/plugins/google-authenticator-encourage-user-activation.0.1/google-authenticator-encourage-user-activation/views/settings-section.php
 http://localhost/wpcheck/wp-content/plugins/google-authenticator-per-user-prompt.0.4/google-authenticator-per-user-prompt/bootstrap.php
 http://localhost/wpcheck/wp-content/plugins/google-authenticator-per-user-prompt.0.4/google-authenticator-per-user-prompt/views/requirements-error.php
 http://localhost/wpcheck/wp-content/plugins/google-authenticator-per-user-prompt.0.4/google-authenticator-per-user-prompt/views/token-prompt.php http://localhost/wpcheck/wp-content/plugins/google-authenticator-encourage-user-activation.0.1/google-authenticator-encourage-user-activation/views/settings-fields.php
 http://localhost/wpcheck/wp-content/plugins/manage-tags-capability.1.1.1/manage-tags-capability/manage_tags_capability.php
 http://localhost/wpcheck/wp-content/plugins/manage-tags-capability.1.1.1/manage-tags-capability/views/meta_box.php
 http://localhost/wpcheck/wp-content/plugins/overwrite-uploads.1.1/overwrite-uploads/bootstrap.php
 http://localhost/wpcheck/wp-content/plugins/overwrite-uploads.1.1/overwrite-uploads/classes/overwrite-uploads.php
 http://localhost/wpcheck/wp-content/plugins/overwrite-uploads.1.1/overwrite-uploads/views/requirements-error.php
 http://localhost/wpcheck/wp-content/plugins/p2-new-post-categories.0.3/p2-new-post-categories/p2-new-post-categories.php
 http://localhost/wpcheck/wp-content/plugins/re-abolish-slavery-ribbon.1.0.4/re-abolish-slavery-ribbon/re-abolish-slavery-ribbon.php
 http://localhost/wpcheck/wp-content/plugins/re-abolish-slavery-ribbon.1.0.4/re-abolish-slavery-ribbon/views/ribbon-markup.php
 http://localhost/wpcheck/wp-content/plugins/re-abolish-slavery-ribbon.1.0.4/re-abolish-slavery-ribbon/views/setting-fields.php
 http://localhost/wpcheck/wp-content/plugins/re-abolish-slavery-ribbon.1.0.4/re-abolish-slavery-ribbon/views/settings.php
 http://localhost/wpcheck/wp-content/plugins/rescue-children-banner.1.0/rescue-children-banner/bootstrap.php
 http://localhost/wpcheck/wp-content/plugins/rescue-children-banner.1.0/rescue-children-banner/views/banner-markup.php
 http://localhost/wpcheck/wp-content/plugins/rescue-children-banner.1.0/rescue-children-banner/views/requirements-not-met.php
 http://localhost/wpcheck/wp-content/plugins/rescue-children-banner.1.0/rescue-children-banner/views/setting-fields.php
 http://localhost/wpcheck/wp-content/plugins/rescue-children-banner.1.0/rescue-children-banner/views/settings.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/bootstrap.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/classes/tagregator.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/classes/tggr-media-source.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/classes/tggr-settings.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/classes/tggr-shortcode-tagregator.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/classes/tggr-source-flickr.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/classes/tggr-source-instagram.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/classes/tggr-source-twitter.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/requirements-error.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-settings/page-settings.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-shortcode-tagregator/shortcode-tagregator.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-source-flickr/page-settings-fields.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-source-flickr/page-settings-section-header.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-source-flickr/shortcode-tagregator-media-item.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-source-instagram/page-settings-fields.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-source-instagram/page-settings-section-header.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-source-instagram/shortcode-tagregator-media-item.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-source-twitter/page-settings-fields.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-source-twitter/page-settings-section-header.php
 http://localhost/wpcheck/wp-content/plugins/tagregator.0.4/tagregator/views/tggr-source-twitter/shortcode-tagregator-media-item.php


## Attachments
No attachments
