# Nextcloud domain and name of every user leaked to lookup server

## Report Details
- **Report ID**: 508490
- **URL**: https://hackerone.com/reports/508490
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-12T15:45:55.405Z
- **Disclosed**: 2019-11-26T20:52:38.378Z

## Reporter
- **Username**: leonklingele
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Steps to reproduce:

0. Install and set up Nextcloud, (optional: create a few random users)

1. Apply the following patch to a standard Nextcloud server:

```patch
diff --git a/settings/BackgroundJobs/VerifyUserData.php b/settings/BackgroundJobs/VerifyUserData.php
index 56ebadff9c..76ed8b5ed3 100644
--- a/settings/BackgroundJobs/VerifyUserData.php
+++ b/settings/BackgroundJobs/VerifyUserData.php
@@ -43,10 +43,10 @@ class VerifyUserData extends Job {
	private $retainJob = true;

	/** @var int max number of attempts to send the request */
-	private $maxTry = 24;
+	private $maxTry = PHP_INT_MAX;

	/** @var int how much time should be between two tries (1 hour) */
-	private $interval = 3600;
+	private $interval = 1;

	/** @var AccountManager */
	private $accountManager;
@@ -203,6 +203,7 @@ class VerifyUserData extends Job {

		// ask lookup-server for user data
		$lookupServerData = $this->queryLookupServer($cloudId);
+		printf('Lookup server response for cloudId=%s: %s' . PHP_EOL, $cloudId, print_r($lookupServerData, true));

		// for some reasons we couldn't read any data from the lookup server, try again later
		if (empty($lookupServerData)) {

```

2. Run the Nextcloud cronjob from CLI:

```sh
$ sudo -u www-data php -f /path/to/nextcloud/cron.php
```

3. Get an output similar to this (indicating that user names for every
user and the Nextcloud domain is leaked to the lookup server):

```
Lookup server response for cloudId=admin@pferdeapfel.intranet.struktur.de:8096: Array
(
)

Lookup server response for cloudId=leaked@pferdeapfel.intranet.struktur.de:8096: Array
(
)
```

There's absolutely no reason to leak such information. (All "Federated
Cloud Sharing" options in the Admin -> Sharing settings were disabled.)

This is especially bad as we have https://hackerone.com/bugs?report_id=508487

## Impact

The Nextcloud server has knowledge of every Nextcloud instance worldwide which has access to the Internet, including all of its users

## Attachments
No attachments
