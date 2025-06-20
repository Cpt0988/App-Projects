import string
import secrets
# homework check for uppercase and symbols
#checks
def contain_upper(password: str)-> bool:
    for char in password:
        if char.isupper():
            return True
        
        
def contain_symbols(password: str)-> bool:
    for char in password:
        if char in string.punctuation:
            return True
        
    return True


def generate_password(length : int, symbols: bool, uppercase: bool)->str:
    comboination : str = string.ascii_lowercase + string.digits
    
    if symbols:
        comboination += string.ascii_uppercase
    
    comboation_length = len(comboination)
    new_password : str = ''
    
    for _ in range(length):
        new_password += comboination[secrets.randbelow(comboation_length)]
    return new_password

if __name__ == '__main__':
    for i in range(1,6):
        new_pass :str = generate_password(length=10,symbols=True, uppercase=True)
        specs : str = f' u:{contain_upper(new_pass)}, s:{contain_symbols(new_pass)}'
        print(f'{i} -> {new_pass}{specs}')
