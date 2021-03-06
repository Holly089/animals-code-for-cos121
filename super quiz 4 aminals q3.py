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
    the file"""
    file = open(filename)
    lines = file.readlines()
    file.close()
    animal_dictionary = {}
    lines.remove(lines[0])
    for line in lines:
        line = line.strip()
        line=line.split(",")
        if len(line) == 5:
            line.append("")
        animal = Animal(line[0] ,line[1], line[2], line[3], line[4], line[5])
        animal_dictionary[animal.identifier] = animal
        
    return animal_dictionary
        
        
        
        
        
filename = 'new_zealand_animals.csv'
animals = read_data_file(filename)
print(animals[1])        