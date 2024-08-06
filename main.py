from shinchan import Shinchan

def main():
    shinchan = Shinchan("Shinchan")

    while True:
        print("\nChoose an activity:")
        print("1. Play with Nani")
        print("2. Watch Action Kamen")
        print("3. Play with Shiro")
        print("4. Dance")
        print("5. Eat Ramen")
        print("6. Check Status")
        print("7. Energy Drink")
        print("8. Random Event")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            shinchan.play_with_nani()
        elif choice == "2":
            shinchan.watch_action_kamen()
        elif choice == "3":
            shinchan.play_with_shiro()
        elif choice == "4":
            shinchan.dance()
        elif choice == "5":
            shinchan.eat_ramen()
        elif choice == "6":
            shinchan.check_status()
        elif choice == "7":
            shinchan.drink_energy_drink()
        elif choice == "8":
            shinchan.random_event()
        elif choice == "9":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
