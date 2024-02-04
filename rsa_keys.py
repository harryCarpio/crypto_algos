from Crypto.PublicKey import RSA  

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print('Private key:')
print(private_key.decode())
print('\nPublic key:')
print(public_key.decode())