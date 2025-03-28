'''
Purpose
Deomonstrate an understanding of using Double Under methods in Object Oriented Programming

Task
Create an example of two classes (ex. one class that holds/contains another) that can
highlight the use of dunder methods in Python.

Specifics
The classes can be almost anything as long as they make some sense
The classes do not need to use the same dunders
include at least 3 non-dunder methods
Include docstrings
Required dunders
len
getitem
setitem
str
eq
lt
add
'''
#Current known cow species
species_list = [(' blue', 'a1', 4), ('black', 'a2', 1), (' pink', 'a3', 2),
                ('green', 'a4', 5), ('  red', 'a5', 3), (' Liam', 'a6', 8),
                (' Noah', 'a7', 45365)]


class spacecow:

    def __init__(self, species, milk, uses):
        """
        Creates an object.

        Args:
            Species(str): color of cow
            milk(str): type of milk it produces
            uses(int): number of times it can be milked

        Creates:
            Spacecow object
        """
        self.species = species
        self.milk = milk
        self.uses = uses

    def __repr__(self):
        """
        prints the spacecows attributes.

        Returns:
            species, milk, uses.
        """
        return 'CowInfo: {}, {}, {}'.format(self.species, self.milk,
                                            str(self.uses))

    def __eq__(self, other):
        """
        Checks if this cows uses is equal to another cows uses.

        Args:
            other(obj)

        Returns:
            True of False.
        """
        return self.species == other.species and self.milk == other.milk

    def __lt__(self, other):
        """
        Checks if cows uses are less than another cows uses.

        Args:
            other(obj)

        Returns:
            True or False.
        """
        return self.uses < other.uses

    def __add__(self, other):
        """
        adds 2 cows uses together.

        Args:
            other(obj)

        Returns:
            sum of their uses.
        """
        return self.uses + other

    def milked(self):
        """
        milks the cow.

        Returns:
            cows uses -1.
        """
        self.uses -= 1


class pen:

    def __init__(self, num):
        """
        creates a pen class to hold the cows.

        Args:
            num(int): num of cows per species

        Returns:
            list of the spacecow objects.
        """
        self.pen_list = []
        #if cows uses = 0, they go to butcher list
        self.butcher = []
        for species in species_list:
            for amount in range(num):
                cow = spacecow(species[0], species[1], species[2])
                self.pen_list.append(cow)

    def print(self):
        #prints the pen list and butches list
        for cow in self.pen_list:
            print(cow)
        for cow in self.butcher:
            print('butch')
            print(cow)

    def __getitem__(self, index):
        """
        returns a certain cow object in pen list.

        Args:
            index(int): location of cow in list

        Returns:
            cow object.
        """
        return self.pen_list[index]

    def is_equal(self, c1, c2):
        """
        CHecks if cow1 is equal to cow2.

        Args:
            c1(int): index of cow 1 in list
            c2(int): index of cow 2 in list

        Returns:
            True of False.
        """
        return self.pen_list[c1] == self.pen_list[c2]

    def __setitem__(self, index, value):
        """
        Sets a cows uses to value given.

        Args:
            index(int): location of cow
            value(int): amount of uses you want the cow to have
        """
        self.pen_list[index].uses = value

    def is_less_than(self, co1, co2):
        """
        Checks if cow 1 is less than cow 2.

        Args:
            co1(int): index of cow 1
            co2(int): index of cow 2

        Returns:
            True of False.
        """
        return self.pen_list[co1] < self.pen_list[co2]

    def add_uses(self):
        """
        adds the uses of all cows in pen.

        Returns:
            sum of all cows uses.
        """
        total = 0
        for cow in self.pen_list:
            total = cow + total
        return total
    def __len__(self):
        """
        Finds the amount of cows in the pen.

        Returns:
            total amount of cows in pen (int).
        """
        return len(self.pen_list)

    def milk(self, cow_color):
        """
        milks a certain cow; uses -1.
        removes cow from list if uses become 0 and adds to butcher list.

        Args:
            cow_color(str):first species/color of cow in the list who has uses remaining
        """
        num = -1
        for cow in self.pen_list:
            num += 1
            if cow.species == cow_color and cow.uses > 0:
                cow.milked()
            if cow.uses == 0:
                self.butcher.append(cow)
                self.pen_list.pop(num)


#test = pen(3)
#test.print()
#test[0] = 56
#print(test[0])
#print(test.is_equal(0, 1))
#print(test.is_less_than(4, 1))
#print(test.add_uses())
#print(len(test))
#print(test.milk('black'))
