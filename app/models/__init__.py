from pydantic import BaseModel
from typing import List


class DetectedPII(BaseModel):
    type: str
    confidence: float


class PIIDetectionResponse(BaseModel):
    detections: List[DetectedPII]
