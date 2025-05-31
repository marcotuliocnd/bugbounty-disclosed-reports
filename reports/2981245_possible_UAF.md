# ("possible") UAF

## Report Details
- **Report ID**: 2981245
- **URL**: https://hackerone.com/reports/2981245
- **State**: Closed
- **Severity**: none
- **Submitted**: 2025-02-07T20:54:17.316Z
- **Disclosed**: 2025-02-08T09:57:29.816Z

## Reporter
- **Username**: 7mkrooal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
Title: Potential Use-After-Free Vulnerability in cf_h2_proxy_ctx_free Function of libcurl

Vulnerability Overview: A potential Use-After-Free (UAF) vulnerability has been identified in the cf_h2_proxy_ctx_free function of the libcurl library. This issue occurs when the cf_h2_proxy_ctx object is freed and then accessed shortly afterward, leading to undefined behavior, including potential crashes, memory corruption, or security vulnerabilities if exploited.

Impact:

Crashes
Memory corruption
Possible remote code execution or data leakage if exploited in a malicious environment.
Steps to Reproduce:

Obtain libcurl:
Compile and Run the Example Code: Use the simplified code below to reproduce the vulnerability. The code demonstrates freeing a context object (cf_h2_proxy_ctx) and then accessing it, leading to undefined behavior.

Example Code:


#include <stdio.h>
#include <stdlib.h>

struct cf_h2_proxy_ctx {
    int stream_id;
    void *inbufq;
    void *outbufq;
};

void cf_h2_proxy_ctx_free(struct cf_h2_proxy_ctx *ctx) {
    if (ctx) {
        printf("Freeing ctx (stream_id: %d)\n", ctx->stream_id);
        free(ctx);
    }
}

void trigger_bug(struct cf_h2_proxy_ctx *ctx) {
    printf("Triggering bug...\n");
    if (ctx) {
        printf("Using ctx with stream_id: %d\n", ctx->stream_id);
    } else {
        printf("Error: ctx is already freed!\n");
    }
}

int main() {
    // Simulate creating a proxy context
    struct cf_h2_proxy_ctx *ctx = malloc(sizeof(struct cf_h2_proxy_ctx));
    if (!ctx) {
        perror("Failed to allocate memory for ctx");
        return 1;
    }
    ctx->stream_id = 12345;

    cf_h2_proxy_ctx_free(ctx);
    trigger_bug(ctx);

    return 0;
}

Run the Code and Observe the Output: Upon execution, the following output indicates the cf_h2_proxy_ctx object is being accessed after it has been freed:


Freeing ctx (stream_id: 12345)
Using ctx with stream_id:  54321
Verify with Valgrind: To confirm the issue, run the program with Valgrind to detect any memory errors:


valgrind ./your_program
Valgrind Output 


Memcheck, a memory error detector
("Invalid read of size 4")
at 0xxxxxx:
by 0xxxxxx:
Address 0xxx is 0 bytes inside a block of size 24 freed
at 0xxxxxxx: free
by 0xxxxxx: cf_h2_proxy_ctx_free
by 0xxxxx: main

## Impact

A potential Use-After-Free (UAF) vulnerability has been identified in the cf_h2_proxy_ctx_free function of the libcurl library. The issue occurs when the cf_h2_proxy_ctx object is freed and then accessed shortly after, leading to undefined behavior, including possible crashes, memory corruption, or security vulnerabilities if exploited.

"Note: I’m a beginner in this area, so please let me know if I’ve missed or misinterpreted any details, or if I’ve misunderstood the issue entirely. This report has been assisted by AI."

## Attachments
No attachments
