from tkinter import Tk,Entry,Button
from cryptography.fernet import Fernet
from json import load,dump


def key()->bytes:
    with open('key.bin','rb') as key:
        return key.read()

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
