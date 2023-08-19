//: [Previous](@previous)

import Foundation

/*
 Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

  

 Example 1:

 Input: s = "anagram", t = "nagaram"
 Output: true
 Example 2:

 Input: s = "rat", t = "car"
 Output: false
  

 Constraints:

 1 <= s.length, t.length <= 5 * 104
 s and t consist of lowercase English letters.
  

 Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
 */

class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
          guard s.count == t.count else {
              return false
          }
          
          var dict = [Character:Int]()
          
          for char in s {
              dict[char,default:0] += 1
          }
          
          for char in t {
              if let count = dict[char], count > 0 {
                  dict[char] = count - 1
              } else {
                  return false
              }
          }
          
          return dict.values.allSatisfy { $0 == 0}
      }
    
    func isAnagram1(_ s: String, _ t: String) -> Bool {
          guard s.count == t.count else {
              return false
          }
          
        let unicode_a = Int(UnicodeScalar("a").value)
        
        var counter = Array.init(repeating: 0, count: 26)
        
        for i in s.unicodeScalars {
            counter[Int(i.value)-unicode_a] += 1
        }
        
        for i in t.unicodeScalars {
            counter[Int(i.value)-unicode_a] -= 1
        }
        
        
        return counter.allSatisfy {$0 == 0}
      }
}
