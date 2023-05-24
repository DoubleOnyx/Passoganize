import cryptography.fernet
from cryptography.fernet import Fernet

# print(Fernet(b'aoni8mzlpR_E9mUBDvjQ3ym_pK4vxTwp-1mlNdoaihI=').encrypt(b'IknowNone'))

# test='90001'
# test=test[1:]
# print(test)

# file='10000'
# file=file[1:]
# print(f'./Password/{file}'+'.bin')

Fernet(b'aoni8mzlpR_E9mUBDvjQ3ym_pK4vxTwp-1mlNdoaihI=').decrypt(b'gAAAAABkbH7C_ecJzXi4h5_TVFXOeL2PXrL-DNjeLrRhcdn4zXfJuSm3XKME_gzo6oWdzNr6uDzkq-TaZhdX8a2r_RT1fMyK7weV2X7miW4IVYufmj-hSl8=')