from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Maps each character-count signature to the list of words that share it.
        # defaultdict(list) creates an empty list the first time a new key is used,
        # so we can append without checking whether the key exists.
        res = defaultdict(list)

        for s in strs:
            # One slot per lowercase letter: index 0 = 'a', 1 = 'b', ..., 25 = 'z'
            count = [0] * 26

            for c in s:
                # ord() gives a character's ASCII number. Subtracting ord("a")
                # shifts 'a'..'z' down to 0..25, so each letter gets its own slot.
                count[ord(c) - ord("a")] += 1

            # Anagrams have identical counts, so they land under the same key.
            # Lists can't be dictionary keys (they're mutable), so convert to a tuple.
            res[tuple(count)].append(s)

        # Each value in res is one group of anagrams.
        return list(res.values())

# Time:  O(n * k), where n = number of strings and k = length of the longest string
# Space: O(n * k) to store all the strings in the dictionary