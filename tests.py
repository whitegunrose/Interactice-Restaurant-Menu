from functions import *

assert is_valid_name("a") == False
assert is_valid_name("bo") == False
assert is_valid_name(42) == False
assert is_valid_name(["soup"]) == False
assert is_valid_name("soup") == True
assert is_valid_name("brandon") == True
assert is_valid_name("ORYX") == True

assert delete_dish(['kratos', 'atreus', 'brok'], '1', 3) == -1
assert delete_dish(['december', '25', '2003'], '1', 1) == 'december'
assert delete_dish([], '9', 1) == 0
assert delete_dish(['1'], 0, 0) == None

assert is_num('4') == True
assert is_num(4) == False
assert is_num('56789087654356786543234567897654356789') == True
assert is_num(8765456789097654345678) == False

assert is_valid_spicy_level('3', {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == True
assert is_valid_spicy_level('5', {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == False
assert is_valid_spicy_level(1, {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == False
assert is_valid_spicy_level('1', {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == True

assert is_valid_is_vegetarian('yes') == True
assert is_valid_is_vegetarian('no') == True
assert is_valid_is_vegetarian('i love computer science') == False # This is wrong I love computer science!!!!!
assert is_valid_is_vegetarian('Wait, but I really do!!!') == False # Don't let this code fool you

assert is_valid_price('4.5') == True
assert is_valid_price('9') == True
assert is_valid_price('10.0') == True
assert is_valid_price('Nooooo!!!!') == False
assert is_valid_price("They can't silence my love for computer science any longer!!!") == False # BUT IT'S TRUE

assert is_valid_calories("I'm back!!!") == False # But I really am back
assert is_valid_calories('450') == True
assert is_valid_calories('456789876543456') == True
assert is_valid_calories('I guess this is goodbye...') == False

assert is_num_str_list([4, 1, 3, 456789456]) == False
assert is_num_str_list(['1', '4', '70', '903']) == True
assert is_num_str_list([43, '23', 81]) == False
assert is_num_str_list([129042]) == False

assert is_valid_index('1.5', [1, 2, 3, 4]) == False
assert is_valid_index('4', [0]) == False
assert is_valid_index('2', ['I', 'Love', 'Computer', 'Science'], 1) == True
assert is_valid_index('6', ['GUESS', "WHO'S", 'BACK', 'BACK', 'AGAIN', "SHADY'S BACK", 'TELL A FRIEND'], 3) == True

assert delete_dish([], '4') == 0
assert delete_dish(['hello', 'there'], 2) == None
assert delete_dish(['whats', 'your', 'name', '?'], '-2') == -1
assert delete_dish(['no need to be...', 'afraid....', ':)'], '4', 1) == -1

assert save_menu_to_csv([{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], 'wrong') == -1
assert save_menu_to_csv([{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], 'hello there') == -1
assert save_menu_to_csv([{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], 'file.json') == -1
assert not save_menu_to_csv([{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], 'file.csv') == -1

assert not load_menu_from_csv('basketball.csv', [{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == -1
assert load_menu_from_csv('calculus', [{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == -1
assert load_menu_from_csv('what are you on about', [{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == -1
assert not load_menu_from_csv('iosdeveloper.csv', [{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == -1

assert get_new_menu_dish(['quesadilla', 200, 4.50, 'no'], {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == 4
assert get_new_menu_dish(['taco', 1000, 10.50], {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == 3
assert get_new_menu_dish(['pupusas', 450, 5.50, 'no', 2, 'pork'], {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == 6
assert get_new_menu_dish(['Thank you prof k', 'for your efforts', 'in teaching us python'], {1: "Not spicy", 2: "Low key spicy", 3: "Hot", 4: "Diabolical",}) == 3

assert update_menu_dish([], '1', {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}, 'price', '0') == 0
assert update_menu_dish([{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], '10', {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}, 'name', '1') == -1
assert update_menu_dish([{"name": "quesadilla", "calories": 800, "price": 7.90, "is_vegetarian": "yes", "spicy_level": 1}], 1, {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}, 'price', '0') == -1
assert update_menu_dish([], 2345, {'wrong': 'spicy'}, 'home owner', '345') == -1 

