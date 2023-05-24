#**kwargs
def setting():
    pass

def new(emDict)->dict:
    website=input('Website:')
    mail=input('Mail/Username:')
    pwd=input('Password:')

    print('\n',end='')

    success=f'''Saved new password:
        Website          Mail                    Password
        {website}{' '*(17-len(website))}{mail}{' '*(21-(len(mail)-3))}{pwd}
    '''

    return {'website':website,'mail':mail,'password':pwd,'success':success}

def ls(**kwargs)->dict:
    try:
        index=kwargs['index']
        success=f'Showing Entry at index {index}:'+'''
            Website:{0}
            Mail/Username:{1}
            Password:{2}
        '''
    except:
        index=-1
        success='''Saved passwords:\n   Website          Mail                  Password'''
    
    return {'index':index,'success':success}

def getFormat(main:str):
    return {'new':new,'ls':ls}[main]