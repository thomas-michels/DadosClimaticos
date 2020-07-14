
from werkzeug.exceptions import HTTPException, UnprocessableEntity, NotFound


class BadRequestException(HTTPException):
    def __init__(self, msg: str = 'Bad Request Exception'):
        super().__init__(description=msg)
        self.code = 400


class NotFoundException(NotFound):
    def __init__(self, msg: str = 'Not Found Exception'):
        super().__init__(description=msg)
        self.code = 404


class UnprocessableEntityException(UnprocessableEntity):
    def __init__(self, msg: str = 'Invalid Date Exception'):
        super().__init__(description=msg)
        self.code = 422
