a=input('File to initialize the vending machine:\n')  # Initialize the vending machine from the input file
fin=open(a,"r")
list1=[]
list2=[]
dict1=dict()
for i in fin:
    list1.append(i.strip())
tick=int(list1[0])
list1.pop(0)
for num in list1:
    list2.append(num.split())
for num in range(0,len(list2)):
    dict1[list2[num][0]]=int(list2[num][1])
dest=1
while dest!='Exit':
    if tick==0:
        end=input("Out of Service. Please enter 'Exit':\n")
        dest='Exit'
    else:
         # Display available stations
        a='Station(s): '
        for key, value in dict1.items():
            a=a+key+', '
        a=a[:-2]
        a=a+'.'
        print(a)
        dest=input("Please choose a destination or enter 'Exit':\n")
        if dest in dict1.keys():
            ticknum=input('Please enter the number of tickets:\n')  
            if int(ticknum)>tick:
                print('Error: Cannot handle your request.\n')
            else:
                tick=tick-int(ticknum)
                list3=[]
                sum1=0
                price=int(ticknum)*dict1[dest]
                flag=1
                while flag==1:
                    if sum1>=price:
                        print(f'Destination: {dest}, Quantity: {ticknum}, Price: ${price}, Inserted: ${sum1}.')
                        print(f'Dropped ticket(s). Your change: ${sum1-price}.')
                        flag=0
                        break
                    else:
                        print(f'Destination: {dest}, Quantity: {ticknum}, Price: ${price}, Inserted: ${sum1}.')
                    cn=input("Please insert a coin or enter 'Cancel':\n")
                    if cn=='Cancel':
                        final='Cancelled. '
                        list3.sort()
                        final1=''
                        if len(list3)==0:
                            print(final+'Returned no coin.')
                            flag=0
                        else:
                            for num in list3:
                                final1=final1+' '+'$'+str(num)+','
                            final1=final1[:-1]
                            final1=final1+'.'
                            final=final+'Returned coin(s):'+final1
                            print(final)
                            flag=0
                    else:
                        list3.append(int(cn))
                        sum1=sum1+list3[-1]

print('Bye')
