'''
269. Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are 
sorted lexicographically
by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.

'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) -1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1),len(w2))
            # this following length condition is removed now?
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
              return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}  # {char: bool} False - visited, True - visited and current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True
            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True
            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""


        res.reverse()
        return "".join(res)