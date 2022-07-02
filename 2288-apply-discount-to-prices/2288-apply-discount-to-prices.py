class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        stack = sentence.split(' ')
        lst = []
        for i in range(len(stack)):
            if stack[i].count('$') == 1 and stack[i][0] == '$' and stack[i][1:].isdigit():
                f = int(stack[i][1:]) - (int(stack[i][1:]) * (discount/100))
                f = format(f , '.2f')
                stack[i] = '$' + str(f)

        return(' '.join(stack))