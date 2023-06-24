class BankingAPI:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, name):
        if user_id in self.users:
            return False, 'User already exists.'
        self.users[user_id] = {'name': name, 'accounts': {}}
        return True, 'User created successfully.'

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True, 'User deleted successfully.'
        return False, 'User does not exist.'

    def create_account(self, user_id, account_id):
        if user_id in self.users:
            user = self.users[user_id]
            if account_id in user['accounts']:
                return False, 'Account already exists for the user.'
            user['accounts'][account_id] = 0
            return True, 'Account created successfully.'
        return False, 'User does not exist.'

    def delete_account(self, user_id, account_id):
        if user_id in self.users:
            user = self.users[user_id]
            if account_id in user['accounts']:
                del user['accounts'][account_id]
                return True, 'Account deleted successfully.'
            return False, 'Account does not exist for the user.'
        return False, 'User does not exist.'

    def deposit(self, user_id, account_id, amount):
        if user_id in self.users:
            user = self.users[user_id]
            if account_id in user['accounts']:
                balance = user['accounts'][account_id]
                if amount <= 10000:
                    user['accounts'][account_id] = balance + amount
                    return True, 'Amount deposited successfully.'
                return False, 'Deposit amount exceeds the limit ($10,000).'
            return False, 'Account does not exist for the user.'
        return False, 'User does not exist.'

    def withdraw(self, user_id, account_id, amount):
        if user_id in self.users:
            user = self.users[user_id]
            if account_id in user['accounts']:
                balance = user['accounts'][account_id]
                max_withdrawal = balance * 0.9
                if amount <= max_withdrawal:
                    if balance - amount >= 100:
                        user['accounts'][account_id] = balance - amount
                        return True, 'Amount withdrawn successfully.'
                    return False, 'Account balance cannot go below $100.'
                return False, 'Withdrawal amount exceeds the limit.'
            return False, 'Account does not exist for the user.'
        return False, 'User does not exist.'

    def get_balance(self, username, account_name):
        if username not in self.users:
            return None
        accounts = self.users[username]['accounts']
        if account_name not in accounts or 'balance' not in accounts[account_name]:
            return None
        return accounts[account_name]['balance']


