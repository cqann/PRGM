var x = prompt(1);
var y = prompt(2);
alert(GetSum(x,y));



function GetSum(a,b) {

  var delta = Math.abs(a-b);
  var arr = [];
  var arrsum = 0;

   if (a<b) {
         for (var i = 0; i < delta; i++) {
           arr[i] = a + i;
         }
         for (var i = 0; i < arr.length; i++) {
           arrsum = arrsum + arr[i];
         }
         return arrsum;
   }

   if (a>b) {
         for (var i = 0; i < delta; i++) {
           arr[i] = b + i;
         }
         for (var i = 0; i < arr.length; i++) {
           arrsum = arrsum + arr[i];
         }
         return arrsum;
   }

   if (a==b) {
         return a;
   }
}



var delta = Math.abs(a-b);
var arr = [];
var arrsum = 0;
for (var i = 0; i < delta; i++) {
  arr[i] = a + i;
}
for (var i = 0; i < arr.length; i++) {
  arrsum = arrsum + arr[i];
}
return arrsum;
