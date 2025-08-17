class animal : 
    def __init__(self):
        self.name="Buddy"

    def speak(self):
        print(f"{self.name} makes a sound")
class Dog(animal) :
    def __init__(self,breed):
        super().__init__()
        self.breed=breed    
    def speak(self):
        super().speak()
        print(f"{self.name} barks. It is a {self.breed}.")

# # Create an instance of Dog
dog = Dog("Golden Retriever")
dog.speak()
