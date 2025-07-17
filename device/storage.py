import psutil
from system_component import SystemComponent

class Storage(SystemComponent):
    def get_usage(self):
        devices = []
        partitions = psutil.disk_partitions(all=False)
        for p in partitions:
            # Filter out system partitions
            devices.append({
                'device': p.device,
                'mountpoint': p.mountpoint,
                'fstype': p.fstype,
                'opts': p.opts
            })
        return devices
    
    def get_formatted_usage(self):
        devices = self.get_usage()
        if not devices:
            return "No storage devices found"
        lines = []
        for d in devices:
            lines.append(f"{d['device']} mounted on {d['mountpoint']} ({d['fstype']})")
        return "\n".join(lines)