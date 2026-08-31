class Solution:
    def sortStack(self, st):
        if not st:
            return
        
        x = st.pop()
        self.sortStack(st)
        
        self.insertStack(st, x)
        
    def insertStack(self, st, x):
        if not st or st[-1]<=x:
            st.append(x)
            return
        top = st.pop()
        self.insertStack(st, x)
        st.append(top)
