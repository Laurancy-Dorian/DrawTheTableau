<?php
/**
      DrawTheTableau
    Interface entre la Raspberry
    et l'application mobile
*/

// Fichier d'ecriture d'instruction
$in_file = 'instruction.txt';

// Fichier de lecture
$out_file = 'instruction.txt';

// Si une information a ete envoye depuis l'application, les donnees sont enregistrees dans le fichier
if ($_POST) {
  file_put_contents($in_file, file_get_contents('php://input'));
}

// Lis le fichier de donnees
$msg = readfile($out_file);

// Envoie les donnees
print substr($msg, 0, -1);
?>
