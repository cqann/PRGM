






function validBraces(braces){

var arr = braces.split("");
var normal = ["(",")"];
var square = ["[","]"];
var curly = ["{","}"];
var check = true;

if( (braces.indexOf("(") - braces.indexOf(")") ) !% 2) {
  check = false;
}

if( (braces.indexOf("[") - braces.indexOf("]") ) !% 2) {
  check = false;
}

if( (braces.indexOf("{") - braces.indexOf("}") ) !% 2) {
  check = false;
}

return check;
}
