class Solution:
    def infixToPostfix(self, s):
        st = []
        res = ""

        def precedence(ch):
            if ch == '^':
                return 3
            if ch == '*' or ch == '/':
                return 2
            if ch == '+' or ch == '-':
                return 1
            return 0

        for ch in s:
            if ch.isalnum():
                res += ch

            elif ch == '(':
                st.append(ch)

            elif ch == ')':
                while st and st[-1] != '(':
                    res += st.pop()
                st.pop()

            else:
                while st and st[-1] != '(':
                    top = st[-1]

                    if precedence(top) > precedence(ch):
                        res += st.pop()

                    elif precedence(top) == precedence(ch) and ch != '^':
                        res += st.pop()

                    else:
                        break

                st.append(ch)

        while st:
            res += st.pop()

        return res