#!/usr/bin/env python2.7
# Sean Blanchard
# 10/1/20
#Got help building this class in tutor room CS

import unittest
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value (puts)
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.newTable = dict();
        for pair in pairs:
            self.put(pair[0], pair[1]);
    # Associates the value v with the key k. (append)
    def put(self, k, v):
        if k in self.newTable:
            self.newTable[k].append(v);
        else:
            self.newTable[k] = [v];
    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    #Return self (newtable[iterations])
    def get(self, k):
        try:
            return self.newTable[k]
        except KeyError:
            return []

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):
    try:
        assert k > 0
        subseq = ''
        for i in range(0, k):
        position = 0;
        while True:
            yield (RollingHash(subseq).hash(), (position, subseq));
            previtm = subseq[0];
            subseq = subseq[1:] + seq.next();
            RollingHash(subseq).slide(previtm, subseq[-1:]);
            position += 1;
    except StopIteration:
        return

# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k):
  
    return 0;

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print ('Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0]))
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8)
