# lib/anagram.py

class Anagram:
    def __init__(self, word):
        # Store the word in sorted form to easily compare with other words
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
    
    def match(self, word_list):
        # Create a list to store matching anagrams
        matches = []
        
        # Iterate over each word in the provided list
        for candidate in word_list:
            # Convert the candidate to lowercase and sort its letters
            if sorted(candidate.lower()) == self.sorted_word:
                matches.append(candidate)
        
        # Return the list of matches (could be empty if no matches found)
        return matches
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
# Expected output: ['inlets']
