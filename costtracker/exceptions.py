class CostTrackerError(Exception):
    """Base exception for costtracker"""
    pass

class UnsupportedModelError(CostTrackerError):
    """Raised when model pricing is not available"""
    pass

class InvalidResponseError(CostTrackerError):
    """Raised when response format is invalid"""
    pass
