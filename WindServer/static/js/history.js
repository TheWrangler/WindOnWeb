$(function(){
    $('#city-list-group .list-group-item').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });

    $("#height-select").select2({
        width:"100%",
	    placeholder:"请选择高度",
	    language:"zh-CN"
    });

    $("#datetimepick_cur").datetimepicker({
        format:'YYYY-MM-DD',
        locale:moment.locale('zh-cn')
    });

    $("#datetimepick_start").datetimepicker({
        format:'YYYY-MM',
        locale:moment.locale('zh-cn')
    });

    $("#datetimepick_end").datetimepicker({
        format:'YYYY-MM',
        locale:moment.locale('zh-cn')
    });

    $(document).ready(function(){
        page_config();
    });
});

function day_average()
{
    var hei = $("#height-select").val(); 
    var station = $("#city-list-group .active").text();
    var dt = $("#datetimepick_cur").find("input").val(); 
    if(dt == "")
    {
        alert("请设置检索的日期！");
        return;
    }
    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":" + GetHostPort() + "/WindServer/history/daily/windrose/" + station + "/" + dt + "/"+ hei + "/";
	window.location.href = url;
}

function month_average()
{
    var bWindRose = document.getElementById('wind_rose_layer').checked;
    var product="";
    var hei;
    if(bWindRose)
    {
        product += "windrose+";
        hei = $("#height-select").val(); 
    }

    var bWindCurve = document.getElementById('wind_curve_layer').checked;
    if(bWindCurve)
        product += "windcurve+";

    var bTemp = document.getElementById('temp').checked;
    if(bTemp)
        product += "temp+";

    var bHumidity = document.getElementById('humidity').checked;
    if(bHumidity)
        product += "humidity+";

    if(product == "")
    {
        alert("请选择气象查询要素！");
        return;
    }
    product = product.substring(0,product.length-1);

    var station = $("#city-list-group .active").text();

    var date_from = $("#datetimepick_start").find("input").val(); 
    var date_to = $("#datetimepick_end").find("input").val(); 

    if(date_from == "" || date_to == "")
    {
        alert("请设置检索的日期！");
        return;
    }
    date_from += "-01";
    date_to += "-01";

    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":" + GetHostPort() + "/WindServer/history/month/" + product + "/" + station + "/" + date_from + "/" + date_to + "/";
    if(bWindRose)
        url += hei + "/";

    window.location.href = url;
}

function page_config(product)
{
    var path = window.location.pathname;
    var filters = path.split("/");
    if(filters.length <= 4)
    {
        var cur_dt = DateTimeFormat(new Date());
        cur_dt = cur_dt.substring(0,10);
        $("#datetimepick_cur_input").val(cur_dt);
    }
    else if(filters[3] == "daily")
    {
        $("#height-select").val(filters[7]).trigger("change");
        SelectCity(decodeURI(filters[5]));

        var cur_dt = decodeURI(filters[6]);
        $("#datetimepick_cur_input").val(cur_dt);
    }
    else if(filters[3] == "month")
    {
        SelectCity(decodeURI(filters[5]));

        var start_dt = decodeURI(filters[6]);
        start_dt = start_dt.substring(0,7);
        $("#datetimepick_start_input").val(start_dt);

        var end_dt = decodeURI(filters[7]);
        end_dt = end_dt.substring(0,7);
        $("#datetimepick_end_input").val(end_dt);

        products = filters[4];
        if(products.indexOf('windrose') != -1)
        {
            document.getElementById('wind_rose_layer').checked = true;
        }
        if(products.indexOf('windcurve') != -1)
        {
            document.getElementById('wind_curve_layer').checked = true;
        }
        if(products.indexOf('temp') != -1)
        {
            document.getElementById('temp').checked = true;
        }
        if(products.indexOf('humidity') != -1)
        {
            document.getElementById('humidity').checked = true;
        }

        if(filters.length > 9)
            $("#height-select").val(filters[8]).trigger("change");
    }
}