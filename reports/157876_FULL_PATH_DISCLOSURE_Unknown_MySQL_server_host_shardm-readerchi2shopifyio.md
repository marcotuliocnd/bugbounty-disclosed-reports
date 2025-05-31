# (FULL PATH DISCLOSURE) Unknown MySQL server host 'shardm-reader.chi2.shopify.io'  

## Report Details
- **Report ID**: 157876
- **URL**: https://hackerone.com/reports/157876
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-09T14:26:51.118Z
- **Disclosed**: 2016-09-01T15:57:38.623Z

## Reporter
- **Username**: jamesclyde
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hello,

Found a website of you guys that is poiting to: shardm-reader.chi2.shopify.io' 
This domain is disclosure fill path because there is none MySQL server host.

POC: https://104.196.154.1/

Response a whole page with path disclosures:

lib/patches/mysql_monitoring.rb:19:in `connect'
lib/patches/mysql_monitoring.rb:19:in `block in raw_connect_with_monitoring'
lib/patches/mysql_monitoring.rb:18:in `raw_connect_with_monitoring'
lib/routing/connection.rb:15:in `connection'
app/models/concerns/benchmarking.rb:15:in `block (2 levels) in add_benchmark_around_method'
app/models/concerns/benchmarking.rb:24:in `with_benchmark'
app/models/concerns/benchmarking.rb:14:in `block in add_benchmark_around_method'
app/models/shop.rb:619:in `for_domain'
app/controllers/application_controller.rb:303:in `shop_for'
app/controllers/application_controller.rb:96:in `with_shop_fallback'
app/controllers/application_controller.rb:87:in `with_shop'
app/controllers/application_controller.rb:73:in `set_billing_api_request_id'
app/controllers/application_controller.rb:64:in `add_request_id_to_log_context'
app/controllers/application_controller.rb:245:in `conditionally_enable_debug_log'
app/controllers/application_controller.rb:54:in `block in identity_cache_memoization'
app/controllers/application_controller.rb:54:in `identity_cache_memoization'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:284:in `call'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:284:in `block in measure'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:53:in `duration'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:284:in `measure'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:75:in `block (3 levels) in statsd_measure'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:284:in `call'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:284:in `block in measure'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:53:in `duration'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:284:in `measure'
/artifacts/ruby/2.2.0/bundler/gems/statsd-instrument-50b2496ea65b/lib/statsd/instrument.rb:75:in `block (2 levels) in statsd_measure'
semian (0.4.1) lib/semian/mysql2.rb:82:in `block in connect'


Please let me know!!

## Attachments
No attachments
