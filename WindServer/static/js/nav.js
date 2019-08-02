function nav_catalog(catalog)
{
    var catalog_site;
    if(catalog == "首页")
        catalog_site = "index";
    else if(catalog == "激光雷达")
        catalog_site = "lidar";
    else if(catalog == "融合产品")
        catalog_site = "fusion";
    else if(catalog == "T-logP图")
        catalog_site = "tlogp";
    else if(catalog == "统计查询")
        catalog_site = "history";
    else if(catalog == "服务咨询")
        catalog_site = "service";
    else if(catalog == "关于我们")
        catalog_site = "about";

    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":" + GetHostPort() + "/WindServer/" + catalog_site + "/";

	window.location.href = url;
}