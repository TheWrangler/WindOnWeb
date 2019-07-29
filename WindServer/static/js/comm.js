function SelectCity(city)
{
    var citys = document.getElementById("city-list-group").childNodes;
    for(let station of citys)
    {
        if(station.nodeName == "#text")
            continue;
            
        if(city == station.id)
            document.getElementById(station.id).classList.add("active");
        else document.getElementById(station.id).classList.remove("active");
    }
}

function update_img(imgSrc)
{
    var element = document.getElementById('active_img');
    element.src = imgSrc;
}