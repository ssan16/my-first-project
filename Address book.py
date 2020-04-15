import addressbook as addressbook

print('----My Adress Book----')


def displayuserinfo (userinfo):
    print('/t')
    print('til match found for', userinfo[0], '', userinfo[1],'!')
    print('/tFirst Name:', userinfo[0])
    print('/tLast Name:', userinfo[1])
    print('/tAddress:', userinfo[2])
    print('/tEmail:', userinfo[3])
    print('/tPhone Number:', userinfo[4])
    return


firstname = ''
lastname = ''
entryfound = ''

while firstname != 'q':
    firstname = input('Whats the first name:')

    if firstname == 'q':
        break
    else:
        lastname = input('Whats the last name:')

    addressbook = open(todo.txt)
    for line in addressbook:
        userinfo = line.split('|')
        if((userinfo[0] == firstname and userinfo[1] == lastname)):
            entryfound = True
            break
        else:
            entryfound = False
            continue

if entryfound == False:
    print('Invalid')
else:
    displayuserinfo(userinfo)
    addressbook.close()
    entryfound = ''




