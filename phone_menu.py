

## updated thing


on = True
off = False
def show_screen():
    print("\n" + "─" * 50)
    print("┌" + "─" * 48 + "┐")
    print("│" + " " * 18 + "iPhone 20" + " " * 19 + "  │")
    print("├" + "─" * 48 + "┤")
    print("│                                                │")
    print("│  📞 Phone      -- 1                            │")
    print("│  💬 Messages   -- 2                            │")
    print("│  📷 Camera     -- 3                            │")
    print("│  ⚙️ Settings    -- 4                            │")
    print("│  🎮 App Store  -- 5                            │")
    print("│  Power Off  -- 6                            │")
    print("│                                                │")
    print(" " + "─" * 48 + " ")

def user_click_one():
    print("="*50)
    print("📱 All Contacts: ")
    print("="*50)
    print("1. Cody --- 212")
    print("2. Aaron --- 221")
    print("3. Chase --- 221")
    print("4. Kevin --- 221")
    print("5. Back Home <= ")
    users_action = input("Call Who...? \n")
    
    if users_action == "1":
        print("\n📞 Calling Cody... 212")
    if users_action == "2":
        print("\n📞 Calling Aaron... 212")
    if users_action == "3":
        print("\n📞 Calling Chase... 212")
    if users_action == "4":
        print("\n📞 Calling Kevin... 212")
    if users_action == "<" or users_action == "5":
        show_screen()

def user_click_two():
    print("="*50)
    print("📱 iOS Messages ")
    print("="*50)

def user_click_three():
    print("="*50)
    print("📱 Camera ")
    print("="*50)
    
def user_click_four():
    print("="*50)
    print("📱 Settings ")
    print("="*50)
    
def user_click_five():
    print("="*50)
    print("📱 Games ")
    print("="*50)
    
def user_click_six():
    print("Powering Off....")
 
def main():
    while on:
        show_screen()
        users_action = input(" ")
        if users_action == "1":
            print("📞 Opening Contacts...")
            user_click_one()
        elif users_action == "2":
            print("📱 Opening Messages...")
        elif users_action == "3":
            print("📷 Opening Camera...")
        elif users_action == "4":
            print("⚙️ Opening Settings...")
        elif users_action == "5":
            print("🎮 Opening Games...")
        elif users_action == "6":
            print(" Power Off...")
        break
main()

