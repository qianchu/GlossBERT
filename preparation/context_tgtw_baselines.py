import sys

eval_dataset = ['senseval2', 'senseval3', 'semeval2007', 'semeval2013', 'semeval2015', 'ALL']
train_dataset = ['SemCor']

file_path = []
for dataset in eval_dataset:
    file_path.append('./Evaluation_Datasets/' + dataset + '/' + dataset+'_test_sent_cls.csv')
for dataset in train_dataset:
    file_path.append('./Training_Corpora/' + dataset + '/' + dataset.lower()+'_train_sent_cls.csv')
    
for flag in ['c','w']:
    for csv_file in file_path:
            
        lines=open(csv_file).readlines()
        for i in range(1,len(lines)):
            sentence,tgt_i_start,tgt_i_end,tgt_id,tgt_lemma, tgt_pos,sense_key=lines[i].split('\t')
            if flag=='c':
                sentence=sentence.split()
                del sentence[int(tgt_i_start):int(tgt_i_end)]
                sentence=sentence[:int(tgt_i_start)]+['[MASK]']+sentence[int(tgt_i_start):]
                sentence=' '.join(sentence)
                tgt_i_start,tgt_i_end=tgt_i_start,str(int(tgt_i_start)+1)
            elif flag=='w':
                sentence=sentence.split()
                w=sentence[int(tgt_i_start):int(tgt_i_end)]
                sentence=' '.join(w)
                tgt_i_start,tgt_i_end=str(0),str(len(w))

            lines[i]='\t'.join([sentence,tgt_i_start,tgt_i_end,tgt_id,tgt_lemma, tgt_pos,sense_key])


        with open(csv_file+'_'+flag+'.csv','w') as f:
            f.write(''.join(lines))