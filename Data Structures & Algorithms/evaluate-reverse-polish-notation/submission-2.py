class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "/", "*"])
        temp = tokens[0]

        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in operators:
                    if tokens[i] == "+":
                        temp = int(tokens[i-1]) + int(tokens[i-2])
                    elif tokens[i] == "-":
                        temp = int(tokens[i-2]) - int(tokens[i-1])
                    elif tokens[i] == "*":
                        temp = int(tokens[i-2]) * int(tokens[i-1])
                    elif tokens[i] == "/":
                        temp = int(int(tokens[i-2]) / int(tokens[i-1]))

                    tokens = tokens[:i-2] + [str(temp)] + tokens[i+1:]

                    # tokens[i-2] = str(temp)
                    # del tokens[i]
                    # del tokens[i-1]
                    break

        return int(tokens[0])
                