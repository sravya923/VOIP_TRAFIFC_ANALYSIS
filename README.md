WIRESHARK TOOL AND REPORT 
 Title: VoIP Traffic Analysis Using SIP 

This activity aims to analyze Session Initiation Protocol (SIP) traffic, a key component of VoIP 
communication, using Wireshark, an open-source network protocol analyzer 
 
Introduction 
• VoIP Traffic Analysis: is the process of examining both signaling and media traffic within Voice 
over IP (VoIP) systems. It involves analyzing communication protocols, such as the Session 
Initiation Protocol (SIP), which is essential for establishing, managing, and terminating VoIP 
calls. 
• The primary purpose of this activity is to gain insights into the behavior and performance of 
VoIP traffic. By leveraging tools like Wireshark, an open-source network protocol analyzer, the 
analysis focuses on identifying potential issues, optimizing performance, and ensuring security 
within VoIP networks. This hands-on activity enables the identification of signaling flows, 
packet loss, jitter, and other factors that may impact call quality or functionality. 
 
Tools and Methodology 
• Tools Used: Wireshark (Open-source network protocol analyzer) 
▪ PCAP File: sip-call-proxy-server.pcap 
Methodology:   
The steps below were taken to analyze SIP traffic from a VoIP call: 
1. Downloaded the sample PCAP file containing SIP traffic from GITHUB. 
2. Opened the PCAP file in Wireshark. 
3. Filtered traffic using the SIP filter (sip). 
4. Examined SIP messages such as INVITE, ACK, RINGING, 200 OK, and BYE. 
5. Exported relevant SIP stream details for analysis. 
 
 
Analysis and Findings: 
Packet Details: The SIP packets analyzed are (INVITE, RINGING, 200 OK, BYE) 
For each packet, include: 
1.Packet Type:  Session Initiation Protocol (INVITE) 
From:  From: <sip:201@10.33.6.101>;tag=1c751049942 
SIP from address: sip:201@10.33.6.101 
SIP from tag: 1c751049942 
To:  To: <sip:101@10.33.6.102;user=phone> 
Call-ID: Call-ID: 75104938772201062721@10.33.6.101 
  
                            
 
 
2. Packet Type: Session Initiation Protocol (180) 
From:  From: <sip:201@10.33.6.101>;tag=1c751049942 
To:   To: <sip:101@10.33.6.102;user=phone>;tag=1c2071048551 
Call-ID:  Call-ID: 75104938772201062721@10.33.6.101 
                   
 
 
3. Packet Type:   Session Initiation Protocol (200) OK 
From: From: <sip:201@10.33.6.101>;tag=1c751049942   
To:    To: <sip:101@10.33.6.102;user=phone>;tag=1c2071048551 
Call-ID:   Call-ID: 75104938772201062721@10.33.6.101 
                                
 
  4. Packet Type:  Session Initiation Protocol (BYE) 
  From:  From: <sip:101@10.33.6.102;user=phone>;tag=1c2071048551 
  To:  To: <sip:201@10.33.6.101>;tag=1c751049942 
  Call-ID:    Call-ID: 75104938772201062721@10.33.6.101 
 
                              
 
 
 
Observations: 
The SIP call began with an INVITE message from  
<sip:201@10.33.6.101>;tag=1c751049942  . The call was accepted with a 200 OK 
response, and the session was terminated with a BYE message. The analysis showed 
that the signaling was successfully captured, but no RTP traffic was present in this 
sample. 
 
Conclusion: 
         This activity demonstrated how to analyze VoIP traffic using Wireshark. SIP traffic was 
successfully filtered and examined, revealing the call flow from initiation to termination. This 
analysis highlights the importance of SIP in VoIP communication and its role in ensuring 
seamless signaling. 
 
