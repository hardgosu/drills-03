import pickle

class Npc:
    def __init__(self, name, x, y):
        self.name = name
        self.x, self.y = x, y

data = [1,2,3,4,5]
with open('data.pickle', 'wb') as f: pickle.dump(data, f)
with open('data.pickle', 'rb') as f: read_data = pickle.load(f)
print(read_data)



yuri = Npc('Yuri', 100, 200)
with open('npc.pickle', 'wb') as f: pickle.dump(yuri, f)
with open('npc.pickle', 'rb') as f: read_npc = pickle.load(f)
print(read_npc.name, read_npc.x, read_npc.y)


print(yuri.__dict__)
new_data = {"name": "jusu", "x":400, "y":900}
yuri.__dict__.update(new_data)
print(yuri.__dict__)
print(yuri.name, yuri.x, yuri.y)