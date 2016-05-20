/**
 * Created by josep on 19/05/16.
 */
function loadArtistData(href){
    $.ajax({
        //load only related artists by now.
        url: href+"/related-artists",
        datatype: "jsonp",
        success: function (data) {
            var arr = data.artists;
            var options = $("#id_related>option");
            $.map(options, function(option){
                option.selected = "";
                $.map(arr, function(artist){
                    if(option.innerHTML === artist.name){
                        option.selected = "selected";
                    }
                });
            });
        },
    });
}


function select(event, ui){
    if(ui.item) {
        $("#id_spotify_id").val(ui.item.id);
        loadArtistData(ui.item.href);
    }
}

function loadArtistList(request, response){
    var current = $("#id_name").val();
    $.ajax({
        url: "https://api.spotify.com/v1/search",
        datatype: "jsonp",
        data: {
            q: current,
            type: "artist",
            limit: 50
        },
        success: function(data){
            response( $.map( data.artists.items, function (item) {
                return {
                    label: item.name,
                    value: item.name,
                    id: item.id,
                    href: item.href,
                };
            }));
        },
    });
}

$(function(){
    $("#id_name").autocomplete({
        source: loadArtistList,
        minLenght: 2,
        select: select
    });
});