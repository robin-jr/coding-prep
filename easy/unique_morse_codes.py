class Solution:
    morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                   "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result_codes = set()
        for word in words:
            curr_code = ""
            for char in word:
                curr_code += self.morse_codes[ord(char) - ord('a')]
            result_codes.add(curr_code)
        return len(result_codes)
