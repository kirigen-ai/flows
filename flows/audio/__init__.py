from .music import MusicAnalysisAgent, MusicGenerationAgent
from .speech import SpeechAnalysisAgent, SpeechGenerationAgent

from enum import Enum
from pydantic import BaseModel, Field

class AudioFormat(str, Enum):    
    mp3 = "mp3"
    mp4 = "mp4"
    ogg = "ogg"
    wav = "wav"
    raw = "raw"

class AudioQuality(str, Enum):
    low     = "low"
    medium  = "medium"
    high    = "high"

class AudioMetadata(BaseModel):
    data: bytes             = Field(description="The audio data.", default_factory=bytes)
    duration: float         = Field(description="The duration of the audio file.", default=0.0)
    channels: int           = Field(description="The number of channels in the audio file.", default=1, le=1)    
    format: AudioFormat     = Field(description="The format of the audio file.", default=AudioFormat.mp3)
    quality: AudioQuality   = Field(description="The quality of the audio file.", default=AudioQuality.medium)
    sample_rate: int        = Field(description="The sample rate of the audio file.", default=24000)
    tags: dict[str, str]    = Field(description="The tags of the audio file.", default_factory=dict)

class AudioTranscriptionPart(BaseModel):
    text: str       = Field(description="The text of the audio transcription part.", default="")
    start: float    = Field(description="The start time of the audio transcription part.", default=0.0)
    end: float      = Field(description="The end time of the audio transcription part.", default=0.0)

class AudioTranscription(BaseModel):
    parts: list[AudioTranscriptionPart] = Field(description="The parts of the audio transcription.", default_factory=list)

__all__ = [ 
    "AudioFormat", 
    "AudioQuality", 
    "AudioMetadata", 
    "AudioTranscriptionPart", 
    "AudioTranscription", 
    
    "MusicAnalysisAgent",
    "MusicGenerationAgent",

    "SpeechAnalysisAgent",
    "SpeechGenerationAgent",
]