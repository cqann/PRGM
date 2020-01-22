

function isIsogram(str){
   check = true;
   str = str.toLowerCase();
   arr = str.split("");

   for (var i = 0; i < arr.length; i++) {
     if (str.indexOf(arr[i]) != i || str.lastIndexOf(arr[i]) != i) {
       check = false;
     }
   }

   return check;



}
