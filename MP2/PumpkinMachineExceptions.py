# DO NOT EDIT

class OutOfStockException(Exception):  # DO NOT EDIT
    """Raised when something is out of stock"""
    pass


class NeedsCleaningException(Exception):  # DO NOT EDIT
    """Raised when the pumpkin machine needs cleaning"""
    pass


class InvalidChoiceException(Exception):  # DO NOT EDIT
    """Raised when an invalid choice is picked"""
    pass


class ExceededRemainingChoicesException(Exception):  # DO NOT EDIT
    """Raised when there are too many choices"""
    pass


class InvalidPaymentException(Exception):  # DO NOT EDIT
    """Raised when an invalid payment amount is given"""
    pass


class InvalidStageException(Exception):  # DO NOT EDIT
    """Raised when an action occurs in the wrong stage"""
    pass
# DO NOT EDIT
