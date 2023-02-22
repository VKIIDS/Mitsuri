print ('''

███╗░░░███╗██╗████████╗░██████╗██╗░░░██╗██████╗░██╗
████╗░████║██║╚══██╔══╝██╔════╝██║░░░██║██╔══██╗██║
██╔████╔██║██║░░░██║░░░╚█████╗░██║░░░██║██████╔╝██║
██║╚██╔╝██║██║░░░██║░░░░╚═══██╗██║░░░██║██╔══██╗██║
██║░╚═╝░██║██║░░░██║░░░██████╔╝╚██████╔╝██║░░██║██║
╚═╝░░░░░╚═╝╚═╝░░░╚═╝░░░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝

''')

print('What you want to use?')
print('[+] Calculator')
print ('[+] Ip info')
print ('[+] Exploit database')
print ('[+] Google hacking database')
print ('[+] Courses')
print ('[+] Info')
print ('[+] Nmap scripts')
print('[+] How to install')
print('[+] Contact me')
print ('For example: Ip_info, Contact_me or more')
a = input('What you wanna use from this script: ')
if a == ('Calculator'):
    A = int(input('Print your first number: '))
    B = int(input('Print your two number: '))
    print ('%, *, **, /, //, -, +, ')
    C = input('What you want to do: ')
    if C == ('*'):
        print (A * B)
    elif C == ('**'):
        print (A ** B)
    elif C == ('%'):
        print(A % B)
    elif C == ('/'):
        print(A / B)
    elif C == ('//'):
        print(A // B)
    elif C == ('-'):
        print(A - B)
    elif C == ('+'):
        print(A + B)
print("Wanna continue?")
c = input()
if c == ('yes'):
    continue 