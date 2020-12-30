<!DOCTYPE html>
<html>
<head>
	<title>Home Page</title>
</head>
<style type="text/css">
	body{
		background-color: white;
	}
	.logo img{
		width:80%;
		height:120px;
	}

 .heading{
		font-family: cursive;
		background-color: #031458;
		  color:white;
		   height: 90px;
		   
		    
	}

	

@media screen and (max-width: 1060px) {
.logo img{
	width: 80%;
	height: 120px;

}
.heading{
	color:white;
	height: 120px;
}
}
@media screen and (max-width: 1018px) {
	.logo img{
	width: 80%;
	height: 120px;

}
.heading{
	color:white;
	padding-top: 10px;
	
	
}

.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 28px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}

marquee img{
	height: 200px;
	width: 200px;
}
}

@media screen and (max-width: 768px) {
	.logo img{
	width: 80%;
	height: 120px;

}
.heading{
	color:white;
	height: 120px;
	
}

.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 25px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}

marquee img{
	height: 160px;
	width: 160px;
}
}
@media screen and (max-width: 668px) {
	.logo img{
	width: 80%;
	height: 120px;

}
 .heading{
	color:white;
	height: 120px;
	text-align: center;
}

.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 23px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}

marquee img{
	height: 140px;
	width: 140px;
}
}
@media screen and (max-width: 568px) {
	.logo img{
	width: 90%;
	height: 100px;
	margin-left:0px; 

}
.heading{
	width:100%;
	height: 100px;
}
.heading h1{
	color:white;
	font-size: 25px;	
	text-align: center;

}
.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 20px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}


marquee img{
	height: 120px;
	width: 120px;
}
}
@media screen and (max-width: 548px) {
	.logo img{
		width: 80%
		height: 100px;
	margin-left:0px; 

}
.heading{
	width:auto;
	height:100px;
	
}
.heading h1{
	color:white;


	padding-left: 30px;
	
}
.heading1 h1{
	width: 100%;
	height: 100%;
	font-size: 20px;
	
}
.image2 img{
	

	width: 100%;
	height: 100%;
}

marquee img{
	height: 100px;
	width: 100px;
}	

}



</style>
<body>
<table width="100%">
	<tr>
		<td colspan  = "2" align="center" width="100%">
			<div class = "logo">
			<img src = "{{url_for('static',filename = 'images/unnamed.png')}}"></div>
		</td>
	</tr>
	<tr>
		<td colspan  = "2" align="center" width="100%">
			<div class = "heading">
			<h1>Welcome to the Virtual lab of <br>AKRG CET</h1></div>
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="50px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width = "40%">
			<div class = "heading1">
			<h1 style="font-family:cursive; color:black;">Here you can perform your Lab Works from Home!!
			We are providing different compilers to work 
				on your lab assignments and to finish your programs</h1></div>
		</td>

		<td align="center" width="60%">
			<div class = "image2">
			<img src = "{{url_for('static',filename = 'images/student.jpg')}}" width="60%"></div>
		</td>

	</tr>

	<tr>
		<td colspan="2" align="center">
			<h1 style="font-family:candara; color:#031458;">Available Compilers</h1>
		</td>
	</tr>
	
	<tr>
		<div class = "inside">
		<td align="center" width="50%">
			<a href = "/c" ><img src = "{{url_for('static',filename = 'images/cc.png')}}" 	width="30%;"></a>

		</td>
		<td  align="center" width="50%">
			<a href = "/c1"><img src = "{{url_for('static',filename = 'images/c+++.png')}}" width="25%;" ></a>
			
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/python"><img src = "{{url_for('static',filename = 'images/python.png')}}"  width="30%;"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "/java"><img src = "{{url_for('static',filename = 'images/java1.png')}}" width="30%;" ></a>
		</td>
	</tr>
<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/ds"><img src = "{{url_for('static',filename = 'images/ds.png')}}"  width="40%"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "/ads"><img src = "{{url_for('static',filename = 'images/ads.png')}}" width="30%;" ></a>
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/htm"><img src = "{{url_for('static',filename = 'images/html.png')}}"  width="30%;"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "/sql"><img src = "{{url_for('static',filename = 'images/sql2.png')}}" width="30%;" ></a>
		</td>
	</tr>
<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/ml"><img src = "{{url_for('static',filename = 'images/ml.png')}}"  width="30%;"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "/rp"><img src = "{{url_for('static',filename = 'images/rp.png')}}"  width="30%;" ></a>
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr>
	<tr>
		<td align="center" width="50%">
			<a href = "/nix"><img src = "{{url_for('static',filename = 'images/nix.png')}}" width="30%;"></a>
		</td>
		<td  align="center" width="50%">
			<a href = "#"></a>
		</td>
	</tr>
	<tr>
		<td align="center" width="50%" height="100px;">
		</td>
		<td  align="center" width="50%">
		</td>
	</tr></div>

<tr><td colspan="2" width="100%" align="center">
<h2 style="font-size: 20px;">To Submit your assingment Please <a href = " https://mail.google.com/mail/u/0/#inbox?compose=CllgCJZXhcwTsHSHBNMPhzvKghKlClmNMTQLBzJmXKXzmRqQWBkQkGWfGllLgtgchSDPXPwDhXV" target="_blank">Click Here</a></h2></td></tr>

<tr><td colspan="2" width="100%" >

<label style="font-size: 20px; font-family: candara; color: black;">Sincere thanks to </label></td></tr>
<tr><td colspan="2" width="100%">
<marquee >

	<a href = "https://www.programiz.com/" target="_blank"><img src = "{{url_for('static',filename = 'images/pz.png')}}"></a>
	<a href = "https://www.javatpoint.com/" target="_blank"><img src = "{{url_for('static',filename = 'images/javatpoint.png')}}" width="300px" height="250px;"></a>
	<a href = "https://www.onlinegdb.com/" target="_blank"><img src = "{{url_for('static',filename = 'images/online.png')}}" width="300px" height="250px;"></a>
	<a href = "https://paiza.io/en" target="_blank"><img src = "{{url_for('static',filename = 'images/paiza.png')}}" width="300px" height="250px;"></a>
</marquee></td></tr>
<tr><td colspan="2" width="100%" align="center">
<footer style=" color: white;font-family: candara;font-size: 20px;background-color: #031458; padding-top: 20px; padding-bottom: 20px;">©CopyRight By CSE Students(2k17 - 2021)</footer></td></tr>
</table>
</body>
</html>
