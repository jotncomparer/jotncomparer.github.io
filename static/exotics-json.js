$(document).ready(function() {
    // Handle player button clicks
    $('.player-button').on('click', function() {
        $('.player-button').removeClass('active');
        $(this).addClass('active');

        var player = $(this).data('player');
        updateExoticData(player);
    });

    // Load initial data for the first player
    var initialPlayer = $('.player-button.active').data('player');
    updateExoticData(initialPlayer);

    // Function to update the exotic data
    function updateExoticData(player) {
        var table = $('#exoticTable').DataTable();
        table.clear().draw();
        console.log(`Calling updateExoticData for player: ${player}`);

        $.getJSON(`/get_exotic_data/${player}`, function(data) {
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
