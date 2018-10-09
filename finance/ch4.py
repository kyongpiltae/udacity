import numpy as np


def test_run():
    print np.array([2,3,4])
    print np.empty(5)
    print np.empty((5,4))
    print np.empty((3,3,3))
    print np.ones((3,3))
    print np.ones((3,3),dtype=np.int)
    print np.random.random((5,4))
    print np.random.normal((5,4))
    print np.random.normal(5,10,(5,4))

    print np.random.randint(10)
    print np.random.randint(0,10)
    print np.random.randint(0,10,size=5)
    

    a= np.random.random((5,4))
    print a.size
    print a.shape

    b= np.random.randint(0,10,size=(5,4))
    print "Array:\n" , b
    print "Array's sum:\n" , b.sum()
    print "Array's sum:\n" , b.sum(axis=0)
    print "Array's sum:\n" , b.sum(axis=1)
    print "Array's  min :\n" , b.min(axis=1)
    print "Array's max:\n" , b.max(axis=1)
    print "Array's mean:\n" , b.mean()



if __name__ == "__main__":
    test_run()


