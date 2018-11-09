<?php
function imgsubmit(){
    session_start();
    $id = session_id();
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "big_five_research";
    $a = $_POST['a'];
    $b = $_POST['b'];
    $c = $_POST['c'];
    $d = $_POST['d'];
    $e = $_POST['e'];
    $f = $_POST['f'];
    $g = $_POST['g'];
    $h = $_POST['h'];
    $i = $_POST['i'];
    $imgchoice = $_POST['imgchoice'];
    $choicenumbr = $_POST['choicenumbr'];

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    $sql = "INSERT INTO pixelgame_table (userID, a, b, c, d, e, f, g, h, i, imgchoice, choicenumbr) VALUES ('$id', '$a', '$b', '$c', '$d', '$e', '$f', '$g', '$h', '$i', '$imgchoice', '$choicenumbr')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
    $conn->close();
}
imgsubmit();
?>
