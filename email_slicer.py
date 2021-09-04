import re
falg=True
choise="y"
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
while choise.lower()=="y":
    while falg==True:
        mail=input("Enter Your email here : ")
        if(re.search(regex,mail)):  
            #print("Valid Email")
            x=mail.index('@')
            un=mail[:x]
            dn=mail[x:]
            print("-"*60)
            print("User Name : {}     |     Domain Name : {}".format(un,dn))
            print("-"*60)
            break
        else:  
            print("Invalid Email")
            continue
    choise=input("Want to slice again press ' y ' : ")
print("_"*60)