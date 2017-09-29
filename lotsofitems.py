from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///itemcatalog_final_withusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Pushpak Teja", email="mpushpakteja@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#  for UrbanBurger
category1 = Category(user_id=1, name="Food")

session.add(category1)
session.commit()

Item2 = Item(user_id=1, title="Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     category=category1)

session.add(Item2)
session.commit()


Item1 = Item(user_id=1, title="French Fries", description="with garlic and parmesan",
                      category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, title="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, title="Chocolate Cake", description="fresh baked and served with ice cream",
                     category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, title="Sirloin Burger", description="Made with grade A beef",
                    category=category1)

session.add(Item4)
session.commit()

Item5 = Item(user_id=1, title="Root Beer", description="16oz of refreshing goodness",
                     category=category1)

session.add(Item5)
session.commit()

Item6 = Item(user_id=1, title="Iced Tea", description="with Lemon",
                     category=category1)

session.add(Item6)
session.commit()

Item7 = Item(user_id=1, title="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
                     category=category1)

session.add(Item7)
session.commit()

Item8 = Item(user_id=1, title="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     category=category1)

session.add(Item8)
session.commit()


#  for Super Stir Fry
category2 = Category(user_id=1, name="Sports")

session.add(category2)
session.commit()


Item1 = Item(user_id=1, title="Cricket", description="Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book",
                     category=category2)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, 
    title="Badminton", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook",category=category2)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, title="Hockey", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                    category=category2)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, title="Baseball", description="Steamed dumplings made with vegetables, spices and meat. ",
                    category=category2)

session.add(Item4)
session.commit()

Item5 = Item(user_id=1, title="Tennis", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                    category=category2)

session.add(Item5)
session.commit()

Item6 = Item(user_id=1, title="Rugby", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                      category=category2)

session.add(Item6)
session.commit()


#  for Panda Garden
category1 = Category(user_id=1, name="Profession")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, title="Doctor", description="a Viettitlese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, title="Engineer", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, title="Lawyer", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
                     category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, title="Teacher", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                    category=category1)

session.add(Item4)
session.commit()

Item2 = Item(user_id=1, title="Chef", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     category=category1)

session.add(Item2)
session.commit()


#  for Thyme for that
category1 = Category(user_id=1, name="Books")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, title="Fiction", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                    category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, title="Sci-fi", description="Portabello mushrooms in a creamy risotto",
                  category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, title="Romance", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                   category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, title="Short stories", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     category=category1)

session.add(Item4)
session.commit()

Item5 = Item(user_id=1, title="Horror", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                    category=category1)

session.add(Item5)
session.commit()

Item2 = Item(user_id=1, title="Thriller", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                    category=category1)

session.add(Item2)
session.commit()


#  for Tony's Bistro
category1 = Category(user_id=1, name="Numbers")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, title="Rational", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, title="Whole", description="Chicken... and rice",
                    category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, title="Complex", description="Spaghetti with some incredible tomato sauce made by mom",
                     category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, title="Irrational",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", category=category1)

session.add(Item4)
session.commit()

Item5 = Item(user_id=1, title="Real", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
              category=category1)

session.add(Item5)
session.commit()


#  for Andala's
category1 = Category(user_id=1, name="Parts of Speech")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, title="Noun", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                    category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, title="Pronoun", description="Chicken cooked in Marsala wine sauce with mushrooms",
                    category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, title="Verb", description="Delicious chicken and veggies encapsulated in fried dough.",
                    category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, title="Adverb", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                    category=category1)

session.add(Item4)
session.commit()

Item2 = Item(user_id=1, title="Adjective", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                      category=category1)

session.add(Item2)
session.commit()


#  for Auntie Ann's
category1 = Category(user_id=1, name="Fashion")

session.add(category1)
session.commit()

Item9 = Item(user_id=1, title="Shirts", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                    category=category1)

session.add(Item9)
session.commit()


Item1 = Item(user_id=1, title="Trousers", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, title="Wallets", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                 category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, title="Shoes", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                     category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, title="Glasses", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     category=category1)

session.add(Item4)
session.commit()

Item2 = Item(user_id=1, title="Tee shirts", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     category=category1)

session.add(Item2)
session.commit()

Item10 = Item(user_id=1, title="Jeans", description="vanilla ice cream made with organic spinach leaves",
                      category=category1)

session.add(Item10)
session.commit()


#  for Cocina Y Amor
category1 = Category(user_id=1, name="Gadgets")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, title="Computers", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                   category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, title="Mobile Phones", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                    category=category1)

session.add(Item2)
session.commit()


category1 = Category(user_id=1, name="Tablets")
session.add(category1)
session.commit()

Item1 = Item(user_id=1, title="Speakers", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                      category=category1)

session.add(Item1)
session.commit()

Item1 = Item(user_id=1, title="Ebook Readers", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                    category=category1)

session.add(Item1)
session.commit()


Item1 = Item(user_id=1, title="AI assistants", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                     category=category1)

session.add(Item1)
session.commit()


print "added  items!"
