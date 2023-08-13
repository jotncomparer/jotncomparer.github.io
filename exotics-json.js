var xhr = new XMLHttpRequest();

xhr.onload = function() {                       // When readystate changes
    // The following conditional check will not work locally - only on a server
    if(xhr.status === 200) {                      // If server status was ok
      responseObject = JSON.parse(xhr.responseText);

      //var index = responseObject.Response.length;
      //var index = 50;

      var viewAllBtn = document.getElementById('display');
      viewAllBtn.addEventListener('click', displayAll, false);
      /*
      var viewAllContent = '';
      function displayAll(){
        for (var i = 0; i < index; i++) { // Loop through object
          viewAllContent += '<div>';
          viewAllContent += '<p style = "text-align: center">' + '<b>' + responseObject.Response[0].weapons[i].referenceId + '</b>' + '</p>';;
          //viewAllContent += '<p> hey it works, how about that! </p>';
          viewAllContent += '</div>';
        }
        document.getElementById('content').innerHTML = viewAllContent;*/

        var responseIndex = responseObject.Response.length;

        var viewAllContent = '';
        function displayAll() 
        {
          for(var i = 0; i < responseIndex; i++)
          {
            var weaponIndex = responseObject.Response[i].weapons.length;

            viewAllContent += '<div>';
            viewAllContent += '<p style = "text-align: center">' + '<b>' + responseIndex + '</b>' + '</p>';
            viewAllContent += '<p style = "text-align: center">' + '<b>' + weaponIndex + '</b>' + '</p>';
            viewAllContent += '</div>';

            for(var j = 0; j < weaponIndex; j++)
            {
              viewAllContent += '<div>';
              viewAllContent += '<p style = "text-align: center">' + '<b>' + responseObject.Response[i].weapons[j].referenceId + '</b>' + '</p>';;
              viewAllContent += '</div>';
            }
          }
          document.getElementById('content').innerHTML = viewAllContent;
        }  
    }
}

xhr.open('GET', 'exotic.json', true);        // Prepare the request
xhr.send(null);
