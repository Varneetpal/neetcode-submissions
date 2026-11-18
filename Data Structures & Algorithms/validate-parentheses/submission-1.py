class Solution:
    def isValid(self, s: str) -> bool:

        if s is None:
            return True

        openB = set(["{", "[", "("])
        closeB = set(['}', ']', ')'])

        bracketTrack = []

        for b in s:
            if b in openB:
                bracketTrack.append(b)
            elif b in closeB:
                if (b == ')' and bracketTrack[-1] == '('):
                    bracketTrack.pop()
                elif (b == '}' and bracketTrack[-1] == '{'):
                    bracketTrack.pop()
                elif (b == ']' and bracketTrack[-1] == '['):
                    bracketTrack.pop()
                else:
                    return False

        if len(bracketTrack) == 0:
            return True

        return True