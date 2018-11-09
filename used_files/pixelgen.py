

def makepage():
    htmlstart = """
    <!DOCTYPE html>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0"/>
                <link rel="stylesheet" href="../used_files/CSS/pixelgame.css">
		        <style type="text/css" id="pixelclasses"></style>
                <script src="../used_files/JS/include.js"></script>
                <script src="../used_files/JS/pixelgame.js"></script>
            </head>
            <body onload="create_classes()" style="display: flex;">
            <?php
            session_start();
            ?>
    """
    htmlend = """
            </body>
            </html>"""
    return htmlstart + make_php_piece() + gen_gameframe(8) + htmlend


def make_php_piece():
    return """
    <?php
    include('pixelsave.php');
    ?>
    """


def gen_gameframe(pixels_per_row):
    htmlstring = """<gamecontainer style="margin: 10vh auto;">"""
    alfa = "abcdefghijklmnopqrstuvwxyz"
    for i in range(9):
        #img_start = "<imagecontainer onclick='pixelsclicked(\"" + alfa[i] +"\")' id=\"" + alfa[i] + "\">"
        img_start = "<imagecontainer onclick='pixelsclicked(\"" + alfa[i] + "\")' id=\"" + alfa[i] + "\">"

        img_elems = ""
        for j in range(pixels_per_row**2):
            img_elems += "<div " + gen_class(alfa[i], j) + "</div>"
        htmlstring += img_start + img_elems + "</imagecontainer>"
    return htmlstring

def gen_class(letter, number):
    return "class='" + letter + str(number) + "'>"

with open("testpixel.html", "w+") as of:
    of.write(makepage())
