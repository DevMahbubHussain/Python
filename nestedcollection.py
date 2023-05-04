supermarket = {
    'store1':{
        'name':'Mahbub general store',
        'items':[
            {'name':'Shop','quantity':100},
            {'name': 'brush', 'quantity': 200},
            {'name': 'pen', 'quantity': 300}
        ]
    },

    'store2': {
        'name': 'Mamun general store',
        'items': [
            {'name': 'python', 'quantity': 100},
            {'name': 'django', 'quantity': 200},
            {'name': 'Java', 'quantity': 300}
        ]
    },

}

for d in supermarket['store2']['items']:
    if d['name'] == 'django':
        print(d['quantity'])

print(supermarket['store1']['name'])
print(supermarket.get('store2').get('name','store name'))