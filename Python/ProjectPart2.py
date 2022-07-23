def dic_list_gen(strings, listoflists):
 acc = []
 dict1 = {}
 for lists in listoflists:
   for i in range(len(strings)):
     dict1[strings[i]] = lists[i]
 print(dict1)
dic_list_gen(['Example','Other lengths'], [['Made-Up','Possible'], ["What", "the", "hell", "I forgot dictionaries"]])