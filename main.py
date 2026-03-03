class Student:
    passing_score = 60

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        if self.passing_score >= self.passing_score:
            return True

    @classmethod
    def change_passing_score(cls, new_score):
        cls.passing_score = new_score

    @staticmethod
    def is_valid_score(score):
        if 0 < score <= 100:
            return True

