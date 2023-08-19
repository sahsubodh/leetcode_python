//: [Previous](@previous)

import Foundation

var greeting = "Hello, playground"

//: [Next](@next)


/*
 Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

  

 Example 1:

 Input: strs = ["eat","tea","tan","ate","nat","bat"]
 Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
 Example 2:

 Input: strs = [""]
 Output: [[""]]
 Example 3:

 Input: strs = ["a"]
 Output: [["a"]]
  

 Constraints:

 1 <= strs.length <= 104
 0 <= strs[i].length <= 100
 strs[i] consists of lowercase English letters.
 */


class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var ans = [[Int]:[String]]()
        let aAscii = "a" as Character
        for str in strs {
            var count = Array.init(repeating:0,count:26)
            for char in str {
                count[Int(char.asciiValue! - aAscii.asciiValue!)] += 1
            }
            
            ans[count,default:[]].append(str)
        }
        return Array(ans.values)
    }
}

var sol = Solution()
sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
