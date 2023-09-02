def add_lesson(lesson_title: str) -> list:
    """
    Add the lesson to the end of the schedule if it does not exist.
    :param lesson_title: Lesson title
    :return: Modified course plan
    """
    if course_plan[-1] != lesson_title:
        course_plan.append(lesson_title)
    return course_plan


def insert_lesson(lesson_title: str, lesson_index: int) -> list:
    """
    Insert the lesson to the given index, if it does not exist.
    :param lesson_title: Lesson title
    :param lesson_index: Index of the lesson to be inserted
    :return: Modified course plan
    """
    if lesson_index in range(len(course_plan)):
        if lesson_title not in course_plan:
            if course_plan[lesson_index] != lesson_title:
                course_plan.insert(lesson_index, lesson_title)
    return course_plan


def remove_lesson(lesson_title: str) -> list:
    """
    Remove the lesson, if it exists.
    Each time a lesson is removed, you should do the same with the Exercises, if there are
any following the lessons.
    :param lesson_title: Lesson title
    :return: Modified course plan
    """
    if lesson_title in course_plan:
        lesson_index = course_plan.index(lesson_title)
        if lesson_index + 1 == f"{lesson_title}-Exercise":
            course_plan.pop(lesson_index)
        course_plan.remove(lesson_title)
    return course_plan


def swap_lesson(lesson_title_1: str, lesson_title_2: str) -> list:
    """
    Swap the position of the two lessons if they exist.
    Each time a lesson is swapped, you should do the same with the Exercises, if there are
any following the lessons.
    :param lesson_title_1: First title
    :param lesson_title_2: Second title
    :return: Modified course plan
    """
    if lesson_title_1 in course_plan and lesson_title_2 in course_plan:
        index_1 = course_plan.index(lesson_title_1)
        index_2 = course_plan.index(lesson_title_2)
        if index_1 in range(len(course_plan)) and index_2 in range(len(course_plan)):
            course_plan[index_1], course_plan[index_2] = course_plan[index_2], course_plan[index_1]
            if f'{lesson_title_1}-Exercise' in course_plan and f'{lesson_title_2}-Exercise' in course_plan:
                index_1_ex = course_plan.index(f'{lesson_title_1}-Exercise')
                index_2_ex = course_plan.index(f'{lesson_title_2}-Exercise')
                course_plan[index_1_ex], course_plan[index_2_ex] = course_plan[index_2_ex], course_plan[index_1_ex]
            elif f'{lesson_title_1}-Exercise' in course_plan:
                index_1_ex = course_plan.index(f'{lesson_title_1}-Exercise')
                course_plan.insert(index_2 + 1, f'{lesson_title_1}-Exercise')
                course_plan.pop(index_1_ex)
            elif f'{lesson_title_2}-Exercise' in course_plan:
                course_plan.remove(f'{lesson_title_2}-Exercise')
                course_plan.insert(index_1 + 1, f'{lesson_title_2}-Exercise')
        return course_plan


def exercise_lesson(lesson_title: str) -> list:
    """
     Add Exercise in the schedule right after the lesson index, if the lesson
exists and there is no exercise already, in the following format "{lessonTitle}-Exercise". If the
lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.
    :param lesson_title: Lesson title
    :return: Modified course plan
    """

    if lesson_title not in course_plan:
        course_plan.append(lesson_title)
        course_plan.append(f"{lesson_title}-Exercise")

    else:
        lesson_index = course_plan.index(lesson_title)
        if f"{lesson_title}-Exercise" not in course_plan:
            if lesson_index == len(course_plan) - 1:
                course_plan.append(f"{lesson_title}-Exercise")
            elif course_plan[lesson_index + 1] != f"{lesson_title}-Exercise":
                course_plan.insert(lesson_index + 1, f"{lesson_title}-Exercise")

    return course_plan


course_plan = input().split(', ')
command = input()

while command != 'course start':
    command = command.split(':')
    if command[0] == 'Add':
        title = command[1]
        add_lesson(title)
    elif command[0] == 'Insert':
        title = command[1]
        index = int(command[2])
        insert_lesson(title, index)
    elif command[0] == 'Remove':
        title = command[1]
        remove_lesson(title)
    elif command[0] == 'Swap':
        title_1 = command[1]
        title_2 = command[2]
        swap_lesson(title_1, title_2)
    elif command[0] == 'Exercise':
        title = command[1]
        exercise_lesson(title)
    command = input()

for index, element in enumerate(course_plan):
    print(f"{index + 1}.{element}")
