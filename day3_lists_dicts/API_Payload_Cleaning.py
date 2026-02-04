def API_Payload_Cleaning(payload): 
    for key in list(payload.keys()):
        val = payload[key]
        
        if val is None:
            del payload[key]  
        elif isinstance(val, str):
            payload[key] = val.replace(" ", "") 
    return payload

print(API_Payload_Cleaning({
  "name": "  Name ",
  "email": " name@gmail.com ",
  "age": None
}))