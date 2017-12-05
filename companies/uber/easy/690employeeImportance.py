"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        empMap = {i.id: i for i in employees}
        empList = []
        imp = 0
        empList.append(id)
        while len(empList) != 0:
            popped = empList.pop(0)
            imp += empMap[popped].importance
            for subs in empMap[popped].subordinates:
                empList.append(subs)
        return imp
