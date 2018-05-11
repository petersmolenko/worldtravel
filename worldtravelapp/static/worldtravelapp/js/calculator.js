//--------------------Calculator tour--------------------------------//
	var sumVal = document.querySelectorAll(".serv-container .sum-val");
	var priceVal = document.querySelectorAll(".serv-container .price-val");
	var countServ = document.querySelectorAll(".serv-container .count-serv");
	var itogVal = document.getElementById("itog-val");
	var b = document.getElementById("button-calc");
	function calculate(){
		var summ=0;
		for(var i = 0; i<sumVal.length; i++) {
		sumVal[i].innerHTML=parseInt(countServ[i].value)*parseInt(priceVal[i].innerHTML);
			summ+=parseInt(sumVal[i].innerHTML);
	}
		itogVal.innerHTML = summ;
	}
	window.onload =calculate;
	b.onclick=calculate;
//----------------------------------------------------------------------------