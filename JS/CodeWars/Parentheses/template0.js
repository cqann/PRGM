var count = 1;
updatesPerSecond = 30;

function update() {
    clearScreen();
    var x = 0;
    var y = 0;


  	for (var i = 0; i <= count ; i++) {
        line(0, y, x, totalHeight, 1, "black");
        x = x + totalWidth/count;
        y = x + totalHeight/count;
      }

   count = count + 1;

   if (count > 300) {
     count = 0;
   }
}
