<?php
$fp = fopen("/tmp/tempfile", "w");
$data = $_REQUEST['temp'];
fwrite($fp, $data);
fclose($fp);

$fp = fopen("/tmp/tempdata", "a");
fwrite($fp, $data."\n");
fclose($fp);

?>
