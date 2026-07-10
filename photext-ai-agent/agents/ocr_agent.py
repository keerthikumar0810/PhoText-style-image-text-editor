class OCRAgent:
    def __init__(self):
        pass
        
    def detect_text_regions(self, image_path: str) -> list:
        """
        Detects text bounding boxes in the given image.
        Returns a list of regions.
        """
        # TODO: Implement OCR logic (e.g. Tesseract, EasyOCR, or Vision API)
        return [
            {"id": "region_1", "text": "Sample Text", "box": {"x": 10, "y": 10, "w": 100, "h": 50}}
        ]
