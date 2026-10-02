class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtracks(s, open_count, close_count):
            if len(s) == 2*n:
                result.append(s)
                return 
            
            if open_count < n:
                backtracks(s+ "(", open_count+1, close_count)
            
            if close_count<open_count:
                backtracks(s+ ")", open_count, close_count+1)
        backtracks("",0,0)
        return result