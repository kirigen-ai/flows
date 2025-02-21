from .image import ImageAnalysisAgent, ImageGenerationAgent
from .video import VideoAnalysisAgent, VideoGenerationAgent
from pydantic import BaseModel, Field

from enum import Enum

class AspectRatio(str, Enum):
    square  = "square"
    portrait= "portrait"
    landscape= "landscape"

###############################################################################################################

class ImageAspectRatio(AspectRatio): pass

class ImageFormat(str, Enum):
    png     = "png"
    jpeg    = "jpeg"
    webp    = "webp"
    bmp     = "bmp"
    gif     = "gif"
    tiff    = "tiff"
    svg     = "svg"
    raw     = "raw"    

class ImageSize(str, Enum):
    xxsmall = "xxsmall"
    xsmall  = "xsmall"
    small   = "small"
    medium  = "medium"
    large   = "large"
    xlarge  = "xlarge"
    xxlarge = "xxlarge"

class ImageQuality(str, Enum):
    low     = "low"
    medium  = "medium"
    high    = "high"

class ImageMetadata(BaseModel):
    data: bytes             = Field(description="The audio data.", default_factory=bytes)
    description: str        = Field(description="The description of the image.", default="")    
    format: ImageFormat     = Field(description="The format of the audio file.", default=ImageFormat.png)
    quality: ImageQuality   = Field(description="The quality of the audio file.", default=ImageQuality.medium)    
    tags: dict[str, str]    = Field(description="The tags of the audio file.", default_factory=dict)

###############################################################################################################

class VideoAspectRatio(AspectRatio): pass

class VideoFormat(str, Enum):
    avi     = "avi"
    gif     = "gif"
    raw     = "raw"
    mov     = "mov"
    mp4     = "mp4"
    webm    = "webm"

class VideoSize(str, Enum):
    xxsmall = "xxsmall"
    xsmall  = "xsmall"
    small   = "small"
    medium  = "medium"
    large   = "large"
    xlarge  = "xlarge"
    xxlarge = "xxlarge"

class VideoQuality(str, Enum):
    low     = "low"
    medium  = "medium"
    high    = "high"

class VideoMetadata(BaseModel):
    data: bytes             = Field(description="The audio data.", default_factory=bytes)
    description: str        = Field(description="The description of the image.", default="")
    format: VideoFormat     = Field(description="The format of the audio file.", default=VideoFormat.mp4)
    quality: VideoQuality   = Field(description="The quality of the audio file.", default=VideoQuality.medium)
    tags: dict[str, str]    = Field(description="The tags of the audio file.", default_factory=dict)

class VideoTranscriptionPart(BaseModel):
    text: str       = Field(description="The text of the audio transcription part.", default="")
    start: float    = Field(description="The start time of the audio transcription part.", default=0.0)
    end: float      = Field(description="The end time of the audio transcription part.", default=0.0)

class VideoTranscription(BaseModel):
    parts: list[VideoTranscriptionPart] = Field(description="The parts of the audio transcription.", default_factory=list)

###############################################################################################################

__all__ = [
    "ImageAspectRatio",
    "ImageSize",
    "ImageFormat",
    "ImageQuality",
    "ImageMetadata",

    "ImageAnalysisAgent",
    "ImageGenerationAgent",

    "VideoAspectRatio",
    "VideoSize",
    "VideoFormat",
    "VideoQuality",    
    "VideoMetadata",
    "VideoTranscriptionPart",
    "VideoTranscription",
    
    "VideoAnalysisAgent",
    "VideoGenerationAgent",
]