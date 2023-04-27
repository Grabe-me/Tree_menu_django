
def parametrs(num):
    params = ''.join([f'<param{i}>/' for i in range(1,num+1)])
    print(params)

# parametrs(5)

address_list = ['1', '2', '3', '2']
if len(address_list) and address_list[-1] in address_list[:-1]:
    address = address_list.index(address_list[-1])
    address_list = address_list[:address+1]
    address = address_list[-1]
    print(address_list)
else:
    print(address_list)