# DBMS information getting exposed publicly on -- [ ██████████ ]

## Report Details
- **Report ID**: 2370578
- **URL**: https://hackerone.com/reports/2370578
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-02-11T18:03:43.282Z
- **Disclosed**: 2024-03-22T17:31:51.980Z

## Reporter
- **Username**: dishant_singh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
hi there, 
when i was working on your [domain](█████). i got to know that website is using drupal. and after a long fuzzing i found a file on your domain which was leaking some user hashed and data stored in your DBMS this data could be confidential to you so i am mentioning it below make sure to check carefully.

## Impact

DBMS sensitive data getting leaked on your domain ███████

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit ██████████
2. you will get a file extract it and open that file you will se following things:
```
$connection->insert('aggregator_feed')
->fields(array(
  'fid',
  'uuid',
  'langcode',
  'title',
  'url',
  'refresh',
  'checked',
  'queued',
  'link',
  'description',
  'image',
  'hash',
  'etag',
  'modified',
))
->values(array(
  'fid' => '1',
  'uuid' => 'de39df51-b417-4bf2-a044-68ae0f780d77',
  'langcode' => 'en',
  'title' => 'Test feed',
  'url' => 'https://www.drupal.org/planet/rss.xml',
  'refresh' => '3600',
  'checked' => '1439763863',
  'queued' => '0',
  'link' => 'https://www.drupal.org/planet',
  'description' => 'Drupal.org - aggregated feeds in category Planet Drupal',
  'image' => NULL,
  'hash' => '133c56975228c5f17dd847130e3f1d288cdd405c0a67eb0331f3b274ab9e76c6',
  'etag' => '"1439760783-1"',
  'modified' => '1439760783',
))
```

And infos like below too:
```
->values(array(
  'collection' => '',
  'name' => 'block.block.stark_testblock',
  'data' => 'a:12:{s:4:"uuid";s:36:"0054bb60-0286-4b98-a000-b5791a63f30a";s:8:"langcode";s:2:"en";s:6:"status";b:1;s:12:"dependencies";a:3:{s:7:"content";a:1:{i:0;s:56:"block_content:basic:068eb76b-d90f-4513-8500-ae8bc880bd63";}s:6:"module";a:5:{i:0;s:13:"block_content";i:1;s:8:"language";i:2;s:4:"node";i:3;s:6:"system";i:4;s:4:"user";}s:5:"theme";a:1:{i:0;s:5:"stark";}}s:2:"id";s:15:"stark_testblock";s:5:"theme";s:5:"stark";s:6:"region";s:4:"help";s:6:"weight";i:-7;s:8:"provider";N;s:6:"plugin";s:50:"block_content:068eb76b-d90f-4513-8500-ae8bc880bd63";s:8:"settings";a:7:{s:2:"id";s:50:"block_content:068eb76b-d90f-4513-8500-ae8bc880bd63";s:5:"label";s:10:"Test block";s:8:"provider";s:13:"block_content";s:13:"label_display";s:7:"visible";s:6:"status";b:1;s:4:"info";s:0:"";s:9:"view_mode";s:4:"full";}s:10:"visibility";a:4:{s:8:"language";a:4:{s:2:"id";s:8:"language";s:9:"langcodes";a:1:{s:2:"en";s:2:"en";}s:6:"negate";b:0;s:15:"context_mapping";a:1:{s:8:"language";s:53:"@language.current_language_context:language_interface";}}s:9:"node_type";a:4:{s:2:"id";s:9:"node_type";s:7:"bundles";a:2:{s:7:"article";s:7:"article";s:17:"test_content_type";s:17:"test_content_type";}s:6:"negate";b:0;s:15:"context_mapping";a:1:{s:4:"node";s:29:"@node.node_route_context:node";}}s:12:"request_path";a:4:{s:2:"id";s:12:"request_path";s:5:"pages";s:7:"<front>";s:6:"negate";b:0;s:15:"context_mapping";a:0:{}}s:9:"user_role";a:4:{s:2:"id";s:9:"user_role";s:5:"roles";a:2:{s:13:"authenticated";s:13:"authenticated";s:13:"administrator";s:13:"administrator";}s:6:"negate";b:0;s:15:"context_mapping";a:1:{s:4:"user";s:39:"@user.current_user_context:current_user";}}}}',
))
```

## Suggested Mitigation/Remediation Actions
the file should not be accessible publicly



## Attachments
No attachments
