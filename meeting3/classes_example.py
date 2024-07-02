class Tool:

    def __init__(self, name):
        self.name = name
        self.maintenance = []

    def add_maintenance(self, date, description):
        self.maintenance.append({
            'date': date,
            'description':description
        })


tool = Tool("ABC123")
# print(type(tool))
# print(tool.name)
tool.add_maintenance('2024-08-01', 'clean the tool')
print(tool.maintenance)

# tool2 = Tool("XYZ")
# print(tool2.name)

# s1 = "abc"
# s2 = "xyz"
#
# s1 = str("abc")
# s1.replace("a", "z")
# str.replace(s1, "a", "z")