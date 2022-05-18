
function requette(action, param)
{
    fetch("/controller/auto/" + action )
    .then(reponse => reponse.json())
    .then(reponse => alert(JSON.stringify(reponse)))
}
function start()
{
    requette("start")
    document.querySelector("#start").disabled = true
    document.querySelector("#stop").disabled = false

}

function stop()
{
    requette("stop")
    document.querySelector("#start").disabled = false
    document.querySelector("#stop").disabled = true
}

window.addEventListener("keydown", (event) =>{

    switch (event.key)
    {
        case "n":
            stop();     
            break;

        case "Enter":
            start();
            break;    
    }
});


window.onload( document.querySelector("#stop").disabled = true )

