import collections


total_length = input()
total_length = int(total_length)
ids_dict = collections.defaultdict(list)
success_ids = set()
result_list = []
for _ in range(total_length):
    text = input()
    ids, _, result = text.split(' ')
    ids_dict[ids].append(text)
    if ids in success_ids:
        continue
    else:
        if result == 'success':
            success_ids.add(ids)
success_ids = list(sorted(success_ids))
for ids in success_ids:
    temp_list = ids_dict[ids]
    temp_list.sort(key=lambda x: int(x.split(' ')[1]))
    result_list.extend(temp_list)
if result_list:
    for line in result_list:
        print(line)
else:
    print(0)
