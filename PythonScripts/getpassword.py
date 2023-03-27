from pwinput import pwinput

username = input('Username : ')
password = pwinput(prompt='Password : ', mask='0')

print(f'Got Username : {username}')
print(f'Got Password : {password}')

