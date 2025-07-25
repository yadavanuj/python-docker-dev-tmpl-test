import pytest
from app.services.pii_detection_service import PIIDetectionService

@pytest.fixture
def pii_detector():
    return PIIDetectionService()

def test_detect_pii_with_aadhar(pii_detector):
    text = "My aadhar number is 123456789012"
    detections = pii_detector.detect_pii(text)
    assert len(detections) == 1
    assert detections[0].type == "Aadhar Card"

def test_detect_pii_with_pan(pii_detector):
    text = "My PAN card is ABCDE1234F"
    detections = pii_detector.detect_pii(text)
    assert len(detections) == 1
    assert detections[0].type == "PAN Card"

def test_detect_pii_with_phone(pii_detector):
    text = "My phone number is 9876543210"
    detections = pii_detector.detect_pii(text)
    assert len(detections) == 1
    assert detections[0].type == "Phone Number (India)"

def test_detect_pii_with_obfuscation(pii_detector):
    text = "My aadhar is 1234-5678-9012"
    detections = pii_detector.detect_pii(text)
    assert len(detections) == 1
    assert detections[0].type == "Aadhar Card"

def test_no_pii(pii_detector):
    text = "This is a normal sentence without any personal information."
    detections = pii_detector.detect_pii(text)
    assert len(detections) == 0
