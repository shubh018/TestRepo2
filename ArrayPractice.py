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


if __name__ == '__main__':
    extract_num()
    result_dict = {'55DFF9E8F4845A11316849EC74C01D30A387D6D0170F3DBBFAFE7E22CA7A21FF': {'project_id': 'QA_88941', 'zipcode': '61857', 'vaccinations': '7'}, 'A04F132C7C93DF8B0D896A5334FD89AD933EA7747FF70CBB940722E9359A2235': {'project_id': 'QA_88941', 'zipcode': '12769', 'vaccinations': '14'}, '4BC5B5C0C74BADFFCC7ACB902A9CD02C36153AF2EDB617E7B3726EE00FC5263C': {'project_id': 'QA_88941', 'zipcode': '48302', 'vaccinations': '7'}, '8952115444BAB6DE66AAB97501F75FEE64BE3448203A91B47818E5E8943E0DFB': {'project_id': 'QA_88941', 'zipcode': '85345', 'vaccinations': '8'}, 'B2B20C1ABF5B17B6123C17DD1BC13317CDF37F2319D7412CEC095A55026B412B': {'project_id': 'QA_88941', 'zipcode': '37219', 'vaccinations': '7'}, 'D886A46E106FE104CAF1946FD74A365B5042F595E749B23FC70A64506EDFFEA1': {'project_id': 'QA_88941', 'zipcode': '46705', 'vaccinations': '8'}, '9A3B84136CAE8F86009596DF91507EE5F5C54708CF7B79E374C17C3ECA2E519F': {'project_id': 'QA_88941', 'zipcode': '25986', 'vaccinations': '7'}, '6C77B607E17DF16D31C46C746A36328056FC8D153B71370ED1A56D4C0700238E': {'project_id': 'QA_88941', 'zipcode': '97333', 'vaccinations': '13'}, '9A0251AB1BCA1C475E9E05274B1ADC553D9D740683FCC4FC70C8BB276B693903': {'project_id': 'QA_88941', 'zipcode': '78280', 'vaccinations': '14'}, '036104E933AA516031C91B8D952049919CFA9E643E89AAEBD5738131FD17401A': {'project_id': 'QA_88941', 'zipcode': '61077', 'vaccinations': '15'}, '498F5FBC64890CF8DAF0EF093AAE639099C5D66838BCE24498C4903D186957B8': {'project_id': 'QA_88941', 'zipcode': '56534', 'vaccinations': '14'}, '4A6AB875ABEE1175898CE32B79CF79BB1D0340ECE68FA41D7FA1D57D6ED9674B': {'project_id': 'QA_88941', 'zipcode': '48856', 'vaccinations': '6'}, '103006A34E0C5359768743A0C287540CA14E9736CD525FA8EA11E69BC2963EE5': {'project_id': 'QA_88941', 'zipcode': '21162', 'vaccinations': '10'}, 'DF5CEA5E17E7D2AB5FF7876B8DBF90D5CE17A6B24C2039E37224AAA42DB37680': {'project_id': 'QA_88941', 'zipcode': '29422', 'vaccinations': '5'}, 'DAD1574B7F03CA4AAEB45EF8BC5A4F91F0E0FA9A9610EC0FF4023B3DAB615606': {'project_id': 'QA_88941', 'zipcode': '75070', 'vaccinations': '6'}, 'A8D2DE097F81898AB845FE546637A1807C72DDA813F3E80C61BAA3F94DA5CF14': {'project_id': 'QA_88941', 'zipcode': '07604', 'vaccinations': '6'}, '034EBA25ACCE2BE026B3C885B80C4DFF16F6CB3842E63D8E32B9968B9CD7B1EE': {'project_id': 'QA_88941', 'zipcode': '32084', 'vaccinations': '11'}, '02BCFC94730ED9A7DE595073CE24F02D72B240D915D2C517F8C40A56B679F4C3': {'project_id': 'QA_88941', 'zipcode': '32202', 'vaccinations': '13'}, 'EC1A874203C55517F71DFE34BA86744FB41138693A65832B20CFA6F533F75E09': {'project_id': 'QA_88941', 'zipcode': '36360', 'vaccinations': '11'}, '7FB8A56336E161678D48FEE87EE481F9AFDA126E6EE86D139BBB9D23E9FED2D3': {'project_id': 'QA_88941', 'zipcode': '54636', 'vaccinations': '13'}}

    zipcodes_data = [(value['zipcode'],) for key, value in result_dict.items()]
    print(zipcodes_data)

    for values in range(len(zipcodes_data)):
        # Preparing Values
        store_zipcode = str(zipcodes_data[values][0])
        print(store_zipcode)

    print(len(zipcodes_data))