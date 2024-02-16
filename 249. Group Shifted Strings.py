'''
249. Group Shifted Strings

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
'''

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)

        for s in strings:
            if len(s) == 1:
                group_dict[(-1)].append(s)
            else:
                char_diffs = []

                i = 1
                while i < len(s):
                    char_diffs.append(
                        (ord(s[i]) - ord(s[i-1])) % 26
                    )

                    i += 1
                group_dict[tuple(char_diffs)].append(s)
        return group_dict.values()
        