from BankingAPI import BankingAPI

api = BankingAPI()

# Create a user
success, message = api.create_user('user1', 'John Doe')
print(success)  # True
print(message)  # User created successfully.

# Create an account for the user
success, message = api.create_account('user1', 'account1')
print(success)  # True
print(message)  # Account created successfully.

# Deposit into the account
success, message = api.deposit('user1', 'account1', 5000)
print(success)  # True
print(message)  # Amount deposited successfully.

# Withdraw from the account
success, message = api.withdraw('user1', 'account1', 3000)
print(success)  # True
print(message)  # Amount withdrawn successfully.

# Delete the account
success, message = api.delete_account('user1', 'account1')
print(success)  # True
print(message)  # Account deleted successfully.

# Delete the user
success, message = api.delete_user('user1')
print(success)  # True
print(message)  # User deleted successfully.
