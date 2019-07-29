function fusion_caption_2_product(caption)
{
    var product;
    if(caption == "激光雷达DBS-5")
        product = "dbs5";
    else if(caption == "叠加风廓线")
        product = "profile";
    else if(caption == "叠加微波辐射计")
        product = "radio";
    
    return product;
}

function load_fusion(caption)
{
    var product = fusion_caption_2_product(caption);
   

    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/fusion/" + product + "/";

	window.location.href = url;
}

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

    $('#fusion-list-group .list-group-item').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });
    
    $(document).ready(function(){
        var caption = $("#product-list-group .active").text();
        var product = fusion_caption_2_product(caption);
        page_config(product);
    });
});

function GetFilter(product)
{
    var filter = $("#fusion-list-group .active").text();
    return filter;
}

function SelectFusion(fusion)
{
    var fusions = document.getElementById("fusion-list-group").childNodes;
    for(let fusion_e of fusions)
    {
        if(fusion_e.nodeName != "LI")
            continue;
            
        if(fusion == fusion_e.id)
            document.getElementById(fusion_e.id).classList.add("active");
        else document.getElementById(fusion_e.id).classList.remove("active");
    }
}

function fusion_search(product)
{
    var filter = GetFilter(product);
    var station = $("#city-list-group .active").text();
    var dt = $("#datetimepick_cur").find("input").val(); 
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/fusion/" + product + "/" + filter + "/" + station + "/" + dt + "/";

	window.location.href = url;
}

function fusion_last_search(product,dt)
{
    var filter = GetFilter(product);

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/fusion/" + product + "/" + filter + "/" + station + "/" + dt + "/last/";

	window.location.href = url;
}

function fusion_next_search(product,dt)
{
    var filter = GetFilter(product);

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/fusion/" + product + "/" + filter + "/" + station + "/" + dt + "/next/";

	window.location.href = url;
}

//auto refresh page when browse history.
function fusion_auto_refresh(bStart)
{
    var caption = $("#product-list-group .active").text();
    var product = fusion_caption_2_product(caption);

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
    var url = "http://" + hostname + ":80/WindServer/fusion/" + product + "/" + filter + "/" + station + "/" + start_dt +  "/" + end_dt + "/auto/";

	window.location.href = url;
}

//auto refresh page to load newest
function fusion_auto_update()
{
    var caption = $("#product-list-group .active").text();
    var product = fusion_caption_2_product(caption);

    var filter = GetFilter(product);

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/fusion/" + product + "/" + filter + "/" + station + "/update/";

	window.location.href = url;
}

function page_config(product)
{
    var caption = $("#product-list-group .active").text();
    var product = fusion_caption_2_product(caption);

    var path = window.location.pathname;
    var filters = path.split("/");
    if(filters.length <= 5)
    {
        var cur_dt = DateTimeFormat(new Date());
        $("#datetimepick_cur_input").val(cur_dt);
    }
    else if(filters.length <= 9)
    {
        SelectFusion(decodeURI(filters[4]));
        SelectCity(decodeURI(filters[5]));

        if(filters[6] == "update")
        {
            gb_timer = setTimeout(fusion_auto_update,6000);

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
        SelectFusion(decodeURI(filters[4]));
        SelectCity(decodeURI(filters[5]));

        var start_dt = decodeURI(filters[6]);
        $("#datetimepick_start_input").val(start_dt);
        var end_dt = decodeURI(filters[7]);
        $("#datetimepick_end_input").val(end_dt);

        $("#datetimepick_cur_input").val(start_dt);

		gb_timer = setTimeout(fusion_auto_refresh,3000);
    }
}
