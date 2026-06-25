class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        
        def seaprate(email):
            local, domain = [], []
            for i,char in enumerate(email):
                if char == "@":
                    local = email[:i]
                    domain = email[i+1:]
            return [local, domain]
        
        for email in emails:
            user = []
            local, domain = seaprate(email)
            
            for i,char in enumerate(local):
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    user.append(char)
                                       
            user.append("@")
            user.append(domain)
            
            fin = ''.join(user)
            res.append(fin)
            
        return len(set(res))
                    
            