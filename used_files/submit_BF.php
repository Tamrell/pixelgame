<?php
function truesubmit(){
    session_start();
    $id = session_id();
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "big_five_research";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    $sql = "INSERT INTO bfi_results (userID, q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43) VALUES ('$id', $_POST[q0],$_POST[q1],$_POST[q2],$_POST[q3],$_POST[q4],$_POST[q5],$_POST[q6],$_POST[q7],$_POST[q8],$_POST[q9],$_POST[q10],$_POST[q11],$_POST[q12],$_POST[q13],$_POST[q14],$_POST[q15],$_POST[q16],$_POST[q17],$_POST[q18],$_POST[q19],$_POST[q20],$_POST[q21],$_POST[q22],$_POST[q23],$_POST[q24],$_POST[q25],$_POST[q26],$_POST[q27],$_POST[q28],$_POST[q29],$_POST[q30],$_POST[q31],$_POST[q32],$_POST[q33],$_POST[q34],$_POST[q35],$_POST[q36],$_POST[q37],$_POST[q38],$_POST[q39],$_POST[q40],$_POST[q41],$_POST[q42],$_POST[q43])";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}

function check_form() {
    $fills = array("q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", "q27", "q28", "q29", "q30", "q31", "q32", "q33", "q34", "q35", "q36", "q37", "q38", "q39", "q40", "q41", "q42", "q43");
    $foundkeys = array();
    $foundvalues = array();
    $baseline = array();

    foreach ($fills as $key){
        if (isset($_POST[$key])) {
            array_push($foundkeys, $key);
            array_push($foundvalues, $_POST[$key]);
        }
    }
    if( sizeof($foundkeys) == sizeof($fills)) {
        truesubmit();
        header('Location: ./thanks.html');
    } else {
        echo implode(",", $foundkeys);
        echo "<br><br>";
        echo implode(",", $foundvalues);
        echo "<br><br>";
        echo implode("|", $fills);
        echo (string) sizeof($fills);
        echo "= size fills <br>";
        echo (string) sizeof($foundkeys);
        echo "= size foundkeys <br>";
    }
    return "qwertyuiop[oiuytrewqwertyuiopoiuytrewqwertyuio]";
}
?>
