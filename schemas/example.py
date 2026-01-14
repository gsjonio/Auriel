"""
Example Pydantic schema.

:module: schemas.example
"""

from pydantic import BaseModel


class ExampleSchema(BaseModel):
    """
    Example schema used for demonstration.

    :param message: sample text
    """

    message: str
