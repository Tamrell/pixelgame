
from itertools import chain

# Files
qfile = "questions2.txt"
qsfile = "questions2_scoring.txt"

# File extraction
def get_questions(file):
    with open(file, 'r') as q:
        questions = [sq.split('.') for sq in q.readlines()]
        print([q[0] for q in questions][0])
        questions = [[q[0], "I" + q[1][4:].lower()] for q in questions]
        print(questions)
        return questions

def format_choice(q, increasing):
    if increasing:
        return "".join(["\t\t\t<div><input type='radio' name ='" + "q" + str(q) + "' value='" + str(aind+1) + "'></div>\n" for aind in range(5)])
    else:
        return "".join(["\t\t\t<div><input type='radio' name ='" + "q" + str(q) + "' value='" + str(5 - aind) + "'></div>\n" for aind in range(5)])

def get_scoring(score_file):
    with open(score_file, 'r') as sf:
        broad_s = sf.readlines()
        BFA = [line.split('; ') for line in broad_s]
        facets = [[facet[1].split(': ')[1], facet[2].split(': ')[1][:-1]]
                  for facet in BFA]
        scores = [s for s in chain(*facets)]
        scores = [scorelist.split(', ') for scorelist in scores]
        scores = [s for s in chain(*scores)]
        print(scores)
        qdict = {}
        for q in scores:
            if q[-1] == "R":
                qdict[q[:-1]] = False
            else:
                qdict[q] = True
        return qdict


# formatting

templaterow = ["\n\t<qc>\n\t\t<question>\n\t\t", "\t\t</question>\n\t\t<choice>\n","\t\t</choice>\n\t</qc>\n"]
h_templaterow = ["\n\t<qc class='header_qc'>\n\t\t<question>\n\t\t", "\t\t</question>\n\t\t<choice>\n","\t\t</choice>\n\t</qc>\n"]

def table_header():
    """
    :return: string, header for the questions/option table in the survey form
    """
    return h_templaterow[0] + "\tI see Myself as Someone Who:\n" + h_templaterow[1] + likert_header() + h_templaterow[2]

def likert_header():
    """
    :return: string, Likert-scale part of the header for the questions/option table in the survey form
    """
    headings = ["Disaagree strongly", "", "Neither agree not disagree", "", "Agree strongly"]
    return "".join(["\t\t\t<div>" + headings[aind] + "</div>\n" for aind in range(5)])

def questionaire_header():
    return """
    <p>
    Here are a number of characteristics that may or may not describe you.  For example, do you agree that you seldom feel blue, compared to most other people?  Please fill in that which best indicates the extent to which you agree or disagree with each statement listed below. Be as honest as possible, but rely on your initial feeling and do not think too much about each item.
    </p>
    """

start_new = "<maincontainer>\n\t<empty></empty>\n\t<middle_wrapper>\n\t\t<test_heading>" + questionaire_header() + "</test_heading>\n\t\t\t<form action='submit_BFI.php' method='post'>"
end_new = "\n\t\t\t<div style='text-align: center;'><input type='submit' value='Submit'/></div>\n\t\t\t</form>\n\t\t<empty></empty>\t</middle_wrapper>\n\t<empty></empty>\n</maincontainer>"


def format_questions(questions, qdict):
    newfile = ""
    for q in questions:
        increasing = qdict[q[0]]
        newfile += templaterow[0] + q[1] + templaterow[1] + format_choice(q[0], increasing) + templaterow[2]
    return newfile


questions = get_questions(qfile)
qdict = get_scoring(qsfile)
print(qdict.items())
new_html = format_questions(questions, qdict)


with open('BF.html', 'w+') as w:
    tot = start_new + table_header() + new_html + end_new
    w.write(tot)
