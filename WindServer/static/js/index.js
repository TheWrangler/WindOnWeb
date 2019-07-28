var gb_timer = null;

$(function(){
    $('#title-btn-group .btn').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });

    $('#city-list-group .list-group-item').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });

    $("#datetimepick_cur").datetimepicker({
        format:'YYYY-MM-DD hh:mm',
        locale:moment.locale('zh-cn')
    });

    $("#datetimepick_start").datetimepicker({
        format:'YYYY-MM-DD hh:mm',
        locale:moment.locale('zh-cn')
    });

    $("#datetimepick_end").datetimepicker({
        format:'YYYY-MM-DD hh:mm',
        locale:moment.locale('zh-cn')
    });

    $("#height-select").select2({
        width:"100%",
	    placeholder:"请选择高度",
	    language:"zh-CN"
    });

    $(document).ready(function(){
        page_config();
    });
});

function SelectCity(city)
{
    var citys = document.getElementById("city-list-group").childNodes;
    for(let station of citys)
    {
        if(station.nodeName == "#text")
            continue;
            
        if(city == station.id)
            document.getElementById(station.id).classList.add("active");
        else document.getElementById(station.id).classList.remove("active");
    }
}

function update_img(imgSrc)
{
    var element = document.getElementById('active_img');
    element.src = imgSrc;
}

function lidar_search()
{
    var hei = $("#height-select").val(); 
    var dt = $("#datetimepick_cur").find("input").val(); 
    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/index/lidar/" + hei + "/" + station + "/" + dt +  "/";

	window.location.href = url;
}

function lidar_last_search(dt)
{
    var hei = $("#height-select").val();  
    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/index/lidar/" + hei + "/" + station + "/" + dt +  "/last/";

	window.location.href = url;
}

function lidar_next_search(dt)
{
    var hei = $("#height-select").val();  
    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/index/lidar/" + hei + "/" + station + "/" + dt +  "/next/";

	window.location.href = url;
}

//auto refresh page when browse history.
function lidar_auto_refresh(bStart)
{
    var hei = $("#height-select").val();
    var start_dt; 
    if(bStart)
        start_dt = $("#datetimepick_start").find("input").val(); 
    else
    {
        var titles = document.getElementById("title-btn-group").childNodes;
        if(titles != null)
        {
            for(let title of titles)
            {
                if(title.nodeName == "#text")
                    continue;
                    
               if(title.id == "btn-last" || title.id == "btn-next")
                    continue;

                start_dt = title.id;
                break;
            }
        }
        else
        {
            return;
        }
    }

    var end_dt = $("#datetimepick_end").find("input").val(); 

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/index/lidar/" + hei + "/" + station + "/" + start_dt +  "/" + end_dt + "/auto/";

	window.location.href = url;
}

//auto refresh page to load newest
function lidar_auto_update()
{
    var hei = $("#height-select").val();  
    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/index/lidar/" + hei + "/" + station + "/update/";

	window.location.href = url;
}

function page_config()
{
    var path = window.location.pathname;
    var filters = path.split("/");
    if(filters.length <= 5)
        gb_timer = setTimeout(lidar_auto_update,6000);
    else if(filters.length <= 9)
    {
        $("#height-select").val(filters[4]).trigger("change");
        SelectCity(decodeURI(filters[5]));

        if(filters[6] == "update")
            gb_timer = setTimeout(lidar_auto_update,6000);
        else 
        {
            var cur_dt = decodeURI(filters[6]);
            $("#datetimepick_cur_input").val(cur_dt);
        }
    }
    else
    {
        $("#height-select").val(filters[4]).trigger("change");
        SelectCity(decodeURI(filters[5]));

        var start_dt = decodeURI(filters[6]);
        $("#datetimepick_start_input").val(start_dt);
        var end_dt = decodeURI(filters[7]);
        $("#datetimepick_end_input").val(end_dt);

		gb_timer = setTimeout(lidar_auto_refresh,3000);
    }
}