
function requette(action, param)
{
    fetch("/controller/man/" + action + "/" + param)
    .then(reponse => reponse.json())
    .then(reponse => alert(JSON.stringify(reponse)))
}
function start()
{
    requette("start", "0")
    document.querySelectorAll("button").forEach(button => button.disabled = false )

}

function stop()
{
    requette("stop", "0")
    load()
}

function mesureDistanceAvant()
{
    requette("USNDST", "0")
}

function mesureDistanceArriere()
{
    requette("USNDST", "1")
}

function tireLampe()
{
    requette("TIRLMP", "2")
}
function allumerLampe()
{
    requette("TIRLMP", "1")
}
function eteindreLampe()
{
    requette("TIRLMP", "0")
}


function klaxon()
{
    requette("HAPRDR", "0")
}

function haut()
{
    requette("PSTSRV", "0")
}
function droite()
{
    requette("PSTSRV", "1")
}
function gauche()
{
    requette("PSTSRV", "2")
}
function bas()
{
    requette("PSTSRV", "3")
}



function avancer()
{
    requette("MVMTR", "0")
}
function recule()
{
    requette("MVMTR", "3")
}
function rotDroite()
{
    requette("MVMTR", "1")
}
function rotGauche()
{
    requette("MVMTR", "2")
}


window.addEventListener("keydown", (event) => {
    if (event.defaultPrevented) {
        return; // Do nothing if the event was already processed
    }
    
    switch(event.key)
    {
        // deplacements
        case "z":
            avancer();
            break;
    
        case "q":
            gauche();
            break;
    
        case "s":
            recule();
            break;
    
        case "d":
            droite();
            break;

        //  vise 
        case "o":
            haut();
            break;

        case "k":
            rotGauche();
            break;

        case "l":
            bas();
            break;

        case "m":
            rotDroite();
            break;

        // gestion Lampe
        case "t":
            tireLampe();
            break;

        case "c":
            klaxon();
            break;

        // ultrason

        case "a":
            mesureDistanceAvant();
            break;
            
        case "r":
            mesureDistanceArriere();
            break;
        
        case "n":
            stop();
            break;

        case "Enter":
            start();
            break;    

    }

    event.preventDefault();
})

function load()
{
    document.querySelectorAll("button").forEach(button => button.disabled = true )
    
    document.querySelector("#start").disabled = false 
    document.querySelector("#stop").disabled = false
}

window.onload( load())

