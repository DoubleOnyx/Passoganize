website='abc.xyz'
mail='abc@xyz.com'
pwd='124'
p={website:[mail,pwd]}
# result=f'''Saved new password:
#     Website          Mail                    Password
#     {website}{' '*(17-len(website))}{mail}{' '*(21-(len(mail)-3))}{pwd}
# '''

# print(result)

success='''Saved passwords:   
   Website          Mail                    Password'''

c=1
for k,v in p.items():
    success=success+f"\n{'0'*(2-len(str(c)))}{c})"+\
        f"{website}{' '*(17-len(website))}{mail}{' '*(21-(len(mail)-3))}{pwd}"
    c+=1
    print(success)