class Trust:
    def __init__(self, name, trustee, beneficiaries):
        self.name = name
        self.trustee = trustee
        self.beneficiaries = beneficiaries
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def show_trust_info(self):
        print(f"Trust: {self.name}")
        print(f"Trustee: {self.trustee}")
        print(f"Beneficiaries: {', '.join(self.beneficiaries)}")
        print(f"Assets: {self.assets}") 
