import numpy as np 

def test_run():
   
    a = np.array([(1,1,3,4),(2,2,5,6)])
    print a
    mean = a.mean()
    b = mean > a
    print b
  
if __name__ == "__main__":
    test_run()
