class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        else:
            positive = (dividend<0) is (divisor<0)
            dividend = abs(dividend)
            divisor = abs(divisor)
            if divisor ==1:
                qou = dividend 
            else:
                qou = 0 
                while(dividend>=divisor):
                    temp,i=divisor,1 
                    while(dividend>=temp):
                        dividend-=temp
                        qou +=i 
                        i<<=1 
                        temp<<=1 
            if not positive:
                return max(-2147483648,-qou)
            else:
                return min(qou,2147483648)