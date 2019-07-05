function search_from_dev(dev)
{
    var height = $("#height-list-group .active").text();
    if(height == "地面")
        height = "0";

    var city = $("#city-btn-group .active").text();

    var url = "index.html?dev=" + dev + "&height=" + height + "&city=" + city;
    window.location.href = url;
}

function search_from_city(city)
{
    var dev = $("#dev-list-group .active").text();

    var height = $("#height-list-group .active").text();
    if(height == "地面")
        height = "0";

    var url = "index.html?dev=" + dev + "&height=" + height + "&city=" + city;
    window.location.href = url;
}

function search_from_height(height)
{
    var dev = $("#dev-list-group .active").text();

    if(height == "地面")
        height = "0";

    var city = $("#city-btn-group .active").text();

    var url = "index.html?dev=" + dev + "&height=" + height + "&city=" + city;
    window.location.href = url;
}

function search_from_date_time()
{
    
}

$(function(){
    $("#datetimepick1").datetimepicker({
        format:'YYYY-MM-DD hh:mm',
        locale:moment.locale('zh-cn')
    })

    $("#datetimepick2").datetimepicker({
        format:'YYYY-MM-DD hh:mm',
        locale:moment.locale('zh-cn')
    })
});
