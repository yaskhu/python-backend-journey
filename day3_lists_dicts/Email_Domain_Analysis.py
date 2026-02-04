def Email_Domain_Analysis(emails):
    dic={}
    email=0
    yahoo=0
    outlook=0
    for mail in emails:
        if mail.endswith("gmail.com"):
            if email in dic:
                email+=1
            else:
                dic['email']=1
        if mail.endswith("yahoo.com"):
            if yahoo in dic:
                yahoo+=1
            else:
                dic['yahoo']=1
        else:
            outlook+=1
    return dic
print(Email_Domain_Analysis(emails = [
  "a@gmail.com",
  "b@yahoo.com",
  "c@gmail.com",
  "d@outlook.com"
]))