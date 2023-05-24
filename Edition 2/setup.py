if __name__=='__main__':
    from cryptography.fernet import Fernet
    with open('key.key','wb') as keyF:
        keyF.write(Fernet.generate_key())