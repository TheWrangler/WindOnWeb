function lidar_caption_2_product(caption)
{
    var product;
    if(caption == "PPI拼图")
        product = "ppi";
    else if(caption == "VOL模式CAPPI")
        product = "cappi";
    else if(caption == "风廓线THI")
        product = "wind_thi";
    else if(caption == "RHI")
        product = "rhi";
    
    return product;
}

function load_lidar(caption)
{
    var product = lidar_caption_2_product(caption);

    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/lidar/" + product + "/";

	window.location.href = url;
}

$(function(){
    $('#title-btn-group .btn').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });

    $('#city-list-group .list-group-item').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });

    $("#datetimepick_start").datetimepicker({
        format:'yyyy-mm-dd hh:ii',
        language: 'zh-CN',
        autoclose:1
    });

    $("#datetimepick_end").datetimepicker({
        format:'yyyy-mm-dd hh:ii',
        language: 'zh-CN',
        autoclose:1
    });

	$('#ele-list-group .list-group-item').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });

    $("#height-select").select2({
        width:"100%",
	    placeholder:"请选择高度",
	    language:"zh-CN"
    });
	
	$('#dir-list-group .list-group-item').click(function(){
		$(this).addClass("active").siblings().removeClass("active");
	});
	
	$('#azi-list-group .list-group-item').click(function(){
		$(this).addClass("active").siblings().removeClass("active");
    });

    $("#datetime-select").select2({
        width:"100%",
	    placeholder:"请选择时间",
	    language:"zh-CN"
    });
    
    $(document).ready(function(){
        var caption = $("#product-list-group .active").text();
        var product = lidar_caption_2_product(caption);
        page_config(product);
    });
});

function GetFilter(product)
{
    var filter;
    if(product == "ppi")
    {
        filter = $("#ele-list-group .active").text();
        filter = filter.substring(0,filter.length-1);
    }
    else if(product == "cappi")
    {
        filter = $("#height-select").val();
    }
    else if(product == "wind_thi")
    {
        filter = $("#dir-list-group .active").text();
    }
    else if(product == "rhi")
    {
        filter = $("#azi-list-group .active").text();
        filter = filter.substring(0,filter.length-1);
    }
    return filter;
}

function SelectEle(ele)
{
    var eles = document.getElementById("ele-list-group").childNodes;
    for(let ele_e of eles)
    {
        if(ele_e.nodeName != "LI")
            continue;
            
        if(ele == ele_e.id)
            document.getElementById(ele_e.id).classList.add("active");
        else document.getElementById(ele_e.id).classList.remove("active");
    }
}

function SelectDirection(direction)
{
    var directions = document.getElementById("dir-list-group").childNodes;
    for(let direction_e of directions)
    {
        if(direction_e.nodeName != "LI")
            continue;
            
        if(direction == direction_e.id)
            document.getElementById(direction_e.id).classList.add("active");
        else document.getElementById(direction_e.id).classList.remove("active");
    }
}

function SelectAzi(azi)
{
    var azis = document.getElementById("azi-list-group").childNodes;
    for(let azi_e of azis)
    {
        if(azi_e.nodeName != "LI")
            continue;
            
        if(azi == azi_e.id)
            document.getElementById(azi_e.id).classList.add("active");
        else document.getElementById(azi_e.id).classList.remove("active");
    }
}

function lidar_station(product,station)
{
    var filter = GetFilter(product);
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/lidar/" + product + "/" + filter + "/" + station + "/";

    window.location.href = url;
}

function lidar_search(product)
{
    var filter = GetFilter(product);
    var station = $("#city-list-group .active").text();
    var dt = GetCurDateTime(); 
    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/lidar/" + product + "/" + filter + "/" + station + "/" + dt + "/";
    window.location.href = url;
}

function lidar_last_search(product,dt)
{
    var filter = GetFilter(product);

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/lidar/" + product + "/" + filter + "/" + station + "/" + dt + "/last/";

	window.location.href = url;
}

function lidar_next_search(product,dt)
{
    var filter = GetFilter(product);

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/lidar/" + product + "/" + filter + "/" + station + "/" + dt + "/next/";

	window.location.href = url;
}

//auto refresh page when browse history.
function lidar_auto_refresh(bStart)
{
    var caption = $("#product-list-group .active").text();
    var product = lidar_caption_2_product(caption);

    var filter = GetFilter(product);
    
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
    var url = "http://" + hostname + ":80/WindServer/lidar/" + product + "/" + filter + "/" + station + "/" + start_dt +  "/" + end_dt + "/auto/";

	window.location.href = url;
}

//auto refresh page to load newest
function lidar_auto_update()
{
    var caption = $("#product-list-group .active").text();
    var product = lidar_caption_2_product(caption);

    var filter = GetFilter(product);

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/lidar/" + product + "/" + filter + "/" + station + "/update/";

	window.location.href = url;
}

function page_config(product)
{
    var caption = $("#product-list-group .active").text();
    var product = lidar_caption_2_product(caption);

    var path = window.location.pathname;
    var filters = path.split("/");
    if(filters.length <= 5)
    {
        var cur_dt = DateTimeFormat(new Date());
        //$("#datetimepick_cur_input").val(cur_dt);
    }
    else if(filters.length <= 7)
    {
        if(product == "ppi")
            SelectEle(decodeURI(filters[4]));
        else if(product == "cappi")
            $("#height-select").val(filters[4]).trigger("change");
        else if(product == "wind_thi")
            SelectDirection(decodeURI(filters[4]));
        else if(product == "rhi")
            SelectAzi(decodeURI(filters[4]));

        SelectCity(decodeURI(filters[5]));

        var cur_dt = DateTimeFormat(new Date());
        //$("#datetimepick_cur_input").val(cur_dt);
    }
    else if(filters.length <= 9)
    {
        if(product == "ppi")
            SelectEle(decodeURI(filters[4]));
        else if(product == "cappi")
            $("#height-select").val(filters[4]).trigger("change");
        else if(product == "wind_thi")
            SelectDirection(decodeURI(filters[4]));
        else if(product == "rhi")
            SelectAzi(decodeURI(filters[4]));

        SelectCity(decodeURI(filters[5]));

        if(filters[6] == "update")
        {
            gb_timer = setTimeout(lidar_auto_update,6000);

            var cur_dt = DateTimeFormat(new Date());
            //$("#datetimepick_cur_input").val(cur_dt);
        }  
        else 
        {
            var cur_dt = decodeURI(filters[6]);
            //$("#datetimepick_cur_input").val(cur_dt);
        }
    }
    else
    {
        if(product == "ppi")
            SelectEle(decodeURI(filters[4]));
        else if(product == "cappi")
            $("#height-select").val(filters[4]).trigger("change");
        else if(product == "wind_thi")
            SelectDirection(decodeURI(filters[4]));
        else if(product == "rhi")
            SelectAzi(decodeURI(filters[4]));

        SelectCity(decodeURI(filters[5]));

        var start_dt = decodeURI(filters[6]);
        $("#datetimepick_start_input").val(start_dt);
        var end_dt = decodeURI(filters[7]);
        $("#datetimepick_end_input").val(end_dt);

        //$("#datetimepick_cur_input").val(start_dt);

		gb_timer = setTimeout(lidar_auto_refresh,3000);
    }
}