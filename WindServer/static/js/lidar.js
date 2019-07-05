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