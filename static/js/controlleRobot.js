
function requette(action, param)
{
    fetch("/controller/man/" + action + "/" + param)
    .then(reponse => reponse.json())
    .then((reponse) =>{
        var valid = reponse["validation"];
        console.log(valid)
        if (action == "USNDST")
        {
            if (param == "0")
            {
                document.getElementById("distanceAv").innerText= reponse['distance'];
            }
            else{

                document.getElementById("distanceAr").innerHTML = reponse['distance']; 
            }
        }

        if (valid.indexOf("ok") == -1)
        {
            alert("votre commande a rencontrée un probleme et n'a pas pu etre executée")
        }
    })
}

// fonction de demarrage
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

// utilisation des catpteurs US
function mesureDistanceAvant()
{
    requette("USNDST", "0")
}

function mesureDistanceArriere()
{
    requette("USNDST", "1")
}


// utilisation de la LED
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

// utilisation du HP
function klaxon()
{
    requette("HAPRDR", "0")
}


// servomoteurs
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


// deplacements
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

// event Listener pour le keyboard
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
            rotGauche();
            break;
    
        case "s":
            recule();
            break;
    
        case "d":
            rotDroite();
            break;

        //  vise 
        case "o":
            haut();
            break;

        case "k":
            gauche();
            break;

        case "l":
            bas();
            break;

        case "m":
            droite();
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


window.addEventListener("gamepadconnected", function(e) {
console.log(e.gamepad)
});

window.addEventListener("gamepaddisconnected", function(e) {
console.log(e.gamepad)
});




// disable tous les boutons tant que l'on a pas demarrer le robot
function load()
{
    document.querySelectorAll("button").forEach(button => button.disabled = true )
    
    document.querySelector("#start").disabled = false 
    document.querySelector("#stop").disabled = false
}

window.onload( load())

