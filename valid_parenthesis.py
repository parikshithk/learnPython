class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list(s)
        # print(brackets)
        mapper = []
        for i in brackets:
            if i == '(' or i == '{' or i == '[':
                mapper.append(i)
                # print(mapper)
            if not mapper:
                return False
            if i == ')':
                if mapper[len(mapper) - 1] == '(':
                    mapper.pop()
                    # print(mapper)
                else:
                    return False
            if i == '}':
                if mapper[len(mapper) - 1] == '{':
                    mapper.pop()
                    # print(mapper)
                else:
                    return False
            if i == ']':
                if mapper[len(mapper) - 1] == '[':
                    mapper.pop()
                    # print(mapper)
                else:
                    return False
        if not mapper:
            return True
        return False


if __name__ == '__main__':
    input_str = input()
    soln = Solution()
    print(soln.isValid(input_str))
