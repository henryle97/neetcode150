"""
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

Solution:
    

"""

from typing import List
from collections import Counter


def is_anagram(
    src: str, target: str
):  # O(n) with n = max length of src, target
    return Counter(src) == Counter(target)


def find_group_for(word: str, groups: List[List[str]]) -> int:
    for idx, group in enumerate(groups):
        if is_anagram(group[0], word):
            return idx
    return None


def solve(input: List[str]):
    groups = []
    for word in input:
        if len(groups) == 0:
            groups.append([word])
            continue
        group_index = find_group_for(word, groups=groups)
        if group_index is None:
            groups.append([word])
        else:
            groups[group_index].append(word)
    return groups


print(solve(["eat", "tea", "tan", "ate", "nat", "bat"]))
