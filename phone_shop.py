
available_items = {
"Google Pixel 6a": {
"price": 280,
"quantity": 5
},
"SAMSUNG Galaxy S23 Ultra": {
"price": 1200,
"quantity": 3
},
"iPhone 13 Pro Max": {
"price": 1300,
"quantity": 2
},
"Xiaomi Redmi 9A": {
"price": 100,
"quantity": 4
},
"Huawei P50 Pro": {
"price": 1000,
"quantity": 1
},
"OnePlus 9 Pro": {
"price": 800,
"quantity": 1
},
}
cart={}
print('welcome in my store')
meas= '''
what do you want
1-view available item
2-view cart
3- clear cart
4-out
'''
total=[]
while True:
    print(meas)
    user_choice= int(input('enter the number: '))
    if user_choice==4:
        print('out')
        break
    elif user_choice==1:
        for i, item in enumerate(available_items):
         print(f'{i+1}-{item}:',available_items[item]['price'])
        item=(int(input('enter number item do you want(0 to return): ')))
        item_quantity= int(input('enter the quantity number: '))
        if item==0:
         continue
        order_name= list(available_items.keys())[item-1]
        
        cart.update({order_name:{'price':available_items[order_name]['price'],'quantity':item_quantity}})
        if available_items[order_name]['quantity']< cart[order_name]['quantity']:
          print('sorry we just have',available_items[order_name]['quantity'],'only')
          cart[order_name]['quantity']=available_items[order_name]['quantity']
          print("we add all quantity for this item in your cart")
          continue
       
      
        print(order_name,'has been add')
        
    elif user_choice==2:
        if cart=={}:
            print('no item have been bought')
            continue
        else:
            print('cart:')
            print('-'*20)
            for item in cart:
                print(item,':$',cart[item]['price'],'x ',cart[item]['quantity'],'=',cart[item]['price']*cart[item]['quantity'])
                total.append(cart[item]['price']*cart[item]['quantity'])
            print('-'*20)
            print('total cart is: ',sum(total))
    elif user_choice==3:
        print('what item do you want clear:')
        for i, item in enumerate(cart):
             print(f'{i+1}-{item}:',cart[item]['price'])
        print('-1-cart')
        item=(int(input('enter number item do you want(0 to return): ')))
      
        if item==0:
         continue
        order_name= list(available_items.keys())[item-1]
        if item==-1:
            cart =={}
            print('cart has BEEN DELETED')
        else:
            del cart[order_name]
            print('item has BEEN DELETED')
            
            
            
    

        
    


    
    