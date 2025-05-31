# Remote 0click exfiltration of Safari user's IP address

## Report Details
- **Report ID**: 1392211
- **URL**: https://hackerone.com/reports/1392211
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-11-05T07:01:11.431Z
- **Disclosed**: 2022-06-15T20:00:43.926Z

## Reporter
- **Username**: max2x
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** A malicious actor when embedding content into Twitter content (for example, see this ████) can lookup the IP address of a user without the user consenting to loading the 3rd party domain.

**Description:** When the user loads the page and doesn't click on any content Safari preloads the ad target domain (in this case ██████████). Using that, without the user tapping on the link, my server receives a TCP connection where I extract the IP and hostname of the victim. Using that information, I can lookup their approximate address, maybe spoof an IP in their city and spearphish one of their accounts, find their telco or ISP provider and use their twitter name to take over their account, many things are possible.

The problem is caused by use of remote domain links with preconnect.

<link href="https://██████" rel="preconnect">
<link href="//███████" rel="preconnect">

I recommend a mitigation of removing preload and preconnect for 3rd party domains.

This has huge privacy and security implications. I can remotely extract a targeted user's IP address by sending them a email, text message, or just tweeting at them. They are not aware it happened, it doesn't show up in their browser history because the user doesn't tap on the 3rd party link.

Once you have mitigated this issue I will need to notify Apple.

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. I send a targeted user a link to a tweet such as https://twitter.com/██████/status/███████
2. They use Safari to open the link
3. When the user mouses over the image on a mac (or scrolls the screen on an iPhone) Safari will connect to ████.
4. My server lists out incoming TCP connections.

## Impact:

Silently exfiltrating a user's IP address remotely opens them up to lots of attacks. You may see an egg, but I see a gateway to spear phishing the user by initiating regular MITM attack (showing the login request from the same location as the user), I see it been useful to do an account takeover via their ISP or telco. I see it useful to know when a user is at home or at work, in some cases I can tell they work at a certain company. In the case of a popular streamer it opens them up to DDOS attacks by just clicking on a "safe" tweet. There are huge possibilities for doxxing individuals using this exploit.

You can also target an individual (for example an individual you know is in America somewhere) through twitter ads by adding 99 twitter handles from Japan, then the target twitter handle. That way, you know when your ad is shown if it is the target because they won't be in Japan.

The only thing to bring down the impact of this attack is it is macOS and iOS Safari only. But if you don't think this attack has high severity I can demonstrate more use cases.

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

Here is a simple C server for logging incoming connections.

```
#include <netdb.h>
/* --- server.c --- */
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>

int main(int argc, char *argv[])
{
	int listenfd = 0, connfd = 0;
	struct sockaddr_in serv_addr;

	char sendBuff[1025];
	time_t ticks;

	/* creates an UN-named socket inside the kernel and returns
	 * an integer known as socket descriptor
	 * This function takes domain/family as its first argument.
	 * For Internet family of IPv4 addresses we use AF_INET
	 */
	listenfd = socket(AF_INET, SOCK_STREAM, 0);
	memset(&serv_addr, '0', sizeof(serv_addr));
	memset(sendBuff, '0', sizeof(sendBuff));

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_addr.sin_port = htons(443);

	/* The call to the function "bind()" assigns the details specified
	 * in the structure 『serv_addr' to the socket created in the step above
	 */
	bind(listenfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));

	/* The call to the function "listen()" with second argument as 10 specifies
	 * maximum number of client connections that server will queue for this listening
	 * socket.
	 */
	listen(listenfd, 10);

	while(1)
	{
		/* In the call to accept(), the server is put to sleep and when for an incoming
		 * client request, the three way TCP handshake* is complete, the function accept()
		 * wakes up and returns the socket descriptor representing the client socket.
		 */
		struct sockaddr_in client;
		unsigned int fromLen;
		connfd = accept(listenfd, (struct sockaddr*)&client, &fromLen);
printf("Client accepted: %s \n", inet_ntoa(client.sin_addr));  
		struct hostent *hostName;
struct in_addr ipv4addr;

inet_pton(AF_INET, inet_ntoa(client.sin_addr), &ipv4addr);
hostName = gethostbyaddr(&ipv4addr, sizeof ipv4addr, AF_INET);
if (hostName != NULL) {
printf("Host name: %s\n", hostName->h_name);
}


		/* As soon as server gets a request from client, it prepares the date and time and
		 * writes on the client socket through the descriptor returned by accept()
		 */
		ticks = time(NULL);
// printf(sendBuff, sizeof(sendBuff), "%.24s\r\n", ctime(&ticks));
//		printf(sendBuff, sizeof(sendBuff), "%.24s\r\n", ctime(&ticks));
		write(connfd, sendBuff, strlen(sendBuff));

		close(connfd);
		sleep(1);
	}
}

```

## Impact

Silently exfiltrating a user's IP address remotely opens them up to lots of attacks. You may see an egg, but I see a gateway to spear phishing the user by initiating regular MITM attack (showing the login request from the same location as the user), I see it been useful to do an account takeover via their ISP or telco. I see it useful to know when a user is at home or at work, in some cases I can tell they work at a certain company. In the case of a popular streamer it opens them up to DDOS attacks by just clicking on a "safe" tweet. There are huge possibilities for doxxing individuals using this exploit.

You can also target an individual (for example an individual you know is in America somewhere) through twitter ads by adding 99 twitter handles from Japan, then the target twitter handle. That way, you know when your ad is shown if it is the target because they won't be in Japan.

The only thing to bring down the impact of this attack is it is macOS and iOS Safari only. But if you don't think this attack has high severity I can demonstrate more use cases.

## Attachments
No attachments
