class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        num_str = str(num)
        word = ['', ' Thousand', ' Million', ' Billion']
        one = {
            '0': '',
            '1': ' One',
            '2': ' Two',
            '3': ' Three',
            '4': ' Four',
            '5': ' Five',
            '6': ' Six',
            '7': ' Seven',
            '8': ' Eight',
            '9': ' Nine'
        }
        two = {
            '10': ' Ten',
            '11': ' Eleven',
            '12': ' Twelve',
            '13': ' Thirteen',
            '14': ' Fourteen',
            '15': ' Fifteen',
            '16': ' Sixteen',
            '17': ' Seventeen',
            '18': ' Eighteen',
            '19': ' Nineteen'
        }
        three = {
            '0': '',
            '2': ' Twenty',
            '3': ' Thirty',
            '4': ' Forty',
            '5': ' Fifty',
            '6': ' Sixty',
            '7': ' Seventy',
            '8': ' Eighty',
            '9': ' Ninety'
        }
        sliced = []
        num_str = str(num)[::-1]
        import math
        for i in range(math.ceil(len(str(num_str)) / 3)):
            x = num_str[i * 3:min(i * 3 + 3, len(num_str))]
            sliced.append(x[::-1])
        count = 0
        res = []
        for i in sliced:
            temp = ''
            if len(i) == 3:
                if i[0] != '0':
                    temp += one[i[0]] + ' Hundred'
                if i[1:] in two:
                    temp += two[i[1:]]
                else:
                    temp += three[i[1]] + one[i[2]]
            elif len(i) == 2:
                if i in two:
                    temp += two[i]
                else:
                    temp += three[i[0]] + one[i[1]]
            else:
                temp += one[i[0]]
            if temp:
                temp += word[count]
            count += 1
            res.append(temp)

        return ''.join(res[::-1]).strip()