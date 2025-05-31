# Null Pointer Dereference by Crafted Response from AI Model

## Report Details
- **Report ID**: 2958097
- **URL**: https://hackerone.com/reports/2958097
- **State**: Closed
- **Severity**: low
- **Submitted**: 2025-01-25T14:41:24.748Z
- **Disclosed**: 2025-03-26T02:02:48.851Z

## Reporter
- **Username**: canalun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.

## Summary:

- This is regarding Leo AI's "Bring your own model" feature.
- An attacker has to make user set a malicious endpoint as AI's "Server endpoint".
- The code handling a server response assumes a specific structure without validating it. As a result, null pointer dereference causes by a crafted response.

## Products affected: 

Brave browser: Version 1.74.50 Chromium: 132.0.6834.111 (Official Build) (arm64)
(fyi: OS: macOS sequoia 15.2)

## Steps To Reproduce:

- Open `brave://settings/leo-assistant`.
- In "Bring your own model", add a model with the below params.
  - Label: `test`
  - Model request name: `test`
  - Server endpoint: `https://canalun.company/57e23a24db994321970941049b05d1bb`
  - Context size: `4000` (default)
  - API Key: `AAAAAAAAAAAAAAAAAAAAAA` (anything is ok)
  - System Prompt: `` (empty. default)
- On any web page, open Leo AI sidebar, choose this model, and push the `Suggest quetions...` button.
- Even if you open several tabs, the entire browser crash.

## Supporting Material/References:

Log when reproducing it on local build.
```
Received signal 11 SEGV_ACCERR 000000000017
0   libbase.dylib                       0x0000000105a14de4 base::debug::CollectStackTrace(base::span<void const*, 18446744073709551615ul, void const**>) + 28
1   libbase.dylib                       0x00000001059fbb84 base::debug::StackTrace::StackTrace(unsigned long) + 108
2   libbase.dylib                       0x0000000105a14cc0 base::debug::(anonymous namespace)::StackDumpSignalHandler(int, __siginfo*, void*) + 940
3   libsystem_platform.dylib            0x0000000190346e04 _sigtramp + 56
4   libchrome_dll.dylib                 0x00000001138251ec ai_chat::OAIAPIClient::OnQueryCompleted(base::OnceCallback<void (base::expected<std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>>, ai_chat::mojom::APIError>)>, api_request_helper::APIRequestResult) + 188
5   libchrome_dll.dylib                 0x000000011200e4e0 void base::internal::DecayedFunctorTraits<void (brave_vpn::BraveVpnAPIRequest::*)(base::OnceCallback<void (std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>> const&, bool)>, api_request_helper::APIRequestResult), base::WeakPtr<brave_vpn::BraveVpnAPIRequest>&&, base::OnceCallback<void (std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>> const&, bool)>&&>::Invoke<void (brave_vpn::BraveVpnAPIRequest::*)(base::OnceCallback<void (std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>> const&, bool)>, api_request_helper::APIRequestResult), base::WeakPtr<brave_vpn::BraveVpnAPIRequest> const&, base::OnceCallback<void (std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>> const&, bool)>, api_request_helper::APIRequestResult>(void (brave_vpn::BraveVpnAPIRequest::*)(base::OnceCallback<void (std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>> const&, bool)>, api_request_helper::APIRequestResult), base::WeakPtr<brave_vpn::BraveVpnAPIRequest> const&, base::OnceCallback<void (std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>> const&, bool)>&&, api_request_helper::APIRequestResult&&) + 116
6   libchrome_dll.dylib                 0x0000000110e0d99c base::OnceCallback<void (web_app::(anonymous namespace)::LoadedConfigs)>::Run(web_app::(anonymous namespace)::LoadedConfigs) && + 76
7   libchrome_dll.dylib                 0x000000011388c4c4 api_request_helper::APIRequestHelper::DeleteAndSendResult(std::__Cr::__list_iterator<std::__Cr::unique_ptr<api_request_helper::APIRequestHelper::URLLoaderHandler, std::__Cr::default_delete<api_request_helper::APIRequestHelper::URLLoaderHandler>>, void*>, base::OnceCallback<void (api_request_helper::APIRequestResult)>, api_request_helper::APIRequestResult) + 196
8   libchrome_dll.dylib                 0x000000011388e35c void base::internal::DecayedFunctorTraits<void (api_request_helper::APIRequestHelper::*)(std::__Cr::__list_iterator<std::__Cr::unique_ptr<api_request_helper::APIRequestHelper::URLLoaderHandler, std::__Cr::default_delete<api_request_helper::APIRequestHelper::URLLoaderHandler>>, void*>, base::OnceCallback<void (api_request_helper::APIRequestResult)>, api_request_helper::APIRequestResult), base::WeakPtr<api_request_helper::APIRequestHelper>&&, std::__Cr::__list_iterator<std::__Cr::unique_ptr<api_request_helper::APIRequestHelper::URLLoaderHandler, std::__Cr::default_delete<api_request_helper::APIRequestHelper::URLLoaderHandler>>, void*>&&, base::OnceCallback<void (api_request_helper::APIRequestResult)>&&>::Invoke<void (api_request_helper::APIRequestHelper::*)(std::__Cr::__list_iterator<std::__Cr::unique_ptr<api_request_helper::APIRequestHelper::URLLoaderHandler, std::__Cr::default_delete<api_request_helper::APIRequestHelper::URLLoaderHandler>>, void*>, base::OnceCallback<void (api_request_helper::APIRequestResult)>, api_request_helper::APIRequestResult), base::WeakPtr<api_request_helper::APIRequestHelper> const&, std::__Cr::__list_iterator<std::__Cr::unique_ptr<api_request_helper::APIRequestHelper::URLLoaderHandler, std::__Cr::default_delete<api_request_helper::APIRequestHelper::URLLoaderHandler>>, void*>, base::OnceCallback<void (api_request_helper::APIRequestResult)>, api_request_helper::APIRequestResult>(void (api_request_helper::APIRequestHelper::*)(std::__Cr::__list_iterator<std::__Cr::unique_ptr<api_request_helper::APIRequestHelper::URLLoaderHandler, std::__Cr::default_delete<api_request_helper::APIRequestHelper::URLLoaderHandler>>, void*>, base::OnceCallback<void (api_request_helper::APIRequestResult)>, api_request_helper::APIRequestResult), base::WeakPtr<api_request_helper::APIRequestHelper> const&, std::__Cr::__list_iterator<std::__Cr::unique_ptr<api_request_helper::APIRequestHelper::URLLoaderHandler, std::__Cr::default_delete<api_request_helper::APIRequestHelper::URLLoaderHandler>>, void*>&&, base::OnceCallback<void (api_request_helper::APIRequestResult)>&&, api_request_helper::APIRequestResult&&) + 196
9   libchrome_dll.dylib                 0x0000000110e0d99c base::OnceCallback<void (web_app::(anonymous namespace)::LoadedConfigs)>::Run(web_app::(anonymous namespace)::LoadedConfigs) && + 76
10  libchrome_dll.dylib                 0x000000011388e0a0 api_request_helper::APIRequestHelper::URLLoaderHandler::OnParseJsonResponse(api_request_helper::APIRequestResult, base::expected<base::Value, std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>>>) + 1016
11  libchrome_dll.dylib                 0x000000011388ea2c void base::internal::DecayedFunctorTraits<void (api_request_helper::APIRequestHelper::URLLoaderHandler::*)(api_request_helper::APIRequestResult, base::expected<base::Value, std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>>>), base::WeakPtr<api_request_helper::APIRequestHelper::URLLoaderHandler>&&, api_request_helper::APIRequestResult&&>::Invoke<void (api_request_helper::APIRequestHelper::URLLoaderHandler::*)(api_request_helper::APIRequestResult, base::expected<base::Value, std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>>>), base::WeakPtr<api_request_helper::APIRequestHelper::URLLoaderHandler> const&, api_request_helper::APIRequestResult, base::expected<base::Value, std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>>>>(void (api_request_helper::APIRequestHelper::URLLoaderHandler::*)(api_request_helper::APIRequestResult, base::expected<base::Value, std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>>>), base::WeakPtr<api_request_helper::APIRequestHelper::URLLoaderHandler> const&, api_request_helper::APIRequestResult&&, base::expected<base::Value, std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>>>&&) + 184
12  libchrome_dll.dylib                 0x0000000110e0d99c base::OnceCallback<void (web_app::(anonymous namespace)::LoadedConfigs)>::Run(web_app::(anonymous namespace)::LoadedConfigs) && + 76
13  libchrome_dll.dylib                 0x000000011388e818 _ZN4base8internal7InvokerINS0_13FunctorTraitsIOZN18api_request_helper12_GLOBAL__N_127ParseJsonInWorkerTaskRunnerENSt4__Cr12basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEEPNS_19SequencedTaskRunnerENS_12OnceCallbackIFvNS_8expectedINS_5ValueESB_EEEEEE3$_1JOSJ_EEENS0_9BindStateILb0ELb0ELb0ESK_JSJ_EEEFvNSF_ISG_NS_10JSONReader5ErrorEEEEE7RunOnceEPNS0_13BindStateBaseEOSS_ + 92
14  libchrome_dll.dylib                 0x0000000110e0d99c base::OnceCallback<void (web_app::(anonymous namespace)::LoadedConfigs)>::Run(web_app::(anonymous namespace)::LoadedConfigs) && + 76
15  libchrome_dll.dylib                 0x0000000110ffb9ac void base::internal::ReplyAdapter<base::expected<base::Value, base::JSONReader::Error>, base::expected<base::Value, base::JSONReader::Error>>(base::OnceCallback<void (base::expected<base::Value, base::JSONReader::Error>)>, std::__Cr::unique_ptr<base::expected<base::Value, base::JSONReader::Error>, std::__Cr::default_delete<base::expected<base::Value, base::JSONReader::Error>>>*) + 56
16  libchrome_dll.dylib                 0x0000000110e9a904 base::internal::Invoker<base::internal::FunctorTraits<void (*&&)(base::OnceCallback<web_app::(anonymous namespace)::LoadedConfigs ()>, std::__Cr::unique_ptr<web_app::(anonymous namespace)::LoadedConfigs, std::__Cr::default_delete<web_app::(anonymous namespace)::LoadedConfigs>>*), base::OnceCallback<web_app::(anonymous namespace)::LoadedConfigs ()>&&, std::__Cr::unique_ptr<web_app::(anonymous namespace)::LoadedConfigs, std::__Cr::default_delete<web_app::(anonymous namespace)::LoadedConfigs>>*&&>, base::internal::BindState<false, true, false, void (*)(base::OnceCallback<web_app::(anonymous namespace)::LoadedConfigs ()>, std::__Cr::unique_ptr<web_app::(anonymous namespace)::LoadedConfigs, std::__Cr::default_delete<web_app::(anonymous namespace)::LoadedConfigs>>*), base::OnceCallback<web_app::(anonymous namespace)::LoadedConfigs ()>, base::internal::UnretainedWrapper<std::__Cr::unique_ptr<web_app::(anonymous namespace)::LoadedConfigs, std::__Cr::default_delete<web_app::(anonymous namespace)::LoadedConfigs>>, base::unretained_traits::MayNotDangle, (partition_alloc::internal::RawPtrTraits)0>>, void ()>::RunOnce(base::internal::BindStateBase*) + 36
17  libbase.dylib                       0x00000001058e2194 base::OnceCallback<void ()>::Run() && + 68
18  libbase.dylib                       0x00000001059b5624 base::internal::PostTaskAndReplyRelay::RunReply(base::internal::PostTaskAndReplyRelay) + 44
19  libbase.dylib                       0x00000001059b5500 base::internal::Invoker<base::internal::FunctorTraits<void (*&&)(base::internal::PostTaskAndReplyRelay), base::internal::PostTaskAndReplyRelay&&>, base::internal::BindState<false, true, false, void (*)(base::internal::PostTaskAndReplyRelay), base::internal::PostTaskAndReplyRelay>, void ()>::RunOnce(base::internal::BindStateBase*) + 44
20  libbase.dylib                       0x00000001058e2194 base::OnceCallback<void ()>::Run() && + 68
21  libbase.dylib                       0x000000010597c91c base::TaskAnnotator::RunTaskImpl(base::PendingTask&) + 280
22  libbase.dylib                       0x00000001059aa8b8 base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::DoWorkImpl(base::LazyNow*) + 1020
23  libbase.dylib                       0x00000001059aa158 base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::DoWork() + 100
24  libbase.dylib                       0x0000000105a278d0 base::MessagePumpCFRunLoopBase::RunWork() + 156
25  libbase.dylib                       0x0000000105a1e6e8 base::apple::CallWithEHFrame(void () block_pointer) + 16
26  libbase.dylib                       0x0000000105a26e28 base::MessagePumpCFRunLoopBase::RunWorkSource(void*) + 68
27  CoreFoundation                      0x00000001903f8894 __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 28
28  CoreFoundation                      0x00000001903f8828 __CFRunLoopDoSource0 + 176
29  CoreFoundation                      0x00000001903f858c __CFRunLoopDoSources0 + 244
30  CoreFoundation                      0x00000001903f7128 __CFRunLoopRun + 840
31  CoreFoundation                      0x00000001903f6724 CFRunLoopRunSpecific + 588
32  HIToolbox                           0x000000019b94e530 RunCurrentEventLoopInMode + 292
33  HIToolbox                           0x000000019b954348 ReceiveNextEventCommon + 676
34  HIToolbox                           0x000000019b954508 _BlockUntilNextEventMatchingListInModeWithFilter + 76
35  AppKit                              0x0000000193f61034 _DPSNextEvent + 660
36  AppKit                              0x00000001948c52d4 -[NSApplication(NSEventRouting) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 688
37  libchrome_dll.dylib                 0x0000000112609ac8 __71-[BrowserCrApplication nextEventMatchingMask:untilDate:inMode:dequeue:]_block_invoke + 64
38  libbase.dylib                       0x0000000105a1e6e8 base::apple::CallWithEHFrame(void () block_pointer) + 16
39  libchrome_dll.dylib                 0x0000000112609a10 -[BrowserCrApplication nextEventMatchingMask:untilDate:inMode:dequeue:] + 188
40  AppKit                              0x0000000193f54060 -[NSApplication run] + 480
41  libbase.dylib                       0x0000000105a28588 base::MessagePumpNSApplication::DoRun(base::MessagePump::Delegate*) + 396
42  libbase.dylib                       0x0000000105a26794 base::MessagePumpCFRunLoopBase::Run(base::MessagePump::Delegate*) + 140
43  libbase.dylib                       0x00000001059ab4e8 base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::Run(bool, base::TimeDelta) + 528
44  libbase.dylib                       0x00000001059504c0 base::RunLoop::Run(base::Location const&) + 360
45  libcontent.dylib                    0x000000012090237c content::BrowserMainLoop::RunMainMessageLoop() + 180
46  libcontent.dylib                    0x0000000120903fb8 content::BrowserMainRunnerImpl::Run() + 48
47  libcontent.dylib                    0x00000001208ff968 content::BrowserMain(content::MainFunctionParams) + 152
48  libcontent.dylib                    0x00000001216089dc content::RunBrowserProcessMain(content::MainFunctionParams, content::ContentMainDelegate*) + 176
49  libcontent.dylib                    0x000000012160a028 content::ContentMainRunnerImpl::RunBrowser(content::MainFunctionParams, bool) + 1020
50  libcontent.dylib                    0x0000000121609b14 content::ContentMainRunnerImpl::Run() + 548
51  libcontent.dylib                    0x0000000121608048 content::RunContentProcess(content::ContentMainParams, content::ContentMainRunner*) + 1244
52  libcontent.dylib                    0x0000000121608284 content::ContentMain(content::ContentMainParams) + 112
53  libchrome_dll.dylib                 0x0000000110e06dac ChromeMain + 684
54  Brave Browser Development           0x0000000104f007e0 main + 288
55  dyld                                0x000000018ff90274 start + 2840
[end of stack trace]
[0125/231828.615759:ERROR:bootstrap.cc(65)] bootstrap_look_up com.apple.ReportCrash: Unknown service name (1102)
[1]    67722 segmentation fault   --enable-logging --v=0 --disable-brave-update --use-mock-keychain
```

This is caused by here.
```
void OAIAPIClient::OnQueryCompleted(GenerationCompletedCallback callback,
                                    APIRequestResult result) {
  const bool success = result.Is2XXResponseCode();
  // Handle successful request
  if (success) {
    std::string completion = "";
    // We're checking for a value body in case for non-streaming API results.
    if (result.value_body().is_dict()) {
      const base::Value::List* choices =
          result.value_body().GetDict().FindList("choices");
      if (!choices) {
        DVLOG(2) << "No choices list found in response.";
        return;
      }
      if (choices->front().is_dict()) {
        const base::Value::Dict* message =
            choices->front().GetDict().FindDict("message");
        if (!message) {
          DVLOG(2) << "No message dict found in response.";
          return;
        }
        completion = *message->FindString("content"); // ***HERE*** The code assumes the `message` field always has at least one `content` field.
      }
    }

    std::move(callback).Run(base::ok(std::move(completion)));
    return;
  }

  // omit //
}
```

I think nullptr check should be added.

## Impact

- It always causes a crash of the entire browser.
- In general, null pointer dereferences leads to RCE in some cases.
  - I've not been occurred by any idea to exploit this for RCE.
  - I know just a crash is not rewarded, but reported the issue just in case, because it could be used as a step stone to RCE and especially it's in the privileged browser process.

## Attachments
No attachments
