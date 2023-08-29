'''Details = ['101,rama,hyd,asdf1',
'102,krishna,london,asdf2',
'103,reddy,barking,asdf3'
]
for i in Details:
    val = i.split(',')
    print(val[0:4])
    v2= '#'.join(val)
    print(v2) '''
'''
fn= input('Enter First Name\n')
ln= input('Enter Last Name\n')
gen=input('Enter your gender\n')
mob=input('Enter your 10 digits mobile number\n')
langnum = int(input('Enter number of languages known\n'))
lang=[]
for i in range (langnum):
    lan=input('Enter language\n')
    lang.append(lan.upper())
if fn.isalpha()==True and  ln.isalpha()==True:
    print('Name :',fn.title()+ln.title())
else: print('Please enter correct name')

if gen.upper() == 'MALE':
    print('Gender :', 'M')
elif gen.upper() == 'FEMALE':
    print('Gender :', 'F')
else: print('Please enter correct Gender')

if len(mob)==10 and mob.isnumeric()==True:
    print('Mobile number: ',mob)
print('Languages: ',lang) '''
'''
str='book'
res = {}
for i in str:
    print(res.get(i))    '''
'''
frt_dtls={
        'B1':['apple','banana','cherry'],
        'B2':['apple','mango','pineapple'],
        'B3':['mango','cherry','banana']
}
#print(frt_dtls.values())
frt_lst=[ i for frt in frt_dtls.values() for i in frt]
friuts_uniq= sorted(list(set(frt_lst)))
print(friuts_uniq)

for i in friuts_uniq:
    lst=[]
    for k,v in frt_dtls.items():
        if i in v:
            lst.append(k)
    print(i,lst)'''
'''
def add(a,b):
    print("sum is: ",a+b)
add(10,20)'''
'''
f=open('student.txt','a')
noofstudents = int(input('Enter number of students\n'))
for i in range(noofstudents):
    stud_nm=input('Enter student name\n')
    schl_nm=input('Enter scholl name\n')
    loc=input('Enter location\n')
    f.write(stud_nm+"#"+schl_nm+"#"+loc+'\n')
f.close()'''







