class Student:
  
  def __init__(self, name, age, track ,score):
      self.name= name
      self.age= age
      self.track= track
      self.score= score
  
  def change_name(self, name):
      self.name= name
      
  def change_age(self, age):
      self.age= age
      
  def change_track(self, track):
      self.track= track
      
  def get_score(self):
      print(self.score) 



Bob= Student("bob", 26, ["BE", "FE"], 20.90)


Bob.change_name("peter")
Bob.change_age(34)
Bob.change_track("UI/UX")
Bob.get_score()
