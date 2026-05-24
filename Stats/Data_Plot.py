# Plotting decision regions
x_min, x_max = X[:, 0].min(), X[:, 0].max()
y_min, y_max = X[:, 1].min(), X[:, 1].max()
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

fig, ax = plt.subplots(1,4, figsize=(20,8))

Nvals = [0,2,9,60]

for i,idx  in enumerate(Nvals):
    idx = Nvals[i]
    # Apply classifier to grid points
    Z = clflist[idx].predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax[i].contour(xx, yy, Z, alpha=0.3)
    ax[i].plot(X[y==1,0], X[y==1,1],'o', X[y==0,0],X[y==0,1],'*', markersize='8')
    ax[i].set_title('k=' + str(idx+1))


#plt.show()
plt.savefig('knn-experiment.png')

