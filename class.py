class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

class Musician:
  def __init__(self, name, genres = "Pop",instrument=None,  ):
    self.name = name
    self.genres = genres
    self.instrument = instrument
    self.albums_sold = 0


  def __str__(self):
    return f"{self.name} {self.genres} -  {self.instrument} - {self.albums_sold}"

p1 = Musician("John ","Rock", instrument="Guitar")
p2 = Musician("Daisy ", instrument="Violin")
p3 = Musician("Jack ",instrument="Cello")

print(p1)
print(p2)
print(p3)

class Card:
  def __init__(self, suit, face):
    self.suit = suit
    self.face = face
suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cards = []

# Create cards with all combinations of suits and faces
for suit in suits:
    for face in faces:
        # card = Card(suit, face)
        # cards.append(card)
        cards.append((face, suit))

# Print the cards
for card in cards:
    # print(f"Suit: {card.suit}, Face: {card.face}") 
    face, suit = card
    print(f"Suit: {suit}, Face: {face}")
class Band:
   def __init__(self, name):
      self.member_list = []

   def introduce_member(self):
      
      for member in self.member_list:
         print("Band Member: ")
   def add_new_member(self, new_member):
      self.member_list.append(new_member)
   def remove_member(self, old_member):
      self.member_list.append(old_member)
      if len(self.member_list) == 0:
         disbanded = True
      else:
         self.member_list()
         


      