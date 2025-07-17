# filepath: /home/pi/Desktop/oop/dashboard.py
import streamlit as st
import time
import pandas as pd
import plotly.express as px
from system_monitor import SystemMonitor
from logger import Logger

# Configure the page
st.set_page_config(
    page_title="Raspberry Pi System Monitor",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set up logger
logger = Logger.get_logger()

# Initialize system monitor
monitor = SystemMonitor()

# Add sidebar
st.sidebar.title("System Monitor")
st.sidebar.info("Real-time monitoring of your Raspberry Pi system resources.")

# Add refresh rate selector
refresh_rate = st.sidebar.slider(
    "Refresh Rate (seconds)",
    min_value=1,
    max_value=60,
    value=5
)

# Add refresh button
refresh = st.sidebar.button("Refresh Data")

# Function to get system data
@st.cache_data(ttl=refresh_rate)
def get_system_data():
    try:
        return monitor.get_all_usage()
    except Exception as e:
        logger.error(f"Error getting system data: {e}")
        return None

# Main content
st.title("Raspberry Pi System Monitor Dashboard")

# Get system data
usage = get_system_data()

if usage:
    # Create three columns for main metrics
    col1, col2, col3 = st.columns(3)
    
    # CPU Info
    with col1:
        st.subheader("CPU")
        # Create a gauge for CPU usage
        if isinstance(usage['cpu'], str) and "%" in usage['cpu']:
            cpu_value = float(usage['cpu'].split(":")[1].strip().replace("%", ""))
            fig = px.pie(values=[cpu_value, 100-cpu_value], 
                        names=['Used', 'Free'], 
                        hole=0.7, 
                        color_discrete_sequence=['#FF4B4B', '#F0F2F6'])
            fig.update_layout(
                annotations=[dict(text=f"{cpu_value}%", x=0.5, y=0.5, font_size=20, showarrow=False)],
                showlegend=False,
                margin=dict(l=0, r=0, t=0, b=0),
                height=200
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write(usage['cpu'])
        
        st.metric("CPU Speed", usage['cpu_speed'])
        st.metric("Cores", usage['core_count'][0] if isinstance(usage['core_count'], list) else usage['core_count'])
    
    # RAM Info
    with col2:
        st.subheader("Memory")
        if isinstance(usage['ram'], dict) and 'percent' in usage['ram']:
            ram_percent = float(usage['ram']['percent'].replace("%", ""))
            fig = px.pie(values=[ram_percent, 100-ram_percent], 
                        names=['Used', 'Free'], 
                        hole=0.7, 
                        color_discrete_sequence=['#4B73FF', '#F0F2F6'])
            fig.update_layout(
                annotations=[dict(text=usage['ram']['percent'], x=0.5, y=0.5, font_size=20, showarrow=False)],
                showlegend=False,
                margin=dict(l=0, r=0, t=0, b=0),
                height=200
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.metric("Total RAM", usage['ram']['total'])
            st.metric("Used RAM", usage['ram']['used'])
        else:
            st.write(usage['ram'])
    
    # Disk Info
    with col3:
        st.subheader("Disk")
        if isinstance(usage['disk'], dict) and 'percent' in usage['disk']:
            disk_percent = float(usage['disk']['percent'].replace("%", ""))
            fig = px.pie(values=[disk_percent, 100-disk_percent], 
                        names=['Used', 'Free'], 
                        hole=0.7, 
                        color_discrete_sequence=['#49D49D', '#F0F2F6'])
            fig.update_layout(
                annotations=[dict(text=usage['disk']['percent'], x=0.5, y=0.5, font_size=20, showarrow=False)],
                showlegend=False,
                margin=dict(l=0, r=0, t=0, b=0),
                height=200
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.metric("Total Disk", usage['disk']['total'])
            st.metric("Used Disk", usage['disk']['used'])
        else:
            st.write(usage['disk'])
    
    # Create two columns for additional info
    col1, col2 = st.columns(2)
    
    # Temperature
    with col1:
        st.subheader("Temperature")
        if isinstance(usage['temperature'], str) and "°C" in usage['temperature']:
            temp_value = float(usage['temperature'].split(":")[1].strip().replace("°C", ""))
            st.metric("CPU Temperature", f"{temp_value} °C")
            
            # Create a gauge for temperature
            if temp_value > 0:
                # Color based on temperature range
                if temp_value < 50:
                    color = "green"
                elif temp_value < 70:
                    color = "orange"
                else:
                    color = "red"
                    
                st.progress(min(temp_value / 100, 1.0))
        else:
            st.write(usage['temperature'])
            
        st.subheader("Hardware")
        st.info(usage['model'])
        
    # System Info
    with col2:
        st.subheader("Storage Devices")
        st.code(usage['storage'])
        
        st.subheader("USB Devices")
        st.code(usage['usb_devices'])
    
    # Login/Logout Events
    st.subheader("Recent System Events")
    st.code(usage['events'])
    
    # Add timestamp
    st.caption(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    st.error("Error retrieving system data. Please check the logs for details.")