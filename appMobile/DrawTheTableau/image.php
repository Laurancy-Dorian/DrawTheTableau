<div style="display:flex;justify-content:center">
<?php

$folder = "/home/dodo/DrawTheTableau/img/";
$files = scandir($folder, SCANDIR_SORT_DESCENDING);
$newest_file = $files[0];
copy ($folder.$newest_file, "lastImg/img.jpg");
echo '<img style="width:500px;height:500px" src="lastImg/img.jpg"/>';
?>
</div>
