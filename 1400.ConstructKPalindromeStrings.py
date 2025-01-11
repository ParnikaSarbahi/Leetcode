class Solution(object):
    def canConstruct(self, s, k):
        l=list(set(list(s)))
        c=0
        for i in l:
            if s.count(i)%2!=0:
                c+=1
        if c<=k and len(s)>=k:
            return True
        else:
            return False
