class Student:

    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score= float(score)

        
bob = Student(name="Bob", age=26, tracks=["PHP","CSS"], score=20)


class Student2:

    def __init__(self, new_name, new_age, new_track, new_score):
        self.new_name = str(new_name)
        self.new_age = int(new_age)
        self.new_tracks = list(new_track)
        self.new_score = float(new_score)

peter = Student2(new_name ="Peter", new_age = 34, new_track = ["PHP", "CSS", "UI/UX"], new_score = 50 )
print(peter.new_age)
print(peter.new_tracks)
print(peter.new_score)






