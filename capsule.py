from pydantic import BaseModel, field_validator


class Capsule(BaseModel):
    nom: str
    taille: int
    couleur: str

    @field_validator("nom", "couleur")
    @classmethod
    def string_validator(cls, value: str) -> str:
        if not value.isalpha():
            raise ValueError("must be a string")
        if " " in value:
            raise ValueError("must not contain a space")
        return value

    @field_validator("taille")
    @classmethod
    def taille_validator(cls, value: int) -> int:
        if value < 0:
            raise ValueError("must be a positive integer")
        return value

    def is_valid_for_nespresso(self):
        return self.taille == 40