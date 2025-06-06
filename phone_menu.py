from contacts.contacts import show_contacts, add_contacts

on = True
off = False


def show_screen():
    print("┌" + "────────────────────────────────────────────────┐")
    print("│" + "                  " +
          "iPhone 2000 " + "                  " + "│")
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
    all_contacts = show_contacts()
    print("="*50)

    print("┌" + "────────────────────────────────────────────────┐")
    print("│" + "                  " + "All Contacts:""                 " + "│")
    print(" ────────────────────────────────────────────────")
    print("│                                                │")
    for idx, contact in enumerate(all_contacts):
        print(
            f"| {idx + 1}. {contact[0]}:      {contact[1]}                      |")
    print("="*50)
    print("5. Back Home <= ")
    users_action = int(input("Call Who...? \n"))
    print(
        f"\n📞 Calling {all_contacts[users_action][0]} ...{all_contacts[users_action][1][8::]}")
    if users_action == "<" or users_action == "5":
        show_screen()


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
    print("│" + "                  " + "Camera:""                 " + "      │")
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
        elif users_action == "7":
            print("Contacts")
        break


main()
