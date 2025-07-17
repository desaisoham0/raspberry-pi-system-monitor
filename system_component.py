from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union

class SystemComponent(ABC):
    @abstractmethod
    def get_usage(self) -> Any:
        """
        Get raw system information.
        
        Returns:
            Any: Raw system data in various formats depending on the component.
        """
        pass
    
    @abstractmethod
    def get_formatted_usage(self) -> Union[str, Dict, List]:
        """
        Get formatted system information suitable for display.
        
        Returns:
            Union[str, Dict, List]: Formatted system data ready for display.
        """
        pass