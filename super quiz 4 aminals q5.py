"""file containing the class animal
author Holly McClelland
created on 3/10/15"""


class Animal:
    """defines the class animal, useful for zoo data
    atrabutes: identifyer of type int
               species of type str
               age of type int
               sex of type str
               zoo of type str
               notes as tyep str
               
    methods: __str__
            add_note
    
    """
 
    
    def __init__(self, identifier, species, age, sex, zoo, notes):
        """creates a new animal with identifier, 
        species, age, sex, zoo, and notes"""
        self.identifier = identifier
        self.species = species        
        self.age = age
        self.sex = sex
        self.zoo = zoo
        self.notes = notes
        
    
    def __str__(self):
        """returns a formated string for a animal"""
        ends = "=" * 30 
        seperator = "-" * 30 
        notes = self.get_notes()
        first = "\n#{} - {}\n".format(self.identifier, self.species)
        second = "\nAge: {}\nSex: {}\nZoo: {}\n".format(self.age, self.sex, self.zoo)
        third = "\nNotes:\n"
        if type(notes) == list:
            for note in notes:
                third += "{}\n".format(note)
        else:
            third += "{}\n".format(notes)
        return ends +  first + seperator + second +seperator + third + ends
    
    
    def get_notes(self):
        """takes in an animal object and 
        retunrs the string needed for __str__ method"""
        notes_list = self.notes
        number = 1
        if len(notes_list) == 0:
            return "No notes to display."
        
        numbered_list = []
        for line in notes_list:
            numbered_list.append(str(number) + ") " + line)
            number += 1
        return numbered_list
            

    def add_note(self, note):
        """adds an adidtional note to self.note for an animal"""
        notes = self.notes
        notes.append(note)
        self.notes = notes
    

def read_data_file(filename):
    """takes a file name as the parameter then reads and processes 
    the file to return a dictornary of animals with ID as the key"""
    file = open(filename)
    lines = file.readlines()
    file.close()
    animal_dictionary = {}
    lines.remove(lines[0])
    for line in lines:
        line = line.strip()
        line = line.split(",")
        if len(line) == 5:
            line.append([])
            animal = Animal(int(line[0]), line[1], int(line[2]), line[3], line[4], line[5])
        else:
            animal = Animal(int(line[0]), line[1], int(line[2]), line[3], line[4], line[5:])
        animal_dictionary[animal.identifier] = animal
    return animal_dictionary
        
        
def get_filename():
    """Return the name of the data file to be processed
    This value is hard coded in for testing reasons"""
    return 'new_zealand_animals.csv'


def display_animal_information(animals):
    """prompts user to imput an animal ID. 
    if given ID invalid will print an error meaasge.
    displays give animals data"""
    identifier = 0
    ids = sorted(animals.keys())
    while identifier == 0:
        try:
            identifier = input("Enter an animal identifier: ")
            print(animals[int(identifier)])
        except KeyError:
            identifier = 0
            print("Error: Identifiers must be between {} and {}.".format(min(ids), max(ids)))
        except ValueError:
            identifier = 0
    

def zoo_stats(animals):
    """asks user for a zoo name then prints the stats for given zoo"""
    valid_zoo = False
    while valid_zoo == False:
        zoo_name = input("Enter a zoo: ")
        valid_zoo = zoo_valid(zoo_name, valid_zoo)
    animals_in_zoo = zoo_animals(animals, zoo_name)
    number_of_animals = len(animals_in_zoo)
    number_of_species = species_number(animals_in_zoo)
    unique_species_list = get_unique_species(animals, animals_in_zoo, zoo_name)
    stats = get_stats(zoo_name, number_of_animals, number_of_species, unique_species_list)
    print(stats)


def get_stats(zoo_name, number_of_animals, number_of_species, unique_species_list):
    """takes in zoo parameters and retuns a string of the zoos stats"""
    start_end = "=" * 30
    seperator = "-" * 30
    heding = "\nZoo Statistics for {}\n".format(zoo_name)
    no_naimals = "\nNumber of animals: {}\n".format(str(number_of_animals))
    no_species = "Number of species: {}\n".format(str(number_of_species))
    unique_lines = "Unique species:"
    for unique_species in unique_species_list:
        if unique_species == unique_species_list[-1]:
            unique_lines = unique_lines + "\n- {}\n".format(unique_species)
        else:
            unique_lines = unique_lines + "\n- {}".format(unique_species)
    return start_end + heding + seperator + no_naimals + no_species + unique_lines + start_end
    

def get_unique_species(animals, animals_in_zoo, zoo_name):
    """returns a list of animals unique to given zoo"""
    unique_species = []
    other_zoos_animals = []
    for animal in animals:
        if animals[animal].zoo != zoo_name:
            other_zoos_animals.append(animals[animal].species)    
    for animal in animals_in_zoo:
        if animal.species not in other_zoos_animals and animal.species not in unique_species:
            unique_species.append(animal.species)
    unique_species.sort()
    return unique_species

    
def species_number(animals_in_zoo):
    """returns the number of different species in a particular zoo"""
    species = []
    for animal in animals_in_zoo:
        if animal.species not in species:
            species.append(animal.species)
    return len(species)

 
def zoo_animals(animals, zoo_name):
    """takes in a dictornary of animals for multiple zoos and 
     returns a list of animals in a single given zoo"""
    animals_in_zoo = []
    animal_objects = animals.values()
    for animal in animal_objects:
        if animal.zoo == zoo_name:
            animals_in_zoo.append(animal)
    return animals_in_zoo


def zoo_valid(zoo_name, valid_zoo):
    """checks if inputed zoo name is valid"""
    valid_zoos = ["Auckland Zoo", "Wellington Zoo", "Orana Wildlife Park"]
    for zoo in valid_zoos:
        if zoo == zoo_name:
            valid_zoo = True
    if valid_zoo == False:
        print("Error: Zoo not recognised.")    
    return valid_zoo


def main():
    """main function for the animals program"""
    filename = get_filename()
    animals = read_data_file(filename)
    command = ""
    while command == "":
        entered_comand = input("Enter a command: ")
        if entered_comand == "view":
            display_animal_information(animals)
        elif entered_comand == "quit":
            command = "quit"
        elif entered_comand == "stats":
            zoo_stats(animals)
        else:
            print("Error: Invalid input.")
            
main()