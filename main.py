import numpy as np
from PIL import Image

img = np.array(Image.open('airplane.jpg'))      # Load Image
arr = img.reshape((-1, 3))                      # translate image into an array

k = 20                  # determine k and repeat value
repeat = 50

def kmeans(arr, k, repeat):
    N, D = arr.shape            # set the Data point and array

    mu = [arr[np.random.choice(N)]]     # Initialize centroid
    for i in range(1, k):               # set the centroid located be far
        dist = np.linalg.norm(arr - mu[-1], axis=1)     # Obtain the distance between the selected centroid and all data so far
        prob = dist**2 / np.sum(dist**2)                # Calculate distance rate to select the furthest data point
                                                        # as the next centroid by holding on to the previous centroid
        mu.append(arr[np.random.choice(N, p=prob)])     # choose next centroid randomly

    for i in range(repeat):
        dist = np.linalg.norm(arr[:, np.newaxis, :] - mu, axis=2)   # Assign data points to closest centeroid
        r = np.argmin(dist, axis=1)

        prev_mu = mu.copy()                                         # update centroid
        for j in range(k):
            mu[j] = np.mean(arr[r == j], axis=0)

        if np.allclose(mu, prev_mu):                                # Check for convergence
            break                                                   # if convergence, break

    return r, mu            # r = a one-dimensional list that represents the cluster assignment of all data points
                            # mu = k cluster centric arrays

datapoints, centers = kmeans(arr, k, repeat)        # Perform image segmentation to return result values
# Result of k-means clustering for input data points -> Assign each datapoint, cluster centric

res = np.take(centers, datapoints, axis=0)          # Convert each pixel to the center color of the corresponding cluster
res = res.astype(np.uint8)
res2 = res.reshape((img.shape))

final = Image.fromarray(res2)
final.save("Airplane-result_image-20.jpg")   # save result image


