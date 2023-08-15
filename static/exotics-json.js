$(document).ready(function() {
    // Handle player button clicks
    $('.player-button').on('click', function() {
        $('.player-button').removeClass('active');
        $(this).addClass('active');

        var player = $(this).data('player');
        updateExoticData(player);
    });

    // Load initial data for the first player
    updateExoticData('hunter');

    // Function to update the exotic data
    function updateExoticData(player) {
        var table = $('#exoticTable').DataTable();
        table.clear().draw();

        $.getJSON(`static/data/formattedPlayerExoticData/formatted${player}Exotics.json`, function(data) {
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
    }
});
