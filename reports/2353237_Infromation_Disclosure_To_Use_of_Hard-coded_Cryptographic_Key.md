# Infromation Disclosure To Use of Hard-coded Cryptographic Key

## Report Details
- **Report ID**: 2353237
- **URL**: https://hackerone.com/reports/2353237
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-02-02T22:55:18.325Z
- **Disclosed**: 2024-02-06T16:22:34.580Z

## Reporter
- **Username**: ahmed_xyz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
* [ Leaking very sensitive information through a JS file that is clearly for developers within the website and should not be available to the public.

* The leaked information consists of a lot of API keys, Paypal keys, information and keys about the server and the application, and a lot or a lot of sensitive information, and I will explain the information through screenshots. ]

* I will explain and clarify each of these keys that were leaked. I will explain the function of the key, what is its importance, is it considered confidential information or not, and what is the potential impact that would occur if this key was leaked by attackers?, I will try to provide solutions as well .

* Given the functions of these keys and what might happen if they are exploited, I will content myself with providing a detailed breakdown in writing, because if I attempt to exploit them, I strongly believe that severe damage will occur if the exploitation is successful.

## Warning: Please read these details carefully and verify them with one of Reddit’s developers and verify them very carefully because the functions of these keys, their confidentiality, and preserving them from leaking are extremely important for the security of the application and the users.

## POC:
* 1- stripe:{apiKey:e=>{return e||!Object(n.b)()&&!Object(n.c)()?"pk_test_Me5fd06PSuMkMF5YnwuMfFf4":"pk_live_sD8LeDtVnlJwAGf51jLygWpH"
The stripe key, specifically the apiKey within the stripe object, is used for integration with the payment processing service called Stripe on the Reddit website. Stripe offers tools and APIs that allow websites to accept payments securely over the internet.
This apiKey is crucial as it enables Reddit's systems to authenticate and interact securely with Stripe's services. It determines which mode (test or live) Reddit uses to process payment transactions.
Regarding sensitivity, the apiKey itself is considered sensitive information. If this key were to be leaked or compromised by attackers, it could lead to potential unauthorized access to Reddit's payment processing systems via Stripe. This might result in fraudulent transactions, manipulation of payment settings, or even theft of financial information related to transactions made on Reddit.
Moreover, leaking the apiKey might allow attackers to bypass Reddit's controls over payment processing, enabling them to initiate transactions or manipulate payment-related functionalities on the platform. This could impact the financial integrity of Reddit and erode user trust in the security of payment transactions on the site.
In summary, the stripe apiKey is a critical component for Reddit's payment processing through Stripe. Its security is paramount to prevent unauthorized access, fraudulent transactions, and protect sensitive financial data.


* 2- PAYPAL_API_KEY||(Object(n.b)()||Object(n.c)()?"AXHUGZNCrshqynIpOLkQjqlsrA26Knvf4EB5w1RKfsdxKdsA5WSNo9H_Gng6plKyc48qGhXtmwcYahRy":"AXH6yPVeFV8sxT1zMvzr8NyPMXx_YkYui1XCy3btQ_s1Zz2R68JC57PqQ2mrj6la-G8y-7UmZyKVsDaR")
The function of the PAYPAL_API_KEY key in reddit.com
The PAYPAL_API_KEY key is used to authenticate requests to the PayPal API. This API is used by reddit.com to process payments.
The key is a secret vulnerability because it is used to authenticate requests to the API. If the key is leaked to attackers, they can use it to make unauthorized requests to the API. These requests can then be used to:
Process payments without authorization: Attackers could use the key to process payments without authorization from the users. This could be used to steal money from users or to commit fraud.
Change payment information: Attackers could use the key to change payment information, such as the credit card number or expiration date. This could be used to commit fraud or to steal money from users.
Cancel payments: Attackers could use the key to cancel payments that have already been processed. This could be used to steal money from users or to disrupt business.
Is it a secret vulnerability?
Yes, the PAYPAL_API_KEY key is a secret vulnerability. It should not be shared with anyone who does not need to know it.
The impact if it is leaked to attackers
The impact of leaking the PAYPAL_API_KEY key would be significant. It could potentially lead to financial losses for reddit.com, its users, and other businesses that use PayPal.
How to protect reddit.com from attacks
To protect reddit.com from attacks, site administrators should:
Secure the key: The key should be stored in a secure location and only accessible to authorized personnel.
Change the key regularly: The key should be changed regularly to make it more difficult for attackers to obtain it.
Monitor the site for suspicious activity: If administrators see any signs of suspicious activity, they should investigate immediately.
By taking these steps, reddit.com can help to protect itself from attacks using the stolen PAYPAL_API_KEY key.
Specific steps reddit.com can take
In addition to the general steps listed above, reddit.com can also take the following specific steps to protect itself from attacks using the stolen PAYPAL_API_KEY key:
Scan the site for any existing fraudulent payments: Attackers may have already processed fraudulent payments before the key was changed.
Educate users about the risks of fraudulent payments: Users should be aware of the signs of fraudulent payments and should report any suspicious activity to reddit.com.
Work with PayPal to investigate the leak: PayPal may be able to help reddit.com to identify the source of the leak and take steps to prevent it from happening again.
By taking these steps, reddit.com can help to protect its users and its site from attacks.
Specific examples of how attackers could use the PAYPAL_API_KEY key
Here are some specific examples of how attackers could use the PAYPAL_API_KEY key:
To steal money from users: Attackers could use the key to process payments without authorization from the users. They could then withdraw the money from the users' bank accounts.
To commit fraud: Attackers could use the key to change payment information, such as the credit card number or expiration date. This could be used to commit fraud or to steal money from users.
To disrupt business: Attackers could use the key to cancel payments that have already been processed. This could be used to disrupt business or to steal money from businesses.
By understanding the potential risks of leaking the PAYPAL_API_KEY key, reddit.com can take steps to protect itself and its users from attacks.
In the specific case of the key you provided, the impact would be limited because it is a test key. However, it is still important to keep this key secure to prevent it from being used for malicious purposes.


* 3- BRAINTREE_PAYPAL_KEY||(Object(n.b)()?"Aflf49iitQXbetXO8Ufm6q7zjADO-15_X1tzZqv-hveq4htWjHYNxEmrtB0s0yyyLOCG_ceCB-32EtdY":"AXH6yPVeFV8sxT1zMvzr8NyPMXx_YkYui1XCy3btQ_s1Zz2R68JC57PqQ2mrj6la-G8y-7UmZyKVsDaR"),env
The BRAINTREE_PAYPAL_KEY is a key used for integrating Braintree's PayPal services into the Reddit website, specifically for handling and facilitating PayPal transactions.
This key plays a crucial role in allowing Reddit's systems to securely communicate and authenticate with Braintree's PayPal API. It enables the platform to process payments, manage transactions, and facilitate financial interactions between Reddit and Braintree's PayPal infrastructure.
Regarding its sensitivity, the BRAINTREE_PAYPAL_KEY is considered confidential information. If this key were to be leaked or compromised by attackers, it could pose significant security risks and potential financial threats. Attackers might exploit the key to gain unauthorized access to Reddit's Braintree integration, potentially performing unauthorized transactions, altering payment configurations, or accessing sensitive financial data associated with PayPal transactions conducted through Reddit.
Additionally, a leaked BRAINTREE_PAYPAL_KEY might allow attackers to misuse Braintree's PayPal services on behalf of Reddit without proper authorization. This could lead to financial losses, misuse of resources, or disruptions in the payment processing system, impacting both Reddit and its users.
Overall, the BRAINTREE_PAYPAL_KEY is a critical component for enabling PayPal's functionalities via Braintree on Reddit. Its security is vital in preventing unauthorized access, financial fraud, and ensuring the integrity of payment transactions and financial data on the platform.


* 4- PAYPAL_API_KEY||Object(n.b)()||Object(n.c)()?"production":"sandbox",buttons:{premium:"LAYT3KA5EVVTJ",coins500:"SNCZX9LADYMT4",coins1100:"6P6X4LTAKNDGG",coins1800:"2P5FZYZL42NME",coins7200:"W8BKWZXBSWZGC",coins40000:"Y9LZ5M2W6VT3A",coinsGild500:"BPVKB5BY8HXRA",coinsGild1100:"TPGZ3HZ3KE5TS",coinsGild1800:"YXZDTMAGNMMEA",coinsGild7200:"MQDLLC4FBNSZG",coinsGild40000:"T3RL7U6STH7WL"
The PAYPAL_API_KEY you're referring to seems to be a part of the configuration or settings related to PayPal integration within Reddit. However, the format provided appears to have a conditional structure involving Object(n.b)() and Object(n.c)() that seems incomplete, possibly indicating a conditional check or logic associated with the PayPal API key for distinguishing between production and sandbox environments.
In general, the function of a PayPal API key in any online platform, including Reddit, is to authenticate and authorize access to PayPal's services. This key is used to establish a secure connection between Reddit's systems and PayPal's API (Application Programming Interface). It allows Reddit to initiate and manage payment transactions, process financial operations, and interact with PayPal's infrastructure securely.
As for sensitivity, API keys like the PAYPAL_API_KEY are indeed considered sensitive information. If this key were to be exposed or leaked, especially in a scenario where it distinguishes between production (live/real) and sandbox (testing) environments, it could pose several risks:
Unauthorized Transactions: Attackers could potentially use the exposed key to perform unauthorized transactions, manipulate payment configurations, or access sensitive financial data associated with PayPal transactions conducted through Reddit.
Misuse of Sandbox Environment: If the key determines whether Reddit operates in a sandbox environment for testing purposes, unauthorized access might lead to the abuse of testing resources or functionalities, potentially disrupting development or testing processes.
Financial Risks: Leaking sensitive payment-related keys could result in financial losses, fraudulent activities, or disruptions in the payment processing system, affecting both Reddit and its users.
Regarding the provided keys such as buttons, these seem to represent specific identifiers or labels associated with different payment options or packages (e.g., premium subscriptions, various coin packages) within Reddit's payment system. These keys likely serve as references or identifiers for specific payment options presented to users during transactions.
Overall, while the specific context of the conditional statement isn’t entirely clear, the PAYPAL_API_KEY and associated payment identifiers are crucial for Reddit's PayPal integration, and their security is essential to safeguard against unauthorized access, financial fraud, and maintain the integrity of payment transactions within the platform.


* 5- giphyApiKey:"k2kwyMA6VeyHM6ZRT96OXDGaersnx73Z"
The giphyApiKey key is used to authenticate requests to the Giphy API. This API is used by reddit.com to fetch GIFs and other animated images.
The key is a secret vulnerability because it is used to authenticate requests to the API. If the key is leaked to attackers, they can use it to make unauthorized requests to the API. These requests can then be used to:
Fetch GIFs that are not publicly available: Attackers can use the key to fetch GIFs that are only available to premium users or that have been marked as private.
Modify GIFs: Attackers can use the key to modify GIFs, such as changing the text or adding watermarks.
Delete GIFs: Attackers can use the key to delete GIFs.
The impact if it is leaked to attackers
The impact of leaking the giphyApiKey key would depend on how it is used by attackers. However, it could potentially have a significant impact on reddit.com, its users, and the Giphy API.
How to protect reddit.com from attacks
To protect reddit.com from attacks, site administrators should:
Secure the key: The key should be stored in a secure location and only accessible to authorized personnel.
Change the key regularly: The key should be changed regularly to make it more difficult for attackers to obtain it.
Monitor the site for suspicious activity: If administrators see any signs of suspicious activity, they should investigate immediately.
By taking these steps, reddit.com can help to protect itself from attacks using the stolen giphyApiKey key.
Specific steps reddit.com can take
In addition to the general steps listed above, reddit.com can also take the following specific steps to protect itself from attacks using the stolen giphyApiKey key:
Scan the site for any existing malicious GIFs. Attackers may have already uploaded malicious GIFs before the key was changed.
Educate users about the risks of malicious GIFs. Users should be aware that they should not click on any links or open any files in a GIF unless they are sure that the GIF is legitimate.
Work with Giphy to investigate the leak. Giphy may be able to help reddit.com to identify the source of the leak and take steps to prevent it from happening again.
By taking these steps, reddit.com can help to protect its users and its site from attacks.
Specific examples of how attackers could use the giphyApiKey key
Here are some specific examples of how attackers could use the giphyApiKey key:
To spread spam: Attackers could use the key to fetch GIFs that are relevant to a particular topic or audience and then post those GIFs to reddit.com or other websites. This could be used to spread spam, promote illegal content, or engage in other malicious activities.
To spread misinformation: Attackers could use the key to fetch GIFs that contain false or misleading information and then post those GIFs to reddit.com or other websites. This could be used to spread misinformation or propaganda.
To target individuals or groups: Attackers could use the key to fetch GIFs that are targeted at a particular individual or group. This could be used to harass or intimidate individuals or groups.
By understanding the potential risks of leaking the giphyApiKey key, reddit.com can take steps to protect itself and its users from attacks.


* 6-  muxApiKey:"mcpf0hehcbo78k9u67arfer8a"
The muxApiKey is a key used on the Reddit website for handling multimedia content, specifically related to Mux services. Mux provides infrastructure for video streaming, analytics, and monitoring. This key is essentially an identifier that allows Reddit's systems to communicate securely with Mux services, ensuring that multimedia content like videos is properly managed and delivered to users.
This key is considered sensitive and somewhat confidential. If it were to be leaked or compromised by attackers, it could potentially lead to several issues. One of the primary concerns would be unauthorized access or tampering with multimedia content served through Mux. This could result in a compromise of video content, potentially allowing malicious actors to manipulate or replace videos on the Reddit platform, leading to misinformation or security breaches.
Moreover, if this key is exposed, it might enable attackers to use Reddit's resources on the Mux platform without permission, leading to misuse of resources and potentially incurring unexpected costs or disrupting services.
Overall, the muxApiKey is a critical component in managing multimedia content on Reddit, and its security is paramount to ensure the integrity and safety of the platform's multimedia functionalities.


* 7- EMBEDLY_KEY||"522baf40bd3911e08d854040d3dc5c07" The embedlyApiKey on the Reddit website serves the purpose of integrating and displaying embedded content from various sources across the web. Embedly is a service that allows websites to embed rich media content like videos, articles, and images from different platforms and sources.
This key is used by Reddit's systems to communicate securely with Embedly's services, enabling the platform to fetch and display content previews, such as when users post links or embed media in their posts or comments.
Regarding its sensitivity, while it's not a private key per se, it still holds importance in the functionality of the platform. If this key were to be compromised or leaked by attackers, it could lead to potential abuse or disruption of the embedded content functionality on Reddit. Attackers might misuse the key to manipulate embedded content or disrupt the way these external resources are displayed, affecting the user experience by potentially altering the appearance or accessibility of linked content.
Moreover, a leaked embedlyApiKey could allow unauthorized access to Embedly's services using Reddit's account, leading to misuse of resources and potentially incurring unexpected costs or service disruptions.
In summary, the embedlyApiKey is crucial for integrating external content into Reddit, and while not as sensitive as certain authentication keys, its security is vital to ensure the proper functioning and security of embedded content on the platform.


[*] I cannot attach more keys or information, and I will suffice with screenshots. No, the file is very large and I cannot review it. I leave this matter to you because this is confidential information and I will not access it without your permission.
* Link : https://www.redditstatic.com/desktop2x/Governance~Reddit.d5b31ca1a5d24df34b88.js


## Steps To Reproduce:
[add details for how we can reproduce the issue]
* [ I discovered this link while I was conducting a survey and collecting information, and I discovered it when I visited this link https://www.reddit.com/?rdt=49420 after logging into my account, as I will explain in pictures using the Trufflehog tool. ]


## Impact

* The impact is very large due to the large number of leaked information and its many types, and I will not be able to mention all the possible impact due to the large number of leaked information. I will leave this matter to you, and I believe that this will require a great deal of time and effort that

## Attachments
No attachments
