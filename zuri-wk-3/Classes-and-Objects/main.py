class Student:
    # [assignment] Skeleton class. Add your code here
    name = str()
    age = int()
    tracks = []
    score = float()
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = str(name)
        return self.name

    def change_age(self, age):
        self.age = int(age)
        return self.age

    def add_track(self, track):
        li = self.tracks
        li.append(track)
        self.tracks = li
        return li

    def get_score(self):
        self.score = float()
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()


