# functions.py: function definitions for csw8 final project

def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    
    print(f"==========================")
    print(f"What would you like to do?")
    
    for key in menu:
        print(f'{key} - {menu[key]}')
    
    print(f"==========================")



def print_restaurant_menu(restaurant_menu, spicy_scale_map, name_only=False, show_idx=True, start_idx=0, vegetarian_only=False):
    """
    param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
    param: name_only (Boolean)
            If False, then only the name of the dish is printed.
            Otherwise, displays the formatted dish information.
    param: show_idx (Boolean)
            If False, then the index of the menu is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            dish name, where idx is the 0-based index in the list.
    param: start_idx (int)
            an expected starting value for idx that
            gets displayed for the first dish, if show_idx is True.
    param:  vegetarian_only (Boolean)
            If set to False, prints all dishes, regardless of their
            is_vegetarian status ("yes/no" field status).
             If set to True , display only the dishes with
            "is_vegetarian" status set to "yes".
    returns: None; only prints the restaurant menu
    """

    index = start_idx
    print("------------------------------------------")
    for dish in restaurant_menu:

        if name_only == False:
            if show_idx == True:
                if vegetarian_only == True:
                    if dish['is_vegetarian'] == 'yes':
                        print(f"{index}. {dish['name'].upper()}")
                        print(f"* Calories: {dish['calories']}")
                        print(f"* Price: {dish['price']}")
                        print(f"* Is it vegetarian: {dish['is_vegetarian']}")
                        print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
                        print()
                    else:
                        pass
                elif vegetarian_only == False:
                    print(f"{index}. {dish['name'].upper()}")
                    print(f"* Calories: {dish['calories']}")
                    print(f"* Price: {dish['price']}")
                    print(f"* Is it vegetarian: {dish['is_vegetarian']}")
                    print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
                    print()
            elif show_idx == False:
                if vegetarian_only == True:
                    if dish['is_vegetarian'] == 'yes':
                        print(f"{dish['name'].upper()}")
                        print(f"* Calories: {dish['calories']}")
                        print(f"* Price: {dish['price']}")
                        print(f"* Is it vegetarian: {dish['is_vegetarian']}")
                        print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
                        print()
                    else:
                        pass
                elif vegetarian_only == False:
                    print(f"{dish['name'].upper()}")
                    print(f"* Calories: {dish['calories']}")
                    print(f"* Price: {dish['price']}")
                    print(f"* Is it vegetarian: {dish['is_vegetarian']}")
                    print(f"* Spicy level: {spicy_scale_map[dish['spicy_level']]}")
                    print()


        elif name_only == True:
            if show_idx == True:
                if vegetarian_only == True:
                    if dish['is_vegetarian'] == "yes":
                        
                        print(f"{start_idx}. {dish['name'].upper()}")
                        
                    else:
                        pass

                elif vegetarian_only == False:
                    
                    print(f"{index}. {dish['name'].upper()}")
                    
            elif show_idx == False:
                if vegetarian_only == True:
                    if dish['is_vegetarian'] == 'yes':
                        print(dish['name'].upper())
                    else:
                        pass
                elif vegetarian_only == False:
                    print(dish['name'].upper())
        index += 1
    print("------------------------------------------")




def list_helper(list_menu, restaurant_menu_list, spicy_scale_map):
    """
    param: list_menu (list) - a list with menu options
    param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
    param: spicy_scale_map (dict) - a dictionary object that is expected
    Function is called when user input in main.py == 'U'
    """
    if len(restaurant_menu_list) == 0:
        print("WARNING: There is nothing to display!")
        # Pause before going back to the main menu
        input("::: Press Enter to continue")
    else:
        subopt = get_selection("List", list_menu)
        if subopt == 'A':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1)
        elif subopt == 'V':
            print_restaurant_menu(restaurant_menu_list, spicy_scale_map, show_idx=True, start_idx=1, vegetarian_only=True)

######## LIST OPTION ########

def get_selection(action, suboptions, to_upper=True, go_back=False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu
    The function displays a submenu for the user to choose from.
    Asks the user to select an option using the input() function.
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.
    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What field would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper()  # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection


def is_num(val):
    """
    The function checks if `val` is a string;
    returns False if `val` is not a string.
    Otherwise, returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise.
    """
    
    if type(val) == str:
        
        for i in val:
            if "0" <= i <= "9" or i == ".":
                return True
        
    elif type(val) != str:
        return False
    pass


def is_valid_name(name_str):
    """
    param: name_str (string) - a text that is supposed to
            contain between 3 and 25 characters (inclusive
            of both)
    returns:
        - True if it's a text of the valid length
        - False, otherwise
    """
    if type(name_str) == str:
        length = len(name_str)
        
        if 3 <= length <= 25:
            return True
        else:
            return False
    else:
        return False


def is_valid_spicy_level(spicy_level_str, spicy_scale_map):
    """
    param: spicy_level_str (string) - a string that is
            expected to contain the level of spiciness
    param: spicy_scale_map (dict) - a dictionary that
            contains the mapping between the integer
            priority value of spiciness to its representation
            (e.g., key 1 might map to the spiciness value
            "non spicy")
    returns:
        - True if spicy_level_str is a text containing
            an integer value that maps to a key in the
            priority_map
        - False, otherwise
    """
   
    if type(spicy_level_str) == str:
        for i in spicy_level_str:
            if "0" <= i <= "9":
                if int(i) in spicy_scale_map:
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False
        


def is_valid_is_vegetarian(vegetarian_str):
    """
    param: vegetarian_str (string) - a string that is
            expected to contain a text "yes" or "no"
    returns:
        - True if it's a text with the valid value
        - False, otherwise
    """

    if type(vegetarian_str) == str:
        
        if vegetarian_str == "yes" or vegetarian_str == "no":
            return True
        else:
            return False
        
        
    else:
        return False


def is_valid_price(price_str):
    """
    param: price_str (string) - a string that
            contains a decimal number to represent price
    returns:
        - True if it's a text containing decimal number
        - False, otherwise
    """
    
    if is_num(price_str):
       return True
        
    else:
        return False

    

def is_valid_calories(calories_str):
    """
    param: calories_str (str) - a string that is
            expected to represent calories
    returns:
        - True if it's a text containing integer value
        - False, otherwise
    """
    if type(calories_str) == str:
        
        if calories_str.isdigit():
            return True
        else:
            return False
        
    else:
        return False
    

def is_num_str_list(someList):
    
    if len(someList) == 0:
        return False
    
    for item in someList:
        
        if is_num(item) == True:
            continue
        elif is_num(item) == False:
            return False
    return True



def is_valid_index(idx, in_list, start_idx=0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that (idx - start_idx) is >= 0,
    which allows to retrieve an element from in_list.

    returns:
    - True, if idx is a numeric index >= start_idx
    that can retrieve an element from in_list.
    - False if idx is not a string that represents an
    integer value, if int(idx) is < start_idx,
    or if it exceeds the size of in_list.
    """

    if str(idx).isdigit():
        if int(idx) >= start_idx:
            index = int(idx) - start_idx
            if index in range(len(in_list)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    



def get_new_menu_dish(dish_list, spicy_scale_map):
    '''
    validate each element of the list starting from "name" and until "spicy_level"
    If one of them fails, return the name of parameter
    e.g., "name" if "name" is not 3-25 characters long
    or "is_vegetarian" if that field is not set to boolean,
    as well as the value that fails.
    If all validations pass, return the dictionary with the dish fields
    correctly set to the parameters.
    '''
    # [ "burrito", "500", "12.90", "yes", "2" ]
    
    
    
    finalDict = {}
    
    if len(dish_list) == 5:

        dishName = dish_list[0]
        dishCal = dish_list[1]
        dishPrice = dish_list[2]
        dishVeg = dish_list[3]
        dishSpice = dish_list[-1]
    
        nameRes = is_valid_name(dishName)
        calRes = is_valid_calories(dishCal)
        priceRes = is_valid_price(dishPrice)
        vegRes = is_valid_is_vegetarian(dishVeg)
        spiceRes = is_valid_spicy_level(dishSpice, spicy_scale_map)


        if nameRes:
            finalDict.update({"name": dishName})
            
            if calRes:   
                finalDict.update({"calories": int(dishCal)})
                
                if priceRes:
                    finalDict.update({"price": float(dishPrice)})
                    if vegRes:
                        finalDict.update({"is_vegetarian": dishVeg})
                        if spiceRes:
                            finalDict.update({"spicy_level": int(dishSpice)})
                                                
                            return finalDict
    
            
                        else:
                            return ("spicy_level", dishSpice)
                    else:
                        return ("is_vegetarian", dishVeg)
                else:
                    return ("price", dishPrice)
            else:
                return ("calories", dishCal)
        else:
            return ("name", dishName)
    else:
        return len(dish_list)
    

def print_dish(dish, spicy_scale_map, name_only=False):
    """
    param: dish (dict) - a dictionary object that is expected to contain the following keys:
            - "dish": dish's name
            - "calories": calories for this dish
            - "price": price of this dish
            - "is_vegetarian": boolean whether this dish is for vegetarian
            - "spicy_level": integer that represents the level of spiciness
    param: spicy_scale_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "level of spiciness."
            values for each corresponding key are string description of the
            level of spiciness
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the dish is printed.
            Otherwise, displays the formatted restaurant menues.
    returns: None; only prints the restaurant menu item
    """

    if name_only == False:
        print(f'{dish["name"].upper()}')
        print(f'* Calories: {dish["calories"]}')
        print(f'* Price: {dish["price"]}')
        print(f'* Is it vegetarian: {dish["is_vegetarian"]}')
        print(f'* Spicy level: {spicy_scale_map[dish["spicy_level"]]}')
        print()

    elif name_only == True:
        print(f'{dish["name"].upper()}')

    


def delete_helper(restaurant_menu_list, spicy_scale_map):
      """
      param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
      param: spicy_scale_map (dict) - a dictionary object that is expected
      Function is called when user input in main.py == 'D'
      """
      continue_action = 'y'
      while continue_action == 'y':
          if not restaurant_menu_list:
              print("WARNING: There is nothing to delete!")
              break
          print("Which dish would you like to delete?")
          print("Press A to delete the entire menu for this restaurant, M to cancel this operation")
          print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1)
          user_option = input("> ")
          if user_option == "A" or user_option == "a":
              print(f"::: WARNING! Are you sure you want to delete the entire menu ?")
              print("::: Type Yes to continue the deletion.")
              user_option = input("> ")
              if user_option == "Yes" or user_option == "yes" or user_option == "YES":
                  restaurant_menu_list = []
                  print(f"Deleted the entire menu.")
              else:
                  print(f"You entered '{user_option}' instead of Yes.")
                  print("Canceling the deletion of the entire menu.")
              break
          elif user_option == 'M' or user_option == 'm':
              break
          result = delete_dish(restaurant_menu_list, user_option, 1)
          if type(result) == dict:
              print("Success!")
              print(f"Deleted the dish |{result['name']}|")
          elif result == 0:  # delete_item() returned an error
              print("WARNING: There is nothing to delete.")
          elif result == -1:  # is_valid_index() returned False
              print(f"WARNING: |{user_option}| is an invalid dish number!")

          print("::: Would you like to delete another dish?", end=" ")
          continue_action = input("Enter 'y' to continue.\n> ")
          continue_action = continue_action.lower()
      return restaurant_menu_list




def update_helper(restaurant_menu_list, spicy_scale_map):
      """
      param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
      param: spicy_scale_map (dict) - a dictionary object that is expected
      Function is called when user input in main.py == 'D'
      """
      continue_action = 'y'
      while continue_action == 'y':
          if restaurant_menu_list == []: #TODO
              print("WARNING: There is nothing to update!")
              break
          print("::: Which dish would you like to update?")
          print_restaurant_menu(restaurant_menu_list, spicy_scale_map, name_only=True, show_idx=True, start_idx=1)
          print("::: Enter the number corresponding to the dish.")
          user_option = input("> ")
          if is_num(user_option): #TODO - check to see if the number is valid
              dish_idx = int(user_option) - 1
              subopt = get_selection("update", restaurant_menu_list[dish_idx], to_upper=False, go_back=True)
              if subopt == 'M' or subopt == 'm':  # if the user changed their mind
                  break
              print(f"::: Enter a new value for the field |{subopt}|") # TODO
              field_info = str(input("> "))
              result = update_menu_dish(restaurant_menu_list, dish_idx, spicy_scale_map, restaurant_menu_list[dish_idx], field_info) #TODO
              if type(result) == dict:
                  print(f"Successfully updated the field |{restaurant_menu_list[dish_idx]}|:") # TODO
                  print_dish(result, spicy_scale_map)  # TODO
              else:  # update_menu_dish() returned an error
                  print(f"WARNING: invalid information for the field |{restaurant_menu_list[dish_idx]}|!") # TODO
                  print(f"The menu was not updated.")
          else:  # is_valid_index() returned False
              print(f"WARNING: |{user_option}| is an invalid dish number!") # TODO

          print("::: Would you like to update another menu dish?", end=" ")
          continue_action = input("Enter 'y' to continue.\n> ")
          continue_action = continue_action.lower()
          # ---------------------------------------------------------------




def add_helper(restaurant_menu_list, spicy_scale_map):
      """
      param: restaurant_menu (list) - a list object that holds the dictionaries for each dish
      param: spicy_scale_map (dict) - a dictionary object that is expected
       to have the integer keys that correspond to the "level of spiciness."

      returns: None; only directs user to add a new dish to
        restuarant_menu_list
      """
      continue_action = 'y'
      while continue_action == 'y':
        print("::: Enter each required field, separated by commas.")
        # * `name` : name of the dish
        #     * `calories`: number of calories per serving
        #     * 'is_vegetarian' : if the item is vegetarian
        #     * `price` : price of the item
        #     * 'spicy_level' : 1 - 4
        print("::: name of the dish, calories, price, is it vegetarian ( yes | no ), spicy_level ( 1-4 )")
        dish_data = input("> ")  # TODO: get and process the data into a list
        dish_values = dish_data.split(",")
        result_dict = get_new_menu_dish(dish_values, spicy_scale_map)  # TODO: attempt to create a new dish for the menu
        if type(result_dict) == dict:
            restaurant_menu_list.append(result_dict)  # TODO: add a new dish to the list of dish menus
            print(f"Successfully added a new dish!")
            print_dish(result_dict, spicy_scale_map)
        elif type(result_dict) == int:
            print(f"WARNING: invalid number of fields!")
            print(f"You provided {result_dict}, instead of the expected 5.\n")
        else:
            print(f"WARNING: invalid dish field: {result_dict}\n")

        print("::: Would you like to add another dish?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()





def delete_dish(in_list, idx, start_idx=0):
    """
    param: in_list - a list from which to remove a dish
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of a dish in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing
    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from in_list.
    On success, the function saves the dish from in_list
    and returns it after it is deleted from in_list.
    returns:
    If the input list is empty, return 0.
    If idx is not of type string, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.
    Helper functions:
    - is_valid_index()
    """
    
    if len(in_list) == 0:
        return 0
    
    elif len(in_list) != 0 and type(idx) != str:
        return None
    
    elif len(in_list) != 0 and type(idx) == str and is_valid_index(idx, in_list) == False:
        return -1
    
    elif len(in_list) != 0 and type(idx) == str and is_valid_index(idx, in_list) == True: 
        if int(idx) >= int(start_idx):
            itemToDelete = in_list[int(idx) - start_idx]
            in_list.remove(itemToDelete)
        else:
            return -1
        return itemToDelete

    

def save_helper(restaurant_menu_list):
    """
    param: restaurant_menu (list) - a list object that holds the dictionaries for each dish 
    Function is called when user option == 'S'
    """
    continue_action = 'y'   
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = save_menu_to_csv(restaurant_menu_list, filename)  # TODO: Call the function with appropriate inputs and capture the output
        if result == -1:  # TODO
            print(f"WARNING: |{filename}| is an invalid file name!")  # TODO
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{filename}|")
            break




def save_menu_to_csv(restaurant_menu_list, filename):
    """
    param: restaurant_menu_list(list of dict) - The list shore dictionary of dishes 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the menu items. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every dishes dictionary in the dictionaries list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:
    * name
    * calories
    * price
    * is_vegetarian
    * spicy_level
    
    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    import os

    if filename[-4:] == ".csv":
        if os.path.exists(filename):
            with open(filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                
                stringList = []
                for items in restaurant_menu_list:
                    stringList.append(items)
                    
                csv_writer.writerow(stringList)

            return None
        
    else:
        return -1
    


def load_menu_from_csv(filename, restaurant_menu_list, spicy_scale_map):
    """
    param: filename (str) - the name of the file from which to read the contents.
    param: restaurant_menu_list (list) - A list of dish dictionary objects to which
            the dishes read from the provided filename are appended.
            If restaurant_menu_list is not empty, the existing menu items are not deleted.
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the spicy value "Not Spicy" or "Low")
            Needed by the helper function (see below).

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` (for csv.reader()) and `import os`
    (for `os.path.exists()).

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode.
    For each row in the csv file, the function will count each row (1-based counting) and
    proceed to create a new restaurant menu item using the `get_new_menu_dish()` function.
    - If the function `get_new_menu_dish()` returns a valid dish object (dictionary),
    it gets appended to the end of the `in_list`.
    - If the `get_new_menu_dish()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid dish data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_list` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_list and their indices are appended to the new list that's returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read into the `in_list`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_menu_dish().

    Helper functions:
    - get_new_menu_dish()
    """

    import csv
    import os

    in_list = []
    
    
    if filename[-4:] == ".csv":
        if os.path.exists(filename):
            
            with open(filename) as file_name:
                file_reader = csv.reader(file_name)
                    
                counter = 0
                for item in file_reader:
                    counter += 1
                        
                    if type(get_new_menu_dish(item, spicy_scale_map)) == dict: 
                        restaurant_menu_list.append(get_new_menu_dish(item, spicy_scale_map))
                            
                            
                    else:
                        in_list.append(counter)
    
                return in_list  
        else:
            return None     
    else:
        return -1

        
    

def load_helper(restaurant_menu_list, spicy_scale_map):
    """
    def save_helper(restaurant_menu_list):
    continue_action = 'y'   
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = save_menu_to_csv(restaurant_menu_list, filename)  # TODO: Call the function with appropriate inputs and capture the output
        if result == -1:  # TODO
            print(f"WARNING: |{filename}| is an invalid file name!")  # TODO
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully saved restaurant menu to |{filename}|")
            break
    """
    continue_action = 'y'
    while continue_action == 'y':
        print("::: Enter the filename ending with '.csv'.")
        filename = input("> ")
        result = load_menu_from_csv(filename, restaurant_menu_list, spicy_scale_map)
        if result == -1:  # TODO
            print(f"WARNING: |{filename}| is an invalid file name!")  # TODO
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")
        else:
            print(f"Successfully restored restaurant menu to |{filename}|")
            break




def update_menu_dish(restaurant_menu_list, idx, spicy_scale_map, field_key, field_info, start_idx=0):
    """
    param: restaurant_menu_list (list) - a menu that contains
            a list of dishes
    param: idx (str) - a string that is expected to contain an integer
            index of a restaurant in the input list
    param: spicy_scale_map (dict) - a dictionary that contains the mapping
            between the integer spiciness value (key) to its representation
            (e.g., key 1 might map to the priority value "non spicy")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing
    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.
    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.
    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
     Depending on the field_key, it also calls:
-    - is_valid_name()
-    - is_valid_calories()
-    - is_valid_price()
-    - is_valid_is_vegetarian()
-    - is_valid_spicy_level()
    """
    if type(idx) == str:

        if len(restaurant_menu_list) > 0:
            index = int(idx) - start_idx
            if is_valid_index(index, restaurant_menu_list):
                
                if field_key in restaurant_menu_list[index]:

                    if field_key == 'name':
                        if is_valid_name(field_info):
                            restaurant_menu_list[index].update({'name': field_info.strip()})
                        else:
                            return field_key
                        
                    elif field_key == 'calories':
                        if is_valid_calories(field_info):
                            restaurant_menu_list[index].update({'calories': int(field_info)})
                        else:
                            return field_key
                        
                    elif field_key == 'price':
                        if is_valid_price(field_info):
                            restaurant_menu_list[index].update({'price': float(field_info)})
                        else:
                            return field_key
                    
                    elif field_key == 'is_vegetarian':
                        if is_valid_is_vegetarian(field_info):
                            restaurant_menu_list[index].update({'is_vegetarian': (field_info.strip()).lower()})
                        else:
                            return field_key
                        
                    elif field_key == 'spicy_level':
                        if is_valid_spicy_level(field_info, spicy_scale_map) and int(field_info) <= 4:
                            restaurant_menu_list[index].update({'spicy_level': int(field_info)})
                        else:
                            return field_key
                    

                    return restaurant_menu_list[index]
                else:
                    return -2
            else:
                return -1
        else:
            return 0

    elif type(idx) == int:
        return -1
    
    



def get_restaurant_expense_rating(restaurant_menu_list):
    """
    param: restaurant_menu_list - a list of restaurants and their dishes (list of dicts)
    
    Computes the average price of all the items on the menu and display the expense rating of the restaurant.
    average_price < 10 -> Expense rating is : $
    10 <= average_price < 20 -> Expense rating is : $$
    average_price >= 20: Expense rating is : $$$
    
    returns: the average price of the items as a float
    """
    num_of_dishes = len(restaurant_menu_list)
    total_amount = 0

    for dishes in restaurant_menu_list:
        total_amount += dishes['price']

    average_price = total_amount/num_of_dishes

    if average_price < 10.0:
        print('Expense rating is : $')
        print()
    elif average_price >= 10.0 and average_price < 20.0:
        print('Expense rating is : $$')
        print()
    elif average_price >= 20.0:
        print('Expense rating is : $$$')
        print()
    
    

    return float(average_price)
        
    
    
