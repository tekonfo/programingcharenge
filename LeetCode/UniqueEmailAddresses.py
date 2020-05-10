from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        lists = []
        for email in emails:
            local_name, domain = email.split('@')
            local_name = local_name.replace('.', '')
            tmps = local_name.split('+')
            if len(tmps) > 1:
                tmps = tmps[0]
            local_name = ''.join(tmps)
            lists.append('@'.join([local_name, domain]))
        s = set(lists)
        return len(s)

sol = Solution()
emails = ["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com",
            "r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com",
            "fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com",
            "r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com",
            "r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com",
            "fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]
print(sol.numUniqueEmails(emails))

"""
{'rcyoglcng@tgsg.z.com', 'rcyogdrku@tgsg.z.com', 'rcyogng@tgsg.z.com', 'fgruuzj@kziczvh.com', 'fgruuzjb@kziczvh.com', 'rcyog@tgsg.z.com', 'rcyogdcft@tgsg.z.com', 'fgruuzjpj@kziczvh.com', 'rcyogbja@tgsg.z.com', 'rcyogtyli@tgsg.z.com'}
"""