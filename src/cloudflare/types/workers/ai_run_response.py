# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel

__all__ = [
    "AIRunResponse",
    "TextClassification",
    "TextEmbeddings",
    "AutomaticSpeechRecognition",
    "AutomaticSpeechRecognitionWord",
    "ImageClassification",
    "ObjectDetection",
    "ObjectDetectionBox",
    "UnionMember6",
    "UnionMember6ToolCall",
    "Translation",
    "Summarization",
    "ImageToText",
]


class TextClassification(BaseModel):
    label: Optional[str] = None

    score: Optional[float] = None


class TextEmbeddings(BaseModel):
    data: Optional[List[List[float]]] = None

    shape: Optional[List[float]] = None


class AutomaticSpeechRecognitionWord(BaseModel):
    end: Optional[float] = None

    start: Optional[float] = None

    word: Optional[str] = None


class AutomaticSpeechRecognition(BaseModel):
    text: str

    vtt: Optional[str] = None

    word_count: Optional[float] = None

    words: Optional[List[AutomaticSpeechRecognitionWord]] = None


class ImageClassification(BaseModel):
    label: Optional[str] = None

    score: Optional[float] = None


class ObjectDetectionBox(BaseModel):
    xmax: Optional[float] = None

    xmin: Optional[float] = None

    ymax: Optional[float] = None

    ymin: Optional[float] = None


class ObjectDetection(BaseModel):
    box: Optional[ObjectDetectionBox] = None

    label: Optional[str] = None

    score: Optional[float] = None


class UnionMember6ToolCall(BaseModel):
    arguments: Optional[object] = None

    name: Optional[str] = None


class UnionMember6(BaseModel):
    response: Optional[str] = None

    tool_calls: Optional[List[UnionMember6ToolCall]] = None


class Translation(BaseModel):
    translated_text: Optional[str] = None


class Summarization(BaseModel):
    summary: Optional[str] = None


class ImageToText(BaseModel):
    description: Optional[str] = None


AIRunResponse = Union[
    List[TextClassification],
    object,
    TextEmbeddings,
    AutomaticSpeechRecognition,
    List[ImageClassification],
    List[ObjectDetection],
    UnionMember6,
    object,
    Translation,
    Summarization,
    ImageToText,
]
