from functions import *

if __name__ == "__main__":

    the_menu = {
        "L" : "List",
        "A" : "Add",
        "U" : "Update",
        "D" : "Delete",
        "H" : "Display restaurant expense rating",
        "S" : "Save the data to file",
        "R" : "Restore data from file",
        "Q" : "Quit this program"
    }


    restaurant_menu_list = [
  {
    "name": "quesadilla",
    "calories": 800,
    "price": 7.90,
    "is_vegetarian": "yes",
    "spicy_level": 1
  },
  {
    "name": "burrito bowl",
    "calories": 800,
    "price": 9.90,
    "is_vegetarian": "no",
    "spicy_level": 1
  },
  {
    "name": "margherita",
    "calories": 800,
    "price": 18.90,
    "is_vegetarian": "no",
    "spicy_level": 2
  },
  {
    "name": "pasta",
    "calories": 600,
    "price": 15.90,
    "is_vegetarian": "yes",
    "spicy_level": 1
  }
]


    list_menu = {
        "A": "complete menu",
        "V": "vegetarian dishes only",
    }

    spicy_scale_map = {
        1: "Not spicy",
        2: "Low key spicy",
        3: "Hot",
        4: "Diabolical",
    }


    option = None

    while True:
        print_main_menu(the_menu)

        print("::: Enter an option")
        option = input("> ")
        option = option.upper()
        
        if option == "Q":
            print("Goodbye!\n")
            break
        
        elif option == 'L':
          list_helper(list_menu, restaurant_menu_list, spicy_scale_map)

        elif option == 'A':
          add_helper(restaurant_menu_list, spicy_scale_map)

        elif option == 'D':
          restaurant_menu_list = delete_helper(restaurant_menu_list, spicy_scale_map)

        elif option == 'S':
          save_helper(restaurant_menu_list)

        elif option == 'R':
            load_helper(restaurant_menu_list, spicy_scale_map)

        elif option == 'U':
          update_helper(restaurant_menu_list, spicy_scale_map)

        elif option == 'H':
          get_restaurant_expense_rating(restaurant_menu_list)

        else: 
            if option in the_menu:
                print(f"You selected option {option} to > {the_menu[option]}.")

            else:
                print(f"WARNING: {option} is an invalid option.\n")

                

print("Have a delicious day!")