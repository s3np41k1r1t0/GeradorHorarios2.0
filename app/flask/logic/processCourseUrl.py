import sys
import urllib.parse as urllib
from logic.tt_parser import *
from logic.tt_generator import *
from logic.tt_prettyprinter import *

def processCourseUrl(url,course_id):
    parser = HTMLCourseParser(url)
    course = parser.parse()

    html_result = "<div style='align-self:center;'id='coursediv" + str(course_id) + "' >"
    html_result += "<b style='font-size: 22px; margin-right: 10px'>%s </b>" % (course.long_name)
    #html_result += "<span class='greytxt' style='font-size: 14px;'> (%s) </span>" % (course.name)

    block_id = 0
    sorted_blocks = sorted(course.lesson_blocks, key=lambda x: x.category, reverse=True)
    for block in sorted_blocks:
        block_id += 1
        html_result += "<input type='checkbox' id='course%itype%i' name='course%itype%i' value='%s' checked><label for='course%itype%i' style='font-size: 17px'>%s</label>" \
                       % (course_id, block_id, course_id, block_id, block.category, course_id, block_id, block.category)

    html_result += "<a href='#' class='fas fa-times' style='align-items: center;inline-size: 0' onclick='removeCourse(coursediv" + str(course_id) + ")'></a>"
    html_result += "<input type='hidden' name='course%i' value='%s'>" % (course_id, url)

    html_result += "</div>"

    return html_result

if __name__ == "__main__":
    course_id = int(sys.argv[1])
    url = urllib.unquote(sys.argv[2])
    print(processCourseUrl(url,course_id))
