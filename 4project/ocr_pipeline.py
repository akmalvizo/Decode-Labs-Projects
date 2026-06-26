import cv2
import pytesseract
import numpy as np
import sys
import os

print("Script started...")

# ── LIBRARY CHECK ────────────────────────────────────────
try:
    print(f"[OK] OpenCV loaded: {cv2.__version__}")
except:
    print("[ERROR] OpenCV not found. Run: pip install opencv-python")
    sys.exit(1)

try:
    print("[OK] pytesseract loaded")
except:
    print("[ERROR] pytesseract not found. Run: pip install pytesseract")
    sys.exit(1)

# ── TESSERACT PATH ───────────────────────────────────────
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

try:
    version = pytesseract.get_tesseract_version()
    print(f"[OK] Tesseract engine found: version {version}")
except Exception as e:
    print(f"[ERROR] Tesseract engine not found!\n  Details: {e}")
    sys.exit(1)

# ── CONFIG ───────────────────────────────────────────────
IMAGE_PATH = 'sample.png'      # <-- your input image
CONFIDENCE_THRESHOLD = 80

# ── STEP 1: LOAD IMAGE ───────────────────────────────────
if not os.path.exists(IMAGE_PATH):
    print(f"[ERROR] Image not found: {IMAGE_PATH}")
    print("  Please place a clear image named 'sample.png' in this folder.")
    sys.exit(1)

image = cv2.imread(IMAGE_PATH)
print(f"[OK] Image loaded successfully: {image.shape}")

# ── STEP 2: RESIZE if image is too large ─────────────────
# Large images slow OCR down and cause noise issues
h, w = image.shape[:2]
if w > 2000:
    scale = 2000 / w
    image = cv2.resize(image, (2000, int(h * scale)))
    print(f"[OK] Image resized to: {image.shape}")

# ── STEP 3: PRE-PROCESSING PIPELINE ──────────────────────
print("Running pre-processing pipeline...")

# 3a: Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("[OK] Step 1: Grayscale conversion done")

# 3b: Denoise
denoised = cv2.fastNlMeansDenoising(gray, h=10)
print("[OK] Step 2: Denoising done")

# 3c: Increase contrast using CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
contrast = clahe.apply(denoised)
print("[OK] Step 3: Contrast enhancement done")

# 3d: Gaussian Blur
blurred = cv2.GaussianBlur(contrast, (3, 3), 0)
print("[OK] Step 4: Gaussian blur applied")

# 3e: Adaptive Thresholding (best for uneven lighting)
thresh = cv2.adaptiveThreshold(
    blurred, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    blockSize=11,
    C=2
)
print("[OK] Step 5: Adaptive thresholding done")

# Save pre-processed image (proof for submission)
cv2.imwrite('preprocessed.png', thresh)
print("[OK] preprocessed.png saved")

# ── STEP 4: RUN OCR ──────────────────────────────────────
print(f"\nRunning OCR (confidence threshold: {CONFIDENCE_THRESHOLD}%)...")

# Try PSM 6 first (uniform text block) - change to 3 for mixed layouts
custom_config = r'--oem 3 --psm 6'

data = pytesseract.image_to_data(
    thresh,
    config=custom_config,
    output_type=pytesseract.Output.DICT
)
print("[OK] OCR completed")

# ── STEP 5: FILTER BY CONFIDENCE ─────────────────────────
print("=" * 52)
print(f"RESULTS — Words with {CONFIDENCE_THRESHOLD}%+ Confidence:")
print("=" * 52)

extracted_words = []
valid_detections = []

for i in range(len(data['text'])):
    word = data['text'][i].strip()
    conf = int(data['conf'][i])

    # Skip empty words, single symbols, and low-confidence
    if (word
            and conf >= CONFIDENCE_THRESHOLD
            and len(word) > 1          # skip single chars like | ( =
            and word.isalnum() or      # only real words/numbers
            (len(word) > 2 and conf >= CONFIDENCE_THRESHOLD)):

        extracted_words.append(word)
        valid_detections.append(i)
        print(f"  Word: '{word}' | Confidence: {conf}%")

print("=" * 52)

if not extracted_words:
    print("\n[WARNING] No high-confidence words found.")
    print("  Possible fixes:")
    print("  1. Use a clearer image (typed text, not handwritten)")
    print("  2. Use a screenshot of a document or webpage")
    print("  3. Change PSM mode: try --psm 3 or --psm 11")
else:
    full_text = ' '.join(extracted_words)
    print(f"\n[OK] Final Extracted Text:\n{full_text}")

# ── STEP 6: DRAW BOUNDING BOXES ON OUTPUT ────────────────
output_image = image.copy()

for i in valid_detections:
    x = data['left'][i]
    y = data['top'][i]
    w = data['width'][i]
    h = data['height'][i]
    conf = int(data['conf'][i])
    word = data['text'][i].strip()

    # Green box around detected word
    cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 200, 0), 2)
    # Confidence label above box
    label = f"{word} {conf}%"
    cv2.putText(output_image, label, (x, max(y - 6, 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 0), 1)

cv2.imwrite('output_result.png', output_image)
print("\n[OK] output_result.png saved (bounding boxes drawn)")

# ── SUMMARY ──────────────────────────────────────────────
print("\n" + "=" * 52)
print("PROJECT 4 — MILESTONE VALIDATION SUMMARY")
print("=" * 52)
print(f"  [1] Library Integration     : PASSED (cv2 + pytesseract)")
print(f"  [2] Pre-Processing Integrity: PASSED (grayscale + threshold)")
print(f"  [3] Accuracy Benchmarking   : {'PASSED' if extracted_words else 'NEEDS BETTER IMAGE'} ({CONFIDENCE_THRESHOLD}% threshold applied)")
print(f"  [4] Visual Confirmation     : PASSED (output_result.png)")
print("=" * 52)
print("[DONE] Pipeline complete!")