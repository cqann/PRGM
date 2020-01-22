

//songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  // =>  WE ARE THE CHAMPIONS MY FRIEND
songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB");

function songDecoder(song){

   console.log(song);


   while (song.charAt(0) == "W" && song.charAt(1) == "U" && song.charAt(2) == "B") {
     song = song.replace("WUB", "");
   }

   while (song.charAt(song.length-1) == " " && song.charAt(song.length-1) == " " && song.charAt(song.length-1) == " ") {
     song = song.replace("WUB", "");
   }

   for (var i = 0; i < 1000; i++) {
     if (song.charAt(song.indexOf("WUB") + 3) == "W" && song.charAt(song.indexOf("WUB") + 4) == "U" && song.charAt(song.indexOf("WUB") + 5) == "B") {
       removeSpace(song);
     }
   }


   function removeSpace(str) {
     var arr = str.split("");
     arr[str.indexOf("WUB") + 3] = "";
     arr[str.indexOf("WUB") + 4] = "";
     arr[str.indexOf("WUB") + 5] = "";
     var newstr = arr.join();
     return newstr;
   }

   var result = song.replace(/WUB/g," ");
   console.log(result);
   return result;
}
