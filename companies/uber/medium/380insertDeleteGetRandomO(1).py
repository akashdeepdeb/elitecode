import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.rand = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.rand.get(val) == None or self.rand.get(val) == 0:
            self.rand[val]=1
            self.size+=1
            return True
        return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.rand.get(val) == None:
            return False
        del self.rand[val]
        self.size-=1
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(list(self.rand.keys()))




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
