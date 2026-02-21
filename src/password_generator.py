import random

def password_generator(length:int):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    cap_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    special_char = '!@#$%^&*()'
    all_char = alpha + cap_alpha + num + special_char
    passd = [random.choice(all_char) for i in range(length) ]
    print(''.join(passd))

    wrd = ''
    for i in range(length):
        if i == 0:
            #print(random.choice(cap_alpha),end='')
            wrd += random.choice(cap_alpha)
        elif i >=1 and i <=4:
            #print(random.choice(alpha),end='')
            wrd += random.choice(alpha)
        elif i ==5:
            #print(random.choice(special_char),end='')
            wrd += random.choice(special_char)
        else:
            #print(random.choice(num),end='')
            wrd += random.choice(num)
    #print(wrd)
    return wrd

pass_len = int(input("enter lenght of password: "))
password = password_generator(pass_len)
print(password)




