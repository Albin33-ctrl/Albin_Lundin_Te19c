<script src="https://koda.nu/simple.js">
  
  var zombies = [];
  
  var i = 0;
  
  while (i < 100)
  {
  	 zombies.push({x: random(totalWidth), 
               y: random(totalHeight), 
               speed: random(1,5)});
    i+= 1; 
  }
  
  
  function update()
  {
    clearScreen();
    
    var i =0;
    
    while (i < 100)
    {
      var zombie = zombies[i];
      picture(zombie.x, zombie.y, "http://spelprogrammering.nu/bilder/zombie.png")
  	
      if (zombie.x < mouse.x)
        zombie.x += zombie.speed;
      else
        zombie.x -= zombie.speed;
    
      if (zombie.y < mouse.y)
        zombie.y += zombie.speed;
      else
        zombie.y -= zombie.speed;
    
      if (distance(mouse, zombie) < 5)
      {
      alert("Game over");
      stopUpdate();
      }
       
       
      i += 1;
    }
  }

</script>