# [Monero wallet RPC] File precreation to file ownership and credentials leak

## Report Details
- **Report ID**: 2425873
- **URL**: https://hackerone.com/reports/2425873
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-03-20T17:04:04.690Z
- **Disclosed**: 2024-09-04T17:07:49.843Z

## Reporter
- **Username**: selmelc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
Hello,

During my testing I observed a problematic file creation in the monero wallet rpc which causes the credentials of that rpc to potentially leak to an attacker if this vulnerability is exploited correctly.

The vulnerable code is located [here](https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/wallet/wallet_rpc_server.cpp#L248) at the line 248 of the wallet_rpc_server.cpp file inside the wallet_rpc_server::init method.
```
...
        std::string temp = "monero-wallet-rpc." + bind_port + ".login";
        rpc_login_file = tools::private_file::create(temp);
...
```
We see here that the monero-wallet-rpc will generate a file with a none random name and will later write the username and password of the RPC in it.

Another interesting  piece of code is the implementation of private_file::create() and most importantly at [line 196](https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/common/util.cpp#L196)
```
    const int fdr = open(name.c_str(), (O_RDONLY | O_CREAT), S_IRUSR);
```

What I observed here is that the O_EXCL flag isn't used, this means that if the file exists before this line of code is triggered then the file is simply opened instead of being created and will keep all its original meta information such as permissions and owner.

This is problematic as an attacker could precreate the monero-wallet-rpc.[port].login file and give themself arbitrary permissions and full ownership of the credentials file before the victim starts the RPC server.

## Patch suggestion:
At first I thought the O_EXCL flag wasn't used for functional reasons but from testing I observe that the file is deleted as the RPC server goes down anyway so using the O_EXCL flag would patch this vulnerability without affecting functionality at all.

## Releases Affected:

  * Tested on linux, from main branch. Vulnerable code present for a long time at least the last 6 years.

## Steps To Reproduce:

  1. Have two users on a linux system (A and V).
  1. For simplicity move them both in the same working directory
  1. As A execute the following commands: `touch monero-wallet-rpc.16969.login;chmod a+rwx monero-wallet-rpc.16969.login`
  1. V has a monero wallet that is located at /home/selmelc/Monero/wallets/selmelc/selmelc.keys.
  1. V wants to start a wallet RPC server so they start monerod in the background and executes the following command: `monero-wallet-rpc --wallet-file /home/selmelc/Monero/wallets/selmelc/selmelc.keys --prompt-for-password --rpc-bind-port 16969`
 1. As A execute `ls -l monero-wallet-rpc.16969.login; cat monero-wallet-rpc.16969.login` and you can observe that the attacker A owns the credential file that should be owned by the victim V and the attacker can read it.

See screenshots where I reproduce those steps, on the left is the attacker and on the right the victim starting the RPC server:

{F3133373}


XMR address: `44FvRkLxcfnc8zBNFHU8xoh9LdvTgF8iEJUpkrBtGMBLgVf5UGuHrUD3mgMJyMYGb3BhXE8wzGJqrbxCDFijNo27CuVHByo`

## Impact

A confidential file (RPC .login) can be tampered and disclosed to an attacker.

## Attachments
- Capture.PNG
