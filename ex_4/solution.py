import json


class Subject:
    """
    A class representing an academic subject.

    Attributes:
        __name (str): The name of the subject.
    """
    def __init__(self, name: str) -> None:
        """
        Initialize a Subject instance.

        Args:
            name (str): The name of the subject.
        """
        self.__name = name

    @property
    def name(self) -> str:
        """
        Get the subject name.

        Returns:
            str: The name of the subject.
        """
        return self.__name


class Teacher:
    """
    A class representing a teacher.

    Attributes:
        __name (str): The name of the teacher.
    """
    def __init__(self, name: str) -> None:
        """
        Initialize a Teacher instance.

        Args:
            name (str): The name of the teacher.
        """
        self.__name = name

    @property
    def name(self) -> str:
        """
        Get the teacher name.

        Returns:
            str: The name of the teacher.
        """
        return self.__name


class Lesson:
    """
    A class representing a scheduled lesson.

    This class combines a subject, teacher, time slot, day of week,
    and room number into a single lesson entity.

    Attributes:
        __subject (Subject): The subject being taught.
        __teacher (Teacher): The teacher conducting the lesson.
        __time (str): The time of the lesson (e.g., "10:00-11:30").
        __day (str): The weekday of the lesson.
        __room (str): The room number where the lesson takes place.
    """

    def __init__(self, subject: 'Subject', teacher: 'Teacher',
                 time: str, day: str, room: str) -> None:
        """
        Initialize a Lesson instance.

        Args:
            subject (Subject): The subject being taught.
            teacher (Teacher): The teacher conducting the lesson.
            time (str): The time of the lesson (e.g., "10:00-11:30").
            day (str): The weekday of the lesson.
            room (str): The room number where the lesson takes place.
        """
        self.__subject = subject
        self.__teacher = teacher
        self.__time = time
        self.__day = day
        self.__room = room

    @property
    def day(self) -> str:
        """
        Get the day of the lesson.

        Returns:
            str: The weekday of the lesson.
        """
        return self.__day

    def __repr__(self):
        """
        Return a string representation of the lesson.

        Returns:
            str: A formatted string with time, subject, teacher, and room.
        """
        return (f'{self.__time} | {self.__subject.name} | '
                f'{self.__teacher.name} | ауд. {self.__room}')


class Schedule:
    """
    A class representing a weekly schedule of lessons.

    This class loads lesson data from a JSON file and displays the schedule
    organized by weekday.

    Attributes:
        _lessons (list[Lesson]): List of all lessons in the schedule.
        __filename (str): The path to the JSON file containing schedule data.
    """
    def __init__(self, filename: str='Schedule.json') -> None:
        """
        Initialize a Schedule instance.

        Args:
            filename (str, optional): The path to the JSON schedule file.
                                     Defaults to 'Schedule.json'.
        """
        self._lessons = []
        self.__filename = filename

    def load(self) -> None:
        """
        Load schedule data from the JSON file.

        Reads the JSON file, parses each entry, and creates Subject, Teacher,
        and Lesson objects. Populates the _lessons list with the created lessons.

        Raises:
            FileNotFoundError: If the schedule file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        with open(self.__filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

            for item in data:
                subject = Subject(item['subject'])
                teacher = Teacher(item['teacher'])

                lesson = Lesson(
                    subject,
                    teacher,
                    item['time'],
                    item['day'],
                    item['room']
                )

                self._lessons.append(lesson)

    def show(self) -> None:
        """
        Display the schedule organized by weekday.

        Prints lessons for each weekday (Monday through Friday) in order.
        For each day, shows all lessons scheduled on that day with their details.
        """
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
        for day in days:
            print(f'\n {day}')
            for lesson in self._lessons:
                if lesson.day == day:
                    print(lesson)
