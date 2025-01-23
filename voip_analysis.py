import pyshark  

 
pcap_file = "SIP-Call-with-proxy-Server.pcap"   
capture = pyshark.FileCapture(pcap_file, display_filter="sip")  
 

 
print("Analyzing SIP packets...\n")  
for packet in capture:   
    try:
        
        sip_layer = packet.sip
        
         
        message_type = sip_layer.get_field("Request-Line") or sip_layer.get_field("Status-Line")
         

        from_field = sip_layer.get_field("From")   
        to_field = sip_layer.get_field("To")   
        call_id = sip_layer.get_field("Call-ID")   

         
        print(f"Message Type: {message_type}")
        print(f"From: {from_field}")
        print(f"To: {to_field}")
        print(f"Call-ID: {call_id}")
        print("-" * 50)  

    except AttributeError:
         
        continue

 
capture.close()  
print("SIP traffic analysis completed.")   

with open("sip_analysis_results.txt", "w") as file:
    for packet in capture:
        try:
            sip_layer = packet.sip
            message_type = sip_layer.get_field("Request-Line") or sip_layer.get_field("Status-Line")
            from_field = sip_layer.get_field("From")
            to_field = sip_layer.get_field("To")
            call_id = sip_layer.get_field("Call-ID")
            
            file.write(f"Message Type: {message_type}\n")
            file.write(f"From: {from_field}\n")
            file.write(f"To: {to_field}\n")
            file.write(f"Call-ID: {call_id}\n")
            file.write("-" * 50 + "\n")
        except AttributeError:
            continue
print("Results saved to sip_analysis_results.txt")
