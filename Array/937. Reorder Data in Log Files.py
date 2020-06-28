class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if not logs:
            return []
        letter_list = []
        digit_list = []
        for log in logs:
            if log[-1].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)

        letter_list.sort(key=lambda x: x[len(x.split(' ')[0]):] + x.split(' ')[0])
        return letter_list + digit_list