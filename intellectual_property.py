class IntellectualProperty:
    def __init__(self, title, owner, type_of_ip, registration_number):
        self.title = title
        self.owner = owner
        self.type_of_ip = type_of_ip  # e.g., "Trademark", "Copyright", "Patent"
        self.registration_number = registration_number

    def __str__(self):
        return f"{self.type_of_ip}: {self.title} | Owner: {self.owner} | Reg#: {self.registration_number}"