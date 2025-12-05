from models.postgresql.interfaces.course import CourseInterface
from models.postgresql.settings.connection import DbConnectionHandler
from models.postgresql.entities.course import Course
from sqlalchemy import select

class CourseRepository(CourseInterface):
    def __init__(self, connection:DbConnectionHandler) -> None:
        self.__connection = connection
    
    async def register_course(self, titulo: str, aulas: int, horas: int) -> None:
        async with self.__connection as conn:
            try:
                new_course = Course(titulo = titulo, aulas = aulas, horas = horas)
                conn.session.add(new_course)
                await conn.session.commit()
            except Exception as exception:
                await conn.session.rollback()
                raise exception
    
    async def get_courses(self) -> list[Course]:
        async with self.__connection as conn:
            try:
                query = select(Course)
                course_list = conn.session.execute(query)
                
                return course_list
            except Exception as exception:
                raise exception
            