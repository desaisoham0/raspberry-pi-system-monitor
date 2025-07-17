# Raspberry Pi System Monitor

A comprehensive, object-oriented system monitoring application for Raspberry Pi devices that provides real-time metrics and visualizations through a web-based dashboard.

![Python Tests](https://github.com/yourusername/raspberry-pi-system-monitor/actions/workflows/python-tests.yml/badge.svg)

## Features

- **Real-time System Monitoring**:
  - CPU usage and speed
  - RAM usage (total, used, free)
  - Disk usage (total, used, free)
  - CPU temperature
  - Core count and details
  - Hardware model information
  
- **Device Management**:
  - USB device monitoring
  - Storage device information
  
- **System Events**:
  - Login/logout event tracking
  
- **Interactive Dashboard**:
  - Built with Streamlit for a responsive UI
  - Visualizations using Plotly
  - Customizable refresh rates
  
- **Logging System**:
  - Comprehensive logging of system activities
  - Configurable log levels
  
- **Modular Architecture**:
  - Object-oriented design with inheritance
  - Easy to extend with new system components

## Requirements

- Python 3.11+
- Raspberry Pi (tested on Raspberry Pi 4)
- Required packages (see requirements.txt):
  - psutil
  - streamlit
  - plotly
  - pandas

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/desaisoham0/raspberry-pi-system-monitor.git
   cd raspberry-pi-system-monitor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Monitoring

For basic command-line monitoring:

```bash
python main.py
```

This will display a simple output of all system metrics.

### Dashboard Interface

To start the interactive dashboard:

```bash
streamlit run dashboard.py
```

The dashboard will be available at `http://localhost:8501` or the IP address of your Raspberry Pi if accessing from another device on the network.

## Project Structure

```
├── cache_manager.py      # Caching functionality
├── config.py             # Configuration settings
├── dashboard.py          # Web-based UI using Streamlit
├── logger.py             # Logging functionality
├── main.py               # Command-line entry point
├── requirements.txt      # Project dependencies
├── system_component.py   # Abstract base class for system components
├── system_monitor.py     # Main system monitoring class
│
├── device/               # Device-related components
│   ├── storage.py        # Storage device monitoring
│   └── usb.py            # USB device monitoring
│
├── hardware/             # Hardware-related components
│   └── model.py          # Hardware model information
│
├── logs/                 # Log file directory
│
├── system_events/        # System event tracking
│   └── login_logout_events.py  # Login/logout event monitoring
│
├── system_information/   # System metrics components
│   ├── core.py           # CPU core information
│   ├── cpu.py            # CPU usage and metrics
│   ├── disk_usage.py     # Disk space usage
│   ├── ram.py            # Memory usage
│   └── temperature.py    # Temperature monitoring
│
└── tests/                # Unit tests
    ├── __init__.py
    └── test_system_monitor.py
```

## Extending the System

The modular design makes it easy to add new monitoring components:

1. Create a new class that inherits from `SystemComponent`
2. Implement the required methods: `get_usage()` and `get_formatted_usage()`
3. Add an instance of your component to the `SystemMonitor` class

Example:
```python
from system_component import SystemComponent

class NetworkMonitor(SystemComponent):
    def get_usage(self):
        # Implementation for gathering network statistics
        pass
    
    def get_formatted_usage(self):
        # Format the network statistics for display
        pass
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built using [psutil](https://github.com/giampaolo/psutil) for system metrics
- Dashboard created with [Streamlit](https://streamlit.io/)
- Visualizations powered by [Plotly](https://plotly.com/python/)
