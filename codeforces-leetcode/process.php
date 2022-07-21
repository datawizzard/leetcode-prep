<?php
 session_start();
 
$hostname = 'localhost';       
 $dbname   = 'waterbilling';
 $username = 'root';            
 $password = '';       
 
$conn=mysqli_connect($hostname, $username, $password) or DIE('NOT Connected!');
 mysqli_select_db($conn,$dbname) or DIE('Database name is not available!');
 $login = mysqli_query($conn,"SELECT * FROM user WHERE (username = '" .($_POST['username']) . "') and (password = '" .($_POST['password']) . "')");
 $row=mysqli_fetch_array($login);  
 
 if($row){
 $_SESSION['id'] = $row['id'];

 echo '<script>windows: location="billing.php"</script>';
 }
	else {
		header ("location: index.php?err");
		}
 
 
?>
