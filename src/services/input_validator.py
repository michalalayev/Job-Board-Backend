from abc import ABC, abstractmethod
from domain.job_entity import Status
from schemas.job_schemas import JobCreationAPIModel, JobUpdateAPIModel


class IInputValidator(ABC):
    @abstractmethod
    def validate_status(self) -> bool:
        pass


class InputValidator(IInputValidator):
    def __init__(self, input_model: JobCreationAPIModel | JobUpdateAPIModel):
        self.__input_model = input_model

    # Pydantic validates the types on its own so no need
    def validate_status(self) -> bool:
        input_status = self.__input_model.status
        if input_status is None:
            return True
        if input_status in Status._value2member_map_:
            return True
        return False
        # values = [member.value for member in Status]
