function checkClear(position, size, row, col, cords) {
    if (position) {
        while (col > 10 - size) {
		    col--;
		}
        for (var i=0;i<size;i++){
		    if (cords[row][col+i] == 1) {
			    return false;
			}
		}
        return true;
    }
    if (!position) {
	    while (row > 10 - size) {
		    row--;
		}
		for (var i=0;i<size;i++){
		    if (cords[row+i][col] == 1) {
			    return false;
			}
		}
        return true;
	
	}
}

function placeShips(cords) {
    var ships = [5,4,3,3,2];
	// The ships to be placed.
	for (var i=0;i<5;i++) {
	    var row = Math.floor(Math.random()*10);
        var col = Math.floor(Math.random()*10);
		while (cords[row][col] == 1) {
		    row = Math.floor(Math.random()*10);
            col = Math.floor(Math.random()*10);
		}
		// Vertical or horizontal.
		var position = Math.random() >= 0.5;
		
		if(position) {
		    while (!checkClear(position, ships[i], row, col, cords)) {
			    row = Math.floor(Math.random()*10);
                col = Math.floor(Math.random()*10);
			}
            while (col > 10 - ships[i]) {
			    col = col - 1;
			}
            for (var j=0;j<ships[i];j++) {
			    cords[row][col + j] = 1;
			}
		}
		if (!position) {
		    while (!checkClear(position, ships[i], row, col, cords)) {
			    row = Math.floor(Math.random()*10);
                col = Math.floor(Math.random()*10);
		    }
            while (row > 10 - ships[i]) {
			    row = row - 1;
            }      
            for (var j=0;j<ships[i];j++) {
			    cords[row+j][col] = 1;
			}
	    }
    }
}

function showShips () {
	for(var i=0;i<10;i++){
		for(var j=0;j<10;j++) {
			if (cords2[i][j] == 1) {
			    var ship = getElementInsideContainer("board2", "square_"+i+" "+j);
			    ship.style.backgroundImage="url('../../static/img/ship.jpg')";
			}
		}
	}
}