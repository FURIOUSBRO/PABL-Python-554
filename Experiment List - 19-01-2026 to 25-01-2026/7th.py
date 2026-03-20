#You are given an integer array arr[]. You need to find the maximum sum of a 
#subarray (containing at least one element) in the array arr[].
#Note : A subarray is a continuous part of an array.
#Examples:
#Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
#Output: 11
#Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.

class Solution:
    
    # Function to find maximum subarray sum
    def maxSubarraySum(self, arr):
        # Initialize with first element
        max_sum = arr[0]
        current_sum = arr[0]
        
        # Traverse array
        for i in range(1, len(arr)):
            
            # Kadane's Algorithm
            current_sum = max(arr[i], current_sum + arr[i])
            
            # Update maximum sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum
