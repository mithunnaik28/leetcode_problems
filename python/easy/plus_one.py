class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number=int("".join(map(str,digits)))
        sum=number+1
        f_list=list(map(int,str(sum)))
        
        return f_list
