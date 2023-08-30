x=[{'id': 28, 'name': 'Action'},
 {'id': 12, 'name': 'Adventure'},
 {'id': 14, 'name': 'Fantasy'},
 {'id': 878, 'name': 'Science Fiction'}]

def convert(List):
    L=[]
    for i in List:
        L.append(i['name'])
        
    return L

print(convert(x))