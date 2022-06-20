"""
Bishop 8.3.4
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def get_test_image() -> np.ndarray:
    """
    Returns:
    (H, W) with values \in {-1, 1}
    """
    test_image_path = Path(__file__).joinpath("../w3.png").resolve()
    img = np.asarray(Image.open(test_image_path))[..., 0]/255
    img = np.where(img > 0, -1, 1)
    return img

def corrupt(img: np.ndarray, corruption_p:float=0.1) -> np.ndarray:
    """
    Args
    ----
    img: (H, W) numpy array with values {-1, 1}
    p: probability of each pixel flipping. [0, 1]
    Returns:
    (H, W) corrupted array
    """
    corruption = np.random.choice([1, -1], img.shape, replace=True, p=[1-corruption_p, corruption_p] )
    return img*corruption

class Denoiser:
    def __init__(self, img: np.ndarray, h:float=0, beta:float=1.0, eta:float=2.1):
        self.height, self.width = img.shape
        self.img = img.flatten()
        self.latents = img.copy().flatten()
        self.h = h
        self.beta = beta
        self.eta = eta

    def sum_neighbors(self, ind):
        """
        Args
        ----
            ind: indeces of image - np.ndarray of shape (N)
        Return
        ------
            sums of neighbors: np.ndarray of shape (N)
                img[ind-1] + img[ind+1] + img[ind-width] + img[ind+width]
        """
        width = self.width
        left = ind - 1
        right = ind + 1
        top = ind - width
        bot = ind + width
        return self.latents[left] + self.latents[right] + self.latents[top] + self.latents[bot] 

    def energy(self, ind, val):
        """
        Args
        ----
            ind: indeces of image - np.ndarray of shape (N)
            val: value of pixels being considered
        Return
        ------
            (N)
            energy at pixels given by inds with latents set at val 
        """
        return  self.h*val - \
                self.beta*val*self.sum_neighbors(ind) - \
                self.eta*val*self.img[ind]
    
    def run(self, n_iters:int = 1000, n_samples: int = 10000):
        """
        Run the denoiser for n_iterations processing n_samples at each pass
        Returns:
        denoised image (H, W)
        """
        for _ in range(n_iters):
            # Generate Samples
            samples = np.random.random((n_samples, 2)) 
            # Ignore edges
            samples[:, 0] = samples[:, 0] * (self.width-3) + 1 
            samples[:, 1] = samples[:, 1] * (self.height-3) + 1 
            inds = np.round(samples[:, 0] * self.width + samples[:, 1]).astype(np.int32)

            # Evaluate latents and minimize energy
            new_latents = np.where(self.energy(inds, -1) < self.energy(inds, 1), -1, 1)
            self.latents[inds] = new_latents
        return self.latents.reshape((self.height, self.width))


if __name__ == "__main__":
    img = get_test_image()
    corrupt_img = corrupt(img)
    denoised_image = Denoiser(corrupt_img).run()

    # Plotting
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(img)
    ax[1].imshow(corrupt_img)
    ax[2].imshow(denoised_image)
    plt.show()