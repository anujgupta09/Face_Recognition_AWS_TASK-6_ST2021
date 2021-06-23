def send_whatsup_msg(whatsup_no):
    
    from datetime import datetime
    obj_now = datetime.now()
    hour = obj_now.hour
    minute = obj_now.minute
    minute_plus1 = minute+1
    
    final_no = '+91'+whatsup_no
    import pywhatkit
    try:
        pywhatkit.sendwhatmsg(final_no,
                        "Whatsup Done Correctly",
                        hour, minute_plus1)
        print("Message Sent","to",whatsup_no)
    except:
        print("An Unexpected Error!")