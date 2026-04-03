LOG_FILE=None

def set_log_file(file_path:str):
    """
    Set log file path
    """

    global LOG_FILE
    LOG_FILE=file_path


def log_output(message:str):
    """
    Print to console + optionally write to file
    """

    print(message)

    # If logging is enabled then write to file
    if LOG_FILE:
        with open(LOG_FILE, "a") as f:
            f.write(message + "\n")