# Wordpress Users Disclosure (/wp-json/wp/v2/users/) on sifchain.finance

## Report Details
- **Report ID**: 1195194
- **URL**: https://hackerone.com/reports/1195194
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-12T23:42:53.302Z
- **Disclosed**: 2021-05-13T00:43:58.962Z

## Reporter
- **Username**: ibrahimatix0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
##Information:

Using REST API, we can see all the WordPress users/author with some of their information.

##Step To Reproduce:

You can get user info by entering below url in your browser:
https://www.sifchain.finance/wp-json/wp/v2/users/
##Results:

```
[{"id":194643529,"name":"alithecurios","url":"","description":"","link":"https:\/\/sifchain.finance\/author\/alithecurios\/","slug":"alithecurios","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/04fd4bda8c4fbc9e9803b9e7b443d20c?s=24&d=identicon&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/04fd4bda8c4fbc9e9803b9e7b443d20c?s=48&d=identicon&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/04fd4bda8c4fbc9e9803b9e7b443d20c?s=96&d=identicon&r=g"},"meta":{"admin_color":"fresh"},"_links":{"self":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users\/194643529"}],"collection":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users"}]}},{"id":194643526,"name":"Asha Sreekumar","url":"","description":"","link":"https:\/\/sifchain.finance\/author\/asha8fd635db6e9\/","slug":"asha8fd635db6e9","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/921005cc7364499b48fddd53e56631c5?s=24&d=identicon&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/921005cc7364499b48fddd53e56631c5?s=48&d=identicon&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/921005cc7364499b48fddd53e56631c5?s=96&d=identicon&r=g"},"meta":{"admin_color":"fresh"},"_links":{"self":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users\/194643526"}],"collection":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users"}]}},{"id":194418990,"name":"Nick Friedland","url":"http:\/\/sifchain.wordpress.com","description":"","link":"https:\/\/sifchain.finance\/author\/nick0ba02a28924\/","slug":"nick0ba02a28924","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/97d871be405966ec0a282936d91d052a?s=24&d=identicon&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/97d871be405966ec0a282936d91d052a?s=48&d=identicon&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/97d871be405966ec0a282936d91d052a?s=96&d=identicon&r=g"},"meta":{"admin_color":"fresh"},"_links":{"self":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users\/194418990"}],"collection":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users"}]}},{"id":194643527,"name":"thomassifchain","url":"","description":"","link":"https:\/\/sifchain.finance\/author\/thomassifchain\/","slug":"thomassifchain","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/b8b1d369fba5dbcde51a60bd415cdc5a?s=24&d=identicon&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/b8b1d369fba5dbcde51a60bd415cdc5a?s=48&d=identicon&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/b8b1d369fba5dbcde51a60bd415cdc5a?s=96&d=identicon&r=g"},"meta":{"admin_color":"fresh"},"_links":{"self":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users\/194643527"}],"collection":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users"}]}},{"id":194428061,"name":"ultrus77","url":"","description":"","link":"https:\/\/sifchain.finance\/author\/ultrus77\/","slug":"ultrus77","avatar_urls":{"24":"https:\/\/secure.gravatar.com\/avatar\/eb17cf74a5235990f75b618313feb155?s=24&d=identicon&r=g","48":"https:\/\/secure.gravatar.com\/avatar\/eb17cf74a5235990f75b618313feb155?s=48&d=identicon&r=g","96":"https:\/\/secure.gravatar.com\/avatar\/eb17cf74a5235990f75b618313feb155?s=96&d=identicon&r=g"},"meta":{"admin_color":"fresh"},"_links":{"self":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users\/194428061"}],"collection":[{"href":"https:\/\/sifchain.finance\/wp-json\/wp\/v2\/users"}]}}]

```

##Fix:

Use this code will hide the users list and give 404 as the result, while rest of the api calls keep running as they were.

```
add_filter( 'rest_endpoints', function( $endpoints ){
    if ( isset( $endpoints['/wp/v2/users'] ) ) {
        unset( $endpoints['/wp/v2/users'] );
    }
    if ( isset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] ) ) {
        unset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] );
    }
    return $endpoints;
});

```

## Impact

Authors : LTR , LTREditor can be created scenario of doing bruteforce attacks to this users.

## Attachments
No attachments
