/**
 * Created by josep on 19/05/16.
 */
function load_artist_data(href){
    $.ajax({
        //load only related artists by now.
        url: href+'/related-artists',
        datatype: 'jsonp',
        success: function (data) {
            arr = data.artists;
            options = $("#id_related>option")
            $.map(options, function(option){
                option.selected = '';
                $.map(arr, function(artist){
                    console.log("checking "+option.innerHTML + " against "+ artist.name);
                    if(option.innerHTML === artist.name){
                        option.selected = 'selected';
                    }
                })
            });
            /*
            $.map( arr, function(item){
                for(i=0; i < $("#id_related>option").length; i++){
                    //console.log("checking "+$("#id_related>option")[i].innerHTML + " against "+ item.name);
                    if( $("#id_related>option")[i].innerHTML == item.name ){
                        $("#id_related>option")[i].selected = 'selected';
                        break;
                    }
                }
            });
            */
        },
    });
}


function select(event, ui){
    if(ui.item) {
        $("#id_spotify_id").val(ui.item.id);
        load_artist_data(ui.item.href);
    }
}

function load_artist_list(request, response){
    var current = $("#id_name").val();
    $.ajax({
        url: 'https://api.spotify.com/v1/search',
        datatype: 'jsonp',
        data: {
            q: current,
            type: 'artist',
            limit: 50
        },
        success: function(data){
            response( $.map( data.artists.items, function (item) {
                return {
                    label: item.name,
                    value: item.name,
                    id: item.id,
                    href: item.href,
                }
            }));
        },
    });
}

$(function(){
    $("#id_name").autocomplete({
        source: load_artist_list,
        minLenght: 2,
        select: select,
    });
});