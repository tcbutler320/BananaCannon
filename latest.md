<!--
**DID YOU MAKE SURE TO CLEAR CACHE BEFORE OPENING AN ISSUE?**
Sometimes your browser has old files cached and the bug you are experiencing might be already fixed, or is just a side effect of a new update. If you don't know how to do that, this website should help: https://www.pcmag.com/how-to/how-to-clear-your-cache-on-any-browser

-->

**Describe the bug**: The [Tribe Chat](https://dev.monkeytype.com/tribe) is vulnerable to Authentication Bypass by Spoofing allowing any user to send messages that appear to come from other users. Malicious users can abuse current socket message authentication measures to spoof other u


https://user-images.githubusercontent.com/41709108/120562925-68490b80-c3d5-11eb-8ca0-e184e75d550f.mp4


sers in the chat room by modifying raw socket.io messages.

<!-- **Did it happen in incognito mode?**

https://user-images.githubusercontent.com/41709108/120562760-0ee0dc80-c3d5-11eb-9133-2279e1d5fae5.mp4


Sometimes things work in incognito mode, which allows me to further track down the issue. -->


**To Reproduce** <!-- Steps to reproduce the behavior: -->

1. Go to a tribe chat room, ex: https://dev.monkeytype.com/tribe_1d849e
2. Send a message, capturing the socket.io message. 
`42["mp_chat_message",{"isSystem":false,"isLeader":true,"message":"Hey this is still alice","from":{"id":"UocD_4qRZiXGbXf8AA-n","name":"alice"}}]`
3. Modify the name parameter, and re-send
`42["mp_chat_message",{"isSystem":false,"isLeader":true,"message":"Hey this is still alice","from":{"id":"UocD_4qRZiXGbXf8AA-n","name":"bob"}}]`  

**Expected behavior** After sending the socket

**Screenshots** <!-- If applicable, add screenshots to further help explain your problem. -->

**Desktop:** <!-- if you encountered an issue while using Monkeytype on your computer please complete the following information, delete this section if not-->

- OS: [] <!-- e.g. Windows 10, MacOS, Linux-->
- Browser [] <!-- e.g. Chrome, Firefox, Safari, etc... -->
- Browser Version [] <!-- e.g. 22 -->


**Additional context** <!-- Add any other context about the problem here. -->
