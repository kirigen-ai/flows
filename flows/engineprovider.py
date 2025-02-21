from abc import ABC, abstractmethod
from typing import AsyncIterator
from typing_extensions import Any
from pydantic import BaseModel, Field


class ProviderConfiguration(BaseModel):
    """Configuration for a provider"""
    model: str          = Field(description="Name of the model used by the provider", default="")
    api_key: str        = Field(description="API key for the provider", default="")
    api_url: str        = Field(description="API URL for the provider", default="")    



class EngineProvider(ABC):
    def __init__(self, config: ProviderConfiguration, **kwargs) -> None:
        """Initialization of provider with configuration"""
        raise NotImplementedError
    
    @abstractmethod
    async def initialize(self) -> None:
        """Async initialization for loading models or establishing connections"""
        raise NotImplementedError
        
    @abstractmethod
    async def call(self, **kwargs) -> AsyncIterator[Any]:
        """Default streaming interface for provider calls"""
        raise NotImplementedError
        
    def shutdown(self) -> None:
        """Synchronous cleanup of resources"""
        raise NotImplementedError