#!/usr/bin/env python
import numpy as np
from scipy import linalg
from scipy.sparse import diags



def main():
	n = 100
	k = -1*np.array([np.ones(n-1),-2*np.ones(n),1*np.ones(n-1)])
	offset = [-1,0,1]
	A = diags(k,offset).toarray()	
	print(A)
	eigenvalues = np.linalg.eigvals(A)
	#print(eigenvalues)
	maxeigen=max(eigenvalues)
	mineigen=min(eigenvalues)
	print(maxeigen,mineigen)
	landa=2
	

	
	#solve
	s=(100,1)
	b=np.ones(s)
	iteration=0
	x1 = np.ones((100,1))
	err = np.ones((100,1))*100
	main_m=np.identity(100)-np.dot(0.5,A)
	while np.max(err) > 0:
		iteration=iteration+1
	
		xn = np.dot(main_m,x1)+np.dot(0.5,b)
		err = abs((xn - x1)/(xn+0.0001))*100
		x1 = xn
	print("first:",x1)	
	print(iteration)
	


	
	x=linalg.solve(A, b)
	print("the aswer is:",x)

	
if __name__ == '__main__':
	main()
