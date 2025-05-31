# HTML injection in API response including request url

## Report Details
- **Report ID**: 1719588
- **URL**: https://hackerone.com/reports/1719588
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-10-02T04:02:09.331Z
- **Disclosed**: 2023-05-18T14:40:33.796Z

## Reporter
- **Username**: prilvesh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Hi  Reddit , 
I found a way to  distribute, persist &   store  Illegal images    such as child porn , beheadings  on reddit and in plain sight  .
I can also store & distribute xml ,json   data eg illegal links .
I can also store & communicate illegal instructions  aka terrorist messages  in  html  and  plain text.
This hack  also bypasses all security related to detecting illegal messages & pictures on reddit


## Impact:
Many possible impacts :
Criminals  could trade child porn ,beheading and other illegal  images on reddit  without detection .
Criminals & Terrorist groups could  distribute illegal  bombing & attack messages  
Criminals could store JavaScript code  
User will not be presented with Warning that you are navigating away from Reddit.com 
Criminals could  pretend to be Legitimate  Reddit employees and trick  reddit users into  navigating to & executing the code simply by right click Go to in there browser as  a result Criminals could  exploit reddit users &  steal there cookies and   infect them with  viruses etc once they execute the  stored code . 
All of the above would by pass Reedits automated  systems .
To execute this proof of concepts please Login to reddit as a user than navigate to the  url.


There are 3 classes 
1) Storage , Persistence by criminals
2) Retrieval , By criminals
3)Executions -involuntary by unsuspecting reddit users.
The data  retrieval can be voluntary eg criminal networks  doing scheduled drop offs and pick ups , or hackers deliberately persisting malicious code that infects or spies on involuntary curious users   landing form hrefs and following instructions but  instead  getting pawned  due to executing the JavaScript.


##PROOF OF Distributing child porn  
You will see BART SIMPSON image as an example but  its clear that he  API  isn't going to run any sort of Image recognition validation or neural net on  this API  input. The below demonstrates  misusing the  reditt.com  api  to store  illegal images
It also demonstrates criminals can than access and trade illegal  like child porn images in plain site on reddit. 


<code>
https://s.reddit.com/REDIT.EXPERIMENTAL.FEATURE:Hi.user.You.know.we.got.the.stuff.right.click.and.go.on.data..........data:image/jpeg;base64,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

Also Criminals can get the data to persist and store it on reddit.com  as valid links in  href of a elements.
<a href='insert_above_url_in_here'  > Now it persists</a>
This method will not be detected by current automation systems  ,Criminals can  further avoid human  simply by posting normal valid comments and a links  eg on monday normal and than on Friday lets say 12 pm  for 2 hours  at a scheduled window they can edit the same comment and update it to   Child porn or illegal images so there clients can down load it  for  trading purposes. etc.

##PROOF OF Terrorist & Illegal bombing messages being distributed 
Once again criminals can have the data stored on reddit.com and persist through using <a href='insert_below_url_in_here'  > Now it persists</a> a
So this  demonstrates  Illegal message and persistence.
when the user is on the  url he will see message and instructions on how to join and view the message  which is just right click and go.

<code>
https://s.reddit.com/WELCOME_TO_MY_CRIME_NETWORK_RIGHT_CLICK_AND_NAVIGATE_TO_THIS=data:text/html,<style>body{background-color:red;color:white}h1{font-size:50pt;margin-top:400PX;margin-left:100px;}p{font-size:25pt;margin-left:100px;}</style><h1>Top Secret ILLEGAL Criminal MESSAGE DISTRIBUTION</h1><p> This message will not be detected by AI systems,Your Mission  is  to Blow up something on the 12 of December 2022  4 pm a  water melon   at location MEXICO CITY</h1>

Once again the same avoid  human  detection with scheduled edits and can actually mobilize new reddit users to join in.

##PROOF  OF  Storing and Distributing Javascript
This demonstrates storing, distribution  of  potentially dangerous JavaScript code  using reddit.com
The code can persist as part of    a comment  using  <a href='insert_below_url_in_here'  > Now it persists</a>

<code>
https://s.reddit.com/WELCOME.TO.REDDITS.EXPERIMENTAL.FEATURE.RIGHT.CLICK.AND.GO.TO:data:text/html,%3Cscript%3Ealert('You%20could%20have%20been%20hacked%20with%20more%20advances%20js%20')%3C/script%3E%22


##PROOF OF Storing  and Distributing JSON data  using reddit.
This demonstrates storing, distribution  json data eg  criminals   exchanging data such as illegal  links or data.
The  json can persist as part of    a comment  using  <a href='insert_below_url_in_here'  > Now it persists</a>

<code>
https://s.reddit.com/ILLEGAL_JSON_DISTRIBUTION_DOWNLOAD_HERE=data:text/json;charset=utf-8,[%20%7B%20%22id%22:%201,%20%22name%22:%20%22Leanne%20Graham%22,%20%22username%22:%20%22Bret%22,%20%22email%22:%20%22Sincere@april.biz%22,%20%22address%22:%20%7B%20%22street%22:%20%22Kulas%20Light%22,%20%22suite%22:%20%22Apt.%20556%22,%20%22city%22:%20%22Gwenborough%22,%20%22zipcode%22:%20%2292998-3874%22,%20%22geo%22:%20%7B%20%22lat%22:%20%22-37.3159%22,%20%22lng%22:%20%2281.1496%22%20%7D%20%7D,%20%22phone%22:%20%221-770-736-8031%20x56442%22,%20%22website%22:%20%22hildegard.org%22,%20%22company%22:%20%7B%20%22name%22:%20%22Romaguera-Crona%22,%20%22catchPhrase%22:%20%22Multi-layered%20client-server%20neural-net%22,%20%22bs%22:%20%22harness%20real-time%20e-markets%22%20%7D%20%7D,%20%7B%20%22id%22:%202,%20%22name%22:%20%22Ervin%20Howell%22,%20%22username%22:%20%22Antonette%22,%20%22email%22:%20%22Shanna@melissa.tv%22,%20%22address%22:%20%7B%20%22street%22:%20%22Victor%20Plains%22,%20%22suite%22:%20%22Suite%20879%22,%20%22city%22:%20%22Wisokyburgh%22,%20%22zipcode%22:%20%2290566-7771%22,%20%22geo%22:%20%7B%20%22lat%22:%20%22-43.9509%22,%20%22lng%22:%20%22-34.4618%22%20%7D%20%7D,%20%22phone%22:%20%22010-692-6593%20x09125%22,%20%22website%22:%20%22anastasia.net%22,%20%22company%22:%20%7B%20%22name%22:%20%22Deckow-Crist%22,%20%22catchPhrase%22:%20%22Proactive%20didactic%20contingency%22,%20%22bs%22:%20%22synergize%20scalable%20supply-chains%22%20%7D%20%7D,%20%7B%20%22id%22:%203,%20%22name%22:%20%22Clementine%20Bauch%22,%20%22username%22:%20%22Samantha%22,%20%22email%22:%20%22Nathan@yesenia.net%22,%20%22address%22:%20%7B%20%22street%22:%20%22Douglas%20Extension%22,%20%22suite%22:%20%22Suite%20847%22,%20%22city%22:%20%22McKenziehaven%22,%20%22zipcode%22:%20%2259590-4157%22,%20%22geo%22:%20%7B%20%22lat%22:%20%22-68.6102%22,%20%22lng%22:%20%22-47.0653%22%20%7D%20%7D,%20%22phone%22:%20%221-463-123-4447%22,%20%22website%22:%20%22ramiro.info%22,%20%22company%22:%20%7B%20%22name%22:%20%22Romaguera-Jacobson%22,%20%22catchPhrase%22:%20%22Face%20to%20face%20bifurcated%20interface%22,%20%22bs%22:%20%22e-enable%20strategic%20applications%22%20%7D%20%7D,%20%7B%20%22id%22:%204,%20%22name%22:%20%22Patricia%20Lebsack%22,%20%22username%22:%20%22Karianne%22,%20%22email%22:%20%22Julianne.OConner@kory.org%22,%20%22address%22:%20%7B%20%22street%22:%20%22Hoeger%20Mall%22,%20%22suite%22:%20%22Apt.%20692%22,%20%22city%22:%20%22South%20Elvis%22,%20%22zipcode%22:%20%2253919-4257%22,%20%22geo%22:%20%7B%20%22lat%22:%20%2229.4572%22,%20%22lng%22:%20%22-164.2990%22%20%7D%20%7D,%20%22phone%22:%20%22493-170-9623%20x156%22,%20%22website%22:%20%22kale.biz%22,%20%22company%22:%20%7B%20%22name%22:%20%22Robel-Corkery%22,%20%22catchPhrase%22:%20%22Multi-tiered%20zero%20tolerance%20productivity%22,%20%22bs%22:%20%22transition%20cutting-edge%20web%20services%22%20%7D%20%7D,%20%7B%20%22id%22:%205,%20%22name%22:%20%22Chelsey%20Dietrich%22,%20%22username%22:%20%22Kamren%22,%20%22email%22:%20%22Lucio_Hettinger@annie.ca%22,%20%22address%22:%20%7B%20%22street%22:%20%22Skiles%20Walks%22,%20%22suite%22:%20%22Suite%20351%22,%20%22city%22:%20%22Roscoeview%22,%20%22zipcode%22:%20%2233263%22,%20%22geo%22:%20%7B%20%22lat%22:%20%22-31.8129%22,%20%22lng%22:%20%2262.5342%22%20%7D%20%7D,%20%22phone%22:%20%22(254)954-1289%22,%20%22website%22:%20%22demarco.info%22,%20%22company%22:%20%7B%20%22name%22:%20%22Keebler%20LLC%22,%20%22catchPhrase%22:%20%22User-centric%20fault-tolerant%20solution%22,%20%22bs%22:%20%22revolutionize%20end-to-end%20systems%22%20%7D%20%7D,%20%7B%20%22id%22:%206,%20%22name%22:%20%22Mrs.%20Dennis%20Schulist%22,%20%22username%22:%20%22Leopoldo_Corkery%22,%20%22email%22:%20%22Karley_Dach@jasper.info%22,%20%22address%22:%20%7B%20%22street%22:%20%22Norberto%20Crossing%22,%20%22suite%22:%20%22Apt.%20950%22,%20%22city%22:%20%22South%20Christy%22,%20%22zipcode%22:%20%2223505-1337%22,%20%22geo%22:%20%7B%20%22lat%22:%20%22-71.4197%22,%20%22lng%22:%20%2271.7478%22%20%7D%20%7D,%20%22phone%22:%20%221-477-935-8478%20x6430%22,%20%22website%22:%20%22ola.org%22,%20%22company%22:%20%7B%20%22name%22:%20%22Considine-Lockman%22,%20%22catchPhrase%22:%20%22Synchronised%20bottom-line%20interface%22,%20%22bs%22:%20%22e-enable%20innovative%20applications%22%20%7D%20%7D,%20%7B%20%22id%22:%207,%20%22name%22:%20%22Kurtis%20Weissnat%22,%20%22username%22:%20%22Elwyn.Skiles%22,%20%22email%22:%20%22Telly.Hoeger@billy.biz%22,%20%22address%22:%20%7B%20%22street%22:%20%22Rex%20Trail%22,%20%22suite%22:%20%22Suite%20280%22,%20%22city%22:%20%22Howemouth%22,%20%22zipcode%22:%20%2258804-1099%22,%20%22geo%22:%20%7B%20%22lat%22:%20%2224.8918%22,%20%22lng%22:%20%2221.8984%22%20%7D%20%7D,%20%22phone%22:%20%22210.067.6132%22,%20%22website%22:%20%22elvis.io%22,%20%22company%22:%20%7B%20%22name%22:%20%22Johns%20Group%22,%20%22catchPhrase%22:%20%22Configurable%20multimedia%20task-force%22,%20%22bs%22:%20%22generate%20enterprise%20e-tailers%22%20%7D%20%7D,%20%7B%20%22id%22:%208,%20%22name%22:%20%22Nicholas%20Runolfsdottir%20V%22,%20%22username%22:%20%22Maxime_Nienow%22,%20%22email%22:%20%22Sherwood@rosamond.me%22,%20%22address%22:%20%7B%20%22street%22:%20%22Ellsworth%20Summit%22,%20%22suite%22:%20%22Suite%20729%22,%20%22city%22:%20%22Aliyaview%22,%20%22zipcode%22:%20%2245169%22,%20%22geo%22:%20%7B%20%22lat%22:%20%22-14.3990%22,%20%22lng%22:%20%22-120.7677%22%20%7D%20%7D,%20%22phone%22:%20%22586.493.6943%20x140%22,%20%22website%22:%20%22jacynthe.com%22,%20%22company%22:%20%7B%20%22name%22:%20%22Abernathy%20Group%22,%20%22catchPhrase%22:%20%22Implemented%20secondary%20concept%22,%20%22bs%22:%20%22e-enable%20extensible%20e-tailers%22%20%7D%20%7D,%20%7B%20%22id%22:%209,%20%22name%22:%20%22Glenna%20Reichert%22,%20%22username%22:%20%22Delphine%22,%20%22email%22:%20%22Chaim_McDermott@dana.io%22,%20%22address%22:%20%7B%20%22street%22:%20%22Dayna%20Park%22,%20%22suite%22:%20%22Suite%20449%22,%20%22city%22:%20%22Bartholomebury%22,%20%22zipcode%22:%20%2276495-3109%22,%20%22geo%22:%20%7B%20%22lat%22:%20%2224.6463%22,%20%22lng%22:%20%22-168.8889%22%20%7D%20%7D,%20%22phone%22:%20%22(775)976-6794%20x41206%22,%20%22website%22:%20%22conrad.com%22,%20%22company%22:%20%7B%20%22name%22:%20%22Yost%20and%20Sons%22,%20%22catchPhrase%22:%20%22Switchable%20contextually-based%20project%22,%20%22bs%22:%20%22aggregate%20real-time%20technologies%22%20%7D%20%7D,%20%7B%20%22id%22:%2010,%20%22name%22:%20%22Clementina%20DuBuque%22,%20%22username%22:%20%22Moriah.Stanton%22,%20%22email%22:%20%22Rey.Padberg@karina.biz%22,%20%22address%22:%20%7B%20%22street%22:%20%22Kattie%20Turnpike%22,%20%22suite%22:%20%22Suite%20198%22,%20%22city%22:%20%22Lebsackbury%22,%20%22zipcode%22:%20%2231428-2261%22,%20%22geo%22:%20%7B%20%22lat%22:%20%22-38.2386%22,%20%22lng%22:%20%2257.2232%22%20%7D%20%7D,%20%22phone%22:%20%22024-648-3804%22,%20%22website%22:%20%22ambrose.net%22,%20%22company%22:%20%7B%20%22name%22:%20%22Hoeger%20LLC%22,%20%22catchPhrase%22:%20%22Centralized%20empowering%20task-force%22,%20%22bs%22:%20%22target%20end-to-end%20models%22%20%7D%20%7D%20]

The same applies to xml data infact  hackers could  host  and persist  almost any type of data they want .
As the api system does not handle validation , error checking and content length  accept for the arbitrary get limit implemented by ngix.


##Conclusion 
I have tested over 50  times  on the api endpoints above and have not been flagged once or rate limited .
An attacker an store and persist any type of data or code they want  and evade  automated detections  because the detection system will not check or validate the api endpoints for  unwanted content , further more the attacker can steal users data and infect them with viruses, trackers ,spyware with more complex stored java scripts ,   if curious users  click the link land on the api page and follow the  simple instructions out of curiosity .
According to my studies at Cisa.gov  this would be classified as very dangerous ability for an attacker , criminal network and  other government funded hackers to have .

I hope this report has been extremely helpful .
Thanks

## Impact

Main impact I would say is  ability to store , distribute  Javascript code , viruses ,malware  and  Illegal pictures.
Span of impact   steal reddit users  data  and  infect reddit users who out of curiosity follow the simple and easy to execute instructions once they view the page  out of curiosity little do they know they would get infected or seen unwanted  illegal material. 

Many possible impacts :
Criminals could store  &persists  JavaScript code 
Users who click the <a> href links in  Redditt comments would land on the api page  and  out of curiosity think its valid  messages from Reddit  and actually execute the  JavaScript code , json  or terrorist influencing  mobilization messages.
Criminals could trade child porn ,beheading and other illegal images on reddit without detection .
Criminals & Terrorist groups could distribute illegal bombing & attack messages
Criminals could store JavaScript code
User will not be presented with Warning that you are navigating away from Reddit.com
Criminals could pretend to be Legitimate Reddit employees and trick reddit users into navigating to & executing the code simply by right click Go to in there browser as a result Criminals could exploit reddit users & steal there cookies and infect them with viruses etc once they execute the stored code .
All of the above would by pass Reedits automated systems .

## Attachments
No attachments
