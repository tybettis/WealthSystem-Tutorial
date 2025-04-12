from holding_company import HoldingCompany

class Entity:
    def __init__(self, name):
        self.name = name

hc = HoldingCompany("Tyson Wealth Holdings", "12-3456789", "123 Strategy Lane")
hc.add_entity(Entity("Parent Company LLC"))
hc.add_entity(Entity("IP Holdings"))
hc.add_entity(Entity("Private Banking"))

print(hc)
print("Entities:", hc.list_entities())
