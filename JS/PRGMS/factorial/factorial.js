
var OgNum = prompt("Write a number");
var NumList = [];
var Result = 1 ;

for (var i = 0; i < OgNum; i++) {

    NumList[i] = OgNum-i;

}

for (var i = 0; i < NumList.length; i++) {
  Result = Result*NumList[i];
}

alert(OgNum + " factorial is " + Result );
