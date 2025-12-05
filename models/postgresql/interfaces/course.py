from models.postgresql.entities.course import Course

class CourseInterface:    
    async def register_course(self, titulo: str, aulas: int, horas: int) -> None:
        pass
    
    async def get_courses(self) -> list[Course]:
        pass
            