# NEON PRO ENGINE: New App Instance Generator
import os

def create_fresh_project(app_name, package_name):
    # Generating unique build environment
    build_settings = {
        "title": app_name,
        "package": package_name,
        "icon": "assets/custom_icon.png", # Unique icon handle
        "version": "1.0.0"
    }
    return build_settings

# New App Config
app_config = create_fresh_project("NeonTool_001", "com.neonpro.tool001")
print(f"Starting {app_config['title']} with {app_config['package']}...")
