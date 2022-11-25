def example_function(name):
    print("Hello " + name)


example_function("PuffoGino")

def my_cats(**cats):
  print("The name of my second cat is " + cats["second"])

my_cats(first = "PuffoGino", second = "Nino")

def my_cats(cats):
  for cat in cats:
    print(cat)

cats = ["PuffoGino", "Nino", "Gingerino"]

my_cats(cats)

def my_cats_food(food = "Crocchini"):
  print("My cats eat " + food)

my_cats_food("Hamburger")
my_cats_food("Polpette")
my_cats_food()
my_cats_food("Bustina")