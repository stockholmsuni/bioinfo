f=open('T0834.jhE3.ur50.fasta')
d=dict()
prev_i=0
for line in f:
    d[prev_i]=line
    prev_i=line
print (d)
