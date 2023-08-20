<?php

function generateRandomString() {
	$length = 10;
	$characters = "0123456789abcdef";
	$string = "";
	for ($p = 0; $p < $length; $p++) {
		$string .= $characters[mt_rand(0, strlen($characters)-1)];
	}
	return $string;
}

function makeRandomPath($dir, $ext) {
	do {
		$path = $dir."/".generateRandomString().".".$ext;
	}	while (file_exists($path));
	return $path;
}

function makeRandomPathFromFilename($dir, $filename) {
	$ext = pathinfo($filename, PATHINFO_EXTENSION);
	return makeRandomPath($dir, $ext);
}

$upload_status = 1;
$target_path = makeRandomPathFromFilename("uploads", $_FILES["fileupload"]["name"]);

if ($_FILES["fileupload"]["size"] > 1000) {
	echo "File is too big!\n";
	$upload_status = 0;
}

if (move_uploaded_file($_FILES["fileupload"]["tmp_name"], $target_path)) {
	echo "The file <a href=\"$target_path\"> $target_path </a> has been uploaded.\n";
} else {
	echo "There was an error uploading the file, please try again!\n";
	$upload_status = 0;
}

if ($upload_status == 1) {
	echo "Success!\n";
} else {
	echo "Failure!\n";
}

?>
