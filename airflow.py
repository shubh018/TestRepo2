import json

# The value obtained
value = 631665.1245

# Calculate ±15%
lower_bound = value - (0.15 * value)
upper_bound = value + (0.15 * value)

# Sample JSON data (replace this with your actual JSON)
json_data = '''[
    {
        "threshold": 0,
        "percentile sum": 792279,
        "cumulative sum": 691457184
    },
    {
        "threshold": 0.0001,
        "percentile sum": 7279355,
        "cumulative sum": 690664905
    },
    {
        "threshold": 0.0002,
        "percentile sum": 14521142,
        "cumulative sum": 683385550
    },
    {
        "threshold": 0.0003,
        "percentile sum": 18597373,
        "cumulative sum": 668864408
    },
    {
        "threshold": 0.0004,
        "percentile sum": 20280987,
        "cumulative sum": 650267035
    },
    {
        "threshold": 0.0005,
        "percentile sum": 20671038,
        "cumulative sum": 629986048
    },
    {
        "threshold": 0.0006,
        "percentile sum": 20485197,
        "cumulative sum": 609315010
    },
    {
        "threshold": 0.0007,
        "percentile sum": 20123095,
        "cumulative sum": 588829813
    },
    {
        "threshold": 0.0008,
        "percentile sum": 19662478,
        "cumulative sum": 568706718
    },
    {
        "threshold": 0.0009,
        "percentile sum": 19117272,
        "cumulative sum": 549044240
    },
    {
        "threshold": 0.001,
        "percentile sum": 18587978,
        "cumulative sum": 529926968
    },
    {
        "threshold": 0.0011,
        "percentile sum": 17988357,
        "cumulative sum": 511338990
    },
    {
        "threshold": 0.0012,
        "percentile sum": 17266056,
        "cumulative sum": 493350633
    },
    {
        "threshold": 0.0013,
        "percentile sum": 16612881,
        "cumulative sum": 476084577
    },
    {
        "threshold": 0.0014,
        "percentile sum": 15994366,
        "cumulative sum": 459471696
    },
    {
        "threshold": 0.0015,
        "percentile sum": 15417737,
        "cumulative sum": 443477330
    },
    {
        "threshold": 0.0016,
        "percentile sum": 14862091,
        "cumulative sum": 428059593
    },
    {
        "threshold": 0.0017,
        "percentile sum": 14329704,
        "cumulative sum": 413197502
    },
    {
        "threshold": 0.0018,
        "percentile sum": 13814981,
        "cumulative sum": 398867798
    },
    {
        "threshold": 0.0019,
        "percentile sum": 13293125,
        "cumulative sum": 385052817
    },
    {
        "threshold": 0.002,
        "percentile sum": 12807724,
        "cumulative sum": 371759692
    },
    {
        "threshold": 0.0021,
        "percentile sum": 12357725,
        "cumulative sum": 358951968
    },
    {
        "threshold": 0.0022,
        "percentile sum": 11928191,
        "cumulative sum": 346594243
    },
    {
        "threshold": 0.0023,
        "percentile sum": 11524121,
        "cumulative sum": 334666052
    },
    {
        "threshold": 0.0024,
        "percentile sum": 11101865,
        "cumulative sum": 323141931
    },
    {
        "threshold": 0.0025,
        "percentile sum": 10685716,
        "cumulative sum": 312040066
    },
    {
        "threshold": 0.0026,
        "percentile sum": 10298042,
        "cumulative sum": 301354350
    },
    {
        "threshold": 0.0027,
        "percentile sum": 9935972,
        "cumulative sum": 291056308
    },
    {
        "threshold": 0.0028,
        "percentile sum": 9582663,
        "cumulative sum": 281120336
    },
    {
        "threshold": 0.0029,
        "percentile sum": 9283363,
        "cumulative sum": 271537673
    },
    {
        "threshold": 0.003,
        "percentile sum": 9025469,
        "cumulative sum": 262254310
    },
    {
        "threshold": 0.0031,
        "percentile sum": 8777323,
        "cumulative sum": 253228841
    },
    {
        "threshold": 0.0032,
        "percentile sum": 8701125,
        "cumulative sum": 244451518
    },
    {
        "threshold": 0.0033,
        "percentile sum": 9388270,
        "cumulative sum": 235750393
    },
    {
        "threshold": 0.0034,
        "percentile sum": 7716704,
        "cumulative sum": 226362123
    },
    {
        "threshold": 0.0035,
        "percentile sum": 7334772,
        "cumulative sum": 218645419
    },
    {
        "threshold": 0.0036,
        "percentile sum": 7012681,
        "cumulative sum": 211310647
    },
    {
        "threshold": 0.0037,
        "percentile sum": 6718720,
        "cumulative sum": 204297966
    },
    {
        "threshold": 0.0038,
        "percentile sum": 6452578,
        "cumulative sum": 197579246
    },
    {
        "threshold": 0.0039,
        "percentile sum": 6188518,
        "cumulative sum": 191126668
    },
    {
        "threshold": 0.004,
        "percentile sum": 5916610,
        "cumulative sum": 184938150
    },
    {
        "threshold": 0.0041,
        "percentile sum": 5682533,
        "cumulative sum": 179021540
    },
    {
        "threshold": 0.0042,
        "percentile sum": 5463161,
        "cumulative sum": 173339007
    },
    {
        "threshold": 0.0043,
        "percentile sum": 5250228,
        "cumulative sum": 167875846
    },
    {
        "threshold": 0.0044,
        "percentile sum": 5045999,
        "cumulative sum": 162625618
    },
    {
        "threshold": 0.0045,
        "percentile sum": 4854988,
        "cumulative sum": 157579619
    },
    {
        "threshold": 0.0046,
        "percentile sum": 4678894,
        "cumulative sum": 152724631
    },
    {
        "threshold": 0.0047,
        "percentile sum": 4506129,
        "cumulative sum": 148045737
    },
    {
        "threshold": 0.0048,
        "percentile sum": 4342414,
        "cumulative sum": 143539608
    },
    {
        "threshold": 0.0049,
        "percentile sum": 4187361,
        "cumulative sum": 139197194
    },
    {
        "threshold": 0.005,
        "percentile sum": 4043514,
        "cumulative sum": 135009833
    },
    {
        "threshold": 0.0051,
        "percentile sum": 3894522,
        "cumulative sum": 130966319
    },
    {
        "threshold": 0.0052,
        "percentile sum": 3761413,
        "cumulative sum": 127071797
    },
    {
        "threshold": 0.0053,
        "percentile sum": 3635313,
        "cumulative sum": 123310384
    },
    {
        "threshold": 0.0054,
        "percentile sum": 3515050,
        "cumulative sum": 119675071
    },
    {
        "threshold": 0.0055,
        "percentile sum": 3394841,
        "cumulative sum": 116160021
    },
    {
        "threshold": 0.0056,
        "percentile sum": 3285769,
        "cumulative sum": 112765180
    },
    {
        "threshold": 0.0057,
        "percentile sum": 3182392,
        "cumulative sum": 109479411
    },
    {
        "threshold": 0.0058,
        "percentile sum": 3074439,
        "cumulative sum": 106297019
    },
    {
        "threshold": 0.0059,
        "percentile sum": 2983476,
        "cumulative sum": 103222580
    },
    {
        "threshold": 0.006,
        "percentile sum": 2900988,
        "cumulative sum": 100239104
    },
    {
        "threshold": 0.0061,
        "percentile sum": 2788997,
        "cumulative sum": 97338116
    },
    {
        "threshold": 0.0062,
        "percentile sum": 2714374,
        "cumulative sum": 94549119
    },
    {
        "threshold": 0.0063,
        "percentile sum": 2604155,
        "cumulative sum": 91834745
    },
    {
        "threshold": 0.0064,
        "percentile sum": 2524263,
        "cumulative sum": 89230590
    },
    {
        "threshold": 0.0065,
        "percentile sum": 2455618,
        "cumulative sum": 86706327
    },
    {
        "threshold": 0.0066,
        "percentile sum": 2353545,
        "cumulative sum": 84250709
    },
    {
        "threshold": 0.0067,
        "percentile sum": 2316738,
        "cumulative sum": 81897164
    },
    {
        "threshold": 0.0068,
        "percentile sum": 2197915,
        "cumulative sum": 79580426
    },
    {
        "threshold": 0.0069,
        "percentile sum": 2129521,
        "cumulative sum": 77382511
    },
    {
        "threshold": 0.007,
        "percentile sum": 2062975,
        "cumulative sum": 75252990
    },
    {
        "threshold": 0.0071,
        "percentile sum": 1994376,
        "cumulative sum": 73190015
    },
    {
        "threshold": 0.0072,
        "percentile sum": 1934752,
        "cumulative sum": 71195639
    },
    {
        "threshold": 0.0073,
        "percentile sum": 1873175,
        "cumulative sum": 69260887
    },
    {
        "threshold": 0.0074,
        "percentile sum": 1810572,
        "cumulative sum": 67387712
    },
    {
        "threshold": 0.0075,
        "percentile sum": 1758512,
        "cumulative sum": 65577140
    },
    {
        "threshold": 0.0076,
        "percentile sum": 1707017,
        "cumulative sum": 63818628
    },
    {
        "threshold": 0.0077,
        "percentile sum": 1648965,
        "cumulative sum": 62111611
    },
    {
        "threshold": 0.0078,
        "percentile sum": 1604742,
        "cumulative sum": 60462646
    },
    {
        "threshold": 0.0079,
        "percentile sum": 1552466,
        "cumulative sum": 58857904
    },
    {
        "threshold": 0.008,
        "percentile sum": 1505052,
        "cumulative sum": 57305438
    },
    {
        "threshold": 0.0081,
        "percentile sum": 1462586,
        "cumulative sum": 55800386
    },
    {
        "threshold": 0.0082,
        "percentile sum": 1418126,
        "cumulative sum": 54337800
    },
    {
        "threshold": 0.0083,
        "percentile sum": 1375709,
        "cumulative sum": 52919674
    },
    {
        "threshold": 0.0084,
        "percentile sum": 1332348,
        "cumulative sum": 51543965
    },
    {
        "threshold": 0.0085,
        "percentile sum": 1297166,
        "cumulative sum": 50211617
    },
    {
        "threshold": 0.0086,
        "percentile sum": 1254459,
        "cumulative sum": 48914451
    },
    {
        "threshold": 0.0087,
        "percentile sum": 1214908,
        "cumulative sum": 47659992
    },
    {
        "threshold": 0.0088,
        "percentile sum": 1177599,
        "cumulative sum": 46445084
    },
    {
        "threshold": 0.0089,
        "percentile sum": 1141678,
        "cumulative sum": 45267485
    },
    {
        "threshold": 0.009,
        "percentile sum": 1112537,
        "cumulative sum": 44125807
    },
    {
        "threshold": 0.0091,
        "percentile sum": 1076942,
        "cumulative sum": 43013270
    },
    {
        "threshold": 0.0092,
        "percentile sum": 1046715,
        "cumulative sum": 41936328
    },
    {
        "threshold": 0.0093,
        "percentile sum": 1015495,
        "cumulative sum": 40889613
    },
    {
        "threshold": 0.0094,
        "percentile sum": 983444,
        "cumulative sum": 39874118
    },
    {
        "threshold": 0.0095,
        "percentile sum": 956103,
        "cumulative sum": 38890674
    },
    {
        "threshold": 0.0096,
        "percentile sum": 929159,
        "cumulative sum": 37934571
    },
    {
        "threshold": 0.0097,
        "percentile sum": 901061,
        "cumulative sum": 37005412
    },
    {
        "threshold": 0.0098,
        "percentile sum": 875232,
        "cumulative sum": 36104351
    },
    {
        "threshold": 0.0099,
        "percentile sum": 850193,
        "cumulative sum": 35229119
    },
    {
        "threshold": 0.01,
        "percentile sum": 827935,
        "cumulative sum": 34378926
    },
    {
        "threshold": 0.0101,
        "percentile sum": 803567,
        "cumulative sum": 33550991
    },
    {
        "threshold": 0.0102,
        "percentile sum": 780330,
        "cumulative sum": 32747424
    },
    {
        "threshold": 0.0103,
        "percentile sum": 756562,
        "cumulative sum": 31967094
    },
    {
        "threshold": 0.0104,
        "percentile sum": 736168,
        "cumulative sum": 31210532
    },
    {
        "threshold": 0.0105,
        "percentile sum": 718910,
        "cumulative sum": 30474364
    },
    {
        "threshold": 0.0106,
        "percentile sum": 693919,
        "cumulative sum": 29755454
    },
    {
        "threshold": 0.0107,
        "percentile sum": 678567,
        "cumulative sum": 29061535
    },
    {
        "threshold": 0.0108,
        "percentile sum": 656974,
        "cumulative sum": 28382968
    },
    {
        "threshold": 0.0109,
        "percentile sum": 640368,
        "cumulative sum": 27725994
    },
    {
        "threshold": 0.011,
        "percentile sum": 622646,
        "cumulative sum": 27085626
    },
    {
        "threshold": 0.0111,
        "percentile sum": 605339,
        "cumulative sum": 26462980
    },
    {
        "threshold": 0.0112,
        "percentile sum": 587677,
        "cumulative sum": 25857641
    },
    {
        "threshold": 0.0113,
        "percentile sum": 571468,
        "cumulative sum": 25269964
    },
    {
        "threshold": 0.0114,
        "percentile sum": 555604,
        "cumulative sum": 24698496
    },
    {
        "threshold": 0.0115,
        "percentile sum": 542297,
        "cumulative sum": 24142892
    },
    {
        "threshold": 0.0116,
        "percentile sum": 527712,
        "cumulative sum": 23600595
    },
    {
        "threshold": 0.0117,
        "percentile sum": 513339,
        "cumulative sum": 23072883
    },
    {
        "threshold": 0.0118,
        "percentile sum": 500497,
        "cumulative sum": 22559544
    },
    {
        "threshold": 0.0119,
        "percentile sum": 486839,
        "cumulative sum": 22059047
    },
    {
        "threshold": 0.012,
        "percentile sum": 473995,
        "cumulative sum": 21572208
    },
    {
        "threshold": 0.0121,
        "percentile sum": 460806,
        "cumulative sum": 21098213
    },
    {
        "threshold": 0.0122,
        "percentile sum": 447493,
        "cumulative sum": 20637407
    },
    {
        "threshold": 0.0123,
        "percentile sum": 435865,
        "cumulative sum": 20189914
    },
    {
        "threshold": 0.0124,
        "percentile sum": 425172,
        "cumulative sum": 19754049
    },
    {
        "threshold": 0.0125,
        "percentile sum": 412323,
        "cumulative sum": 19328877
    },
    {
        "threshold": 0.0126,
        "percentile sum": 403415,
        "cumulative sum": 18916554
    },
    {
        "threshold": 0.0127,
        "percentile sum": 394390,
        "cumulative sum": 18513139
    },
    {
        "threshold": 0.0128,
        "percentile sum": 382360,
        "cumulative sum": 18118749
    },
    {
        "threshold": 0.0129,
        "percentile sum": 372710,
        "cumulative sum": 17736389
    },
    {
        "threshold": 0.013,
        "percentile sum": 363067,
        "cumulative sum": 17363679
    },
    {
        "threshold": 0.0131,
        "percentile sum": 354122,
        "cumulative sum": 17000612
    },
    {
        "threshold": 0.0132,
        "percentile sum": 346129,
        "cumulative sum": 16646490
    },
    {
        "threshold": 0.0133,
        "percentile sum": 337835,
        "cumulative sum": 16300361
    },
    {
        "threshold": 0.0134,
        "percentile sum": 328108,
        "cumulative sum": 15962526
    },
    {
        "threshold": 0.0135,
        "percentile sum": 320416,
        "cumulative sum": 15634418
    },
    {
        "threshold": 0.0136,
        "percentile sum": 312472,
        "cumulative sum": 15314002
    },
    {
        "threshold": 0.0137,
        "percentile sum": 304806,
        "cumulative sum": 15001530
    },
    {
        "threshold": 0.0138,
        "percentile sum": 297521,
        "cumulative sum": 14696724
    },
    {
        "threshold": 0.0139,
        "percentile sum": 290011,
        "cumulative sum": 14399203
    },
    {
        "threshold": 0.014,
        "percentile sum": 282662,
        "cumulative sum": 14109192
    },
    {
        "threshold": 0.0141,
        "percentile sum": 276177,
        "cumulative sum": 13826530
    },
    {
        "threshold": 0.0142,
        "percentile sum": 268844,
        "cumulative sum": 13550353
    },
    {
        "threshold": 0.0143,
        "percentile sum": 263296,
        "cumulative sum": 13281509
    },
    {
        "threshold": 0.0144,
        "percentile sum": 256058,
        "cumulative sum": 13018213
    },
    {
        "threshold": 0.0145,
        "percentile sum": 249561,
        "cumulative sum": 12762155
    },
    {
        "threshold": 0.0146,
        "percentile sum": 245117,
        "cumulative sum": 12512594
    },
    {
        "threshold": 0.0147,
        "percentile sum": 239110,
        "cumulative sum": 12267477
    },
    {
        "threshold": 0.0148,
        "percentile sum": 231926,
        "cumulative sum": 12028367
    },
    {
        "threshold": 0.0149,
        "percentile sum": 227786,
        "cumulative sum": 11796441
    },
    {
        "threshold": 0.015,
        "percentile sum": 222797,
        "cumulative sum": 11568655
    },
    {
        "threshold": 0.0151,
        "percentile sum": 216396,
        "cumulative sum": 11345858
    },
    {
        "threshold": 0.0152,
        "percentile sum": 213318,
        "cumulative sum": 11129462
    },
    {
        "threshold": 0.0153,
        "percentile sum": 206131,
        "cumulative sum": 10916144
    },
    {
        "threshold": 0.0154,
        "percentile sum": 203890,
        "cumulative sum": 10710013
    },
    {
        "threshold": 0.0155,
        "percentile sum": 197894,
        "cumulative sum": 10506123
    },
    {
        "threshold": 0.0156,
        "percentile sum": 192478,
        "cumulative sum": 10308229
    },
    {
        "threshold": 0.0157,
        "percentile sum": 187662,
        "cumulative sum": 10115751
    },
    {
        "threshold": 0.0158,
        "percentile sum": 184410,
        "cumulative sum": 9928089
    },
    {
        "threshold": 0.0159,
        "percentile sum": 180386,
        "cumulative sum": 9743679
    },
    {
        "threshold": 0.016,
        "percentile sum": 175944,
        "cumulative sum": 9563293
    },
    {
        "threshold": 0.0161,
        "percentile sum": 172235,
        "cumulative sum": 9387349
    },
    {
        "threshold": 0.0162,
        "percentile sum": 169139,
        "cumulative sum": 9215114
    },
    {
        "threshold": 0.0163,
        "percentile sum": 164525,
        "cumulative sum": 9045975
    },
    {
        "threshold": 0.0164,
        "percentile sum": 161367,
        "cumulative sum": 8881450
    },
    {
        "threshold": 0.0165,
        "percentile sum": 156824,
        "cumulative sum": 8720083
    },
    {
        "threshold": 0.0166,
        "percentile sum": 154243,
        "cumulative sum": 8563259
    },
    {
        "threshold": 0.0167,
        "percentile sum": 149916,
        "cumulative sum": 8409016
    },
    {
        "threshold": 0.0168,
        "percentile sum": 148062,
        "cumulative sum": 8259100
    },
    {
        "threshold": 0.0169,
        "percentile sum": 144828,
        "cumulative sum": 8111038
    },
    {
        "threshold": 0.017,
        "percentile sum": 140904,
        "cumulative sum": 7966210
    },
    {
        "threshold": 0.0171,
        "percentile sum": 137836,
        "cumulative sum": 7825306
    },
    {
        "threshold": 0.0172,
        "percentile sum": 136291,
        "cumulative sum": 7687470
    },
    {
        "threshold": 0.0173,
        "percentile sum": 131738,
        "cumulative sum": 7551179
    },
    {
        "threshold": 0.0174,
        "percentile sum": 129726,
        "cumulative sum": 7419441
    },
    {
        "threshold": 0.0175,
        "percentile sum": 125034,
        "cumulative sum": 7289715
    },
    {
        "threshold": 0.0176,
        "percentile sum": 123663,
        "cumulative sum": 7164681
    },
    {
        "threshold": 0.0177,
        "percentile sum": 121058,
        "cumulative sum": 7041018
    },
    {
        "threshold": 0.0178,
        "percentile sum": 118531,
        "cumulative sum": 6919960
    },
    {
        "threshold": 0.0179,
        "percentile sum": 117263,
        "cumulative sum": 6801429
    },
    {
        "threshold": 0.018,
        "percentile sum": 114215,
        "cumulative sum": 6684166
    },
    {
        "threshold": 0.0181,
        "percentile sum": 110978,
        "cumulative sum": 6569951
    },
    {
        "threshold": 0.0182,
        "percentile sum": 109193,
        "cumulative sum": 6458973
    },
    {
        "threshold": 0.0183,
        "percentile sum": 106999,
        "cumulative sum": 6349780
    },
    {
        "threshold": 0.0184,
        "percentile sum": 104175,
        "cumulative sum": 6242781
    },
    {
        "threshold": 0.0185,
        "percentile sum": 102986,
        "cumulative sum": 6138606
    },
    {
        "threshold": 0.0186,
        "percentile sum": 100246,
        "cumulative sum": 6035620
    },
    {
        "threshold": 0.0187,
        "percentile sum": 98808,
        "cumulative sum": 5935374
    },
    {
        "threshold": 0.0188,
        "percentile sum": 95770,
        "cumulative sum": 5836566
    },
    {
        "threshold": 0.0189,
        "percentile sum": 93668,
        "cumulative sum": 5740796
    },
    {
        "threshold": 0.019,
        "percentile sum": 91621,
        "cumulative sum": 5647128
    },
    {
        "threshold": 0.0191,
        "percentile sum": 91054,
        "cumulative sum": 5555507
    },
    {
        "threshold": 0.0192,
        "percentile sum": 89061,
        "cumulative sum": 5464453
    },
    {
        "threshold": 0.0193,
        "percentile sum": 87407,
        "cumulative sum": 5375392
    },
    {
        "threshold": 0.0194,
        "percentile sum": 85961,
        "cumulative sum": 5287985
    },
    {
        "threshold": 0.0195,
        "percentile sum": 83554,
        "cumulative sum": 5202024
    },
    {
        "threshold": 0.0196,
        "percentile sum": 81876,
        "cumulative sum": 5118470
    },
    {
        "threshold": 0.0197,
        "percentile sum": 80650,
        "cumulative sum": 5036594
    },
    {
        "threshold": 0.0198,
        "percentile sum": 78793,
        "cumulative sum": 4955944
    },
    {
        "threshold": 0.0199,
        "percentile sum": 77129,
        "cumulative sum": 4877151
    },
    {
        "threshold": 0.02,
        "percentile sum": 75973,
        "cumulative sum": 4800022
    },
    {
        "threshold": 0.0201,
        "percentile sum": 74691,
        "cumulative sum": 4724049
    },
    {
        "threshold": 0.0202,
        "percentile sum": 72790,
        "cumulative sum": 4649358
    },
    {
        "threshold": 0.0203,
        "percentile sum": 71327,
        "cumulative sum": 4576568
    },
    {
        "threshold": 0.0204,
        "percentile sum": 69867,
        "cumulative sum": 4505241
    },
    {
        "threshold": 0.0205,
        "percentile sum": 68585,
        "cumulative sum": 4435374
    },
    {
        "threshold": 0.0206,
        "percentile sum": 67599,
        "cumulative sum": 4366789
    },
    {
        "threshold": 0.0207,
        "percentile sum": 66248,
        "cumulative sum": 4299190
    },
    {
        "threshold": 0.0208,
        "percentile sum": 64624,
        "cumulative sum": 4232942
    },
    {
        "threshold": 0.0209,
        "percentile sum": 64478,
        "cumulative sum": 4168318
    },
    {
        "threshold": 0.021,
        "percentile sum": 62930,
        "cumulative sum": 4103840
    },
    {
        "threshold": 0.0211,
        "percentile sum": 60992,
        "cumulative sum": 4040910
    },
    {
        "threshold": 0.0212,
        "percentile sum": 59440,
        "cumulative sum": 3979918
    },
    {
        "threshold": 0.0213,
        "percentile sum": 58778,
        "cumulative sum": 3920478
    },
    {
        "threshold": 0.0214,
        "percentile sum": 57999,
        "cumulative sum": 3861700
    },
    {
        "threshold": 0.0215,
        "percentile sum": 56442,
        "cumulative sum": 3803701
    },
    {
        "threshold": 0.0216,
        "percentile sum": 55247,
        "cumulative sum": 3747259
    },
    {
        "threshold": 0.0217,
        "percentile sum": 55110,
        "cumulative sum": 3692012
    },
    {
        "threshold": 0.0218,
        "percentile sum": 53350,
        "cumulative sum": 3636902
    },
    {
        "threshold": 0.0219,
        "percentile sum": 53176,
        "cumulative sum": 3583552
    },
    {
        "threshold": 0.022,
        "percentile sum": 52015,
        "cumulative sum": 3530376
    },
    {
        "threshold": 0.0221,
        "percentile sum": 50776,
        "cumulative sum": 3478361
    },
    {
        "threshold": 0.0222,
        "percentile sum": 50078,
        "cumulative sum": 3427585
    },
    {
        "threshold": 0.0223,
        "percentile sum": 49477,
        "cumulative sum": 3377507
    },
    {
        "threshold": 0.0224,
        "percentile sum": 47616,
        "cumulative sum": 3328030
    },
    {
        "threshold": 0.0225,
        "percentile sum": 47147,
        "cumulative sum": 3280414
    },
    {
        "threshold": 0.0226,
        "percentile sum": 46466,
        "cumulative sum": 3233267
    },
    {
        "threshold": 0.0227,
        "percentile sum": 44753,
        "cumulative sum": 3186801
    },
    {
        "threshold": 0.0228,
        "percentile sum": 44414,
        "cumulative sum": 3142048
    },
    {
        "threshold": 0.0229,
        "percentile sum": 44266,
        "cumulative sum": 3097634
    },
    {
        "threshold": 0.023,
        "percentile sum": 42730,
        "cumulative sum": 3053368
    },
    {
        "threshold": 0.0231,
        "percentile sum": 42240,
        "cumulative sum": 3010638
    },
    {
        "threshold": 0.0232,
        "percentile sum": 41677,
        "cumulative sum": 2968398
    },
    {
        "threshold": 0.0233,
        "percentile sum": 40727,
        "cumulative sum": 2926721
    },
    {
        "threshold": 0.0234,
        "percentile sum": 39447,
        "cumulative sum": 2885994
    },
    {
        "threshold": 0.0235,
        "percentile sum": 40500,
        "cumulative sum": 2846547
    },
    {
        "threshold": 0.0236,
        "percentile sum": 38673,
        "cumulative sum": 2806047
    },
    {
        "threshold": 0.0237,
        "percentile sum": 37839,
        "cumulative sum": 2767374
    },
    {
        "threshold": 0.0238,
        "percentile sum": 37545,
        "cumulative sum": 2729535
    },
    {
        "threshold": 0.0239,
        "percentile sum": 36016,
        "cumulative sum": 2691990
    },
    {
        "threshold": 0.024,
        "percentile sum": 36461,
        "cumulative sum": 2655974
    },
    {
        "threshold": 0.0241,
        "percentile sum": 35535,
        "cumulative sum": 2619513
    },
    {
        "threshold": 0.0242,
        "percentile sum": 34834,
        "cumulative sum": 2583978
    },
    {
        "threshold": 0.0243,
        "percentile sum": 33954,
        "cumulative sum": 2549144
    },
    {
        "threshold": 0.0244,
        "percentile sum": 33653,
        "cumulative sum": 2515190
    },
    {
        "threshold": 0.0245,
        "percentile sum": 33146,
        "cumulative sum": 2481537
    },
    {
        "threshold": 0.0246,
        "percentile sum": 32334,
        "cumulative sum": 2448391
    },
    {
        "threshold": 0.0247,
        "percentile sum": 32125,
        "cumulative sum": 2416057
    },
    {
        "threshold": 0.0248,
        "percentile sum": 31910,
        "cumulative sum": 2383932
    },
    {
        "threshold": 0.0249,
        "percentile sum": 30850,
        "cumulative sum": 2352022
    },
    {
        "threshold": 0.025,
        "percentile sum": 30437,
        "cumulative sum": 2321172
    },
    {
        "threshold": 0.0251,
        "percentile sum": 29570,
        "cumulative sum": 2290735
    },
    {
        "threshold": 0.0252,
        "percentile sum": 29796,
        "cumulative sum": 2261165
    },
    {
        "threshold": 0.0253,
        "percentile sum": 28656,
        "cumulative sum": 2231369
    },
    {
        "threshold": 0.0254,
        "percentile sum": 28127,
        "cumulative sum": 2202713
    },
    {
        "threshold": 0.0255,
        "percentile sum": 28107,
        "cumulative sum": 2174586
    },
    {
        "threshold": 0.0256,
        "percentile sum": 27501,
        "cumulative sum": 2146479
    },
    {
        "threshold": 0.0257,
        "percentile sum": 26875,
        "cumulative sum": 2118978
    },
    {
        "threshold": 0.0258,
        "percentile sum": 26218,
        "cumulative sum": 2092103
    },
    {
        "threshold": 0.0259,
        "percentile sum": 25991,
        "cumulative sum": 2065885
    },
    {
        "threshold": 0.026,
        "percentile sum": 25610,
        "cumulative sum": 2039894
    },
    {
        "threshold": 0.0261,
        "percentile sum": 25637,
        "cumulative sum": 2014284
    },
    {
        "threshold": 0.0262,
        "percentile sum": 24470,
        "cumulative sum": 1988647
    },
    {
        "threshold": 0.0263,
        "percentile sum": 25087,
        "cumulative sum": 1964177
    },
    {
        "threshold": 0.0264,
        "percentile sum": 23905,
        "cumulative sum": 1939090
    },
    {
        "threshold": 0.0265,
        "percentile sum": 23403,
        "cumulative sum": 1915185
    },
    {
        "threshold": 0.0266,
        "percentile sum": 23094,
        "cumulative sum": 1891782
    },
    {
        "threshold": 0.0267,
        "percentile sum": 23093,
        "cumulative sum": 1868688
    },
    {
        "threshold": 0.0268,
        "percentile sum": 22000,
        "cumulative sum": 1845595
    },
    {
        "threshold": 0.0269,
        "percentile sum": 22387,
        "cumulative sum": 1823595
    },
    {
        "threshold": 0.027,
        "percentile sum": 22123,
        "cumulative sum": 1801208
    },
    {
        "threshold": 0.0271,
        "percentile sum": 21702,
        "cumulative sum": 1779085
    },
    {
        "threshold": 0.0272,
        "percentile sum": 21129,
        "cumulative sum": 1757383
    },
    {
        "threshold": 0.0273,
        "percentile sum": 20390,
        "cumulative sum": 1736254
    },
    {
        "threshold": 0.0274,
        "percentile sum": 20787,
        "cumulative sum": 1715864
    },
    {
        "threshold": 0.0275,
        "percentile sum": 20020,
        "cumulative sum": 1695077
    },
    {
        "threshold": 0.0276,
        "percentile sum": 19414,
        "cumulative sum": 1675057
    },
    {
        "threshold": 0.0277,
        "percentile sum": 19545,
        "cumulative sum": 1655643
    },
    {
        "threshold": 0.0278,
        "percentile sum": 19406,
        "cumulative sum": 1636098
    },
    {
        "threshold": 0.0279,
        "percentile sum": 18896,
        "cumulative sum": 1616692
    },
    {
        "threshold": 0.028,
        "percentile sum": 18205,
        "cumulative sum": 1597796
    },
    {
        "threshold": 0.0281,
        "percentile sum": 17912,
        "cumulative sum": 1579591
    },
    {
        "threshold": 0.0282,
        "percentile sum": 18434,
        "cumulative sum": 1561679
    },
    {
        "threshold": 0.0283,
        "percentile sum": 17814,
        "cumulative sum": 1543245
    },
    {
        "threshold": 0.0284,
        "percentile sum": 17878,
        "cumulative sum": 1525431
    },
    {
        "threshold": 0.0285,
        "percentile sum": 17518,
        "cumulative sum": 1507553
    },
    {
        "threshold": 0.0286,
        "percentile sum": 17325,
        "cumulative sum": 1490035
    },
    {
        "threshold": 0.0287,
        "percentile sum": 16763,
        "cumulative sum": 1472710
    },
    {
        "threshold": 0.0288,
        "percentile sum": 16432,
        "cumulative sum": 1455947
    },
    {
        "threshold": 0.0289,
        "percentile sum": 16257,
        "cumulative sum": 1439515
    },
    {
        "threshold": 0.029,
        "percentile sum": 15689,
        "cumulative sum": 1423258
    },
    {
        "threshold": 0.0291,
        "percentile sum": 15550,
        "cumulative sum": 1407569
    },
    {
        "threshold": 0.0292,
        "percentile sum": 15224,
        "cumulative sum": 1392019
    },
    {
        "threshold": 0.0293,
        "percentile sum": 15085,
        "cumulative sum": 1376795
    },
    {
        "threshold": 0.0294,
        "percentile sum": 14880,
        "cumulative sum": 1361710
    },
    {
        "threshold": 0.0295,
        "percentile sum": 14434,
        "cumulative sum": 1346830
    },
    {
        "threshold": 0.0296,
        "percentile sum": 14834,
        "cumulative sum": 1332396
    },
    {
        "threshold": 0.0297,
        "percentile sum": 14096,
        "cumulative sum": 1317562
    },
    {
        "threshold": 0.0298,
        "percentile sum": 14485,
        "cumulative sum": 1303466
    },
    {
        "threshold": 0.0299,
        "percentile sum": 13873,
        "cumulative sum": 1288981
    },
    {
        "threshold": 0.03,
        "percentile sum": 13811,
        "cumulative sum": 1275108
    },
    {
        "threshold": 0.0301,
        "percentile sum": 13832,
        "cumulative sum": 1261297
    },
    {
        "threshold": 0.0302,
        "percentile sum": 13203,
        "cumulative sum": 1247465
    },
    {
        "threshold": 0.0303,
        "percentile sum": 13131,
        "cumulative sum": 1234262
    },
    {
        "threshold": 0.0304,
        "percentile sum": 12853,
        "cumulative sum": 1221131
    },
    {
        "threshold": 0.0305,
        "percentile sum": 12961,
        "cumulative sum": 1208278
    },
    {
        "threshold": 0.0306,
        "percentile sum": 12731,
        "cumulative sum": 1195317
    },
    {
        "threshold": 0.0307,
        "percentile sum": 12185,
        "cumulative sum": 1182586
    },
    {
        "threshold": 0.0308,
        "percentile sum": 12616,
        "cumulative sum": 1170401
    },
    {
        "threshold": 0.0309,
        "percentile sum": 12303,
        "cumulative sum": 1157785
    },
    {
        "threshold": 0.031,
        "percentile sum": 11851,
        "cumulative sum": 1145482
    },
    {
        "threshold": 0.0311,
        "percentile sum": 11835,
        "cumulative sum": 1133631
    },
    {
        "threshold": 0.0312,
        "percentile sum": 11661,
        "cumulative sum": 1121796
    },
    {
        "threshold": 0.0313,
        "percentile sum": 11460,
        "cumulative sum": 1110135
    },
    {
        "threshold": 0.0314,
        "percentile sum": 11491,
        "cumulative sum": 1098675
    },
    {
        "threshold": 0.0315,
        "percentile sum": 10989,
        "cumulative sum": 1087184
    },
    {
        "threshold": 0.0316,
        "percentile sum": 11233,
        "cumulative sum": 1076195
    },
    {
        "threshold": 0.0317,
        "percentile sum": 11076,
        "cumulative sum": 1064962
    },
    {
        "threshold": 0.0318,
        "percentile sum": 10558,
        "cumulative sum": 1053886
    },
    {
        "threshold": 0.0319,
        "percentile sum": 10620,
        "cumulative sum": 1043328
    },
    {
        "threshold": 0.032,
        "percentile sum": 10133,
        "cumulative sum": 1032708
    },
    {
        "threshold": 0.0321,
        "percentile sum": 10138,
        "cumulative sum": 1022575
    },
    {
        "threshold": 0.0322,
        "percentile sum": 9972,
        "cumulative sum": 1012437
    },
    {
        "threshold": 0.0323,
        "percentile sum": 9895,
        "cumulative sum": 1002465
    },
    {
        "threshold": 0.0324,
        "percentile sum": 9934,
        "cumulative sum": 992570
    },
    {
        "threshold": 0.0325,
        "percentile sum": 9814,
        "cumulative sum": 982636
    },
    {
        "threshold": 0.0326,
        "percentile sum": 9422,
        "cumulative sum": 972822
    },
    {
        "threshold": 0.0327,
        "percentile sum": 9240,
        "cumulative sum": 963400
    },
    {
        "threshold": 0.0328,
        "percentile sum": 8984,
        "cumulative sum": 954160
    },
    {
        "threshold": 0.0329,
        "percentile sum": 9411,
        "cumulative sum": 945176
    },
    {
        "threshold": 0.033,
        "percentile sum": 8720,
        "cumulative sum": 935765
    },
    {
        "threshold": 0.0331,
        "percentile sum": 8756,
        "cumulative sum": 927045
    },
    {
        "threshold": 0.0332,
        "percentile sum": 8625,
        "cumulative sum": 918289
    },
    {
        "threshold": 0.0333,
        "percentile sum": 8783,
        "cumulative sum": 909664
    },
    {
        "threshold": 0.0334,
        "percentile sum": 8393,
        "cumulative sum": 900881
    },
    {
        "threshold": 0.0335,
        "percentile sum": 8488,
        "cumulative sum": 892488
    },
    {
        "threshold": 0.0336,
        "percentile sum": 8267,
        "cumulative sum": 884000
    },
    {
        "threshold": 0.0337,
        "percentile sum": 8154,
        "cumulative sum": 875733
    },
    {
        "threshold": 0.0338,
        "percentile sum": 8101,
        "cumulative sum": 867579
    },
    {
        "threshold": 0.0339,
        "percentile sum": 7798,
        "cumulative sum": 859478
    },
    {
        "threshold": 0.034,
        "percentile sum": 7699,
        "cumulative sum": 851680
    },
    {
        "threshold": 0.0341,
        "percentile sum": 7938,
        "cumulative sum": 843981
    },
    {
        "threshold": 0.0342,
        "percentile sum": 7689,
        "cumulative sum": 836043
    },
    {
        "threshold": 0.0343,
        "percentile sum": 7449,
        "cumulative sum": 828354
    },
    {
        "threshold": 0.0344,
        "percentile sum": 7421,
        "cumulative sum": 820905
    },
    {
        "threshold": 0.0345,
        "percentile sum": 7328,
        "cumulative sum": 813484
    },
    {
        "threshold": 0.0346,
        "percentile sum": 7270,
        "cumulative sum": 806156
    },
    {
        "threshold": 0.0347,
        "percentile sum": 7235,
        "cumulative sum": 798886
    },
    {
        "threshold": 0.0348,
        "percentile sum": 7487,
        "cumulative sum": 791651
    },
    {
        "threshold": 0.0349,
        "percentile sum": 7280,
        "cumulative sum": 784164
    },
    {
        "threshold": 0.035,
        "percentile sum": 7289,
        "cumulative sum": 776884
    },
    {
        "threshold": 0.0351,
        "percentile sum": 6794,
        "cumulative sum": 769595
    },
    {
        "threshold": 0.0352,
        "percentile sum": 6520,
        "cumulative sum": 762801
    },
    {
        "threshold": 0.0353,
        "percentile sum": 6720,
        "cumulative sum": 756281
    },
    {
        "threshold": 0.0354,
        "percentile sum": 6361,
        "cumulative sum": 749561
    },
    {
        "threshold": 0.0355,
        "percentile sum": 6587,
        "cumulative sum": 743200
    },
    {
        "threshold": 0.0356,
        "percentile sum": 6315,
        "cumulative sum": 736613
    },
    {
        "threshold": 0.0357,
        "percentile sum": 6259,
        "cumulative sum": 730298
    },
    {
        "threshold": 0.0358,
        "percentile sum": 6266,
        "cumulative sum": 724039
    },
    {
        "threshold": 0.0359,
        "percentile sum": 6328,
        "cumulative sum": 717773
    },
    {
        "threshold": 0.036,
        "percentile sum": 6022,
        "cumulative sum": 711445
    },
    {
        "threshold": 0.0361,
        "percentile sum": 6090,
        "cumulative sum": 705423
    },
    {
        "threshold": 0.0362,
        "percentile sum": 6000,
        "cumulative sum": 699333
    },
    {
        "threshold": 0.0363,
        "percentile sum": 5889,
        "cumulative sum": 693333
    },
    {
        "threshold": 0.0364,
        "percentile sum": 5739,
        "cumulative sum": 687444
    },
    {
        "threshold": 0.0365,
        "percentile sum": 5643,
        "cumulative sum": 681705
    },
    {
        "threshold": 0.0366,
        "percentile sum": 5624,
        "cumulative sum": 676062
    },
    {
        "threshold": 0.0367,
        "percentile sum": 5504,
        "cumulative sum": 670438
    },
    {
        "threshold": 0.0368,
        "percentile sum": 5456,
        "cumulative sum": 664934
    },
    {
        "threshold": 0.0369,
        "percentile sum": 5371,
        "cumulative sum": 659478
    },
    {
        "threshold": 0.037,
        "percentile sum": 5414,
        "cumulative sum": 654107
    },
    {
        "threshold": 0.0371,
        "percentile sum": 5265,
        "cumulative sum": 648693
    },
    {
        "threshold": 0.0372,
        "percentile sum": 5113,
        "cumulative sum": 643428
    },
    {
        "threshold": 0.0373,
        "percentile sum": 5389,
        "cumulative sum": 638315
    },
    {
        "threshold": 0.0374,
        "percentile sum": 5111,
        "cumulative sum": 632926
    },
    {
        "threshold": 0.0375,
        "percentile sum": 5096,
        "cumulative sum": 627815
    },
    {
        "threshold": 0.0376,
        "percentile sum": 4807,
        "cumulative sum": 622719
    },
    {
        "threshold": 0.0377,
        "percentile sum": 4854,
        "cumulative sum": 617912
    },
    {
        "threshold": 0.0378,
        "percentile sum": 4973,
        "cumulative sum": 613058
    },
    {
        "threshold": 0.0379,
        "percentile sum": 4793,
        "cumulative sum": 608085
    },
    {
        "threshold": 0.038,
        "percentile sum": 4742,
        "cumulative sum": 603292
    },
    {
        "threshold": 0.0381,
        "percentile sum": 4727,
        "cumulative sum": 598550
    },
    {
        "threshold": 0.0382,
        "percentile sum": 4760,
        "cumulative sum": 593823
    },
    {
        "threshold": 0.0383,
        "percentile sum": 4491,
        "cumulative sum": 589063
    },
    {
        "threshold": 0.0384,
        "percentile sum": 4636,
        "cumulative sum": 584572
    },
    {
        "threshold": 0.0385,
        "percentile sum": 4503,
        "cumulative sum": 579936
    },
    {
        "threshold": 0.0386,
        "percentile sum": 4498,
        "cumulative sum": 575433
    },
    {
        "threshold": 0.0387,
        "percentile sum": 4231,
        "cumulative sum": 570935
    },
    {
        "threshold": 0.0388,
        "percentile sum": 4461,
        "cumulative sum": 566704
    },
    {
        "threshold": 0.0389,
        "percentile sum": 4178,
        "cumulative sum": 562243
    },
    {
        "threshold": 0.039,
        "percentile sum": 4294,
        "cumulative sum": 558065
    },
    {
        "threshold": 0.0391,
        "percentile sum": 4059,
        "cumulative sum": 553771
    },
    {
        "threshold": 0.0392,
        "percentile sum": 4041,
        "cumulative sum": 549712
    },
    {
        "threshold": 0.0393,
        "percentile sum": 4065,
        "cumulative sum": 545671
    },
    {
        "threshold": 0.0394,
        "percentile sum": 4250,
        "cumulative sum": 541606
    },
    {
        "threshold": 0.0395,
        "percentile sum": 4067,
        "cumulative sum": 537356
    },
    {
        "threshold": 0.0396,
        "percentile sum": 3864,
        "cumulative sum": 533289
    },
    {
        "threshold": 0.0397,
        "percentile sum": 3974,
        "cumulative sum": 529425
    },
    {
        "threshold": 0.0398,
        "percentile sum": 3698,
        "cumulative sum": 525451
    },
    {
        "threshold": 0.0399,
        "percentile sum": 3721,
        "cumulative sum": 521753
    },
    {
        "threshold": 0.04,
        "percentile sum": 3593,
        "cumulative sum": 518032
    },
    {
        "threshold": 0.0401,
        "percentile sum": 3592,
        "cumulative sum": 514439
    },
    {
        "threshold": 0.0402,
        "percentile sum": 3694,
        "cumulative sum": 510847
    },
    {
        "threshold": 0.0403,
        "percentile sum": 3679,
        "cumulative sum": 507153
    },
    {
        "threshold": 0.0404,
        "percentile sum": 3576,
        "cumulative sum": 503474
    },
    {
        "threshold": 0.0405,
        "percentile sum": 3423,
        "cumulative sum": 499898
    },
    {
        "threshold": 0.0406,
        "percentile sum": 3552,
        "cumulative sum": 496475
    },
    {
        "threshold": 0.0407,
        "percentile sum": 3607,
        "cumulative sum": 492923
    },
    {
        "threshold": 0.0408,
        "percentile sum": 3439,
        "cumulative sum": 489316
    },
    {
        "threshold": 0.0409,
        "percentile sum": 3393,
        "cumulative sum": 485877
    },
    {
        "threshold": 0.041,
        "percentile sum": 3582,
        "cumulative sum": 482484
    },
    {
        "threshold": 0.0411,
        "percentile sum": 3341,
        "cumulative sum": 478902
    },
    {
        "threshold": 0.0412,
        "percentile sum": 3261,
        "cumulative sum": 475561
    },
    {
        "threshold": 0.0413,
        "percentile sum": 3146,
        "cumulative sum": 472300
    },
    {
        "threshold": 0.0414,
        "percentile sum": 3289,
        "cumulative sum": 469154
    },
    {
        "threshold": 0.0415,
        "percentile sum": 3168,
        "cumulative sum": 465865
    },
    {
        "threshold": 0.0416,
        "percentile sum": 3179,
        "cumulative sum": 462697
    },
    {
        "threshold": 0.0417,
        "percentile sum": 3139,
        "cumulative sum": 459518
    },
    {
        "threshold": 0.0418,
        "percentile sum": 3115,
        "cumulative sum": 456379
    },
    {
        "threshold": 0.0419,
        "percentile sum": 3081,
        "cumulative sum": 453264
    },
    {
        "threshold": 0.042,
        "percentile sum": 3046,
        "cumulative sum": 450183
    },
    {
        "threshold": 0.0421,
        "percentile sum": 2965,
        "cumulative sum": 447137
    },
    {
        "threshold": 0.0422,
        "percentile sum": 2851,
        "cumulative sum": 444172
    },
    {
        "threshold": 0.0423,
        "percentile sum": 2782,
        "cumulative sum": 441321
    },
    {
        "threshold": 0.0424,
        "percentile sum": 2874,
        "cumulative sum": 438539
    },
    {
        "threshold": 0.0425,
        "percentile sum": 2726,
        "cumulative sum": 435665
    },
    {
        "threshold": 0.0426,
        "percentile sum": 2845,
        "cumulative sum": 432939
    },
    {
        "threshold": 0.0427,
        "percentile sum": 2875,
        "cumulative sum": 430094
    },
    {
        "threshold": 0.0428,
        "percentile sum": 2690,
        "cumulative sum": 427219
    },
    {
        "threshold": 0.0429,
        "percentile sum": 2830,
        "cumulative sum": 424529
    },
    {
        "threshold": 0.043,
        "percentile sum": 2740,
        "cumulative sum": 421699
    },
    {
        "threshold": 0.0431,
        "percentile sum": 2539,
        "cumulative sum": 418959
    },
    {
        "threshold": 0.0432,
        "percentile sum": 2676,
        "cumulative sum": 416420
    },
    {
        "threshold": 0.0433,
        "percentile sum": 2599,
        "cumulative sum": 413744
    },
    {
        "threshold": 0.0434,
        "percentile sum": 2659,
        "cumulative sum": 411145
    },
    {
        "threshold": 0.0435,
        "percentile sum": 2510,
        "cumulative sum": 408486
    },
    {
        "threshold": 0.0436,
        "percentile sum": 2459,
        "cumulative sum": 405976
    },
    {
        "threshold": 0.0437,
        "percentile sum": 2498,
        "cumulative sum": 403517
    },
    {
        "threshold": 0.0438,
        "percentile sum": 2401,
        "cumulative sum": 401019
    },
    {
        "threshold": 0.0439,
        "percentile sum": 2547,
        "cumulative sum": 398618
    },
    {
        "threshold": 0.044,
        "percentile sum": 2410,
        "cumulative sum": 396071
    },
    {
        "threshold": 0.0441,
        "percentile sum": 2276,
        "cumulative sum": 393661
    },
    {
        "threshold": 0.0442,
        "percentile sum": 2482,
        "cumulative sum": 391385
    },
    {
        "threshold": 0.0443,
        "percentile sum": 2395,
        "cumulative sum": 388903
    },
    {
        "threshold": 0.0444,
        "percentile sum": 2353,
        "cumulative sum": 386508
    },
    {
        "threshold": 0.0445,
        "percentile sum": 2381,
        "cumulative sum": 384155
    },
    {
        "threshold": 0.0446,
        "percentile sum": 2260,
        "cumulative sum": 381774
    },
    {
        "threshold": 0.0447,
        "percentile sum": 2370,
        "cumulative sum": 379514
    },
    {
        "threshold": 0.0448,
        "percentile sum": 2326,
        "cumulative sum": 377144
    },
    {
        "threshold": 0.0449,
        "percentile sum": 2276,
        "cumulative sum": 374818
    },
    {
        "threshold": 0.045,
        "percentile sum": 2272,
        "cumulative sum": 372542
    },
    {
        "threshold": 0.0451,
        "percentile sum": 1993,
        "cumulative sum": 370270
    },
    {
        "threshold": 0.0452,
        "percentile sum": 2136,
        "cumulative sum": 368277
    },
    {
        "threshold": 0.0453,
        "percentile sum": 2186,
        "cumulative sum": 366141
    },
    {
        "threshold": 0.0454,
        "percentile sum": 363955,
        "cumulative sum": 363955
    }
]'''

# Parse the JSON data
data = json.loads(json_data)

# Initialize variables to store the nearest value and its difference
nearest_value = None
smallest_difference = float('inf')

# Find the nearest value within ±15% of the given number
for entry in data:
    cumulative_sum = entry["cumulative sum"]
    print("1",abs(lower_bound - cumulative_sum))
    print("2", abs(upper_bound - cumulative_sum))
    if lower_bound <= cumulative_sum <= upper_bound:
        difference = abs(value - cumulative_sum)
        if difference < smallest_difference:
            nearest_value = entry
            smallest_difference = difference

# Determine if the nearest value is closer to +15% or -15%
if nearest_value:
    nearest_cumulative_sum = nearest_value["cumulative sum"]
    if nearest_cumulative_sum < value:
        closeness = "-15%"
    else:
        closeness = "+15%"

print(nearest_value)
