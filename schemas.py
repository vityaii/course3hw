from pydantic import BaseModel, field_validator, ConfigDict
from typing import List
import re

# Базовая модель для оценки
class GradeBase(BaseModel):
    subject: str  # Предмет
    score: int  # Оценка

    # Валидатор для проверки названия предмета
    @field_validator("subject")
    def validate_subject(cls, value):
        if not re.match(r"^[a-zA-Z\s\-]+$", value):  # Проверяем, что предмет содержит только буквы, пробелы и дефисы
            raise ValueError("Subject must only contain letters, spaces, and hyphens")
        return value

    # Валидатор для проверки оценки
    @field_validator("score")
    def validate_score(cls, value):
        if not (0 <= value <= 100):  # Проверяем, что оценка находится в диапазоне от 0 до 100
            raise ValueError("Score must be between 0 and 100")
        return value


# Модель для создания оценки
class GradeCreate(GradeBase):
    pass


# Модель для отображения оценки
class Grade(GradeBase):
    id: int  # Уникальный идентификатор оценки
    student_id: int  # ID студента, которому принадлежит эта оценка

    # Настройка для поддержки работы с SQLAlchemy
    model_config = ConfigDict(from_attributes=True)


# Базовая модель для студента
class StudentBase(BaseModel):
    name: str  # Имя студента
    age: int  # Возраст студента

    # Валидатор для проверки имени студента
    @field_validator("name")
    def validate_name(cls, value):
        if not re.match(r"^[a-zA-Z\s]+$", value):  # Проверяем, что имя содержит только буквы и пробелы
            raise ValueError("Name must only contain letters and spaces")
        return value

    # Валидатор для проверки возраста студента
    @field_validator("age")
    def validate_age(cls, value):
        if not (1 <= value <= 120):  # Проверяем, что возраст находится в диапазоне от 1 до 120
            raise ValueError("Age must be between 1 and 120")
        return value


# Модель для создания студента
class StudentCreate(StudentBase):
    pass


# Модель для отображения студента
class Student(StudentBase):
    id: int  # Уникальный идентификатор студента
    grades: List[Grade] = []  # Список оценок студента

    # Настройка для поддержки работы с SQLAlchemy
    model_config = ConfigDict(from_attributes=True)