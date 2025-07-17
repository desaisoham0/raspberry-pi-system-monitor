"""
Logging module for the system monitor.
"""

import logging
import os
from datetime import datetime

class Logger:
    _instance = None
    _logger = None
    
    @classmethod
    def get_logger(cls):
        if cls._logger is None:
            # Create a logs directory if it doesn't exist
            logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
            os.makedirs(logs_dir, exist_ok=True)
            
            # Set up logging
            log_filename = os.path.join(logs_dir, f"system_monitor_{datetime.now().strftime('%Y%m%d')}.log")
            
            # Configure the logger
            cls._logger = logging.getLogger('system_monitor')
            cls._logger.setLevel(logging.INFO)
            
            # Create file handler
            file_handler = logging.FileHandler(log_filename)
            file_handler.setLevel(logging.INFO)
            
            # Create console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.WARNING)
            
            # Create formatter and add it to the handlers
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            
            # Add the handlers to the logger
            cls._logger.addHandler(file_handler)
            cls._logger.addHandler(console_handler)
        
        return cls._logger
