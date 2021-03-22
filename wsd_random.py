import sys

lines=open(sys.argv[1]).readlines()
target_id_prev=None
candidate_nums=[]
candidate_num=None
for line in lines[1:]:
    target_id=line.split('\t')[0]
    if target_id!=target_id_prev:
        target_id_prev=target_id
        if candidate_num:
            candidate_nums.append(candidate_num)
        candidate_num=1
        

    else:
        candidate_num+=1

print('mean candidate num',sum(candidate_nums)/len(candidate_nums))
