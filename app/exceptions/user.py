from fastapi import HTTPException
from starlette import status

username_already_taken_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Username already taken"
)

professor_without_institute_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Professor without institute"
)
