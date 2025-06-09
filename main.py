from phone_menu import PhoneMenu 

def main():
    menu = PhoneMenu()
    while menu.ON:
        menu.show_screen()
        users_action = input(" ")
        if users_action == "1":
            menu.user_click_one()
        elif users_action == "2":
            menu.user_click_two()
        elif users_action == "3":
            menu.user_click_three()
        elif users_action == "4":
            menu.user_click_four()
        elif users_action == "5":   
            menu.user_click_five()
        elif users_action == "6":
            menu.user_click_six()
        break
main()