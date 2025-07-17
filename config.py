"""
Configuration manager for the system monitor.
"""

class Config:
    # Temperature settings
    TEMP_FILE_PATH = '/sys/class/thermal/thermal_zone0/temp'
    
    # Model information
    MODEL_FILE_PATH = '/proc/device-tree/model'
    
    # Event logging
    EVENT_COUNT = 10
    
    # File system path for disk usage
    ROOT_PATH = '/'
    
    # CPU measurement interval (seconds)
    CPU_INTERVAL = 1
    
    @classmethod
    def get(cls, setting, default=None):
        """
        Get a configuration setting.
        
        Args:
            setting: The name of the setting to retrieve
            default: Default value if setting is not found
            
        Returns:
            The setting value or default if not found
        """
        return getattr(cls, setting, default)
