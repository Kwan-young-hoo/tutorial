# coding=utf-8


from urllib.request import urlopen

import pandas as pd

import json

import sqlite3


def lotto(chasu):
    url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=" + str(chasu)

    result_data = urlopen(url)

    result = result_data.read()

    data = json.loads(result)

    print(data)

    data_1 = pd.DataFrame.from_dict(data, orient='index')

    data_1 = data_1.transpose()

    return data_1


if __name__ == "__main__":

    for i in range(1, 818):
        data_1 = lotto(i)

        con = sqlite3.connect("d:/myprojects/tutorial/lotto.db")

        data_1.to_sql('lent', con, if_exists='append', index=False)

        con.close()
