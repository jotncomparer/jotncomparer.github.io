$(document).ready(function() {
  var table = $('#exoticTable').DataTable({
      order: [[1, 'desc']]
  });

  $.getJSON('formattedHunterExotics.json', function(data) {
      $.each(data.exoticWeapons, function(index, weapon) {
          table.row.add([
              weapon.name,
              weapon.kills,
              weapon.precision
          ]);
      });

      // After adding all rows, draw the table to display the data
      table.draw();
  });
});
