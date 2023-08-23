//: [Previous](@previous)

import Foundation

/*
 
 125. Valid Palindrome
 
 A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
 
 Given a string s, return true if it is a palindrome, or false otherwise.
 
 
 
 Example 1:
 
 Input: s = "A man, a plan, a canal: Panama"
 Output: true
 Explanation: "amanaplanacanalpanama" is a palindrome.
 Example 2:
 
 Input: s = "race a car"
 Output: false
 Explanation: "raceacar" is not a palindrome.
 Example 3:
 
 Input: s = " "
 Output: true
 Explanation: s is an empty string "" after removing non-alphanumeric characters.
 Since an empty string reads the same forward and backward, it is a palindrome.
 
 
 Constraints:
 
 1 <= s.length <= 2 * 105
 s consists only of printable ASCII characters.
 */

class Solution {
    func isPalindrome(_ s: String) -> Bool {
        var arr:[Character] = s.filter { $0.isLetter || $0.isNumber }
        
        var right = arr.count - 1
        var left = 0
        
        while (left < right) {
            if arr[left].lowercased() == arr[right].lowercased() {
                left += 1
                right -= 1
            } else {
                return false
            }
        }
        
        return true
    }
}
