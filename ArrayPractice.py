import json
import re


def two_sum():
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    nums, target = [3, 2, 3], 6
    result = []

    dic = {}

    for i in range(len(nums)):
        if abs(target - nums[i]) in dic.keys():
            return result
        else:
            dic.update({nums[i]: i})

    return "No matching pair found"

def extract_num():
    st = "123Shubham456Saxena"
    em = "From: shubham@mail.com Sent At: 22nd July 2024 Sent Time: 3:00 PM"
    lin = """
    X-DS PAM-Confidence: $0.8475
    X-DSPAM-Confidence: $0.8475
    X-DSPAM-Confidence: $0.8476
    X-DSPAM-Confidence: $0.847
    X:DSPAM-Confidence: $0.90000
    Y-DSPAM-Confidence: $0.840000
    X-DSPAM-Confidence: $0.84775
    X-DSPAM-Confidence: $0.84
    """

    for lines in lin.split('\n'):
        print(re.findall('^X-DSPAM-Confidence: (\$[0-9.]+)', lines.lstrip()))

    print(re.findall('\S+@+\S+', em))
    print(re.findall('From.*@([^ ]*)', em))
    ls = re.findall('[A-Z]+[a-z]+', st)
    di = {}

    for names in range(len(ls)):
        if names == 0:
            di.update({"First Name": str(ls[names])})
        else:
            di.update({"Second Name": str(ls[names])})

    print(di)

def word_frequency():
    st, dic = "This is a long string that is very long and this can be used", {}
    st = st.lower().split(' ')

    for words in st:
        dic[words] = dic.get(words, 0) + 1

    sorted_dict = dict(sorted(dic.items(), key=lambda items: items[1], reverse=True))
    print(sorted_dict)
    i = 1

    for key, value in sorted_dict.items():
        print(f"Rank {str(i)} for {str(key)} with frequency {str(value)}")
        i += 1


if __name__ == '__main__':
    word_frequency()