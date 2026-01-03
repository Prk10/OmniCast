from abc import ABC, abstractmethod

class DocumentRenderer(ABC):
    @abstractmethod
    def render(self, html_content: str) -> bytes:
        pass
    @abstractmethod
    def screenshot(self, html_content: str) -> bytes:
        pass