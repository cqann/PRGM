




function expandedForm(num) {

    var numstr = num.toString();
    var numarr = numstr.split("");

    for (var i = 0; i < numarr.length; i++) {

      for (var j = 0; j < (numarr.length-i-1); j++) {

          if (numarr[i] == 0) {
            numarr.splice(i,1);
            continue;
          } else {
            numarr[i] = numarr[i]  + 0;
          }

      }

    }

    var result = numarr.join(" + ");

    return result;



}
