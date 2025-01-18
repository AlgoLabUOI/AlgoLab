import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from math import log10

# Function to calculate MSE
def calculate_mse(image1, image2):
    return np.mean((image1 - image2) ** 2)

# Function to calculate PSNR
def calculate_psnr(image1, image2):
    mse = calculate_mse(image1, image2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    return 10 * log10((max_pixel ** 2) / mse)

# Function to calculate BER (Bit Error Rate)
def calculate_ber(image1, image2):
    # Flatten and binarize the images (thresholding to handle grayscale images)
    binary1 = np.where(image1 > 127, 1, 0).flatten()
    binary2 = np.where(image2 > 127, 1, 0).flatten()
    return np.sum(binary1 != binary2) / len(binary1)

# Function to calculate Normalized Correlation
def calculate_normalized_correlation(image1, image2):
    image1 = image1.flatten()
    image2 = image2.flatten()
    return np.sum(image1 * image2) / np.sqrt(np.sum(image1 ** 2) * np.sum(image2 ** 2))

# Main function
def compute_image_metrics(image1_path, image2_path):
    # Load images
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    if image1 is None or image2 is None:
        raise ValueError("One or both images could not be loaded. Please check the file paths.")

    if image1.shape != image2.shape:
        raise ValueError("Images must have the same dimensions for comparison.")

    # Compute metrics
    mse_value = calculate_mse(image1, image2)
    psnr_value = calculate_psnr(image1, image2)
    ssim_value = ssim(image1, image2)
    ber_value = calculate_ber(image1, image2)
    normalized_correlation = calculate_normalized_correlation(image1, image2)

    # Display results
    print("Metrics between the two images:")
    print(f"MSE: {mse_value}")
    print(f"PSNR: {psnr_value} dB")
    print(f"SSIM: {ssim_value}")
    print(f"BER: {ber_value}")
    print(f"Normalized Correlation: {normalized_correlation}")

# Example usage
# Replace 'original_image.png' and 'modified_image.png' with your file paths
image1_path = "g:/Shared drives/THESIS JOURNALS/---MEROLLI/IOSPress/Revision 1/DataSet/image metrics/pages/initial_text-4.png"
image2_path = "g:/Shared drives/THESIS JOURNALS/---MEROLLI/IOSPress/Revision 1/DataSet/image metrics/pages/colored_text-4.png"
compute_image_metrics(image1_path, image2_path)
