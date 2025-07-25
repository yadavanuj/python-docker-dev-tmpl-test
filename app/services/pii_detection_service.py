import re
import json
from typing import List
from app.models import DetectedPII


class PIIDetectionService:
    def __init__(self, patterns_file: str = "app/pii_patterns.json"):
        self.patterns = self._load_patterns(patterns_file)

    def _load_patterns(self, patterns_file: str) -> List[dict]:
        with open(patterns_file, "r") as f:
            return json.load(f)["patterns"]

    def _normalize_text(self, text: str) -> str:
        return re.sub(r"[^a-zA-Z0-9]", "", text).upper()

    def detect_pii(self, text: str) -> List[DetectedPII]:
        normalized_text = self._normalize_text(text)
        detected_pii = []
        for pattern in self.patterns:
            matches = re.findall(pattern["regex"], normalized_text)
            if matches:
                detected_pii.append(
                    DetectedPII(type=pattern["name"], confidence=pattern["confidence"])
                )
        return detected_pii
