class PrivateBanking:
    def __init__(self, bank_name, primary_contact):
        self.bank_name = bank_name
        self.primary_contact = primary_contact
        self.accounts = {}

    def add_account(self, account_name, balance):
        self.accounts[account_name] = balance

    def get_balance(self, account_name):
        return self.accounts.get(account_name, "Account not found.")

    def __str__(self):
        return f"PrivateBanking: {self.bank_name} | Contact: {self.primary_contact}\nAccounts: {self.accounts}"