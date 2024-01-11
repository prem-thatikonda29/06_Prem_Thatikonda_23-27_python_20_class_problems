class Bank:
    def __init__(self):
        # Dictionary to store customer accounts with account number as the key
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        # Create a new account with the given account number and initial balance
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account created successfully for account number {account_number} with initial balance {initial_balance}.")
        else:
            print(f"Account with account number {account_number} already exists.")

    def get_balance(self, account_number):
        # Get the balance for a specific account
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"Account with account number {account_number} does not exist.")
            return None

    def deposit(self, account_number, amount):
        # Deposit money into a specific account
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited {amount} into account number {account_number}. New balance: {self.accounts[account_number]}.")
        else:
            print(f"Account with account number {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        # Withdraw money from a specific account
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew {amount} from account number {account_number}. New balance: {self.accounts[account_number]}.")
            else:
                print(f"Insufficient funds in account number {account_number}.")
        else:
            print(f"Account with account number {account_number} does not exist.")

def main(): 
    my_bank = Bank()

    my_bank.create_account(1001, 500)
    my_bank.create_account(1002, 12000)

    my_bank.deposit(1001, 200)
    my_bank.withdraw(1002, 300)

    print(f"Balance in account 1001: {my_bank.get_balance(1001)}")

    print("Final account balances:")
    for acc_num, balance in my_bank.accounts.items():
        print(f"Account number: {acc_num}   Balance: {balance}")


if __name__ == "__main__":
    main()
