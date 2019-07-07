function load_fusion(product)
{
    var product_site;
    if(product == "激光雷达DBS-5")
        product_site = "dbs5";
    else if(product == "叠加风廓线")
        product_site = "profile";
    else if(product == "叠加微波辐射计")
        product_site = "radio";

    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/fusion/" + product_site + "/";

	window.location.href = url;
}

function search_dbs5()
{
	var fusion = $("#fusion-list-group .active").text();
    var station = $("#city-btn-group .active").text();
    var start_dt = $("#datetimepick_start").find("input").val();
    var end_dt = $("#datetimepick_end").find("input").val();

	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/fusion/" + "dbs5/" + fusion + "/" + station + "/" + start_dt + "/" + end_dt + "/";

	window.location.href = url;
}

function search_profile()
{
	var fusion = $("#fusion-list-group .active").text();
    var station = $("#city-btn-group .active").text();
    var start_dt = $("#datetimepick_start").find("input").val();
    var end_dt = $("#datetimepick_end").find("input").val();

	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/fusion/" + "profile/" + fusion + "/" + station + "/" + start_dt + "/" + end_dt + "/";

	window.location.href = url;
}

function search_radio()
{
	var fusion = $("#fusion-list-group .active").text();
    var station = $("#city-btn-group .active").text();
    var start_dt = $("#datetimepick_start").find("input").val();
    var end_dt = $("#datetimepick_end").find("input").val();

	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/fusion/" + "radio/" + fusion + "/" + station + "/" + start_dt + "/" + end_dt + "/";

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

	$('#fusion-list-group .list-group-item').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });

	$('#city-btn-group .btn').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });
});