$(function(){
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
});