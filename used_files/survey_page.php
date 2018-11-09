<!DOCTYPE html>
<html >
    <head>
        <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="../CSS/bigfive_form.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="../JS/include.js"></script>
    </head>
    <body>

<!-- https://stackoverflow.com/questions/15505225/inject-css-stylesheet-as-string-using-javascript -->

<style>
  .hide { position:absolute; top:-1px; left:-1px; width:0px; height:0px; }
</style>

<?php
include('submit_BF.php');

if($_SERVER['REQUEST_METHOD']=='POST'){
    echo check_form();
}
?>

        <!--<maincontainer w3-include-html="BF_Questions.html"></maincontainer>-->
        <maincontainer w3-include-html="BF.html"><iframe name="hiddenFrame" class="hide"></iframe>
            <?php
            echo check_form();
            ?>

        </maincontainer>
        <script>
            includeHTML();
        </script>
    </body>
</html>
