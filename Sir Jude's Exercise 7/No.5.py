print('Welcome to K-mer Counts!')
def kmers(dna, ln):
    print('Here are your datas:')
    print(dna)
    print(ln)
    print('Here is your K-mer Count:')
    cnt= {}
    num= len(dna)-ln+1
    for i in range(num):
        kmer = dna[i:i+ln]
        if kmer not in cnt:
            cnt[kmer] = 1
        elif kmer in cnt:
            cnt[kmer] += 1
    return cnt

def datas():
    dna = input('Please input your DNA here: ')
    ln = int(input('Please Input the length of the substring(k): '))
    print(kmers(dna, ln))
datas()
print('Thankyou for using our service!')