''' Prog 1
std_fnm = input("Enter Student fname\n")
std_lnm = input("Enter Student lname\n")
f_nm = std_fnm+std_lnm
#print(f_nm.upper())
lst=[]
sub1 = int(input("Enter Subject 1 Marks\n"))
sub2 = int(input("Enter Subject 2 Marks\n"))
sub3 = int(input("Enter Subject 3 Marks\n"))
marks = sub1+sub2+sub3
lst.append(f_nm.upper())
lst.append(marks)
print("Student Details: ",lst) '''
'''  New  Prog
num_per=int(input('Enter number of persons\n'))
final_res=[]
for i in range(num_per):
    fnm = input('Enter Person First Name\n')
    lnm=input('Enter Person last Name\n')
    loc=input('Enter Person location\n')
    lang=int(input('Enter number of languages knows\n'))
    res=[]
    res.append(fnm.upper()+lnm.upper())
    res.append(loc.lower())

    res2=[]
    for i in range(lang):
        i=input('Enter Language\n')
        res2.append(i)
    res.append(res2)
    final_res.append(res)
print('All Persons Details: ',final_res)  '''


'''  New Prog
item_details={'Mobile':20000,'Laptop':50000,'Monitor':10000}
itm=input('Enter Item Name\n')
qty=int(input('Enter Item Quantity\n'))
price = item_details[itm]
total = qty*price
print('Purchase Details:')
print('Item Name ',itm)
print('Quantity ',qty)
print('Price ',price)
print('Total ',total)  '''

''' New Prog
print('Welcome to Flipkart Registration')
fnm=input('Enter First Name\n')
lnm=input('Eneter Last Name\n')
loc=input('Enter Location\n')
pin=input('Enter Pincode\n')

details={}
details['FIRST NAME'] = fnm
details['LAST NAME'] =lnm
details['LOCATION']=loc
details['PINCODE']=pin
print('REGISTRATION DETAILS: ',details) '''

''' n=0
for i in range(5, 20,2):
    i = n+i
    print(i) '''

'''for i in range(5, 20,2):
    i = i+1
    print(i) '''

''' for i in range(0,100):
    i = 1+i
    if i%4 == 0:
        print(i) '''
''' for i in range(0,100):
    i = 1+i
    if i%2 == 1:
        print(i) '''

''' for rama in range (10,0,-1):
    print (rama) '''

''' n=0
lst=[10,20,30,40,50]
for i in list(lst):
    n=n+i
print(n) '''

''' lst1=[]
lst2=['rama','krishna','reddy']
for i in (lst2):
    lst1.append(i.upper())
print(lst1) '''

'''for i in range(100,200):
    if i%7==0:
        print(i) '''

'''  word=input('Please enter a word: ')
revstrng=''
for i in range(len(word)-1,-1,-1):
    revstrng +=word[i]
    print(i)
print(revstrng)
#print(word[::-1])  '''
'''
num=[1,2,3,4,5,6,7,8,9,10,11,12,13]
even=0
odd=0
for i in num:
    if not i%5:
        even +=1
    else:
        odd +=1
print('Odd numbers: ',odd)
print('even number: ',even) '''

'''
movies={
    'robo':25,
    'saho':20,
    'bahubali':5,
    'pawan':2
}
movnm=input('Enter movie name\n')
tckts= int(input('Enter number of tickets\n'))

if movnm not in (movies.keys()):
    print('Movie is not available now')
elif movnm in (movies.keys()) and tckts <= movies[movnm]:
    print('Tickets Available')
else:
    print('Tickets unavailable')  '''