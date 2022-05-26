# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(players, parsley):
    # [assignment] Add your code here
        list1 = list (players)
        list2 = list (parsley)
        list1.sort()
        list2.sort()
        return (list1 == list2)
      
print(find_anagram("players","parsley"))       
               
          

