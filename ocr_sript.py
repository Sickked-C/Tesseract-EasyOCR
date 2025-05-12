import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import pytesseract
import os
import easyocr
import matplotlib.pyplot as plt


# Perform OCR using Tesseract on a single image
def read_and_predict_image_tesseract(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    ocr_result = pytesseract.image_to_string(image_rgb, lang='vie+eng')
    return ocr_result


# Perform OCR using Tesseract on all images in a folder
def read_and_predict_images_in_folder_tesseract(folder_path):
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

    ocr_results = []
    for image_file in image_files:
        ocr_results.append((image_file, read_and_predict_image_tesseract(image_file)))

    return ocr_results


# Handle image selection and prediction (Tesseract)
def select_image_and_predict_tesseract():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    ocr_result = read_and_predict_image_tesseract(file_path)
    print(f"Predicted Text:\n{ocr_result}\n")
    display_image_and_result_tesseract(file_path, ocr_result)


# Handle folder selection and prediction for multiple images (Tesseract)
def select_folder_and_predict_tesseract():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    ocr_results = read_and_predict_images_in_folder_tesseract(folder_path)
    print("Prediction results from images:")
    for path, result in ocr_results:
        print(f"File: {path}\nResult: {result}\n")

    display_multiple_image_results_tesseract(ocr_results)


# Display OCR results from multiple images in a new window (Tesseract)
def display_multiple_image_results_tesseract(ocr_results):
    result_window = tk.Toplevel()
    result_window.title("Tesseract OCR Results from Multiple Images")

    frame = tk.Frame(result_window)
    frame.pack(fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_area = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text_area.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=text_area.yview)

    for path, result in ocr_results:
        text_area.insert(tk.END, f"File: {path}\nResult: {result}\n\n")

    result_window.mainloop()


# Display image and OCR result in a new window (Tesseract)
def display_image_and_result_tesseract(image_path, ocr_result):
    result_window = tk.Toplevel()
    result_window.title("Tesseract OCR Result")

    image = Image.open(image_path)
    image = image.resize((400, 300))
    image_photo = ImageTk.PhotoImage(image)

    label_image = tk.Label(result_window, image=image_photo)
    label_image.image = image_photo
    label_image.pack(padx=10, pady=10)

    label_result = tk.Label(result_window, text=f"Predicted Text:\n{ocr_result}",
                            wraplength=600, justify="left")
    label_result.pack(padx=10, pady=10)

    result_window.mainloop()


# Initialize EasyOCR reader
reader = easyocr.Reader(['en', 'vi'], gpu=False)


# Perform OCR using EasyOCR on a single image
def read_and_predict_image_easyocr(image_path):
    image = cv2.imread(image_path)
    ocr_result = reader.readtext(image)
    return image, ocr_result


# Handle image selection and prediction (EasyOCR)
def select_image_and_predict_easyocr():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not file_path:
        return

    image, ocr_result = read_and_predict_image_easyocr(file_path)
    print(f"Prediction result from image {file_path}:\n{ocr_result}\n")
    display_image_and_result_easyocr(file_path, image, ocr_result)


# Perform OCR using EasyOCR on all images in a folder
def read_and_predict_images_in_folder_easyocr(folder_path):
    ocr_results = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            file_path = os.path.join(folder_path, file_name)
            image, result = read_and_predict_image_easyocr(file_path)
            ocr_results.append((file_path, result))
    return ocr_results


# Handle folder selection and predict OCR for each image (EasyOCR)
def select_folder_and_predict_easyocr():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    ocr_results = read_and_predict_images_in_folder_easyocr(folder_path)
    print("Prediction results from images:")
    for path, result in ocr_results:
        print(f"File: {path}\nResult: {result}\n")

    display_multiple_image_results_easyocr(ocr_results)


# Display multiple OCR results (EasyOCR)
def display_multiple_image_results_easyocr(ocr_results):
    result_window = tk.Toplevel()
    result_window.title("EasyOCR Results from Multiple Images")

    frame = tk.Frame(result_window)
    frame.pack(fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_area = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text_area.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=text_area.yview)

    for path, result in ocr_results:
        text_area.insert(tk.END, f"File: {path}\nResult: {result}\n\n")


# Display image with OCR results annotated (EasyOCR)
def display_image_and_result_easyocr(image_path, img, results):
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
        img = cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    result_window = tk.Toplevel()
    result_window.title("EasyOCR Result")

    label_result = tk.Label(result_window, text=f"Predicted Text:\n{results}", wraplength=600, justify="left")
    label_result.pack(padx=10, pady=10)

    result_window.mainloop()


# Create main GUI window
root = tk.Tk()
root.title("Image Text Recognition Application")
root.geometry("600x360")
root.resizable(width=True, height=True)

# Create button layout
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

button_select_image_tesseract = tk.Button(frame_buttons, text="Select Image and Predict (Tesseract)",
                                          command=select_image_and_predict_tesseract)
button_select_image_tesseract.pack(pady=20)

button_select_image_easyocr = tk.Button(frame_buttons, text="Select Image and Predict (EasyOCR)",
                                        command=select_image_and_predict_easyocr)
button_select_image_easyocr.pack(pady=20)

button_select_folder_tesseract = tk.Button(frame_buttons, text="Select Folder and Predict (Tesseract)",
                                           command=select_folder_and_predict_tesseract)
button_select_folder_tesseract.pack(pady=20)

button_select_folder_easyocr = tk.Button(frame_buttons, text="Select Folder and Predict (EasyOCR)",
                                         command=select_folder_and_predict_easyocr)
button_select_folder_easyocr.pack(pady=20)

# Run main GUI loop
root.mainloop()
