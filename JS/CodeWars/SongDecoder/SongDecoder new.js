

//songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  // =>  WE ARE THE CHAMPIONS MY FRIEND
songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB");

function songDecoder(song){

   console.log(song);
   str = song.replace(/WUB/g," ");

   str = str.trim();

   while (str.indexOf("  ") != -1) {
        str = str.replace(" ","");
   }

   function removeSpace(str) {
     var arr = str.split("");
     arr[str.indexOf("  ")] = "";
     newstr = arr.join();
     return newstr;
   }

   console.log(str);
   return str;
}
