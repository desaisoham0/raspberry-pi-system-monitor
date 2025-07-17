from system_information.cpu import CPU
from system_information.ram import RAM
from system_information.disk_usage import DiskUsage
from system_information.temperature import Temperature
from system_information.core import Core
from hardware.model import Model
from device.usb import USB
from device.storage import Storage
from system_events.login_logout_events import Events
from system_component import SystemComponent
from typing import Dict, List, Optional
from logger import Logger


class SystemMonitor:
    def __init__(self, components: Optional[Dict[str, SystemComponent]] = None):
        # Set up logger
        self.logger = Logger.get_logger()
        
        # Use provided components or create default ones
        if components is None:
            self.cpu_info = CPU()
            self.core_info = Core()
            self.ram_info = RAM()
            self.disk_info = DiskUsage()
            self.temperature_info = Temperature()
            self.model_info = Model()
            self.usb_info = USB()
            self.storage_info = Storage()
            self.events = Events()
        else:
            self.cpu_info = components.get('cpu', CPU())
            self.core_info = components.get('core', Core())
            self.ram_info = components.get('ram', RAM())
            self.disk_info = components.get('disk', DiskUsage())
            self.temperature_info = components.get('temperature', Temperature())
            self.model_info = components.get('model', Model())
            self.usb_info = components.get('usb', USB())
            self.storage_info = components.get('storage', Storage())
            self.events = components.get('events', Events())
            
        self.logger.info("SystemMonitor initialized")

    def get_all_usage(self):
        return {
            'cpu': self.cpu_info.get_formatted_usage(),
            'cpu_speed': self.cpu_info.get_speed(),
            'ram': self.ram_info.get_formatted_usage(),
            'disk': self.disk_info.get_formatted_usage(),
            'temperature': self.temperature_info.get_formatted_usage(),
            'core_count': self.core_info.get_usage(),
            'model': self.model_info.get_formatted_usage(),
            'usb_devices': self.usb_info.get_formatted_usage(),
            'storage': self.storage_info.get_formatted_usage(),
            'events': self.events.get_formatted_usage()
        }
    
    def display_all_usage(self):
        usage = self.get_all_usage()
        print("=== System Monitor ===")
        print("CPU Usage:", usage['cpu'])
        print("CPU Speed:", usage['cpu_speed'])
        print("RAM Usage:", usage['ram'])
        print("Disk Usage:", usage['disk'])
        print("Temperature:", usage['temperature'])
        print("Core Count:", usage['core_count'])
        print("Model:", usage['model'])
        print("USB Devices:", usage['usb_devices'])
        print("Storage Information:", usage['storage'])
        print("Login/Logout Events:", usage['events'])
        
    def update_component(self, component_name: str, component: SystemComponent) -> bool:
        """
        Update a specific system component.
        
        Args:
            component_name: Name of the component to update
            component: New component instance
            
        Returns:
            bool: True if the component was updated, False otherwise
        """
        try:
            if component_name == 'cpu':
                self.cpu_info = component
            elif component_name == 'core':
                self.core_info = component
            elif component_name == 'ram':
                self.ram_info = component
            elif component_name == 'disk':
                self.disk_info = component
            elif component_name == 'temperature':
                self.temperature_info = component
            elif component_name == 'model':
                self.model_info = component
            elif component_name == 'usb':
                self.usb_info = component
            elif component_name == 'storage':
                self.storage_info = component
            elif component_name == 'events':
                self.events = component
            else:
                self.logger.warning(f"Unknown component: {component_name}")
                return False
                
            self.logger.info(f"Component {component_name} updated")
            return True
        except Exception as e:
            self.logger.error(f"Error updating component {component_name}: {e}")
            return False