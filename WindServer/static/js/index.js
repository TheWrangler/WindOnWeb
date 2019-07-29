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

function lidar_search()
{
    var hei = $("#height-select").val(); 
    var dt = $("#datetimepick_cur").find("input").val(); 
    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/index/lidar/" + hei + "/" + station + "/" + dt +  "/";

	window.location.href = url;
}

function lidar_last_search(dt)
{
    var hei = $("#height-select").val();  
    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/index/lidar/" + hei + "/" + station + "/" + dt +  "/last/";

	window.location.href = url;
}

function lidar_next_search(dt)
{
    var hei = $("#height-select").val();  
    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/index/lidar/" + hei + "/" + station + "/" + dt +  "/next/";

	window.location.href = url;
}

function lidar_auto_refresh(bStart)
{
    var hei = $("#height-select").val();
    var start_dt; 
    if(bStart)
    {
        start_dt = $("#datetimepick_start").find("input").val(); 
        if(start_dt == "")
        {
            alert("请设置浏览的起始时间！")
            return;
        }
    } 
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
    if(end_dt == "")
    {
        alert("请设置浏览的结束时间！")
        return;
    }

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/index/lidar/" + hei + "/" + station + "/" + start_dt +  "/" + end_dt + "/auto/";

	window.location.href = url;
}

function lidar_auto_update()
{
    var hei = $("#height-select").val();  
    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/index/lidar/" + hei + "/" + station + "/update/";

	window.location.href = url;
}

function page_config()
{
    var path = window.location.pathname;
    var filters = path.split("/");
    if(filters.length <= 5)
    {
        var cur_dt = DateTimeFormat(new Date());
        $("#datetimepick_cur_input").val(cur_dt);
    }
    else if(filters.length <= 9)
    {
        $("#height-select").val(filters[4]).trigger("change");
        SelectCity(decodeURI(filters[5]));

        if(filters[6] == "update")
        {
            gb_timer = setTimeout(lidar_auto_update,6000);
            var cur_dt = DateTimeFormat(new Date());
            $("#datetimepick_cur_input").val(cur_dt);
        }
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

        $("#datetimepick_cur_input").val(start_dt);

		gb_timer = setTimeout(lidar_auto_refresh,3000);
    }
}