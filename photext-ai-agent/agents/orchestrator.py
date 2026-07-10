from agents.ocr_agent import OCRAgent
from agents.font_agent import FontAgent
from agents.image_editor_agent import ImageEditorAgent

class OrchestratorAgent:
    def __init__(self):
        self.ocr_agent = OCRAgent()
        self.font_agent = FontAgent()
        self.image_editor_agent = ImageEditorAgent()

    def process_initial_upload(self, image_path: str) -> dict:
        """
        Coordinates the processing of an uploaded image through the OCR, Font, and Image Editor agents.
        """
        # 1. Detect text regions
        text_regions = self.ocr_agent.detect_text_regions(image_path)
        
        # 2. Detect fonts and colors for those regions
        font_data = self.font_agent.detect_fonts_and_colors(image_path, text_regions)
        
        # 3. Prepare initial canvas layers
        canvas_state = self.image_editor_agent.create_canvas_layers(image_path, text_regions, font_data)
        
        return {
            "status": "success",
            "canvas_state": canvas_state
        }
