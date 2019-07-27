var gb_timer;

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
        //index_page_config();
        //gb_timer = setInterval(lidar_auto_refresh,5000);
    });
});

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

//auto refresh page.
function lidar_auto_refresh()
{
    var hei = $("#height-select").val(); 
    var dt = $("#datetimepick_cur").find("input").val(); 
    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/index/lidar/" + hei + "/" + station + "/" + dt +  "/";

	window.location.href = url;
}

function page_config()
{
    var path = window.location.pathname;
	var filters = path.split("/");
	
	var idx = 0;
	for(let filter of filters)
	{
        if(filter == 'index')
            break;

        idx++;
    }
    
    idx += 2;
    if(idx >= filters.length-1)
        return;

    if(filters[idx] != "")
        $("#height-select").val(filters[idx]).trigger("change");

    idx++;
    if(filters[idx] != "")
    {
        var citys = document.getElementById("city-list-group").childNodes;
        //var citys = jQuery.children(group);
        for(let station of citys)
        {
            if(station.nodeName == "#text")
                continue;
                
            var station_name = decodeURI(filters[idx]);
            if(station_name == station.id)
                document.getElementById(station.id).classList.add("active");
            else document.getElementById(station.id).classList.remove("active");
        }
    }

    idx++;
    if(idx+3 <filters.length)
    {
        var start_dt = decodeURI(filters[idx]);
        $("#datetimepick_start_input").val(start_dt);
        var end_dt = decodeURI(filters[idx+1]);
        $("#datetimepick_end_input").val(end_dt);
    }
    else
    {
        var cur_dt = decodeURI(filters[idx]);
        $("#datetimepick_cur_input").val(cur_dt);
    } 
}