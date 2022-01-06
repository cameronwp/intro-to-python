import numpy as np


class Dog:
    """
    An actual dog
    """

    def __init__(self, name, breed, is_female):
        """
        Set the properties of this dog
        """
        self.name = name
        self.breed = breed
        self.female = is_female
        self.location = None

    def bark(self):
        """
        Prints a message from the dog
        """
        print(f"Woof woof! My name is: {self.name} and I am a {self.breed}")

    def come(self, location):
        """
        Tells the dog to come to a location

        Params:
            location np.array(2)
        """
        self.location = location

    def distance_from_food_bowl(self, food_bowl_location):
        """
        The dog returns its euclidean distance from a food bowl

        Params:
            food_bowl_location np.array(2)
        """
        if self.location is None:
            print("I don't know where I am")
            return

        return np.linalg.norm(self.location - food_bowl_location)


hawkeye = Dog("Hawkeye", "husky", True)
print(hawkeye.female)
hawkeye.bark()
hawkeye.come(np.array((0, 0)))

distance = hawkeye.distance_from_food_bowl(np.array((4, 4)))

print(f"Hawkeye is {distance} from her food bowl now")
