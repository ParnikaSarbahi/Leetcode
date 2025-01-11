class Solution(object):
    def is_ss(self, sub, s):
        for i in range(len(sub)):
            if sub.count(sub[i]) > s.count(sub[i]):
                return False
        return True
    def wordSubsets(self, words1, words2):
        ret = []
        s = ""
        d = {}
        for i in words2:
            for j in range(len(i)):
                if i[j] in d:
                    d[i[j]] = max(d[i[j]], i.count(i[j]))
                else:
                    d[i[j]] = i.count(i[j])
        for i in d.keys():
            s+=i*d[i]
        for i in words1:
            if self.is_ss(s, i)==False:
                continue
            else:
                ret.append(i)
        return ret
