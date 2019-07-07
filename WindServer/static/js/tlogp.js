function search_tlogp()
{
    var station = $("#city-btn-group .active").text();
    var start_dt = $("#datetimepick_start").find("input").val();
    var end_dt = $("#datetimepick_end").find("input").val();

	var hostname = window.location.hostname;
    var url = "http://" + hostname + ":8000/WindServer/tlogp/" + station + "/" + start_dt + "/" + end_dt + "/";

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

	$('#city-btn-group .btn').click(function() {
        $(this).addClass("active").siblings().removeClass("active");
    });
});