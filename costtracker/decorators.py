from .tracker import track as track_function

def track(func):
    def wrapper(*args, **kwargs):
        response=func(*args, **kwargs)
        track_function(response)
        return response
    
    return wrapper