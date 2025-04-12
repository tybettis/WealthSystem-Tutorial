class ParentCompany:
    def __init__(self, name, ceo, valuation):
        self.name = name
        self.ceo = ceo
        self.valuation = valuation
        self.subsidiaries = []
        self.assets = []

    def add_subsidiary(self, company_name):
        self.subsidiaries.append(company_name)

    def add_asset(self, asset_name):
        self.assets.append(asset_name)

    def summary(self):
        print(f"Parent Company: {self.name}")
        print(f"CEO: {self.ceo}")
        print(f"Valuation: ${self.valuation}")
        print("Subsidiaries:", self.subsidiaries)
        print("Assets:", self.assets)