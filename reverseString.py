class reverseString(object):
    def reverseString(self,str):
        rever_str = str[::-1]
        return rever_str

    def reverseString1(self,str):
        stri = list(str)
        print(stri)
        stri.reverse()
        print(stri)
        return "".join(stri)


str = "hello"
i = reverseString()
print(i.reverseString1(str))