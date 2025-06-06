

## updated thing

on = True
off = False

def show_screen():
    print("┌" + "────────────────────────────────────────────────┐")
    print("│" + "                  " + "iPhone 2000 " + "                  " + "│")
    print(" ────────────────────────────────────────────────")
    print("│                                                │")
    print("│  📞 Phone      -- 1                            │")
    print("│  💬 Messages   -- 2                            │")
    print("│  📷 Camera     -- 3                            │")
    print("│  ⚙️ Settings    -- 4                            │")
    print("│  🎮 Games      -- 5                            │")
    print("│     Power Off  -- 6                            │")
    print("│                                                │")
    print(" ────────────────────────────────────────────────")




def user_click_one():

    print("┌" + "────────────────────────────────────────────────┐")
    print("│" + "                  " + "All Contacts:""                 " + "│")
    print(" ────────────────────────────────────────────────")
    print("│                                                │")
    print("│  1. Cody --- 212-561-1212                      │")
    print("│  2. Aaron --- 212-423-7443                     │")
    print("│  3. Chase --- 212-623-5332                     │")
    print("│  4. Kevin --- 212-323-7334                     │")
    print("│  5. Back To Home <=                            │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    users_action = input("│  Call Who...? ")
    if users_action == "1":
        print("\n📞 Calling Cody...  ")
    if users_action == "2":
        print("\n📞 Calling Aaron...  ")
    if users_action == "3":
        print("\n📞 Calling Chase...   ")
    if users_action == "4":
        print("\n📞 Calling Kevin...   ")
    if users_action == "<" or users_action == "5":
        show_screen()
    print(" ────────────────────────────────────────────────")

def user_click_two():
    print("┌" + "────────────────────────────────────────────────┐")
    print("│" + "                  " + "iOS Message:""                 " + "│")
    print(" ────────────────────────────────────────────────")
    print("│                                                │")
    print("│  0 Messages... Loser                           │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print(" ────────────────────────────────────────────────")
    

def user_click_three():
    print("┌" + "────────────────────────────────────────────────┐")
    print("│" + "                  " + "Camera:""                 " +    "      │")
    print(" ────────────────────────────────────────────────")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│   [◉] Flash    [☐] Filter    [📷] Lens         │")
    print(" ────────────────────────────────────────────────")
    
def user_click_four():
    print("┌" + "────────────────────────────────────────────────┐")
    print("│" + "                  " + "Settings:""                 " + "│")
    print(" ────────────────────────────────────────────────")
    print("│                                                │")
    print("│  1. Wi-Fi          ||||||||   Connected        │")
    print("│  2. Bluetooth      [ ON ]                      │")
    print("│  3. VPN            [ OFF ]                     │")
    print("│  4. Airplane Mode  [ OFF ]                     │")
    print("│  5. Back To Home <=                            │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print(" ────────────────────────────────────────────────")
    
def user_click_five():
    print("┌" + "────────────────────────────────────────────────┐")
    print("│" + "                  " + "Games:""                 " + "       │")
    print(" ────────────────────────────────────────────────")
    print("│                                                │")
    print("│  1. Snake                                    ▶ │")
    print("│  2. Tetris                                   ▶ │")
    print("│  3. Pong                                     ▶ │")
    print("│  4. Space Invaders                           ▶ │")
    print("│  5. Back To Home <=                            │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print(" ────────────────────────────────────────────────")
    
def user_click_six():
    print("┌" + "────────────────────────────────────────────────┐")
    print("│                                                │")
    print(" ────────────────────────────────────────────────")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                 Powering Off....               │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print("│                                                │")
    print(" ────────────────────────────────────────────────")
 
def main():
    while on:
        show_screen()
        users_action = input(" ")
        if users_action == "1":
            user_click_one()
        elif users_action == "2":
            user_click_two()
        elif users_action == "3":
            user_click_three()
        elif users_action == "4":
            user_click_four()
        elif users_action == "5":   
            user_click_five()
        elif users_action == "6":
            user_click_six()
        break
main()

