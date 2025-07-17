"""
Unit tests for SystemMonitor class.
"""

import unittest
from unittest.mock import MagicMock, patch
from system_monitor import SystemMonitor
from system_component import SystemComponent

class MockComponent(SystemComponent):
    """Mock implementation of SystemComponent for testing."""
    
    def __init__(self, usage_value, formatted_value):
        self.usage_value = usage_value
        self.formatted_value = formatted_value
    
    def get_usage(self):
        return self.usage_value
    
    def get_formatted_usage(self):
        return self.formatted_value

class TestSystemMonitor(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        # Create mock components
        self.mock_cpu = MockComponent(50, "CPU Usage: 50%")
        self.mock_ram = MockComponent(
            {"total": 8, "used": 4, "percent": 50},
            {"total": "8.00 GB", "used": "4.00 GB", "percent": "50%"}
        )
        self.mock_disk = MockComponent(
            {"total": 32, "used": 16, "percent": 50},
            {"total": "32.00 GB", "used": "16.00 GB", "percent": "50%"}
        )
        self.mock_temp = MockComponent(45.5, "CPU Temperature: 45.50°C")
        self.mock_core = MockComponent(4, ["4"])
        self.mock_model = MockComponent("Raspberry Pi 4", "Device Model: Raspberry Pi 4")
        self.mock_usb = MockComponent(["Device 1", "Device 2"], "Device 1\nDevice 2")
        self.mock_storage = MockComponent(
            [{"device": "/dev/sda1", "mountpoint": "/", "fstype": "ext4", "opts": "rw"}],
            "/dev/sda1 mounted on / (ext4)"
        )
        self.mock_events = MockComponent("event1\nevent2", "event1\nevent2")
        
        # Create components dictionary
        self.components = {
            'cpu': self.mock_cpu,
            'core': self.mock_core,
            'ram': self.mock_ram,
            'disk': self.mock_disk,
            'temperature': self.mock_temp,
            'model': self.mock_model,
            'usb': self.mock_usb,
            'storage': self.mock_storage,
            'events': self.mock_events
        }
        
        # Create SystemMonitor with mock components
        self.system_monitor = SystemMonitor(self.components)
        
        # Mock the get_speed method on CPU
        self.system_monitor.cpu_info.get_speed = MagicMock(return_value="1500.00 MHz")
    
    def test_get_all_usage(self):
        """Test that get_all_usage returns the correct data."""
        usage = self.system_monitor.get_all_usage()
        
        # Check that all expected keys are present
        expected_keys = ['cpu', 'cpu_speed', 'ram', 'disk', 'temperature', 
                        'core_count', 'model', 'usb_devices', 'storage', 'events']
        for key in expected_keys:
            self.assertIn(key, usage)
        
        # Check specific values
        self.assertEqual(usage['cpu'], "CPU Usage: 50%")
        self.assertEqual(usage['cpu_speed'], "1500.00 MHz")
        self.assertEqual(usage['ram'], {"total": "8.00 GB", "used": "4.00 GB", "percent": "50%"})
        self.assertEqual(usage['temperature'], "CPU Temperature: 45.50°C")
    
    def test_update_component(self):
        """Test that update_component correctly updates a component."""
        # Create a new mock component
        new_cpu = MockComponent(75, "CPU Usage: 75%")
        
        # Update the CPU component
        result = self.system_monitor.update_component('cpu', new_cpu)
        
        # Check that the update was successful
        self.assertTrue(result)
        
        # Check that the component was updated
        usage = self.system_monitor.get_all_usage()
        self.assertEqual(usage['cpu'], "CPU Usage: 75%")
        
        # Test updating an unknown component
        result = self.system_monitor.update_component('unknown', new_cpu)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
