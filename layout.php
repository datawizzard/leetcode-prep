<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Water Billing System</title>
<style type="text/css">
#wrapper {
	background:#333; width:800px; margin:0 auto; }
#header { 
background:#000; width:800px; height:100px; }	
#lft { background:#0F0; width:400px; height:300px; float:left; }	
#ryt { background:#999; width:400px; height:300px; float:right; }
</style>
</head>

<body>
<div id="wrapper">
<div id="header"></div>
<div id="lft"> <p><h1>Client Information</h1></p>
  <form method="post">
<table width="332" border="0">
  <tr>
    
    <td width="332"><input type="hidden"  name="id" value="0" /></td>
  </tr>
  <tr>
    <td>Last Name:</td>
    <td><input type="text" name="lname" /></td>
    </tr>
    <tr>
    <td>First Name:</td>
    <td><input type="text" name="fname" /></td>
    </tr>
    <tr>
    <td>MI:</td>
    <td><input type="text" name="mi" /></td>
 
  </tr>
  <tr>
    <td>Address:</td>
    <td><input type="text" name="address" /></td>
  
  </tr>
  <tr>
    <td>Contact #:</td>
    <td><input type="text" name="contact" /></td>
  
  </tr>
   <tr>
    
    <td><input type="submit" name="add" value="ADD" /></td>
  <td><input type="reset" value="CANCEL" /></td>
  </tr>
 
</table>
</form></div>
<div id="ryt">

<?php
$con = mysqli_connect("localhost","root","");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("waterbilling", $con);

$result = mysql_query("SELECT * FROM owners");

echo "<table border='1' bgcolor='#006600'>
<tr>
<th>Id</th>
<th>Firstname</th>
<th>Lastname</th>
<th>Mi</th>
<th>Address</th>
<th>Contact</th>
</tr>";

while($row = mysqli_fetch_array($result))
  {
  echo "<tr>";
  echo "<td>" . $row['id'] . "</td>";
  echo "<td>" . $row['fname'] . "</td>";
  echo "<td>" . $row['lname'] . "</td>";
  echo "<td>" . $row['mi'] . "</td>";
  echo "<td>" . $row['address'] . "</td>";
  echo "<td>" . $row['contact'] . "</td>";
  echo "</tr>";
  }
echo "</table>";

?>

</div>


</body>
</html>
