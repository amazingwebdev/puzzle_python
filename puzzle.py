import math

class PuzzleSolver():
    __words__ = ['OX', 'CAT', 'TOY', 'AT', 'DOG', 'CATAPULT', 'T']
    __count__ = 0
    __searchList__ = ["CATAPULT", "XZTTOYOO", "YOTOXTXX"]
    __resultList__ = []

    def __init__(self, searchList):
        self.__count__ = 0
        self.__resultList__ = []
        self.__searchList__ = searchList

    def is_word(self, word):
        """
        Returns true of word is in the dictionary, false ohterwise
        """
        return word in self.__words__

    def is_possible_word(self, word):
        for substr in self.__words__:
            if substr.find(word) == 0:
                return 0
        return -1

    def floor(self, value):
        if math.fabs(value-1) < 0.00001:
            return 1
        if math.fabs(value) < 0.00001:
            return 0
        if math.fabs(value+1) < 0.00001:
            return -1
        return value

    def find_words(self, puzzle, row, column):
        """
        Should return the number of all non-distinct occurrences of the words found
        in puzzle, horizontally, vertically or diagonally, and also the reverse in each direction.
        The input to find_words (i.e. puzzle) is a rectangular matrix of characters (lis of strings)
        """
        if self.is_word(self, puzzle):
            self.__count__ += 1
            self.__resultList__.append(puzzle)
        for index in range(8):
            conditionX = self.floor(self,math.cos(45*index/180*math.pi))
            deltaX = 1 if conditionX > 0.2 else -1 if conditionX < 0 else 0
            conditionY = self.floor(self, math.sin(45 * index / 180 * math.pi))
            deltaY = 1 if conditionY > 0.2 else -1 if conditionY < 0 else 0
            search_string = puzzle
            while row + deltaX >= 0 and \
                  row + deltaX < len(self.__searchList__) and \
                  column + deltaY >= 0 and \
                  column + deltaY < len(self.__searchList__[0]) and \
                  self.is_possible_word(self, search_string + self.__searchList__[row+deltaX][column+deltaY]) == 0:
                search_string += self.__searchList__[row+deltaX][column+deltaY]
                if self.is_word(self, search_string):
                    self.__count__ += 1
                    self.__resultList__.append(search_string)
                row += deltaX
                column += deltaY

    def main(self):
        self.__count__ = 0
        for rowIndex, row in enumerate(self.__searchList__):
            for columnIndex, cell in enumerate(row):
                self.find_words(self, cell, rowIndex, columnIndex)
        print('Output:')
        print(self.__count__)

puzzle = PuzzleSolver
# puzzle.main(puzzle)
searchList = eval(input("Please input the question list:\n"))
puzzle.__init__(puzzle, searchList)
puzzle.main(puzzle)