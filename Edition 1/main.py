from tkinter import Tk,Entry,Button
from cryptography.fernet import Fernet
from json import load,dump


def key()->bytes:
    with open('key.bin','rb') as key:
        return key.read()

# class Password2:
#     @staticmethod
#     def field(password:str):
#         pwd=Fernet(Password.key()).encrypt(eval(f"b'{password}'"))
#         return str(pwd).replace('b','').replace("'",'')

#     @staticmethod
#     def unfield(field:str):
#         pwd=Fernet(Password.key()).decrypt(eval(f'b"{field}"'))#.decrypt(eval(f"b'{field}'"))
#         return str(pwd)

#     @staticmethod
#     def pull()->dict:
#         with open('passwords.json','r') as j:
#             return load(j)

#     @staticmethod
#     def push(passwords:dict)->None:
#         ## 
#         passes=Password.pull()
#         with open('passwords.json','w') as jW:
#             passes.update(passwords)
#             dump(passes,jW)
#Password.push({'A':['B',Password.field('C')]})
#Password.unfield('gAAAAABkGXkpH-Snx1wGXW_QztCBa9OnE0yyd0CFxOX9c_V37nEnne8yc6OIxdtgzRmvPse5Fsy7trTU__10280QIS4fPw==')
#print(Fernet(Password.key()).decrypt(b'gAAAAABkGXkpH-Snx1wGXW_QztCBa9OnE0yyd0CFxOX9c_V37nEnne8yc6OIxdtgzRmvPse5Fsy7trTU__10280QIS4fPw=='))

## Rewrite

# class Password:
#     @staticmethod
#     def field(password:str):
#         pwd=Fernet(Password.key()).encrypt(eval(f"b'{password}'"))
#         return str(pwd).replace('b','').replace("'",'')

#     @staticmethod
#     def unfield(field:str):
#         pwd=Fernet(Password.key()).decrypt(field)#.decrypt(eval(f"b'{field}'"))
#         return str(pwd)

#     @staticmethod
#     def pull()->dict:
#         with open('passwords.json','r') as j:
#             pwd = load(j)
#         pwd:dict
#         npwd:dict
#         for k,v in pwd.items():
#             v[1]=Fernet(Password.key()).decrypt()
#             npwd[k]=v                    

#     @staticmethod
#     def push(passwords:dict)->None:
#         ## 
#         passes=Password.pull()
#         with open('passwords.json','w') as jW:
#             passes.update(passwords)
#             dump(passes,jW)

#     @staticmethod
#     def key():
#         with open('key.bin','rb') as key:
#             return key.read()

# class Command:
#     def __init__(self) -> None:
#         pass
#     @staticmethod
#     def new():
#         web,mail,pwd=input('Enter the website:'),input('Enter the mail/username:'),input('Enter the password:')


# if __name__ == '__main__':
#     func={'new':Command.new}
#     func[input('>')]()

'''
> new
'''
class Fernet_:
    fernet=Fernet(key())

class Password:
    ID='10000'

    @staticmethod
    def push(d1:dict):
        for j in d1.values():
            en=Fernet_.fernet.encrypt(eval(f"b'{j[1]}'"))
        d1,fPwdBIN=Password.pack(d1)
        p=Password.nCpull()
        p.update(d1)
        with open('passwords.json','w') as pwdJSON:
            dump(p,pwdJSON)
        with open(fPwdBIN,'wb') as pwdBIN:
           pwdBIN.write(en)

    @staticmethod
    def pull()->dict:
        with open('passwords.json','r') as j:
            pwd = load(j)
        return Password.unpack(pwd)


    @staticmethod
    def unpack(data:dict)->dict:
        new_=dict()
        for entry,entry_ in data.items():
            with open(entry_[1],'rb') as pwdF:
                read=pwdF.read()
                enter=str(Fernet_.fernet.decrypt(read)).replace('b\'','').replace('\'','')
                entry_[1]=enter
            new_[entry]=entry_
        
        return new_
    
    @staticmethod
    def pack(data:dict):
        new_=dict()
        for entry,entry_ in data.items():
            file=Password.ID
            file=file[1:]
            entry_[1]=f'./Password/{file}'+'.bin'
            new_[entry]=entry_
            Password.ID=str(int(Password.ID)+1)

        return new_,entry_[1]

    @staticmethod
    def nCpull():
        '''Pull without change'''
        with open('passwords.json','r') as j:
            pwd = load(j)
        return pwd


#Password.unpack(Password.pull())
di={'Spotify':['adityadasch@gmail.com','Krishna340']}
print(Password.push(di))
print(Password.pull())
