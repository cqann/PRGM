






function tribonacci(signature,n){

  var emptyArr = [];
  if (signature[0]>50) {

    return emptyArr;
  }


  for (var i = 0; i < n; i++) {
    signature[i+3] = signature[i]+signature[i+1]+signature[i+2];
  }

  return signature;
}
