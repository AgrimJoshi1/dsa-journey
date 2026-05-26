class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        l1 = []

        for i in s:
            if i in vowels:
                l1.append(i)

        l1.reverse()
        l2 = []
        ind = 0

        for i in s:
            if i in vowels:
                l2.append(l1[ind])
                ind += 1

            else:
                l2.append(i)

        return "".join(l2)