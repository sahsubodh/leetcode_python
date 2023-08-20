//: [Previous](@previous)

import Foundation

/*
 Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

  

 Example 1:

 Input: nums = [1,1,1,2,2,3], k = 2
 Output: [1,2]
 Example 2:

 Input: nums = [1], k = 1
 Output: [1]
  

 Constraints:

 1 <= nums.length <= 105
 -104 <= nums[i] <= 104
 k is in the range [1, the number of unique elements in the array].
 It is guaranteed that the answer is unique.
  

 Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 */


class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var dict:[Int:Int] = [:]
        
        for i in 0..<nums.count {
            dict[nums[i],default:0] += 1
        }
        
        var freq:[[Int]] = Array.init(repeating: [], count: nums.count + 1)
        
        for (index,value) in dict {
            freq[value].append(index)
        }
        
        var result:[Int] = []
        
        for index in stride(from: freq.count - 1, to: 0, by: -1) {
            for num in freq[index] {
                result.append(num)
            }
            
            if result.count == k {
                return result
            }
        }
        
        return result
    }
}
