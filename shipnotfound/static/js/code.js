function checkForWin(cords) {
    for (var i=0;i<10;i++) {
	    for (var j=0;j<10;j++) {
		    if(cords[i][j] == 1) {
			    return false;
			}
		}
	}
	return true;
}

function getElementInsideContainer(containerID, childID) {
    var elm = {};
    var elms = document.getElementById(containerID).getElementsByTagName("*");
    for (var i = 0; i < elms.length; i++) {
        if (elms[i].id === childID) {
            elm = elms[i];
            break;
        }
    }
    return elm;
}

// Set up the grid with the squares and their values.
function newGrid(){
	var output = '';
	for(var i = 0; i < 10; i++){
	    for (var j = 0; j < 10; j++) {
		    output += '<div id="square_'+i+" "+j+'" onclick="bomb(this,\''+i+'\',\''+j+'\')"></div>';
		}
	}
	document.getElementById('board').innerHTML = output;
}

function newOpponent() {
	var output = '';
	for(var i = 0; i < 10; i++){
	    for (var j = 0; j < 10; j++) {
		    output += '<div id="square_'+i+" "+j+'" name="square_'+i+" "+j+'"></div>';
			
		}
	}
	document.getElementById('board2').innerHTML = output;
}


// Reveal the value of the square.
function bomb(square,i,j){
	var oppX = Math.floor(Math.random()*10);
	var oppY = Math.floor(Math.random()*10);
	while (cords2[oppX][oppY] == 0) {
		var oppX = Math.floor(Math.random()*10);
	    var oppY = Math.floor(Math.random()*10);
	}
	if (cords[parseInt(i)][parseInt(j)] == 0) {
		return;
	}
	else if (cords[parseInt(i)][parseInt(j)] == 1) {
	    score++;
	    cords[parseInt(i)][parseInt(j)] = 0;
	    square.style.backgroundImage="url('../../static/img/hit.jpg')";
		document.getElementById('log').innerHTML += "<br />" + "You hit: (" + (parseInt(i)+1) + "," + (parseInt(j)+1) + ")";
		document.getElementById('log').scrollTop = 9999999;
	}
    else {
	    score++;
	    cords[parseInt(i)][parseInt(j)] = 0;
	    square.style.backgroundImage="url('../../static/img/nohit.jpg')";
		document.getElementById('log').innerHTML += "<br />" + "You missed: (" + (parseInt(i)+1) + "," + (parseInt(j)+1) + ")";
		document.getElementById('log').scrollTop = 9999999;
	}
	if (checkForWin(cords)) {
	    window.alert("Your score: " + (100 - score));
		document.write("Congratulations!!");
	}
	var oppSquare = getElementInsideContainer("board2", "square_"+oppX+" "+oppY)
	if (cords2[oppX][oppY] == 1) {
		cords2[oppX][oppY] = 0;
		oppSquare.style.backgroundImage="url('../../static/img/hit.jpg')";
		document.getElementById('log').innerHTML += "<br />" + " Opp hit: (" + (oppX+1) + "," + (oppY+1) + ")";
		document.getElementById('log').scrollTop = 9999999;
	}
	else {
		cords2[oppX][oppY] = 0;
		oppSquare.style.backgroundImage="url('../../static/img/nohit.jpg')";
		document.getElementById('log').innerHTML += "<br />" + "Opp missed: (" + (oppX+1) + "," + (oppY+1) + ")";
		document.getElementById('log').scrollTop = 9999999;
	}
	if (checkForWin(cords2)) {
	    window.alert("The computer won.");
		document.write("Loser!!");
	}
}