"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
"""
from typing import List

MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


def unique_morse_representations(words: List[str]) -> int:
    d_alph = dict(zip([e for e in 'abcdefghijklmnopqrstuvwxyz'], MORSE))
    s = [''] * len(words)
    for i in range(len(words)):
        for j in range(len(words[i])):
            s[i] += d_alph[words[i][j]]
    return len(set(s))


if __name__ == '__main__':
    print(unique_morse_representations(['gin', 'zen', 'gig', 'msg']))
