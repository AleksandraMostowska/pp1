from abc import ABC, abstractmethod
import re
from typing import Any

class Validator(ABC):

    @abstractmethod
    def validate(data: Any) -> Any:
        pass

class ContactValidator(Validator):
    PATTERN = '^[A-Z][a-z]+ [A-Z][a-z]+,[a-z\d]+@(onet|o1|google|poczta|gmail|op)\.pl,\d{9}$'

    def validate(data: Any) -> Any:
        return re.match(ContactValidator.PATTERN, data)
