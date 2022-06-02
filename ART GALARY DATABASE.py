listofrecord=[]
# code for taking input
def input_record():
    while True:
        name=input('Art name ')
        Aname=input('Artist name ')
        year=input('Year of making ')
        title=input('Unique title ')
        price=int(input('Price '))
        code=int(input('Art code '))
        #making list
        listofrecord.append([name,Aname,year,title,price,code])
        #giving option to user for further addition on the list
        choice=input('enter c to continue or any alphabet to exit')
        if choice!='c' and choice!='C':
            break
# code for displaying record
def display_record():
    serial=1
    for i in listofrecord:
        print('Art No ',serial)
        print('Art name ',i[0])
        print('Artist name ',i[1])
        print('Year of making ',i[2])
        print('Unique Title ',i[3])
        print('Price ',i[4])
        print('ART 2 DIGIT CODE ',i[5])
        #calculation for dicount
        if i[4]>60000:
            print()
            print('AFTER 30% OFF PRICE ',i[4]*30/100)
            print()
        print()
        serial+=1
# code for saving record
def save_record():
    f=open('artgalarydatabase.txt','w')# use write to creat a file
    for i in listofrecord:
        f.write(i[0]+', ')
        f.write(i[1]+', ')
        f.write(i[2]+', ')
        f.write(i[3]+', ')
        f.write(str(i[4])+', ')
        f.write(str(i[5])+'\n')
    f.close()
#code for loading record
def load_record():
    f=open('artgalarydatabase.txt','r')
    for i in f:
        i=i.split(',')
        print(i)
    f.close()
# soecial feature of geeting type of art
def typeofart():
    a=int(input('your art unique 2 digit unique code '))
    if 10<=a<=35:
        print(' art type is ABSTRACT Art')
    elif 36<=a<=90:
        print(' art type if GEOMETRIC Art')
    elif 91<=a==99:
        print(' art type is surrealism')
#making dictionary of options
option={1:input_record,2:display_record,3:save_record,4:load_record,6:exit,5:typeofart}
#printing menu
print('''\t ART  GALARY  DATABASE

Welcome to my art galary Database .Here you can enter your art details.following are some options you can select:

1: For input record
2: For displaying record
3: For saving record
4: For loading record
5: For getting type of art
6: for exiting database

We offer 30% off on paintings worth above 60,000.....:-))
''')
#using else if structure and get function to display options and run  database
while True:
    choice=int(input('WHAT YOU WANT TO PERFORM '))
    if choice==6:
        break
    elif choice>=6:
            print('kindly select from given option')
    else:
        option.get(choice)()

