function load_lidar(product)
{
    var product_site;
    if(product == "PPI拼图")
        product_site = "ppi";
    else if(product == "VOL模式CAPPI")
        product_site = "cappi";
    else if(product == "风廓线THI")
        product_site = "wind_thi";
    else if(product == "RHI")
        product_site = "rhi";

    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/lidar/" + product_site + "/";

	window.location.href = url;
}

function search_ppi()
{
	var ele = $("#ele-list-group .active").text();
    ele = ele.substring(0,ele.length-1);
    
    var station = $("#city-btn-group .active").text();
    var start_dt = $("#datetimepick_start").find("input").val();
    var end_dt = $("#datetimepick_end").find("input").val();

	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/lidar/" + "ppi/" + ele + "/" + station + "/" + start_dt + "/" + end_dt + "/";

	window.location.href = url;
}

function search_cappi()
{
	var hei = $("#hei-list-group .active").text();
    hei = hei.substring(0,hei.length-1);
    
    var station = $("#city-btn-group .active").text();
    var start_dt = $("#datetimepick_start").find("input").val();
    var end_dt = $("#datetimepick_end").find("input").val();

	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/lidar/" + "cappi/" + hei + "/" + station + "/" + start_dt + "/" + end_dt + "/";

	window.location.href = url;
}

function search_windthi()
{
    var direction_caption = $("#dis-list-group .active").text();
    var direction;
    if(direction_caption == "水平风(HWind)")
        direction = "水平风";
    else if(direction_caption == "垂直风(ZWind)")
        direction = "垂直风";

    var station = $("#city-btn-group .active").text();
    var start_dt = $("#datetimepick_start").find("input").val();
    var end_dt = $("#datetimepick_end").find("input").val();

	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/lidar/" + "wind_thi/" + direction + "/" + station + "/" + start_dt + "/" + end_dt + "/";

	window.location.href = url;
}

function search_rhi()
{
	var azi = $("#azi-list-group .active").text();
    azi = azi.substring(0,azi.length-1);
    
    var station = $("#city-btn-group .active").text();
    var start_dt = $("#datetimepick_start").find("input").val();
    var end_dt = $("#datetimepick_end").find("input").val();

	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/lidar/" + "rhi/" + azi + "/" + station + "/" + start_dt + "/" + end_dt + "/";

	window.location.href = url;
}


$(function(){
    $("#datetimepick_start").datetimepicker({
        format:'YYYY-MM-DD hh:mm',
        locale:moment.locale('zh-cn')
    });

    $("#datetimepick_end").datetimepicker({
        format:'YYYY-MM-DD hh:mm',
        locale:moment.locale('zh-cn')
    });

	$('#ele-list-group .list-group-item').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });

	$('#hei-list-group .list-group-item').click(function(){
		$(this).addClass("active").siblings().removeClass("active");
	});
	
	$('#dis-list-group .list-group-item').click(function(){
		$(this).addClass("active").siblings().removeClass("active");
	});
	
	$('#azi-list-group .list-group-item').click(function(){
		$(this).addClass("active").siblings().removeClass("active");
	});

	$('#city-btn-group .btn').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });
});