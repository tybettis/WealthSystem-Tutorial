class HoldingCompany:
    def __init__(self, name, ein, address):
        self.name = name
        self.ein = ein #Employer Identification number
        self.address = address
        self.entities = [] #Subsidiaries, LLCs, or IPs it owns

    def add_entity(self, entity):
        self.entities.append(entity)

    def list_entities(self):
        return [entity.name for entity in self.entities]

    def __repr__(self):
        return f"<HoldingCompany: {self.name} | EIN: {self.ein}" 
                     




