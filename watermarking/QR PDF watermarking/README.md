## A PDF Watermarking Scheme utilizing Invisible QR Code Embedding in the Spatial Domain <br>

The digital world has come to an era of continuous sharing of information, where the preservation of the authenticity and the integrity of digital documents, especially PDFs, has become essential. In this work, we introduce a method for the watermarking of PDF files by embedding Quick Response (QR) codes into the spatial domain of the text-color in a PDF file. The proposed PDF watermarking scheme tasks as input a PDF file and a QR Code, adjusting the QR Code's size to the  length of the text of each page in order for the QR Code to be embedded on each page of the PDF file. For the embedding procedure Arnold's transformation and a particular permutation equal to the size of the QR Code are incorporated to secure the embedding and extraction procedures. The QR Code, being resized to match the length of a page's text is undergone a given series of Arnold's transformations and based on a permutation it is embedded in the characters of the text by spatial-domain watermarking changing slightly the color of particular characters that correspond to pixels with black color in the QR Code. We provide a series of evaluation experiments considering various types of attacks to attest the robustness of the proposed scheme for the preservation of PDF file's authenticity as also its fragility required for tamper detection. The exhibited results achieve an average PSNR of 57.6 db and SSIM of 0.99 when comparing the content of a watermarked pdf against the initial one. Considering the preservation of authenticity, the QR Code extracted after common processing attacks exhibits a PSNR > 68.8 db over SSIM equal to 1 while the tamper detection after malicious editing attacks is successful in all the cases, proving the potentials of the proposed watermarking scheme to protect PDF files. <br><br>


## Requirements

1. **Aspose PDF License**  
   To run the embed algorithm, a valid Aspose PDF license is required. You can obtain a temporary or permanent license from the official [Aspose License Page](https://purchase.aspose.com/temporary-license/).

---

## Usage

To execute the embed algorithm, you will need to provide the following three arguments:

1. **Aspose License Path**  
   The file path to your Aspose PDF license file.

2. **PDF Path**  
   The file path to the PDF document you wish to process.

3. **QR Data Link/Path**  
   The link/path for the generation of the QR

---

### Running the embed and extract Algorithm

Here’s an example of how to run the algorithm after cloning the repository:

```bash
python embed_QR.py <license_path> <pdf_path> <link/path_for_qr_generation>
python extract_QR.py <license_path>

