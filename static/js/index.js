   
function startAutomatique()
{
    console.log("startAutomatique")
    fetch("/run/automatic")
}

function startManuel()
{
    console.log("startManuel")
    fetch('/run/manuel')
}

