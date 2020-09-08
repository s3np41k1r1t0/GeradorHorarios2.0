import sys
import urllib
from logic.tt_parser import *
from logic.tt_generator import *
from logic.tt_prettyprinter import *
from logic.tt_errorprinter import *

def is_url(arg):
    return arg[0:4] == "http"

def generate(argv):
    lesson_blocks = []

    for arg in argv:
        if is_url(arg):
            current_course = HTMLCourseParser(arg).parse()
        else:
            lesson_blocks.append(current_course.get_block_by_category(arg))

    generator = TimetableGenerator()
    generator.generate_timetables(lesson_blocks)

    generator.generated.sort(key=Timetable.total_time)

    if generator.generated:
        printer = HTMLPrettyPrinter()
        return printer.print_timetables(generator.generated, generator.total_combinations)
    else:
        printer = HTMLErrorPrinter()
        return printer.no_timetables()

if __name__ == "__main__":
    main(sys.argv)
