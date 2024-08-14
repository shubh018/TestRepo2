import csv
import datetime
import gzip
import io
import random

# Data to write
import re
import string

def txtWriter1():
    data = [
        "value1|value2|value3",
        "value4|value5|value6",
        "value7|value8|value9"
    ]

    data1 = []

    zipcodes = ((1,), (2,), (4,), (5,), (6,), (7,), (8,), (9,))
    project_id = "testProject"

    zipcode_retail_store_id_mapping = {}

    with open('/Users/shubhamsaxena/Desktop/sample_cvs_store_ids.txt', 'r') as file:
        file_lines = file.readlines()

    random_values = random.sample(file_lines, len(zipcodes))
    s = io.StringIO()

    for values in range(len(zipcodes)):
        row_to_insert = f"{project_id}|{str(datetime.datetime.now().date())}|{str(random_values[values]).strip()}|{str(zipcodes[values][0])}"
        print(row_to_insert)
        s.write(row_to_insert + '\n')

    # Convert the StringIO buffer to a BytesIO buffer
    buf = io.BytesIO()
    buf.write(s.getvalue().encode())
    buf.name = 'file.txt'
    buf.seek(0)

    # Renaming the taxonomy file
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    filename = "{}_taxonomy.txt".format(random_string)


    # Compressing the txt content to .gz
    compressed_buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed_buffer, mode='wb') as gzipped_file:
        gzipped_file.write(s)

    compressed_buffer.seek(0)
    buf = compressed_buffer.read()

    print(buf)


def txtWrite2():
    zipcodes = ((1,), (2,), (4,), (5,), (6,), (7,), (8,), (9,))
    project_id = "testProject"

    with open('/Users/shubhamsaxena/Desktop/sample_cvs_store_ids.txt', 'r') as file:
        file_lines = file.readlines()

    random_values = random.sample(file_lines, len(zipcodes))
    data = []

    for values in range(len(zipcodes)):
        row_to_insert = f"{project_id}|{str(datetime.datetime.now().date())}|{str(random_values[values]).strip()}|{str(zipcodes[values][0])}"
        data.append(row_to_insert)

    modified_content = '\n'.join(data).encode('utf-8')
    print(modified_content)
    compressed_buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed_buffer, mode='wb') as gzipped_file:
        gzipped_file.write(modified_content)

    compressed_buffer.seek(0)
    buf = compressed_buffer.read()

    print(buf)


if __name__ == '__main__':
    txtWrite2()
    st = "qa-auto-user_v7r9@guerrillamailblock.com"
    print(st[:st.find('@')])

    t1 = (("st01", "st02", 20, "01","p1",), ("st11", "st12", 21, "11","p2",), ("st21", "st22", 22, "21","p3",), ("st31", "st32", 32, "31","p4",))
    t2 = {"st01": {"project_id": "p1", "zipcode": "st02", "vaccinations": 20},
          "st11": {"project_id": "p2", "zipcode": "st12", "vaccinations": 21},
          "st21": {"project_id": "p3", "zipcode": "st22", "vaccinations": 22},
          "st31": {"project_id": "p4", "zipcode": "st32", "vaccinations": 32}}

    if len(t1) != len(t2):
        print("Not Equal")

    st = set()

    for values in t1:
        st.update(values)

    for key, value in t2.items():
        for values in t1:
            if values[0] == key:
                print(key, value, values)


    st = '90034'
    print(','.join([st[:4]+str(random.randint(0, 9)) for i in range(6)]))

