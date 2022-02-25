import unittest
import wordleTest as wordle

# For testing purpose we will hardcode solution and attempts, to remove randomness.

class testWordle(unittest.TestCase):
    def test_wordle1(self): # Case where user wins at 5th attempt
        solution = ["A","L","I","V","E"] # Setting solution
        tests = ["JUICE","BRUCE","BONES","VEGAS","ALIVE","BLESS"] # Solution where result should be True
        result = wordle.wordle(solution,tests)
        self.assertTrue(result,"True")
    
    def test_wordle2(self): # Case where user enters a word smaller than 5 letters
        solution = ['B', 'U', 'R', 'S', 'T']
        tests = ["JOINS","BRING","DEPTH","FORT","JUICE","HOTEL"]
        result = wordle.wordle(solution,tests)
        self.assertTrue(result,"Size error")
    
    def test_wordle3(self): # Case where user enters a non alphabetic input
        solution = ['H', 'O', 'N', 'E', 'Y']
        tests = ["JOINS","BRING","DEPTH","FO RT","HEALTH","HOTEL"]
        result = wordle.wordle(solution,tests)
        self.assertTrue(result,"Not alphabetic")
    
    def test_wordle4(self): # Case where user enters same word twice
        solution = ['I', 'N', 'T', 'R', 'O']
        tests = ["JOINS","BRING","DEPTH","VEGAS","JOINS","HOTEL"]
        result = wordle.wordle(solution,tests)
        self.assertTrue(result,"Word has already been tried")
    
    def test_wordle5(self): # Case where user enters non dictionary word
        solution = ['J', 'E', 'W', 'E', 'L']
        tests = ["JOINS","SWILL","DEPTH","VEGAS","JOINS","HOTEL"]
        result = wordle.wordle(solution,tests)
        self.assertTrue(result,"Not a dictionary word")
    
    def test_wordle6(self): # Case where user loses running out of moves
        solution = ['L', 'A', 'R', 'G', 'E']
        tests = ["JOINS","EMAIL","DEPTH","VEGAS","BONES","HOTEL"]
        result = wordle.wordle(solution,tests)
        print(result)
        self.assertTrue(result,"False")
            
    def test_wordle7(self): # Case where user wins on first move
        solution = ['L', 'I', 'K', 'E', 'D']
        tests = ["LIKED","EMAIL","DEPTH","VEGAS","BONES","HOTEL"]
        result = wordle.wordle(solution,tests)
        self.assertTrue(result,"True")
    
    def test_wordle8(self): # Case where user wins on last move
        solution = ['J', 'E', 'S', 'U', 'S']
        tests = ["LIKED","EMAIL","DEPTH","VEGAS","BONES","JESUS"]
        result = wordle.wordle(solution,tests)
        self.assertTrue(result,"True")
    
    def test_wordle9(self):
        solution = ['E', 'M', 'A', 'I', 'L'] # Case where user wins on seond move
        tests = ["LIKED","EMAIL","DEPTH","VEGAS","BONES","JESUS"]
        result = wordle.wordle(solution,tests)
        self.assertTrue(result,"True")


if __name__ == "__main__":
    unittest.main()