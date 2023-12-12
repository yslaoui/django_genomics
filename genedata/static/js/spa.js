function writeGeneMenu() {
    console.log("Gene menu Written")
}

function writeInitialContent() {
    console.log("Initial content Written")
    var contentHTML = "<h2>Select gene location</h2>\n";
    contentHTML += "<a href=\"/list/Chromosome\">Chromosome</a> OR <a href=\"/list/Plasmid\">Plasmid</a>\n";
    contentHTML += "<h2>Show Positive Chromosome</h2>\n";
    contentHTML += "<a href=\"/poslist/\">Show This List</a>\n";
    contentHTML += "<br />\n";
    contentHTML += "<h2>Create Gene Entry</h2>\n";
    contentHTML += "<a href=\"/create_gene/\">Add Gene Entry To DB</a>\n";
    contentHTML += "<br />\n";
    contentHTML += "<h2>Create EC Entry</h2>\n";
    contentHTML += "<a href=\"/create_ec/\">Add EC Entry</a>\n";
    contentHTML += "<br />\n";
    var content_region = document.getElementById("dynamic_content") 
    content_region.innerHTML = contentHTML
}



function initializePage() {
    console.log("Page Initializing");
    writeGeneMenu();
    writeInitialContent();
}

