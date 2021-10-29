pizzas = ['Neapolitan Pizza','Chicago Pizza','Greek Pizza']
friends_pizza = pizzas[:]
pizzas.append('indian pizza')
friends_pizza.append('chines pizza')    
print(f'my fav pizzas\n')
for piz in pizzas:
    print(piz)
print(f'my frends fav pizza are \n')
for piz in friends_pizza:
    print(piz)

