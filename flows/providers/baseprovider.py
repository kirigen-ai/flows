from abc import ABC, abstractmethod
from enum import Enum
from typing_extensions import Any
from pydantic import BaseModel, Field

class ProviderState(Enum):
    UNINITIALIZED   = 0
    INITIALIZING    = 1
    READY           = 2
    ERROR           = 3
    SHUTDOWN        = 4

class ProviderConfiguration(BaseModel):
    """Configuration for a provider"""
    model: str          = Field(description="Name of the model used by the provider", default="")
    api_key: str        = Field(description="API key for the provider", default="")
    api_url: str        = Field(description="API URL for the provider", default="")    

class BaseProvider(ABC):
    def __init__(self, config: ProviderConfiguration, **kwargs) -> None:
        """Initialization of provider with configuration"""
        raise NotImplementedError
    
    @abstractmethod
    async def initialize(self) -> None:
        """Async initialization for loading models or establishing connections"""
        raise NotImplementedError
        
    @abstractmethod
    async def call(self, **kwargs) -> Any:
        """Async method for model inference or API calls"""
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        """Synchronous cleanup of resources"""
        raise NotImplementedError

    @property
    def is_ready(self) -> bool: return self.__state is ProviderState.READY
    __state: ProviderState = ProviderState.UNINITIALIZED