window_size=int(input('Enter a window size number: '))
feature_list='ACDEFGHIKLMNPQRSTVWY'
features_dict=dict() 
binary_list=[0]*38
binary_list.insert(19,1)
i=0
for amino_acids in feature_list:
    features_dict[amino_acids]=binary_list[i:i+20]
    i=i+1
features_dict['Z']=[0]*20
labels_dict={'G':0,'M':1,'STOP':2}
features=list()
labels=list()
f=open('abc.txt','r')
m=0
for line in f:
    if m%3==0:
        features.extend(['Z']*(int(window_size/2)))
        labels.extend(['STOP']*(int(window_size/2)))
    if m%3==1:
        for i in line.strip():
            features.append(i)
    if m%3==2:
        for i in line.strip():
            l1=labels.append(i)
    m=m+1
features.extend(['Z']*(int(window_size/2)))
labels.extend(['STOP']*(int(window_size/2)))
f=open('abc.txt')
o1=open('s1.txt','w')
o2=open('s2.txt','w')
for i in range(int(window_size/2),int(len(labels)-window_size/2)):
    o1.write(labels[i])
    o1.write('\n')
    for window_member in range(i-int(window_size/2),i+int(window_size/2)+1):
        o2.write(features[window_member])
    o2.write('\n')
f.close()
o1.close()
o2.close()
o1=open('s1.txt')
list_of_label_code=list()
for label_contents in o1:
    label_contents=label_contents.strip('\n').split(' ')
    for n,i in enumerate(label_contents):
        if i in labels_dict:
            label_contents[n]=labels_dict[i]
            list_of_label_code.append(label_contents[n])
o2=open('s2.txt')
list_of_feature=list()
for feature_contents in o2:
    list_of_window=list()
    feature_contents=feature_contents.strip('\n').split(' ')
    feature_contents=list(feature_contents[0])
    for n, i in enumerate(feature_contents):
        if i in features_dict:
            feature_contents[n]=features_dict[i]
            list_of_window.extend(feature_contents[n])
    list_of_feature.append(list_of_window)
list_label_final=list()
list_feature_window_final=list()
for i in list_of_label_code:
    if i!=2:
        list_label_final.append(i)
print (list_label_final)

for i in list_of_feature:
    if i[(20*(int(window_size/2))):(20*int((window_size/2+1)))]!=[0]*20:
        list_feature_window_final.append(i)
print (list_feature_window_final)
print (len(list_of_label_code),len(list_of_feature),len(list_label_final),len(list_feature_window_final))
l1=open('output.txt', 'w')
for i in range(0,len(list_feature_window_final),1):
    for k in list_feature_window_final[i]:
        l1.write(str(k))
    l1.write('\n')
