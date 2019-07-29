function DateTimeFormat(dt)
{ 
    var year = dt.getFullYear();       //年
    var month = dt.getMonth() + 1;     //月
    var day = dt.getDate();            //日
   
    var hh = dt.getHours();            //时
    var mm = dt.getMinutes();          //分
    var ss = dt.getSeconds();
   
    var clock = year + "-";
   
    if(month < 10)
        clock += "0";
   
    clock += month + "-";
   
    if(day < 10)
        clock += "0";
       
    clock += day + " ";
   
    if(hh < 10)
        clock += "0";
       
    clock += hh + ":";
    if (mm < 10) clock += '0'; 
    clock += mm; 

    clock += ":";
    if (ss < 10) clock += '0'; 
    clock += ss; 

    return(clock); 
}