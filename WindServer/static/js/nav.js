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

    var hostname = window.location.hostname;
    var url = "http://" + hostname + ":80/WindServer/" + catalog_site + "/";

	window.location.href = url;
}