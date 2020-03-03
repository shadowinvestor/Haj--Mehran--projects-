competitors = input('Please enter the number of competitors: ')
competitors_info={}
for i in range(int(competitors)):
    a = input('Please enter the bib number and the name of the competitor'
                            + 'like "bib number, name": ')
    b=a.split(", ")

    competitors_info[b[0]]=[b[1]]
for key, value in competitors_info.items():
    value.append(input('Please enter the 3 records for the competitor with bib number ' 
                        + key + 'here. exp(12.4, 13,7, fall): '))
    value[-1]=value[-1].split(', ')
#print(competitors_info)
for key, value in competitors_info.items():
    lists=[]
    for i in range(len(value[-1])):    
        try:
            float(value[-1][i])
            lists.append(float(value[-1][i]))
        except ValueError:
            continue

    if len(lists)==0:
        value.append('No valid time')
    else:
        value.append(min(lists))
        
infos=[]
for key, value in competitors_info.items():
    infos.append([key])
    for i in value:
        infos[-1].append(i)
infos.sort(key=lambda x:x[3])
for i in infos:
    print(str(int(infos.index(i))+1)+", "+str((i[0]))+', '+i[1]+', '+str(i[3]))
