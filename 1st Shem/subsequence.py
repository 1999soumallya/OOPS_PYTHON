def subsequence(l1,l2):
    if (all(i in l1 for i in l2)):
        print("True")
    else:
        print("False")
l1=[2,3,4]
l2=[2,2,5]
subsequence(l1,l2)
