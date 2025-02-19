class Tamagotchi:
    """
    Base class for all Tamagotchi pets.
    
    This class provides the common attributes and methods that all Tamagotchi pets share,
    including basic stats management and interactions.

    Attributes:
        name (str): The name of the Tamagotchi
        species (str): The species of the Tamagotchi
        happiness_level (int): Current happiness level, starts at 80
        hunger (int): Current hunger level, starts at 80
        energy (int): Current energy level, starts at 80
    """
    
    def __init__(self, name, species):
        """
        Initialize a new Tamagotchi.

        Args:
            name (str): The name to give to the Tamagotchi
            species (str): The species of the Tamagotchi
        """
        self.name = name
        self.species = species
        self.happiness_level = 80
        self.hunger = 80
        self.energy = 80

    def feed(self):
        """
        Feed the Tamagotchi to increase hunger and decrease energy.
        
        Increases hunger by 10 points and decreases energy by 5 points.
        Values are capped at 150 (maximum) and 0 (minimum).
        """
        self.hunger += 10
        if self.hunger > 150:
            self.hunger = 150

        self.energy -= 5
        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} has been fed. Hunger level: {self.hunger}, Stamina level: {self.energy}")

    def speak(self):
        """Base method for Tamagotchi speech. To be implemented by subclasses."""
        pass

    def rest(self):
        """Base method for Tamagotchi rest. To be implemented by subclasses."""
        pass


class Dog(Tamagotchi):
    """
    Dog class that inherits from Tamagotchi.
    
    Implements dog-specific behavior for speaking (barking) and resting.
    """

    def __init__(self, name):
        """Initialize a new Dog Tamagotchi."""
        super().__init__(name, "Dog")

    def speak(self):
        """
        Make the dog bark, increasing happiness and decreasing energy.
        
        Increases happiness by 5 points and decreases energy by 5 points.
        """
        self.happiness_level += 5
        self.energy -= 5
        if self.happiness_level > 150:
            self.happiness_level = 150

        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} is barking! Happiness level: {self.happiness_level}, Stamina Level: {self.energy}")

    def rest(self):
        """
        Let the dog rest, increasing energy and decreasing hunger.
        
        Increases energy by 25 points and decreases hunger by 15 points.
        """
        self.energy += 25
        self.hunger -= 15
        if self.energy > 150:
            self.energy = 150

        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} is resting! Stamina Level: {self.energy}, Hunger Level: {self.hunger}")


class Cat(Tamagotchi):
    """
    Cat class that inherits from Tamagotchi.
    
    Implements cat-specific behavior for speaking (meowing) and resting.
    """

    def __init__(self, name):
        """Initialize a new Cat Tamagotchi."""
        super().__init__(name, "Cat")

    def speak(self):
        """
        Make the cat meow, increasing happiness and decreasing energy.
        
        Increases happiness by 3 points and decreases energy by 8 points.
        """
        self.happiness_level += 3
        self.energy -= 8
        if self.happiness_level > 150:
            self.happiness_level = 150

        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} is meowing! Happiness Level: {self.happiness_level}, Stamina Level: {self.energy}")

    def rest(self):
        """
        Let the cat rest, increasing energy and decreasing hunger.
        
        Increases energy by 15 points and decreases hunger by 10 points.
        """
        self.energy += 15
        self.hunger -= 10
        if self.energy > 150:
            self.energy = 150

        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} is resting! Stamina Level: {self.energy}, Hunger Level: {self.hunger}")


class Mouse(Tamagotchi):
    """
    Mouse class that inherits from Tamagotchi.
    
    Implements mouse-specific behavior for speaking (squeaking) and resting.
    """

    def __init__(self, name):
        """Initialize a new Mouse Tamagotchi."""
        super().__init__(name, "Mouse")

    def speak(self):
        """
        Make the mouse squeak, increasing happiness and decreasing energy.
        
        Increases happiness by 2 points and decreases energy by 3 points.
        """
        self.happiness_level += 2
        self.energy -= 3
        if self.happiness_level > 150:
            self.happiness_level = 150

        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} is squeaking! Happiness Level: {self.happiness_level}, Stamina Level: {self.energy}")

    def rest(self):
        """
        Let the mouse rest, increasing energy and decreasing hunger.
        
        Increases energy by 20 points and decreases hunger by 15 points.
        """
        self.energy += 20
        self.hunger -= 15
        if self.energy > 150:
            self.energy = 150

        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} is resting! Stamina Level: {self.energy}, Hunger Level: {self.hunger}")


class Tamagotchi_Fantasy:
    """
    Main game class that manages the Tamagotchi game.
    
    Handles creation of new pets, interactions, and game flow.
    """

    def __init__(self):
        """Initialize the game with an empty list of Tamagotchis."""
        self.tamagotchi_list = []

    def create_tamagotchi(self):
        """
        Create a new Tamagotchi based on user input.
        
        Prompts user for name and species, then creates appropriate Tamagotchi subclass.
        """
        name = input("Write a name for your Tamagotchi: ")
        species = input("Choose his/her specie (Dog-Cat-Mouse): ").lower()
        
        if species == "dog":
            self.tamagotchi_list.append(Dog(name))
        elif species == "cat":
            self.tamagotchi_list.append(Cat(name))
        elif species == "mouse":
            self.tamagotchi_list.append(Mouse(name))
        else:
            print("Please, choose the correct specie.")
            return
        print(f"¡ The {species} {name} is now alive!")

    def select_tamagotchi(self):
        """
        Allow user to select a Tamagotchi from the list.
        
        Returns:
            Tamagotchi: The selected Tamagotchi object, or None if selection invalid
        """
        if not self.tamagotchi_list:
            print("Create a Tamagotchi first!")
            return None
            
        print("Your Tamagotchi/s:")
        for i, tamagotchi in enumerate(self.tamagotchi_list):
            print(f"{i+1}. {tamagotchi.name} ({tamagotchi.species})")
            
        choice = int(input("Choose your Tamagotchi: ")) - 1
        if 0 <= choice < len(self.tamagotchi_list):
            return self.tamagotchi_list[choice]
        else:
            print("Not a possible selection.")
            return None

    def view_tamagotchi(self, tamagotchi):
        """
        Display the current stats of a Tamagotchi.
        
        Args:
            tamagotchi (Tamagotchi): The Tamagotchi whose stats to display
        """
        print(f"Status of {tamagotchi.name}, the {tamagotchi.species}:")
        print(f"Happiness: {tamagotchi.happiness_level}")
        print(f"Hunger: {tamagotchi.hunger}")
        print(f"Stamina: {tamagotchi.energy}")

    def interact_tamagotchi(self, tamagotchi):
        """
        Allow user to interact with a Tamagotchi through various actions.
        
        Args:
            tamagotchi (Tamagotchi): The Tamagotchi to interact with
        """
        print(f"\nPlaying with {tamagotchi.name}, the {tamagotchi.species}:")
        print("1. Feed")
        print("2. Speak (Bark-Meow-Squeak)")
        print("3. Rest")
        
        choice = input("Choose and action (1-3): ")
        if choice == "1":
            tamagotchi.feed()
        elif choice == "2":
            tamagotchi.speak()
        elif choice == "3":
            tamagotchi.rest()
        else:
            print("There are only 3 options! How can you fail?")

    def run(self):
        """Start and run the main game loop."""
        while True:
            print("\n****TAMAGOTCHI FANTASY****")
            print("1 - Create a new Tamagotchi")
            print("2 - Play with Tamagotchi")
            print("3 - Watch Tamagotchi Stats")
            print("4 - Exit")
            
            choice = input("Choose and option (1-4): ")

            if choice == "1":
                self.create_tamagotchi()
            elif choice == "2":
                tamagotchi = self.select_tamagotchi()
                if tamagotchi:
                    self.interact_tamagotchi(tamagotchi)
            elif choice == "3":
                tamagotchi = self.select_tamagotchi()
                if tamagotchi:
                    self.view_tamagotchi(tamagotchi)
            elif choice == "4":
                print("Thanks for playing! See you soon!!")
                break
            else:
                print("There are only 4 options. Choose one of them :).")


# Start the game
game = Tamagotchi_Fantasy()
game.run()