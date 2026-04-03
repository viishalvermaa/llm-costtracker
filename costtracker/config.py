import os
import tomllib

DEFAULT_CONFIG = {
    "budget":None,
    "log_file":None,
    "provider":"gemini"
}

def load_config(config_path:str = "costtracker.toml")->dict:
    """
    Load configuration from TOML file.
    If file does not exist or is invalid, return default config.
    """

    # Default config
    config=DEFAULT_CONFIG.copy()

    # Check if config file exists
    if not os.path.exists(config_path):
        return config
    
    try:
        with open(config_path, "rb") as f:
            file_config=tomllib.load(f)

        # Merge file config into default config
        config.update(file_config)
    
    except Exception:
        # Fail silently 
        pass

    return config