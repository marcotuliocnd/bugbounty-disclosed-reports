# Memory Leak in bytes_to_hexstring Function

## Report Details
- **Report ID**: 2779070
- **URL**: https://hackerone.com/reports/2779070
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-10-13T06:42:20.555Z
- **Disclosed**: 2024-10-24T16:15:11.266Z

## Reporter
- **Username**: gajnithehero
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
## Overview
The function` bytes_to_hexstring` located in the `utils.c` file has a confirmed memory leak vulnerability. This function is responsible for converting an array of bytes into a hexadecimal string representation. However, it allocates memory dynamically using `malloc` without any error handling or memory management practices to ensure that the allocated memory is freed after use. This can result in a memory leak, which occurs when dynamically allocated memory is not properly released, leading to potential resource exhaustion over time.

## Vulnerability Details

- **Function:** [`bytes_to_hexstring`](https://github.com/hyperledger/fabric-private-chaincode/blob/2b8ae267b37f0680a4a012f91058bcf78cdf2f79/common/utils.c#L33)

```c
char* bytes_to_hexstring(uint8_t* bytes, size_t len)
{
    const char* hexdigs = "0123456789abcdef";
    size_t k = len * 2 + 1;
    char* out = malloc(k);
    for (int i = 0; i < len; i++)
    {
        out[i * 2] = hexdigs[bytes[i] >> 4];
        out[i * 2 + 1] = hexdigs[bytes[i] & 0x0f];
    }
    out[k - 1] = '\0';
    return out;
}
```

## Description of the Vulnerability:

- The function `bytes_to_hexstring` allocates memory using `malloc(k)` to hold the hexadecimal string (`k = len * 2 + 1`, where len is the length of the input byte array).

- After this memory allocation, the function proceeds to fill the buffer with hexadecimal characters but **never frees the memory** before the function exits.

- This memory must be freed after the function is called, but **the function does not document or enforce the requirement for the caller to free the memory**.

- If the caller fails to release the allocated memory, it will lead to a **memory leak**, as the system cannot reclaim the dynamically allocated memory until the program terminates.

## Steps to Reproduce the Vulnerability

**1)** Call the `bytes_to_hexstring` function multiple times in a loop without freeing the memory it returns.

***Example:**

```c
for (int i = 0; i < 10000; i++) {
    uint8_t data[10] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09};
    char* hex_str = bytes_to_hexstring(data, 10);
    // Do something with hex_str but forget to free it
}
```

**2)** Observe the program's increasing memory consumption, which can be monitored using system tools like `top` (Linux), `Task Manager` (Windows), or similar.

**3)** Eventually, the program will either crash or severely degrade the performance of the system due to high memory usage.

## Suggested Mitigations

**1) Free Allocated Memory:** Ensure that the caller of the function is responsible for freeing the dynamically allocated memory.

   - The function should document that it returns a pointer to allocated memory, and it is the responsibility of the caller to free() that memory once it is no longer needed.
Example of proper usage:

```c
char* hex_str = bytes_to_hexstring(data, len);
// Use hex_str...
free(hex_str); // Ensure that the allocated memory is freed
```

**2) Error Handling for Memory Allocation:** Check the return value of `malloc` for `NULL`. This would add resilience in case of memory allocation failure.

   - Updated code with error handling:

```c
char* bytes_to_hexstring(uint8_t* bytes, size_t len)
{
    const char* hexdigs = "0123456789abcdef";
    size_t k = len * 2 + 1;
    char* out = malloc(k);
    if (out == NULL) {
        return NULL; // Return NULL if memory allocation fails
    }
    for (int i = 0; i < len; i++) {
        out[i * 2] = hexdigs[bytes[i] >> 4];
        out[i * 2 + 1] = hexdigs[bytes[i] & 0x0f];
    }
    out[k - 1] = '\0';
    return out;
}
```

**3) Considerations for Caller Responsibility:** If possible, implement a more robust memory management strategy where the allocation and deallocation of memory are managed by the same function or encapsulated in a higher-level API. For instance, passing in an already-allocated buffer to be filled instead of returning a dynamically allocated buffer.

## Impact

## Implications of the Memory Leak:
- **Resource Exhaustion:** Over time, if `bytes_to_hexstring` is called repeatedly in a long-running program without freeing the returned memory, the program's memory consumption will increase. This can lead to performance degradation, or in worse cases, system crashes due to memory exhaustion.

- **Denial of Service (DoS):** A malicious user could exploit this vulnerability by triggering multiple invocations of this function, exhausting available memory resources and leading to denial of service.

## Conclusion
This report highlights a confirmed **memory leak** vulnerability in the `bytes_to_hexstring` function. The lack of proper memory management results in an increasing consumption of system resources, potentially leading to system crashes or denial of service (DoS) attacks.

The solution involves proper memory deallocation, ensuring that the caller frees the returned memory, and adding error handling for memory allocation failures. Addressing these issues will significantly improve the stability and security of the application.

**Severity Rating:**

- **Impact:** Medium
- **Likelihood:** High (if the function is used in long-running applications)
**Recommended Fix Priority:** High

- References:

Common Weakness Enumeration (CWE-401): Memory Leak

## Attachments
No attachments
