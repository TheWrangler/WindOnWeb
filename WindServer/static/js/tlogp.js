function tlogp_caption_2_product(caption)
{
    var product;
    if(caption == "T-logP图")
        product = "tlogp";
    
    return product;
}

function load_tlogp(caption)
{
    var product = tlogp_caption_2_product(caption);
   
    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/tlogp/" + product + "/";

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

    $("#datetime-select").select2({
        width:"100%",
	    placeholder:"请选择时间",
	    language:"zh-CN"
    });
    
    $(document).ready(function(){
        var caption = $("#product-list-group .active").text();
        var product = tlogp_caption_2_product(caption);
        page_config(product);
    });
});

function tlogp_station(product,station)
{
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/tlogp/" + product + "/" + /* filter + "/"  +*/ station + "/";

	window.location.href = url;
}

function tlogp_search(product)
{
    //var filter = GetFilter(product);
    var station = $("#city-list-group .active").text();
    var dt = GetCurDateTime(); 
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/tlogp/" + product + "/" + /*filter + "/" +*/ station + "/" + dt + "/";

	window.location.href = url;
}

function tlogp_last_search(product,dt)
{
    //var filter = GetFilter(product);

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/tlogp/" + product + "/" + /*filter + "/" +*/ station + "/" + dt + "/last/";

	window.location.href = url;
}

function tlogp_next_search(product,dt)
{
    //var filter = GetFilter(product);

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/tlogp/" + product + "/" + /*filter + "/" +*/ station + "/" + dt + "/next/";

	window.location.href = url;
}

//auto refresh page when browse history.
function tlogp_auto_refresh(bStart)
{
    var caption = $("#product-list-group .active").text();
    var product = tlogp_caption_2_product(caption);

    //var filter = GetFilter(product);
    
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
    var url = "http://" + hostname + ":80/WindServer/tlogp/" + product + "/" + /*filter + "/" +*/ station + "/" + start_dt +  "/" + end_dt + "/auto/";

	window.location.href = url;
}

//auto refresh page to load newest
function tlogp_auto_update()
{
    var caption = $("#product-list-group .active").text();
    var product = tlogp_caption_2_product(caption);

    //var filter = GetFilter(product);

    var station = $("#city-list-group .active").text();
	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/tlogp/" + product + "/" + /*filter + "/" +*/ station + "/update/";

	window.location.href = url;
}

function page_config(product)
{
    var caption = $("#product-list-group .active").text();
    var product = tlogp_caption_2_product(caption);

    var path = window.location.pathname;
    var filters = path.split("/");
    if(filters.length <= 5)
    {
        var cur_dt = DateTimeFormat(new Date());
        //$("#datetimepick_cur_input").val(cur_dt);
    }
    else if(filters.length <= 6)
    {
        SelectCity(decodeURI(filters[4]));

        var cur_dt = DateTimeFormat(new Date());
        //$("#datetimepick_cur_input").val(cur_dt);
    }
    else if(filters.length <= 8)
    {
        SelectCity(decodeURI(filters[4]));

        if(filters[5] == "update")
        {
            gb_timer = setTimeout(tlogp_auto_update,6000);

            var cur_dt = DateTimeFormat(new Date());
            //$("#datetimepick_cur_input").val(cur_dt);
        }  
        else 
        {
            var cur_dt = decodeURI(filters[5]);
            //$("#datetimepick_cur_input").val(cur_dt);
        }
    }
    else
    {
        SelectCity(decodeURI(filters[4]));

        var start_dt = decodeURI(filters[5]);
        $("#datetimepick_start_input").val(start_dt);
        var end_dt = decodeURI(filters[6]);
        $("#datetimepick_end_input").val(end_dt);

        //$("#datetimepick_cur_input").val(start_dt);

		gb_timer = setTimeout(tlogp_auto_refresh,3000);
    }
}