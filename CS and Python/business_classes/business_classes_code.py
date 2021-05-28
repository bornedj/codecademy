class Menu:
  #init
  def __init__(self, name, items, start_time, end_time):
      self.name = name
      self.items = items
      self.start_time = start_time
      self.end_time = end_time

  def __repr__(self):
    return f'{self.name}: available from {self.start_time} till {self.end_time}.'

  # calculate bill
  def calculate_bill(self, purchased_items):
    purchase_total = 0
    for item in purchased_items:
      purchase_total += self.items.get(item) # retreives the price from items list and adds on to total
    return purchase_total

#items
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

dinner_items = {  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

#inits
brunch = Menu('Brunch', brunch_items, 11, 16)
early_bird = Menu('early bird'.title(), early_bird_items, 15, 19)
dinner = Menu('Dinner', dinner_items, 17, 23)
kids = Menu('Kids', kids_items, 11, 21)

#testing the calculate bill method
brunch_price = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print(brunch_price)

#testing early-bird
early_bird_price = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print(early_bird_price)

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  #available menus
  def available_menus(self, time):
    menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menu_list.append(menu)
    return menu_list

#init franchises
flag_ship = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 east mulberry street".title(), [brunch, early_bird, dinner, kids])

#test of available menus
print(flag_ship.available_menus(12))
print(flag_ship.available_menus(17))

#--------------------------------------------------------

class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#init business 
basta = Business("Basta Fazoolin' with my Heart", [flag_ship, new_installment])

#menu items
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
#new menu
arepas_menu = Menu("arepas", arepas_items, 10, 20)

#arepas franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#new business
arepa = Business("Take a' Arepa", [arepas_place])

