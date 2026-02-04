def User_Data_Validation(pack):
    for minipack in pack:
        for key,val in minipack.items():
            if key == 'email' and val != "" :
                print(val)
User_Data_Validation([
  {"id": 1, "email": "a@gmail.com"},
  {"id": 2, "email": ""},
  {"id": 3},
  {"id": 4, "email": "b@gmail.com"}
]
)