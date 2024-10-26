class BankApp:
    users = {
        "user1": {"password": "pass1", "balance": 1000, "account_number": "111-111-111"},
        "user2": {"password": "pass2", "balance": 2000, "account_number": "222-222-222"},
        "user3": {"password": "pass3", "balance": 3000, "account_number": "333-333-333"}
    }

    def __init__(self):
        self.current_user = None

    def login(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            self.current_user = self.users[username]
            return "Login successful"
        return "Invalid username or password"

    def show_account_info(self):
        if self.current_user:
            return {
                "balance": self.current_user["balance"],
                "account_number": self.current_user["account_number"]
            }
        return "No user logged in"

    def logout(self):
        self.current_user = None
        return "Logged out successfully"
    
def main():
    app = BankApp()
    print("Welcome to the Bank App!")
    
    # Loop until login is successful
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        login_msg = app.login(username, password)
        print(login_msg)
        
        if login_msg == "Login successful":
            break
        else:
            print("Please try again.")

    # Loop to prompt for actions after successful login
    while True:
        print("\nOptions:")
        print("1. View Balance")
        print("2. View Account Number")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("Account Balance:", app.show_account_info()["balance"])
        elif choice == "2":
            print("Account Number:", app.show_account_info()["account_number"])
        elif choice == "3":
            print("Exiting application...")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
