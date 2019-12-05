

var q = prompt("Binary number please");

  var result = 0;
  var ArrBin = q.split("");
  ArrBin.reverse();
  console.log(ArrBin);
  for (var i = 0; i < ArrBin.length; i++) {
    console.log(i);
    result = result + ( ArrBin[i] * Math.pow(2,i) );
  }

  return result

alert(result + " is the number in base 10");
