text = input('Digite algo aqui: ')
print('\033[1m\033[4m\033[7mÉ um número?:', text.isnumeric())
print('É uma letra?:', text.isalpha())
print('Está em minúsculas?:',text.islower())
print('Está em maiúsculas?:', text.isupper())
print('É uma letra ou um número?:', text.isalnum())