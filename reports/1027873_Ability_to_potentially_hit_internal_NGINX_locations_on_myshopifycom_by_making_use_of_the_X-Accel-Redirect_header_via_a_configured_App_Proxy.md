# Ability to potentially hit internal NGINX locations on *.myshopify.com by making use of the `X-Accel-Redirect` header via a configured App Proxy

## Report Details
- **Report ID**: 1027873
- **URL**: https://hackerone.com/reports/1027873
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-11-06T00:57:41.300Z
- **Disclosed**: 2021-02-11T20:28:28.527Z

## Reporter
- **Username**: imgnotfound
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
By making use of the [Shopify App Proxy](https://shopify.dev/tutorials/display-data-on-an-online-store-with-an-application-proxy-app-extension) and the [**X-Accel** feature of NGINX](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/), it is possible to hit any configured `internal` NGINX location as your current configuration is not ignoring the `X-Accel-Redirect` header response from an upstream service. 

The way it works is that NGINX allows internal redirection to a location determined by that header returned from a backend - in our case being the configured **App Proxy** backend controlled by the attacker.

For example, the following request would ends up hitting `http://private-service/flag`
{F1067100}

However, I did some very basic fuzzing and wasn't able to hit anything but still reporting and will let you guys assess the risk.

## Steps to reproduce
### Create a service that return a X-Accel-Redirect header
First step, is to create a server that is returning a response with the `X-Accel-Redirect` header.
1. Open [mocky.io](https://designer.mocky.io/design)
2. Within the **HTTP Headers** section, enter:
```
{
	"X-Accel-Redirect": "/collections/all"
}
```
3. Scroll down and click **Generate my HTTP response** and copy the **Mock URL**

Otherwise, you can simply use https://run.mocky.io/v3/d7cdfcbc-6994-4f3b-a323-fe8377535507 which is already configured per above steps

### Setup the App Proxy
1. Within Shopify Partners, create a new private application and install it on your shop
1. From that application setup, go to **Extensions > Online Store** and setup an **App proxy**
1. From that **App proxy** configuration, set the following values:
	1. Subpath prefix: `a`
	1. Subpath `apps`
	1. Proxy URL `https://run.mocky.io/v3/d7cdfcbc-6994-4f3b-a323-fe8377535507` or enter your own mock URL 
1. Within your browser, open your `https://{shop}.myshopify.com/a/apps` by taking care of replacing the `{shop}` placeholder with your actual shop name on which you installed the application

As a result, you are being proxied your current shop `/collections/all` page proving that your current NGINX configuration follows the `X-Accel-Redirect` directive. 

## Mitigation
To mitigate this issue, a `proxy_ignore_headers X-Accel-Redirect` directive should be set in your NGINX configuration as described in the [NGINX documentation](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_ignore_headers)

## Impact

As mentioned, I wasn't actually able to hit any of your internal routes but that could only mean that my URL fuzzing wasn't good enough or that you actually do not have any configured internal routes on that proxy.

## Attachments
- SS.png
