"""Object oriented high score table"""

class Result():
    """An object of the class Result."""

    def __init__(self, name, score):
        """Call constructor to create a score with given name and score (points)."""
        self.name = name
        self.score = score

    def __str__(self):
        """A string representation of the score object."""
        return self.name + ": " + str(self.score)
    
class HighScoreTable():
    """Table with names and scores."""

    def __init__(self):
        """Call constructor to create a high score table."""
        self.table = []

    def add(self, result_object):
        """Add a result to the high score table."""
        self.table.append(result_object)

    def __str__(self):
        """Returns a string representation of the high score table."""
        answer = ""
        for result in self.table:
            answer += str(result) + "\n"
        return answer

    def sort(self):
        """Sort the high score table."""
        # sorting using lambda
        # see: https://docs.python.org/3/howto/sorting.html
        self.table = sorted(self.table, key=lambda score: score.score, reverse=True)
    


class Test:
    """Class to test the high score table."""

    def run(self):
        """Test to run to test the high score table."""
        table = HighScoreTable()
        table.add(Result("Ada", 10))
        table.add(Result("Beda", 30))
        table.add(Result("Ceda", 25))
        table.add(Result("David", 15))
        print(table)

        table.sort()

        print(table)

test = Test()
test.run()