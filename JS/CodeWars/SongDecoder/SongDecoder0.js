

//songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  // =>  WE ARE THE CHAMPIONS MY FRIEND
songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB");

function songDecoder(song){

   console.log(song);
   str = song.replace(/WUB/g," ");

   while (str.charAt(0) == " ") {
     str = str.replace(" ", "");
   }
    while (str.charAt(str.length-1) == " ") {
     str = str.replace(" ", "");
   }

   for (var i = 0; i < 99999; i++) {
     if (str.charAt(str.indexOf(" ") + 1) == " ") {
       removeSpace(str);
     }
   }


   function removeSpace(str) {
     arr = str.split("");
     arr[str.indexOf(" ") + 1] = "";
     newstr = arr.join();
     return newstr;
   }

   console.log(str);
   return str;
}
