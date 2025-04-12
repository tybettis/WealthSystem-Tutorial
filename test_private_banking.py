from private_banking import PrivateBanking

bank = PrivateBanking("US Private Bank", "Elena Morales")
bank.add_account("Family Trust", 1000000)
bank.add_account("Tyson Legacy Trust", 2000000)

print(bank)
print("Family Trust Balance:", bank.get_balance("Family Trust"))