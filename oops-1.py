class employee : 
    def __init__(self):
        self.id=123
        self.salary=50000
        self.name="Uma Pravallika"

    def travel(self,destination):
        print(f"Hello {self.name}, your destination {destination} is reached ")

sam=employee()
print(sam.id)
print(sam.travel("Kerala"))
