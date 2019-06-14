import time

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value:
          if not self.left:
            self.left = BinarySearchTree(value)
          else:
            self.left.insert(value)
        elif value >= self.value:
          if not self.right:
            self.right = BinarySearchTree(value)
          else:
            self.right.insert(value)
        pass

    def contains(self, target):
        if self.value == target:
          return True
        elif target < self.value and not self.left == None:
          return self.left.contains(target)
        elif target >= self.value and not self.right == None:
          return self.right.contains(target)
        else:
          return False
        pass

name1_bst = BinarySearchTree(names_1[0])

for i in range(1, len(names_1)):
    name1_bst.insert(names_1[i])

for j in range(len(names_2)):
    if name1_bst.contains(names_2[j]):
        duplicates.append(names_2[j])


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")




# Stretch Solution
print('\n STRETCH OUTPUT')
names_1.sort()
duplicates = []

for name_2 in names_2:
    names_1_sorted = [*names_1]
    half = len(names_1_sorted) // 2
    found = False
    while found != True and half >= 1:
        if names_1_sorted[half] == name_2:
            found = True
            duplicates.append(name_2)
        elif names_1_sorted[half] < name_2:
            names_1_sorted = names_1_sorted[half:]
            half = len(names_1_sorted) // 2
        elif names_1_sorted[half] > name_2:
            names_1_sorted = names_1_sorted[:half]
            half = len(names_1_sorted) // 2

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

