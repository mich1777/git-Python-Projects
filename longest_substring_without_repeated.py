class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = []
        k = []
        if s=="":
            return 0
        else:
            end = 0
            start = 0
            k.append(s[0])
            for i in range(len(s)-1):
                temp = len(k)
                tempstart = start
                for j in range(len(k)):               
                    if j == 0:
                        k=[]
                    k.append(s[tempstart+j])
                    if s[tempstaj] == s[i+1]:
                        h.append(end-start+1)
                        start = start + j+1
                        k=[]
                    if j+1 == temp:
                            k.append(s[i+1])
                            end += 1
                if i+1 == len(s)-1:
                    h.append(end-start+1)
            if len(s) != 1:
                return max(h)
            else:
                return 1
"""
        h = []
        if s=="":
            return 0
        else:
            end = 0
            start = 0
            for i in range(len(s)-1):
                for j in range(i+1):
                    if j >= start:
                        if s[j] == s[i+1]:
                            h.append(end-start+1)
                            end = i+1
                            start = j+1
                            break
                        if j+1 == i+1:
                            end += 1
                if i+1 == len(s)-1:
                    h.append(end-start+1)
            if len(s) != 1:
                return max(h)
            else:
                return 1
"""
"""
                
        for i in range(len(s)):
            if s[i] == s[h]:
                for j in range(len(s)-i):
                    if s[j] == s[j+1]:
                        k.append(j+1)
                        h = j+1
                        break
        return max()
"""

        
"""
        k = []
        h = 0
        for i in range(len(s)):
            if s[i] == s[h]:
                for j in range(len(s)-i):
                    if s[j] == s[j+1]:
                        k.append(j+1)
                        h = j+1
                        break
        return max(k)
"""      
        
        
"""        
        k = []
        h = 0
        for i in range(len(s)):
            k.append(1)
            
        for i in range(len(s)):
            if k[i] != 0:
                h += 1
                for j in range(len(s)):
                    if s[i] == s[j]:
                        k[j] = 0
        return h
"""
                
