class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curCal = int(tokens[0])
        i = 0
        while i < len(tokens)-2:
            if tokens[i+2] == "+":
                curCal += int(tokens[i+1])
            elif tokens[i+2] == "-":
                curCal -= int(tokens[i+1])
            elif tokens[i+2] == "*":
                curCal = curCal * int(tokens[i+1])
            elif tokens[i+2] == "/":
                curCal = int(curCal/tokens[i+1])
            i+= 1

        return curCal
                