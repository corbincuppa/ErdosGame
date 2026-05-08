<?php
// Read form inputs
# ---------------------- AI --------------------------------------
$order        = $_POST['order'];
$startGraph   = $_POST['startGraph'];
$redGraph     = $_POST['redGraphb'];   
$blueGraph    = $_POST['blueGraph'];
$threads      = $_POST['threads'];
$startPlayer  = $_POST['start_player'];
$bias         = $_POST['bias'];

// Escape arguments to avoid shell injection
$cmd = escapeshellcmd("python3 ./parse_form.py "
    . "$order "
    . "$startGraph "
    . "$redGraph "
    . "$blueGraph "
    . "$threads "
    . "$startPlayer "
    . "$bias"
);

?>