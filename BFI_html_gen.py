""" python code to generate the html for the survey based on BFI (the 44 questions survey)
"""



templaterow = ["\n\t<qc>\n\t\t<question>\n\t\t", "\t\t</question>\n\t\t<choice>\n","\t\t</choice>\n\t</qc>\n"]
h_templaterow = ["\n\t<qc class='header_qc'>\n\t\t<question>\n\t\t", "\t\t</question>\n\t\t<choice>\n","\t\t</choice>\n\t</qc>\n"]


def format_choice(ranktype, qind):
    """

    :param ranktype: positive or negative ranking
    :param qind: question index
    :return: html for question answers form
    """
    if ranktype == "+":
        return "".join(["\t\t\t<div><input type='radio' name ='" + "q" + str(qind) + "' value='" + str(aind+1) + "'></div>\n" for aind in range(5)])
    elif ranktype == "-":
        return "".join(["\t\t\t<div><input type='radio' name ='" + "q" + str(qind) + "' value='" + str(5-aind) + "'></div>\n" for aind in range(5)])



def format_questions(file):
    """ extracts questions from textfile and builds htmlpage from them

    :param file: textfile with questions
    :return: string for htmlfile
    """
    newfile = ""
    for qind, line in enumerate(open(file)):
        sline = line.split(';')
        ranktype, question = sline[0], sline[1]
        newfile += templaterow[0] + question + templaterow[1] + format_choice(ranktype, qind) + templaterow[2]
    return newfile




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
    """
    :return: string, questionaire header
    """
    return """
    <h1>
    The Big Five Inventory(BFI)
    </h1>
    <p>
    Here are a number of characteristics that may or may not apply to you.For example, do you agree that you are someone who likes to spend time with others?\nPlease indicate the extent to which you agree or disagree with that statement.
    </p>
    """


qfile = "questions.txt"

start_new = "<maincontainer>\n\t<empty></empty>\n\t<middle_wrapper>\n\t\t<test_heading>" + questionaire_header() + "</test_heading>\n\t\t\t<form action='submit_BFI.php' method='post'>"
end_new = "\n\t\t\t<input type='submit' value='Submit'>\n\t\t\t</form>\n\t\t<empty></empty>\t</middle_wrapper>\n\t<empty></empty>\n</maincontainer>"

print(questionaire_header())

with open("htmlfile.html", 'w+') as wf:

    tot = start_new + table_header() + format_questions(qfile) + end_new
    wf.write(tot)
