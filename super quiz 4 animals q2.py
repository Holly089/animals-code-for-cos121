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
        notes = self.notes
        if len(notes) == 0:
            notes = "No notes to display."
        first = "\n#{} - {}\n".format(self.identifier, self.species)
        second = "\nAge: {}\nSex: {}\nZoo: {}\n".format(self.age, self.sex, self.zoo)
        third = "\nNotes:\n{}\n".format(notes)
        return ends + first + seperator + second +seperator + third + ends