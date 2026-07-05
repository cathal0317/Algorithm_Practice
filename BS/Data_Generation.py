# Generate data
m=15
means = np.zeros((2,2,m)) #means[:,0,:] are the means for rho_0 and means[:,1,:] are the means for rho_1
for i in range(m):
    means[:,:,i] = 1.5*np.eye(2)+rnd.randn(2,2)
    
sigma = np.sqrt(0.2)
q = 0.4

# n = number of data points
# sigma = real positive number
# means = (2,2,m)
def generate_data(n,means,sigma):
    m = len(means[0,0,:])
    X = np.zeros((n,2))
    y = np.zeros(n)
    for i in range(n):    
        #generate y sample
        y[i] = rnd.binomial(1,q) #y_i = binom(q)
                
        if y[i] == 0:
            # sample from rho_0
            j = rnd.randint(m)
            X[i,:] = means[:,0,j]+sigma*rnd.randn(2)
        else:
            # sample from rho_1
            j = rnd.randint(m)
            X[i,:] = means[:,1,j]+sigma*rnd.randn(2)
    return X,y

n = 200 # number of samples
X,y = generate_data(n,means,sigma)
 
#plot the data
fig, ax = plt.subplots(1)
ax.plot(X[y==1,0],X[y==1,1],'o', X[y==0,0],X[y==0,1],'*', markersize=5)
plt.axis('equal')
plt.show()
