from json import dump,load
from cryptography.fernet import Fernet
import format as fm

def key()->bytes:
    '''Get key that the user created at set-up'''
    with open('key.key','rb') as key:
        return key.read()

class Fernet_:
    fernet=Fernet(key())

class Entry:
    ID='10000'

    @staticmethod
    def push(d1:dict):
        '''Store the entry into the database'''
        for j in d1.values():
            en=Fernet_.fernet.encrypt(eval(f"b'{j[1]}'"))
        d1,fPwdBIN=Entry.pack(d1)
        p=Entry.nCpull()
        p.update(d1)
        with open('Entry.json','w') as pwdJSON:
            dump(p,pwdJSON)
        with open(fPwdBIN,'wb') as pwdBIN:
           pwdBIN.write(en)

    @staticmethod
    def pull()->dict:
        '''Get all entries from database'''
        with open('Entry.json','r') as j:
            pwd = load(j)
        return Entry.unpack(pwd)


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
            with open('./Entry/entryNumber.txt','r') as no:
                file_=no.read()
            file=file_[1:]
            entry_[1]=f'./Entry/{file}'+'.bin'
            new_[entry]=entry_
            with open('./Entry/entryNumber.txt','w') as no:
                no.write(str(int(file_)+1))

        return new_,entry_[1]

    @staticmethod
    def nCpull():
        '''Pull without change'''
        with open('Entry.json','r') as j:
            pwd = load(j)
        return pwd

class Console:
    run=True
    cmd={'new':Entry.push,'ls':Entry.pull}

    @classmethod
    def init(cls):
        #while cls.run:
        for _ in range(10):
            in_=Console.input_() # Get input

            if in_['main']=='new':
                # Execute the function call
                fom=fm.getFormat(in_['main']) 
                pom=fom(in_['args'])
                cls.cmd['new']({pom['website']: #Entry Format 
                    [pom['mail'],pom['password']]
                })

            elif in_['main']=='ls':
                # Execute the function call
                pull=cls.cmd['ls']()

                # Get entries
                entry=Entry.pull()
                entries=[entry_ for entry_ in entry.keys()]

                try:
                    toFm=entry[
                        entries[
                                int(in_['args']['index'])-1
                            ]]
                    format = fm.ls(index=in_['args']['index'])['success'].format(entries[int(in_['args']['index'])-1],toFm[0],toFm[1])
                    print(format)
                except:
                    format = fm.ls()['success']
                    c=1
                    for k,v in entry.items():
                        format=format+f"\n{'0'*(2-len(str(c)))}{c})"+\
                            f"{k}{' '*(17-len(k))}{v[0]}{' '*(21-(len(v[0])-3))}{v[1]}"
                        c+=1 
                    print(format)

    @staticmethod
    def input_()->dict:
        '''Get the command input from console'''
        args_={'i':'index'}
        in_=input('> ').split()
        c=0
        args=dict()
        for parts in in_:
            if c==0:
                c+=1
                continue
            if parts.startswith('-'):
                key=args_[parts.replace('-','')]
                args[key]=in_[c+1]
                c+=2
                continue

        return {'main':in_[0],'args':args}

c=Console()
c.init()
