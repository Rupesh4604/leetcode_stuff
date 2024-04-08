class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count the number of students preferring each type of sandwich
        count = Counter(students)
      
        # Loop through the sandwiches queue
        for sandwich in sandwiches:
            # If no student wants the current type of sandwich, 
            # return the number of students who want the other type
            if count[sandwich] == 0:
                # The 'sandwich ^ 1' toggles between 1 and 0
                return count[sandwich ^ 1]
          
            # Decrement the count for the current sandwich type
            count[sandwich] -= 1
      
        # If all sandwiches match the students' preferences return 0 
        return 0