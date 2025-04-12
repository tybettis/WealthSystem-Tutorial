from parent_company import ParentCompany

# Create a new Parent Company
pc = ParentCompany("Tyson Global Enterprises", "Tyson Bettis", 10000000)

# Add subsidiaries
pc.add_subsidiary("Tyson Wealth Holdings")
pc.add_subsidiary("Tyson IP Holdings")

# Add assets
pc.add_asset("Tyson Legacy Trust")
pc.add_asset("WealthBot AI Patent")

# View summary
pc.summary()