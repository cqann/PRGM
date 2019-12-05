//persistence(39) === 3  because 3*9 = 27, 2*7 = 14, 1*4=4
      //                  and 4 has only one digit

// persistence(999) === 4  because 9*9*9 = 729, 7*2*9 = 126,
                        // 1*2*6 = 12, and finally 1*2 = 2

 //persistence(4) === 0 because 4 is already a one-digit number

persistence(39);

//count++;
function persistence(num) {

  var count = -1;
  return loop(num);

    function loop(num) {
        count++;
        console.log(count);

        var n = num.toString();
        var arr = [];

        for (var i = 0; i < n.length; i++) {
            arr.push(+n.charAt(i));
          }
        //console.log(arr);

          if (arr.length == 1) {
                  return count;
                } else {
                  newNum = 1;

                  for (var i = 0; i < arr.length; i++) {
                    newNum = newNum * arr[i];
                  }


                  loop(newNum);

          }
          return count;
   }
}
