<?php  
  function fetch_data($string, $start_tag, $end_tag){
  
        $position = stripos($string, $start_tag);  
        
    $str = substr($string, $position);  
        
    $str_second = substr($str, strlen($start_tag));  
        
    $second_positon = stripos($str_second, $end_tag);  
        
    $str_third = substr($str_second, 0, $second_positon);  
        
    $fetch_data = trim($str_third);
        
    return $fetch_data; 
  }

$fh = fopen('x.txt','r') or die($php_errormsg);
$x = fread($fh,filesize('x.txt'));

$x = fetch_data($x, '<post>', '</post>');

print($x);


?>
