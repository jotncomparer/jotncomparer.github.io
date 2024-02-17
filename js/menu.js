 /* When the user clicks on the button, 
        toggle between hiding and showing the dropdown content */
        function clan() {
            document.getElementById("clanDrop").classList.toggle("show");
        }

        function cam() {
            document.getElementById("camDrop").classList.toggle("show");
        }

        function con() {
            document.getElementById("conDrop").classList.toggle("show");
        }

        function doug() {
            document.getElementById("dougDrop").classList.toggle("show");
        }

        function hunt() {
            document.getElementById("huntDrop").classList.toggle("show");
        }

        function jack() {
            document.getElementById("jackDrop").classList.toggle("show");
        }

        function kade() {
            document.getElementById("kadeDrop").classList.toggle("show");
        }

        function mark() {
            document.getElementById("markDrop").classList.toggle("show");
        }

        function tom() {
            document.getElementById("tomDrop").classList.toggle("show");
        }

        function xav() {
            document.getElementById("xavDrop").classList.toggle("show");
        }

        // Close the dropdown if the user clicks outside of it
        window.onclick = function (event) {
            if (!event.target.matches('.dropbtn')) {
                var dropdowns = document.getElementsByClassName("dropdown-content");
                var i;
                for (i = 0; i < dropdowns.length; i++) {
                    var openDropdown = dropdowns[i];
                    if (openDropdown.classList.contains('show')) {
                        openDropdown.classList.remove('show');
                    }
                }
            }
        }