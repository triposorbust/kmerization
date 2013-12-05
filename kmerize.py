from sys import argv
from os.path import splitext
from iterators.fastq import FastQ

LENGTH = 15

def kmerize(astring, n):
    d = { }
    for i in xrange(len(astring) - (n-1)):
        key = astring[i:i+n]
        d[key] = d.get(key,0) + 1
    return d

def kmerge(dicta, dictb):
    for key in dictb:
        dicta[key] = dicta.get(key,0) + dictb.get(key)
    return dicta

def main(inputname, iterator, n):
    writename = "{0}.kmers".format(inputname)
    with open(inputname, 'r') as finput, open(writename, 'w') as fwrite:
        d = { }
        for item in iterator(finput):
            d = kmerge(d, kmerize(item.sequence, n))
        for kmer in sorted(d):
            fwrite.write("{0}\t{1}\n".format(kmer, d[kmer]))

if __name__ == "__main__":
    for filename in argv[1:]:
        _,ext = splitext(filename)
        if ext == ".fastq":
            main(filename, FastQ, LENGTH)
        else:
            raise Exception("Unknown file format: {0}!".format(ext))
