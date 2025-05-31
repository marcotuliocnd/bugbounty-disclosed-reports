# Monero can leak unitialized memory

## Report Details
- **Report ID**: 481164
- **URL**: https://hackerone.com/reports/481164
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-01-16T21:33:28.884Z
- **Disclosed**: 2019-07-02T22:49:44.832Z

## Reporter
- **Username**: guido
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: monero

## Vulnerability Information
See this proof of concept:

```cpp
#include <net/http_client.h>
#include <rpc/core_rpc_server_commands_defs.h>
#include <storages/http_abstract_invoke.h>

INITIALIZE_EASYLOGGINGPP

template <class T>
static void invoke_http_json(void)
{
    typename T::request ireq;
    typename T::response ires;

    std::string req_param;
    if(!epee::serialization::store_t_to_json(ireq, req_param)) {
        return;
    }
    printf("%s\n", req_param.c_str());
}

int main(void)
{
    while ( true ) {
        const unsigned char which = rand() % 65;
        printf("which: %u\n", which);
        switch ( which ) {
            case 0:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_HEIGHT>();
                break;

            case 1:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_BLOCKS_FAST>();
                break;

            case 2:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_BLOCKS_BY_HEIGHT>();
                break;

            case 3:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_ALT_BLOCKS_HASHES>();
                break;

            case 4:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_HASHES_FAST>();
                break;

            case 5:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_ADDRESS_TXS>();
                break;

            case 6:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_ADDRESS_INFO>();
                break;

            case 7:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_UNSPENT_OUTS>();
                break;

            case 8:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_RANDOM_OUTS>();
                break;

            case 9:
                invoke_http_json<cryptonote::COMMAND_RPC_SUBMIT_RAW_TX>();
                break;

            case 10:
                invoke_http_json<cryptonote::COMMAND_RPC_LOGIN>();
                break;

            case 11:
                invoke_http_json<cryptonote::COMMAND_RPC_IMPORT_WALLET_REQUEST>();
                break;

            case 12:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_TRANSACTIONS>();
                break;

            case 13:
                invoke_http_json<cryptonote::COMMAND_RPC_IS_KEY_IMAGE_SPENT>();
                break;

            case 14:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_TX_GLOBAL_OUTPUTS_INDEXES>();
                break;

            case 15:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_OUTPUTS_BIN>();
                break;

            case 16:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_OUTPUTS>();
                break;

            case 17:
                invoke_http_json<cryptonote::COMMAND_RPC_SEND_RAW_TX>();
                break;

            case 18:
                invoke_http_json<cryptonote::COMMAND_RPC_START_MINING>();
                break;

            case 19:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_INFO>();
                break;

            case 20:
                invoke_http_json<cryptonote::COMMAND_RPC_STOP_MINING>();
                break;

            case 21:
                invoke_http_json<cryptonote::COMMAND_RPC_MINING_STATUS>();
                break;

            case 22:
                invoke_http_json<cryptonote::COMMAND_RPC_SAVE_BC>();
                break;

            case 25:
                invoke_http_json<cryptonote::COMMAND_RPC_GETBLOCKTEMPLATE>();
                break;

            case 27:
                invoke_http_json<cryptonote::COMMAND_RPC_GENERATEBLOCKS>();
                break;

            case 28:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_LAST_BLOCK_HEADER>();
                break;

            case 29:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_BLOCK_HEADER_BY_HASH>();
                break;

            case 30:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_BLOCK_HEADER_BY_HEIGHT>();
                break;

            case 31:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_BLOCK>();
                break;

            case 32:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_PEER_LIST>();
                break;

            case 33:
                invoke_http_json<cryptonote::COMMAND_RPC_SET_LOG_HASH_RATE>();
                break;

            case 34:
                invoke_http_json<cryptonote::COMMAND_RPC_SET_LOG_LEVEL>();
                break;

            case 35:
                invoke_http_json<cryptonote::COMMAND_RPC_SET_LOG_CATEGORIES>();
                break;

            case 36:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL>();
                break;

            case 37:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_HASHES_BIN>();
                break;

            case 38:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_HASHES>();
                break;

            case 39:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_BACKLOG>();
                break;

            case 40:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_TRANSACTION_POOL_STATS>();
                break;

            case 41:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_CONNECTIONS>();
                break;

            case 42:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_BLOCK_HEADERS_RANGE>();
                break;

            case 43:
                invoke_http_json<cryptonote::COMMAND_RPC_STOP_DAEMON>();
                break;

            case 44:
                invoke_http_json<cryptonote::COMMAND_RPC_FAST_EXIT>();
                break;

            case 45:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_LIMIT>();
                break;

            case 46:
                invoke_http_json<cryptonote::COMMAND_RPC_SET_LIMIT>();
                break;

            case 47:
                invoke_http_json<cryptonote::COMMAND_RPC_OUT_PEERS>();
                break;

            case 48:
                invoke_http_json<cryptonote::COMMAND_RPC_IN_PEERS>();
                break;

            case 49:
                invoke_http_json<cryptonote::COMMAND_RPC_START_SAVE_GRAPH>();
                break;

            case 50:
                invoke_http_json<cryptonote::COMMAND_RPC_STOP_SAVE_GRAPH>();
                break;

            case 51:
                invoke_http_json<cryptonote::COMMAND_RPC_HARD_FORK_INFO>();
                break;

            case 52:
                invoke_http_json<cryptonote::COMMAND_RPC_GETBANS>();
                break;

            case 53:
                invoke_http_json<cryptonote::COMMAND_RPC_SETBANS>();
                break;

            case 54:
                invoke_http_json<cryptonote::COMMAND_RPC_FLUSH_TRANSACTION_POOL>();
                break;

            case 55:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_OUTPUT_HISTOGRAM>();
                break;

            case 56:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_VERSION>();
                break;

            case 57:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_COINBASE_TX_SUM>();
                break;

            case 58:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_BASE_FEE_ESTIMATE>();
                break;

            case 59:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_ALTERNATE_CHAINS>();
                break;

            case 60:
                invoke_http_json<cryptonote::COMMAND_RPC_UPDATE>();
                break;

            case 61:
                invoke_http_json<cryptonote::COMMAND_RPC_RELAY_TX>();
                break;

            case 62:
                invoke_http_json<cryptonote::COMMAND_RPC_SYNC_INFO>();
                break;

            case 63:
                invoke_http_json<cryptonote::COMMAND_RPC_GET_OUTPUT_DISTRIBUTION>();
                break;

            case 64:
                invoke_http_json<cryptonote::COMMAND_RPC_POP_BLOCKS>();
                break;
        }
    }

    return 0;
}
```

Compile:

```
g++ -std=c++11 -I $MONERO_PATH/src -I $MONERO_PATH/contrib/epee/include -I $MONERO_PATH/external/easylogging++ $MONERO_PATH/external/easylogging++/easylogging++.cc uninitialized-memory-send.cpp -lpthread -lboost_system -lcrypto -lssl
```

Run:

```
./a.out | head -n1000000 | sort -u >output
```

If you examine ```output```, you'll see that JSON is generated with random data. This is uninitialized memory created at the instantiation of ```ireq```.

To solve this, initialize ```ireq```. For example, change

```
    typename T::request ireq;
```

to

```
    boost::value_initialized<typename T::request> _ireq;
    typename T::request& ireq = _ireq;

```

Compile and run again, and you'll see that the random data is now gone.

Among other places, ```src/wallet/wallet2.cpp``` contains many calls to ```invoke_http_json```, with some ```::request``` structs initialized with ```AUTO_VAL_INIT```, but some not.
```invoke_http_json``` serializes the ```::request``` struct exactly like in my proof-of-concept which is then sent to the RPC server:


```
namespace epee
{
  namespace net_utils
  {
    template<class t_request, class t_response, class t_transport>
    bool invoke_http_json(const boost::string_ref uri, const t_request& out_struct, t_response& result_struct, t_transport& transport, std::chrono::milliseconds timeout = std::chrono::seconds(15), const boost::string_ref method = "GET")
    {   
      std::string req_param;
      if(!serialization::store_t_to_json(out_struct, req_param))
        return false;

      http::fields_list additional_params;
      additional_params.push_back(std::make_pair("Content-Type","application/json; charset=utf-8"));

      const http::http_response_info* pri = NULL;
      if(!transport.invoke(uri, method, req_param, timeout, std::addressof(pri), std::move(additional_params)))  
      ...
      ...
```

Any outbound traffic (bootstrap node/public RPC server/other) where the ```::request``` struct is not explicitly initialized, is thus susceptible to leaking uninitialized memory. Uninitialized memory is never literally uninitialized -- it contains remnants of previous use of the same memory region, and this can include cryptographic or other private material.

## Impact

Leaking sensitive data to untrusted network peers.

## Attachments
No attachments
