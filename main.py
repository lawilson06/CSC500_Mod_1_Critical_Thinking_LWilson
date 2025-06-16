from user_numbers import UserNumbers

user_calculated_objects = []
counter = 0
user_choice = 0

def user_selection():
    global counter
    while True:
        print('1. Calculate values.')
        print('2. Display values.')
        print('3. Exit program.\n')
        try:
            user_choice_local = int(input('Enter your selection: '))
        except ValueError:
            counter += 1
            print(f'Must enter a valid choice from the menu.')
            if counter >= 3:
                break
            continue
        if user_choice_local in (1,2,3):
            counter = 0
            return user_choice_local
        else:
            counter += 1
            print(f'Must enter a valid choice from the menu.')
            if counter >= 3:
                break
    user_choice_local = 3
    return user_choice_local

def display_values(calculated_list):
    for index,item in enumerate(calculated_list):
        user_num1, user_num2, user_addition, user_subtraction, user_multiplication, user_division = (
            item.get_values())
        print(f"{index+1} - First value: {user_num1} | Second value: {user_num2} | Addition: {user_addition} | "
              f"Subtraction: {user_subtraction} | Multiplication: {user_multiplication} | Division: {user_division}")
    print('')

while counter < 4:
    user_choice = user_selection()
    match user_choice:
        case 1:
            calculated_obj = UserNumbers()
            user_calculated_objects.append(calculated_obj)
        case 2:
            if len(user_calculated_objects) == 0:
                print('Must enter values to display by selecting the first menu option.')
            else:
                display_values(user_calculated_objects)
        case 3:
            print('Exiting the program')
            break

if counter >= 3:
    print('Maximum number of attempts reached.')