

## updated thing
class PhoneMenu:
    """
    A class to represent a phone menu for an iPhone 2000.
    It provides methods to display the main menu and handle user interactions.
    """
    # constants for user actions
    USER_ACTION: str | None = None
    USER_CLICK: str | None = None
    ON: bool = True
    OFF: bool = False
    
    def __init__(self) -> None:
        super().__init__()
        # initialize the phone menu
        self.show_screen()

    def show_screen(self) -> None:
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




    def user_click_one(self) -> None:

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
            self.show_screen()
        print(" ────────────────────────────────────────────────")

    def user_click_two(self) -> None:
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
        

    def user_click_three(self) -> None:
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
        
    def user_click_four(self) -> None:
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
        
    def user_click_five(self) -> None:
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
        
    def user_click_six(self) -> None:
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
 


