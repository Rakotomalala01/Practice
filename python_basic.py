from typing import List, Optional
import math

##Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

            


# import httpx
# from bs4 import BeautifulSoup

# def fetch_rows_from_doc(url: str):
#     response = httpx.get(url, timeout=10.0)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, "html.parser")
#     table = soup.find("table")

#     data = []
#     for row in table.find_all("tr"):
#         cells = row.find_all(["td", "th"])
#         row_data = [cell.get_text(strip=True) for cell in cells]
#         if row_data:
#             data.append(row_data)

#     return data

# def convert_rows_to_coordinates(rows: List[List[str]]):
#     coordinates = []

#     for row in rows[1:]:  
#         x = int(row[0])
#         y = int(row[2])
#         char = row[1]

#         coordinates.append((x, y, char))

#     return coordinates

# def build_grid(coordinates: List[tuple[int, int, str]]):

#     max_x = max(x for x, y, char in coordinates)
#     max_y = max(y for x, y, char in coordinates)

#     grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

#     for x, y, char in coordinates:
#         grid[y][x] = char

#     return grid



# def print_grid(grid: List[List[str]]):
#     for row in reversed(grid):
#         print("".join(row))

# def decode_url_message(url:str):
#     rows = fetch_rows_from_doc(url)
#     coordinates = convert_rows_to_coordinates(rows)
#     grid = build_grid(coordinates)
#     print_grid(grid)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 
 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 
 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        

        for i in range(len(s)) :
            print( t [ i - ( len(s) - 1)] )
            alphabet[s[i]] -= 1
        
        for j in range(len(t)):
            alphabet[t[j]] +=1

        return all(value == 0 for value in alphabet.values())

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for elem in nums:
            
            res.append(target - elem)
        
        print(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet_init = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
            'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 
            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        
        key = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
            'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 
            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        for word in strs :
            for char in word:
                key[char] +=1
        
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums) - 1):
            if(nums[i] < nums[i + 1]):
                count += 1
            else :

                count = 0
    

    def isPalindrome(self, s: str) -> bool:

        alphanumS = ("".join(ch for ch in s if ch.isalnum())).lower()
        half = int(len(alphanumS) / 2)
        res = True
        T1 = []
        T2 = []
        for i in range(0, half ):
            pt1 = i
            pt2 = len(alphanumS) - 1 - i
            T1.append(alphanumS[pt1])
            T2.append(alphanumS[pt2])
            res = res and (alphanumS[pt1] == alphanumS[pt2])
        print(T1)
        print(T2)
        print(res)
        return res

    def characterReplacement(self, s: str, k: int) -> int:

        if k == len(s) or k == len(s) - 1:
            return len(s)
        longest = 0
        l = 0
        r = k + 1
        while(r < len(s)):
            longest = max(longest, len(s[l:r]))
            if ( s[l] == s[r] ):
                r += 1
            else:
                l += 1
        return longest
    
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        enclosing = {")", "]", "}"}


        stack = []
        i = 0

        while i < len(s):
            while s[i] not in enclosing :

                # add the char 
                stack.append(s[i])
                i += 1
                if (i == len(s)): 
                    return False

            # IF char is not enclosing

            if not stack : 
                return False 
            if brackets[s[i]] != stack.pop() :
                return False 
            # remove last in stack check if this enclosing correspond to the last opening 
            i += 1
        
        return not stack
    
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

    def search(self, nums: List[int], target: int) -> int:  

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] == target: return l
            if nums[m] == target: return m
            if nums[r] == target: return r

            if nums[l] < nums[m] :
                if nums[l] < target < nums[m]:
                    # GO LEFT
                    r = m - 1
                else: 
                    # GO RIGHT
                    l = m + 1
            else:
                if nums[m] < target < nums[r]:
                    # GO RIGHT
                    l = m + 1

                else:
                    # GO LEFT
                    r = m - 1

        return - 1
    
    def build_linked_list(values):
        if not values:   # if list is empty
            return None

        head = ListNode(values[0])  # first node
        current = head              # pointer to move along list

        for val in values[1:]:
            current.next = ListNode(val)  # link new node
            current = current.next        # move pointer forward

        return head

    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-101, None)
        begin = res
        while (list1 is not None) and (list2 is not None) :
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else :
                res.next = list2
                list2 = list2.next
            res = res.next
        
        res.next = list1 if list1 else list2

        return begin.next
    

    def hasChild(self, node: Optional[TreeNode]) -> bool:
        return bool(node.left or node.right) 
    
             
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.hasChild( root.left ):
            self.invertTree(root.left)
        elif self.hasChild(root.right) :
            self.invertTree(root.right)
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            
    
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root 
        while cur:
            if (p.val > cur.val) and (q.val > cur.val):
                cur = cur.right
            elif (p.val < cur.val) and (q.val < cur.val):
                cur = cur.left
            else:
                return cur


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depthIndex = 0
        res = [[root.val]]

        def addElem(root: Optional[TreeNode], depthIndex: int) -> List[List[int]]:
            nonlocal res
            if not root:
                return
            elif len(res) < depthIndex + 1:
                res.append([])
            res[depthIndex].append(root.val)
            addElem(root.left, depthIndex + 1)
            addElem(root.right, depthIndex + 1)
        
        addElem(root.left, depthIndex + 1)
        addElem(root.right, depthIndex + 1)
        return res
    
    def exist(self, board: List[List[str]], word: str) -> bool:





        

    

    
















if __name__ == "__main__":
    # url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    sol = Solution()


    head = [1,2,3,4]
    n = 2
    sol.removeNthFromEnd(head, n)









