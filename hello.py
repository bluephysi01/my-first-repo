def print_hello(value: str)-> Str:
    if isinstance(value,str):
        return f'Hello,{value}'
    else:
        return 'This is not string'

if __name__=='__main__':
    result = print_hello('John')
    print(result)

