# API Documentation

## preprocess_image(image)

Preprocesses an image for model inference.

### Input

NumPy Image

### Output

Normalized NumPy array

---

## predict_skin(image)

Predicts the skin type.

### Returns

- Skin Type
- Confidence Score

---

## recommend(skin_type)

Returns skincare recommendations.

### Input

String

Example

"Oily"

### Output

List of recommended products.

---

## generate_report(filename, skin_type, confidence)

Creates a PDF report.

### Output

PDF File