class MockDatabase:
    def __init__(self):
        self.users = {}  # In-memory user data
        self.accounts = {}  # In-memory account data

    def create_user(self, username, full_name):
        self.users[username] = {'full_name': full_name, 'accounts': {}}

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]

    def create_account(self, username, account_name):
        if username in self.users:
            self.users[username]['accounts'][account_name] = {'balance': 0}

    def delete_account(self, username, account_name):
        if username in self.users and account_name in self.users[username]['accounts']:
            del self.users[username]['accounts'][account_name]

    def deposit(self, username, account_name, amount):
        if username in self.users and account_name in self.users[username]['accounts']:
            self.users[username]['accounts'][account_name]['balance'] += amount

    def withdraw(self, username, account_name, amount):
        if username in self.users and account_name in self.users[username]['accounts']:
            current_balance = self.users[username]['accounts'][account_name]['balance']
            if current_balance >= amount:
                self.users[username]['accounts'][account_name]['balance'] -= amount

    def get_balance(self, username, account_name):
        if username in self.users and account_name in self.users[username]['accounts']:
            return self.users[username]['accounts'][account_name]['balance']
        return None
