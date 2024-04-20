class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Step 1: Calculate the total number of apples
        total_apples = sum(apple)
        
        # Step 2: Sort the capacity array in descending order
        capacity.sort(reverse=True)
        
        # Step 3: Initialize variables for current capacity and box count
        current_capacity = 0
        boxes_used = 0
        
        # Step 4: Loop through each box in the sorted capacity array
        for box_capacity in capacity:
            current_capacity += box_capacity
            boxes_used += 1
            
            # Step 5: Check if the accumulated capacity is enough
            if current_capacity >= total_apples:
                break
        
        # Step 6: Return the number of boxes used
        return boxes_used