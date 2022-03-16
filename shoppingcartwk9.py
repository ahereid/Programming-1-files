def main_menu(): 
    while True:
        print()
        print('Welcome to the Shopping Cart Program!')
        print()
        print(' Please select one of the following:')
        print()
        print('''
        1: Add Item
        2: View Cart
        3: Remove Item
        4: Compute Total
        5: Quit''')
        selection = input('Please make a selection:')
        if selection == '1':
            additem()
        elif selection == '2':
            displaycart()
        elif selection == '3':
            removeitem() 
        elif selection == '4':
            pass 
        elif selection == '5':
            quit()
        else:
            print('You did not make a valid selection.')

shopping_list = [] 
price = []  

item = None 
total = 0  

def additem():
    item = input('What would you like to add to your cart?')
    cost = float(input('What is the price of the item?'))
    shopping_list.append(item)
    price.append (cost)
    for (x,y) in zip(shopping_list, price):
        print(f'This item {x}: ${y:.2f} has been added to your cart.')
     
    
def displaycart():
    print('---Shopping Cart---')
    for (x,y) in zip(shopping_list, price):
        print(f'{x} : ${y:.2f}')
        


def removeitem():
    item = input('What would you like to remove from the cart?')
    cost = float(input('What is the price of the item you wish to remove?'))
    shopping_list.remove(item)
    price.remove(cost)
    for (x,y) in zip ( shopping_list, price):
        print(f' This item {x}: {y:.2f} has been removed from your cart.')

def compute_total():
    print(sum(price))

main_menu()